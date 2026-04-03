import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.data import Dataset, DataLoader

from tqdm.auto import tqdm

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

import time

def visualize2DSoftmax(X, y, model):
    """Función para visualizar la frontera de clasificación de un modelo aprendido sobre un conjunto 2-D.

    Argumentos:
    X -- arreglo de numpy con forma (2, N), donde N es el número de puntos.
    y -- arreglo de numpy con forma (N,), que contiene valores "0" o "1" para dos clases distintas.
    model -- objeto PyTorch Module que representa el clasificador a visualizar.
    """
    x_min = np.min(X[:,0]) - 0.5
    x_max = np.max(X[:,0]) + 0.5
    y_min = np.min(X[:,1]) - 0.5
    y_max = np.max(X[:,1]) + 0.5
    xv, yv = np.meshgrid(
        np.linspace(x_min, x_max, num=20),
        np.linspace(y_min, y_max, num=20),
        indexing='ij'
    )
    xy_v = np.hstack((xv.reshape(-1,1), yv.reshape(-1,1)))
    with torch.no_grad():
        preds = model(torch.tensor(xy_v, dtype=torch.float32))
        preds = F.softmax(preds, dim=1).numpy()

    cs = plt.contourf(
        xv, yv, preds[:,0].reshape(20,20),
        levels=np.linspace(0,1,num=20), cmap=plt.cm.RdYlBu
    )
    sns.scatterplot(x=X[:,0], y=X[:,1], hue=y, style=y, ax=cs.ax)


def run_epoch(model, optimizer, data_loader, loss_func, device, results, score_funcs, prefix="", desc=None):
    """
    model -- modelo de PyTorch / "Module" para ejecutar durante una época
    optimizer -- objeto que actualizará los pesos de la red
    data_loader -- DataLoader que devuelve tuplas (entrada, etiqueta)
    loss_func -- función de pérdida que recibe la salida del modelo y las etiquetas
    device -- dispositivo de cómputo donde se realizará el entrenamiento
    score_funcs -- diccionario de métricas para evaluar el rendimiento
    prefix -- prefijo para guardar resultados dentro del diccionario _results_
    desc -- descripción para la barra de progreso
    """
    running_loss = []
    y_true = []
    y_pred = []
    start = time.time()

    for inputs, labels in tqdm(data_loader, desc=desc, leave=False):
        # Mueve el lote al dispositivo que estamos usando.
        inputs = moveTo(inputs, device)
        labels = moveTo(labels, device)

        y_hat = model(inputs)  # aquí se calcula f_Θ(x(i))
        # Calcula la pérdida.
        loss = loss_func(y_hat, labels)

        if model.training:
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        # Guardamos información útil para análisis posterior.
        running_loss.append(loss.item())

        if len(score_funcs) > 0 and isinstance(labels, torch.Tensor):
            # Mueve etiquetas y predicciones a CPU para calcular métricas/guardar resultados
            labels = labels.detach().cpu().numpy()
            y_hat = y_hat.detach().cpu().numpy()

            # Acumula predicciones y etiquetas
            y_true.extend(labels.tolist())
            y_pred.extend(y_hat.tolist())

    # Fin de la época
    end = time.time()

    y_pred = np.asarray(y_pred)
    if len(y_pred.shape) == 2 and y_pred.shape[1] > 1:
        # Problema de clasificación: convertir probabilidades/logits a etiquetas
        y_pred = np.argmax(y_pred, axis=1)
    # En otro caso, asumimos que es un problema de regresión

    results[prefix + " loss"].append(np.mean(running_loss))
    for name, score_func in score_funcs.items():
        try:
            results[prefix + " " + name].append(score_func(y_true, y_pred))
        except:
            results[prefix + " " + name].append(float("NaN"))

    return end - start  # tiempo invertido en la época


def train_simple_network(model, loss_func, train_loader, test_loader=None, score_funcs=None,
                         epochs=50, device="cpu", checkpoint_file=None, lr=0.001):
    """Entrena redes neuronales simples.

    Argumentos:
    model -- modelo de PyTorch / "Module" a entrenar
    loss_func -- función de pérdida que recibe salida y etiquetas
    train_loader -- DataLoader con pares (entrada, etiqueta)
    test_loader -- DataLoader opcional para evaluar después de cada época
    score_funcs -- diccionario de métricas de evaluación
    epochs -- número de épocas de entrenamiento
    device -- dispositivo de cómputo
    """
    to_track = ["epoch", "total time", "train loss"]
    if test_loader is not None:
        to_track.append("test loss")
    for eval_score in score_funcs:
        to_track.append("train " + eval_score)
        if test_loader is not None:
            to_track.append("test " + eval_score)

    total_train_time = 0  # tiempo total acumulado en entrenamiento
    results = {}

    # Inicializa cada métrica con una lista vacía
    for item in to_track:
        results[item] = []

    # SGD = descenso de gradiente estocástico
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

    # Coloca el modelo en el recurso de cómputo correcto
    model.to(device)

    for epoch in tqdm(range(epochs), desc="Epoch"):
        model = model.train()  # pone el modelo en modo entrenamiento

        total_train_time += run_epoch(
            model, optimizer, train_loader, loss_func, device,
            results, score_funcs, prefix="train", desc="Training"
        )

        results["total time"].append(total_train_time)
        results["epoch"].append(epoch)

        if test_loader is not None:
            model = model.eval()
            with torch.no_grad():
                run_epoch(
                    model, optimizer, test_loader, loss_func, device,
                    results, score_funcs, prefix="test", desc="Testing"
                )

    if checkpoint_file is not None:
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'results': results
        }, checkpoint_file)

    return pd.DataFrame.from_dict(results)


def set_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)


class Flatten(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), -1)


class View(nn.Module):
    def __init__(self, *shape):
        super(View, self).__init__()
        self.shape = shape

    def forward(self, input):
        return input.view(*self.shape)


class LambdaLayer(nn.Module):
    def __init__(self, lambd):
        super(LambdaLayer, self).__init__()
        self.lambd = lambd

    def forward(self, x):
        return self.lambd(x)


class DebugShape(nn.Module):
    """
    Módulo útil para depurar la arquitectura de una red neuronal.
    Inserta este módulo entre capas y mostrará la forma de la salida.
    """
    def forward(self, input):
        print(input.shape)
        return input


def weight_reset(m):
    """
    Recorre un módulo de PyTorch y reinicia sus pesos a un estado aleatorio inicial.
    """
    if "reset_parameters" in dir(m):
        m.reset_parameters()
    return


def moveTo(obj, device):
    """
    obj: objeto de Python a mover al dispositivo, o cuyo contenido se moverá al dispositivo
    device: dispositivo de cómputo al que se moverán los objetos
    """
    if hasattr(obj, "to"):
        return obj.to(device)
    elif isinstance(obj, list):
        return [moveTo(x, device) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(moveTo(list(obj), device))
    elif isinstance(obj, set):
        return set(moveTo(list(obj), device))
    elif isinstance(obj, dict):
        to_ret = dict()
        for key, value in obj.items():
            to_ret[moveTo(key, device)] = moveTo(value, device)
        return to_ret
    else:
        return obj


def train_network(model, loss_func, train_loader, val_loader=None, test_loader=None, score_funcs=None,
                  epochs=50, device="cpu", checkpoint_file=None,
                  lr_schedule=None, optimizer=None, disable_tqdm=False):
    """Entrena redes neuronales.

    Argumentos:
    model -- modelo de PyTorch / "Module" a entrenar
    loss_func -- función de pérdida
    train_loader -- DataLoader de entrenamiento
    val_loader -- DataLoader opcional de validación
    test_loader -- DataLoader opcional de prueba
    score_funcs -- diccionario de métricas de evaluación
    epochs -- número de épocas
    device -- dispositivo de cómputo
    lr_schedule -- scheduler para modificar la tasa de aprendizaje durante el entrenamiento
    optimizer -- optimizador a utilizar
    """
    if score_funcs is None:
        score_funcs = {}

    to_track = ["epoch", "total time", "train loss"]
    if val_loader is not None:
        to_track.append("val loss")
    if test_loader is not None:
        to_track.append("test loss")

    for eval_score in score_funcs:
        to_track.append("train " + eval_score)
        if val_loader is not None:
            to_track.append("val " + eval_score)
        if test_loader is not None:
            to_track.append("test " + eval_score)

    total_train_time = 0
    results = {}

    # Inicializa todas las listas de resultados
    for item in to_track:
        results[item] = []

    if optimizer is None:
        # AdamW es un buen optimizador por defecto
        optimizer = torch.optim.AdamW(model.parameters())
        del_opt = True
    else:
        del_opt = False

    # Coloca el modelo en el dispositivo correcto
    model.to(device)

    for epoch in tqdm(range(epochs), desc="Epoch", disable=disable_tqdm):
        model = model.train()  # modo entrenamiento

        total_train_time += run_epoch(
            model, optimizer, train_loader, loss_func, device,
            results, score_funcs, prefix="train", desc="Training"
        )

        results["epoch"].append(epoch)
        results["total time"].append(total_train_time)

        if val_loader is not None:
            model = model.eval()  # modo evaluación: no actualiza pesos
            with torch.no_grad():
                run_epoch(
                    model, optimizer, val_loader, loss_func, device,
                    results, score_funcs, prefix="val", desc="Validating"
                )

        # En PyTorch, por convención, el scheduler se actualiza después de cada época
        if lr_schedule is not None:
            if isinstance(lr_schedule, torch.optim.lr_scheduler.ReduceLROnPlateau):
                lr_schedule.step(results["val loss"][-1])
            else:
                lr_schedule.step()

        if test_loader is not None:
            model = model.eval()
            with torch.no_grad():
                run_epoch(
                    model, optimizer, test_loader, loss_func, device,
                    results, score_funcs, prefix="test", desc="Testing"
                )

        if checkpoint_file is not None:
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'results': results
            }, checkpoint_file)

    if del_opt:
        del optimizer

    return pd.DataFrame.from_dict(results)


### Clases utilitarias para RNN

class LastTimeStep(nn.Module):
    """
    Clase para extraer las activaciones ocultas del último paso temporal
    a partir de la salida de un módulo RNN de PyTorch.
    """
    def __init__(self, rnn_layers=1, bidirectional=False):
        super(LastTimeStep, self).__init__()
        self.rnn_layers = rnn_layers
        if bidirectional:
            self.num_driections = 2
        else:
            self.num_driections = 1

    def forward(self, input):
        # El resultado puede ser una tupla (out, h_t)
        # o una tupla (out, (h_t, c_t))
        rnn_output = input[0]

        last_step = input[1]
        if type(last_step) == tuple:
            last_step = last_step[0]

        # Según la documentación: (num_layers * num_directions, batch, hidden_size)
        batch_size = last_step.shape[1]

        last_step = last_step.view(self.rnn_layers, self.num_driections, batch_size, -1)
        # Nos quedamos con la última capa
        last_step = last_step[self.rnn_layers - 1]
        # Reordenar para que batch sea la primera dimensión
        last_step = last_step.permute(1, 0, 2)
        # Aplanar las últimas dos dimensiones
        return last_step.reshape(batch_size, -1)


class EmbeddingPackable(nn.Module):
    """
    La capa Embedding de PyTorch no soporta objetos PackedSequence.
    Esta clase contenedora lo resuelve. Si la entrada es normal, usa
    la capa Embedding de siempre. Si la entrada es empaquetada, la
    procesa y devuelve una nueva PackedSequence.
    """
    def __init__(self, embd_layer):
        super(EmbeddingPackable, self).__init__()
        self.embd_layer = embd_layer

    def forward(self, input):
        if type(input) == torch.nn.utils.rnn.PackedSequence:
            # Desempaquetar la secuencia
            sequences, lengths = torch.nn.utils.rnn.pad_packed_sequence(
                input.cpu(), batch_first=True
            )
            # Aplicar embeddings
            sequences = self.embd_layer(sequences.to(input.data.device))
            # Volver a empaquetar
            return torch.nn.utils.rnn.pack_padded_sequence(
                sequences, lengths.cpu(),
                batch_first=True, enforce_sorted=False
            )
        else:
            # Aplicar embedding normal
            return self.embd_layer(input)


### Capas para mecanismos de atención

class ApplyAttention(nn.Module):
    """
    Módulo auxiliar para aplicar los resultados de un mecanismo
    de atención a un conjunto de estados de entrada.
    """
    def __init__(self):
        super(ApplyAttention, self).__init__()

    def forward(self, states, attention_scores, mask=None):
        """
        states: tensor con forma (B, T, H), donde T son las posibles entradas
        attention_scores: tensor con forma (B, T, 1), puntaje de atención por elemento
        mask: None si todos los elementos están presentes. En otro caso,
              tensor booleano con forma (B, T), donde True indica elementos válidos.

        retorna: una tupla de dos tensores.
        - primer tensor: contexto final (B, H)
        - segundo tensor: pesos de atención (B, T, 1)
        """
        if mask is not None:
            # Asignar un valor muy negativo a posiciones inválidas
            attention_scores[~mask] = -1000.0

        # Convertir puntajes en pesos con softmax
        weights = F.softmax(attention_scores, dim=1)

        # Combinar estados según los pesos
        final_context = (states * weights).sum(dim=1)
        return final_context, weights


class AttentionAvg(nn.Module):
    def __init__(self, attnScore):
        super(AttentionAvg, self).__init__()
        self.score = attnScore

    def forward(self, states, context, mask=None):
        """
        states: forma (B, T, D)
        context: forma (B, D)
        salida: forma (B, D), promedio ponderado
        """
        B = states.size(0)
        T = states.size(1)
        D = states.size(2)

        scores = self.score(states, context)

        if mask is not None:
            scores[~mask] = float(-10000)

        weights = F.softmax(scores, dim=1)
        context = (states * weights).sum(dim=1)

        return context.view(B, D)


class AdditiveAttentionScore(nn.Module):
    def __init__(self, D):
        super(AdditiveAttentionScore, self).__init__()
        self.v = nn.Linear(D, 1)
        self.w = nn.Linear(2 * D, D)

    def forward(self, states, context):
        """
        states: forma (B, T, D)
        context: forma (B, D)
        salida: forma (B, T, 1), puntaje para cada paso temporal
        """
        T = states.size(1)

        # Repite el contexto T veces
        context = torch.stack([context for _ in range(T)], dim=1)
        state_context_combined = torch.cat((states, context), dim=2)
        scores = self.v(torch.tanh(self.w(state_context_combined)))
        return scores


class GeneralScore(nn.Module):
    def __init__(self, D):
        super(GeneralScore, self).__init__()
        self.w = nn.Bilinear(D, D, 1)

    def forward(self, states, context):
        """
        states: forma (B, T, D)
        context: forma (B, D)
        salida: forma (B, T, 1), puntaje para cada elemento temporal
        """
        T = states.size(1)
        D = states.size(2)

        # Repite el contexto T veces
        context = torch.stack([context for _ in range(T)], dim=1)
        scores = self.w(states, context)
        return scores


class DotScore(nn.Module):
    def __init__(self, D):
        super(DotScore, self).__init__()

    def forward(self, states, context):
        """
        states: forma (B, T, D)
        context: forma (B, D)
        salida: forma (B, T, 1), puntaje por producto punto escalado
        """
        T = states.size(1)
        D = states.size(2)

        scores = torch.bmm(states, context.unsqueeze(2)) / np.sqrt(D)
        return scores


def getMaskByFill(x, time_dimension=1, fill=0):
    """
    x: tensor original con tres o más dimensiones, (B, ..., T, ...)
       donde puede haber elementos no usados
    time_dimension: eje que representa el tiempo
    fill: valor constante que indica elementos no usados

    retorna: tensor booleano con forma (B, T), donde True indica
    que el elemento temporal es válido.
    """
    # Omitimos la dimensión 0 porque corresponde al batch
    to_sum_over = list(range(1, len(x.shape)))

    if time_dimension in to_sum_over:
        to_sum_over.remove(time_dimension)

    with torch.no_grad():
        # Caso especial: si la forma es (B, D), devolvemos directamente qué valores son válidos
        if len(to_sum_over) == 0:
            return (x != fill)

        # Detecta posiciones no vacías y resumir sobre todas las dimensiones salvo batch y tiempo
        mask = torch.sum((x != fill), dim=to_sum_over) > 0

    return mask


class LanguageNameDataset(Dataset):
    def __init__(self, lang_name_dict, vocabulary):
        self.label_names = [x for x in lang_name_dict.keys()]
        self.data = []
        self.labels = []
        self.vocabulary = vocabulary

        for y, language in enumerate(self.label_names):
            for sample in lang_name_dict[language]:
                self.data.append(sample)
                self.labels.append(y)

    def __len__(self):
        return len(self.data)

    def string2InputVec(self, input_string):
        """
        Convierte una cadena de texto en un vector de enteros según el vocabulario.
        input_string: cadena a convertir en tensor
        """
        T = len(input_string)

        # Crea tensor para almacenar el resultado
        name_vec = torch.zeros((T), dtype=torch.long)

        # Recorre la cadena y asignar el índice de cada carácter
        for pos, character in enumerate(input_string):
            name_vec[pos] = self.vocabulary[character]

        return name_vec

    def __getitem__(self, idx):
        name = self.data[idx]
        label = self.labels[idx]

        # Convertir la clase a tensor
        label_vec = torch.tensor([label], dtype=torch.long)

        return self.string2InputVec(name), label


def pad_and_pack(batch):
    # 1, 2 y 3: organiza longitudes, entradas y etiquetas en listas separadas
    input_tensors = []
    labels = []
    lengths = []

    for x, y in batch:
        input_tensors.append(x)
        labels.append(y)
        lengths.append(x.shape[0])  # asumimos forma (T, *)

    # 4: crea la versión rellenada (padded)
    x_padded = torch.nn.utils.rnn.pad_sequence(input_tensors, batch_first=False)

    # 5: crea la versión empaquetada usando longitudes
    x_packed = torch.nn.utils.rnn.pack_padded_sequence(
        x_padded, lengths, batch_first=False, enforce_sorted=False
    )

    # Convierte etiquetas a tensor
    y_batched = torch.as_tensor(labels, dtype=torch.long)

    # 6: devuelve entrada empaquetada y etiquetas
    return x_packed, y_batched