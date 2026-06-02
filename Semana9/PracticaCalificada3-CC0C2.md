### Practica Calificada 3 - CC0C2 Procesamiento del Lenguaje Natural

**Tema general:** modelos de lenguaje causales, generación autoregresiva, fine-tuning, PEFT, LoRA, QLoRA, adaptadores, preferencias y alineamiento.

**Modalidad:** individual.

**Entrega:** repositorio con notebook, README, video técnico y evidencia de ejecución.

**Duración del video:** estrictamente mayor a 12 minutos.

**Condición central:** no habrá exposición presencial por razones de tiempo. Por ello, el video será tratado como evidencia principal de autoría, comprensión técnica y defensa del trabajo.

#### Propósito de la evaluación

La Práctica Calificada 3 evalúa si el estudiante comprende y puede defender técnicamente los conceptos trabajados en los cuadernos 12, 13, 14, 15, 16, 17, 18 y 19 del curso CC0C2.

El objetivo no es premiar la simple ejecución de código ni la generación automática de notebooks mediante IA. El objetivo es verificar si el estudiante puede reconstruir una línea base, modificarla de forma significativa, explicar el flujo interno del modelo, justificar dimensiones, interpretar resultados y defender técnicamente su propio trabajo.

El uso de IA no está prohibido como apoyo. Sin embargo, una entrega producida con IA y no comprendida por el estudiante será considerada inválida.

Código correcto sin explicación correcta no aprueba la práctica.

#### Documentos base permitidos

Cada estudiante debe construir su trabajo a partir de uno o más de los siguientes cuadernos del curso.

- `Cuaderno12-CC0C2.ipynb`: modelo causal decoder-only pequeño.
- `Cuaderno13-CC0C2.ipynb`: GPT-2, tokens, embeddings, decoding y KV cache.
- `Cuaderno14-CC0C2.ipynb`: LLMs causales, instruction tuning, alineamiento y agentes.
- `Cuaderno15-CC0C2.ipynb`: ajuste fino de Transformers con PyTorch y Hugging Face.
- `Cuaderno16-CC0C2.ipynb`: continual pre-training, replay, PEFT, ensambles y fusión.
- `Cuaderno17-CC0C2.ipynb`: LoRA desde PyTorch.
- `Cuaderno18-CC0C2.ipynb`: QLoRA, DPO y ORPO.
- `Cuaderno19-CC0C2.ipynb`: adaptadores.

El estudiante puede reutilizar código del curso, pero debe identificar claramente qué parte proviene del cuaderno base, qué parte fue modificada, qué parte fue agregada por el estudiante y qué parte recibió apoyo de IA.

#### Entregables obligatorios

Cada estudiante debe entregar la dirección de URL de su repositorio con los siguientes elementos.

- Un notebook `.ipynb` reproducible.
- Un archivo `README.md`.
- Un video técnico con voz propia.
- Evidencia de cálculo interno.
- Comparación entre línea base y variante.
- Registro de ejecución con semilla, entorno, librerías, modelo usado y datos usados.
- Una sección llamada `Declaración de autoría y uso de IA`.

#### Modalidad definitiva de evaluación

La práctica se evaluará únicamente mediante la entrega del repositorio y el video técnico.

No habrá exposición presencial.

El video debe cumplir el rol de defensa asíncrona. Por esta razón, no debe ser una presentación superficial ni una lectura de texto. Debe mostrar al estudiante trabajando con su notebook, programando cambios, ejecutando celdas, prediciendo efectos, interpretando resultados y explicando técnicamente el código.

La duración debe ser estrictamente mayor a 12 minutos. Se recomienda una duración entre 14 y 18 minutos.

Un video de 12 minutos exactos o menos no será válido.

#### Regla habilitante de validez académica

La práctica solo será calificada si el video contiene todos los elementos siguientes.

- Explicación del objetivo del proyecto.
- Identificación del cuaderno base usado.
- Explicación de la línea base.
- Explicación de la modificación principal.
- Codificación en vivo de al menos dos cambios.
- Ejecución de esos cambios.
- Predicción del efecto esperado antes de ejecutar.
- Interpretación del resultado obtenido después de ejecutar.
- Explicación de dimensiones, tensores, logits, máscaras, parámetros entrenables o pérdida, según corresponda.
- Respuesta a preguntas técnicas avanzadas.
- Cierre técnico sobre qué hizo, por qué lo hizo y qué significan sus resultados.

Si el video solo muestra celdas ya ejecutadas, solo lee texto, solo describe resultados o no incluye codificación en vivo, la práctica será inválida.

#### Regla frente a entregas generadas por IA

Se considerará entrega superficial o inválida aquella en la que el estudiante haga una o más de las siguientes acciones.

- Lee texto genérico sin conectarlo con su notebook.
- No puede explicar sus propias funciones.
- No puede explicar dimensiones de tensores, embeddings, logits, máscaras o parámetros.
- No puede justificar por qué eligió una variante.
- No puede interpretar los resultados.
- No modifica una celda simple durante el video.
- No explica una línea de código relevante.
- Presenta resultados sin reproducibilidad mínima.
- Presenta un notebook aparentemente correcto, pero sin defensa técnica real.

La IA puede usarse como apoyo. La evaluación se centra en apropiación conceptual, defensa técnica y trazabilidad del trabajo.

#### Estructura obligatoria del video

El video debe seguir esta estructura.

- Presentación breve del proyecto.
- Cuaderno base usado.
- Problema técnico.
- Línea base.
- Modificación principal.
- Primera codificación en vivo.
- Predicción antes de ejecutar.
- Ejecución.
- Interpretación del resultado.
- Segunda codificación en vivo.
- Predicción antes de ejecutar.
- Ejecución.
- Interpretación del resultado.
- Explicación de tensores, logits, máscaras, parámetros o pérdida.
- Comparación línea base contra variante.
- Respuesta a preguntas avanzadas.
- Limitaciones.
- Cierre sobre qué hizo, por qué lo hizo y qué significan sus resultados.
- Puente al curso.

El video debe mostrar pantalla completa o notebook completo. No se aceptan videos compuestos solo por diapositivas. Debe escucharse la voz del estudiante.

#### Codificación en vivo obligatoria

Cada estudiante debe realizar dos ejercicios de codificación en vivo durante el video.

El primer ejercicio será una modificación común obligatoria.

El segundo ejercicio será una modificación específica según el proyecto elegido.

No basta con cambiar un valor. El estudiante debe explicar qué valor tenía antes, qué valor coloca ahora, qué espera que ocurra, qué ocurrió realmente y si el resultado confirma o contradice su hipótesis.

#### Ejercicio A: modificación común obligatoria

El estudiante debe modificar en pantalla una parte del experimento y explicar el efecto esperado antes de ejecutar.

Puede elegir una de las siguientes opciones.

- Cambiar `temperature`, `top_k` o `top_p` y explicar cómo cambia la distribución de generación.
- Cambiar `max_new_tokens` y explicar cómo afecta la inferencia autoregresiva.
- Cambiar `SEQ_LEN` y explicar cómo afecta entrada, objetivo desplazado y máscara causal.
- Cambiar el tamaño de batch y explicar su impacto en memoria y forma de tensores.
- Cambiar el número de ejemplos de entrenamiento y explicar su efecto esperado en pérdida o sobreajuste.
- Cambiar una semilla y explicar por qué puede cambiar la generación.
- Cambiar el prompt y explicar por qué cambia la distribución del siguiente token.
- Congelar o descongelar una capa y explicar qué parámetros se entrenan.

#### Ejercicio B: modificación específica según proyecto

Además del cambio común, el estudiante debe hacer una modificación técnica relacionada directamente con su proyecto.

La modificación debe ser visible en el video, debe ejecutarse y debe interpretarse.

### Proyecto 1: modelo causal decoder-only desde cero

**Cuaderno base:** `Cuaderno12-CC0C2.ipynb`

**Tema central:** entrenamiento causal, máscara, predicción del siguiente token y decoding.

El estudiante debe reconstruir una línea base de modelo decoder-only pequeño, mostrar tokenización, secuencias, embeddings, máscara causal, logits y pérdida. Además, debe comparar al menos dos políticas de decoding.

La modificación obligatoria puede ser cambiar `SEQ_LEN`, el tamaño del modelo, el número de capas o la política de decoding.

La evidencia interna mínima debe incluir la matriz de máscara causal, un ejemplo de entrada `x`, un objetivo desplazado `y` y la forma de los logits.

Código mínimo sugerido para mostrar en el video.

```python
print("x:", x.shape)
print("y:", y.shape)
print("logits:", logits.shape)
print("causal_mask:", causal_mask.shape)
```

Preguntas avanzadas obligatorias.

- Si el modelo predice el siguiente token, ¿por qué la salida tiene una distribución sobre todo el vocabulario en cada posición?
- ¿Qué error conceptual ocurriría si el target no estuviera desplazado?
- ¿Por qué una máscara causal incorrecta puede convertir el entrenamiento en una forma de copia?
- ¿Qué diferencia hay entre reducir la pérdida y generar texto coherente?
- ¿Por qué un modelo pequeño entrenado desde cero puede aprender patrones locales, pero no razonamiento lingüístico robusto?.

### Proyecto 2: GPT-2, DistilGPT-2, decoding y KV cache

**Cuaderno base:** `Cuaderno13-CC0C2.ipynb`

**Tema central:** uso de modelo preentrenado, distribución del siguiente token, decoding y eficiencia.

El estudiante debe usar GPT-2 o DistilGPT-2, inspeccionar los tokens candidatos más probables, comparar greedy, sampling, top-k y top-p, y explicar la diferencia conceptual entre generar con y sin cache.

La modificación obligatoria consiste en diseñar cinco prompts propios: técnico, ambiguo, corto, largo y fuera de dominio. Debe comparar estabilidad, diversidad, repetición y coherencia.

Código mínimo sugerido para mostrar en el video.

```python
with torch.no_grad():
    outputs = model(**inputs)
    next_token_logits = outputs.logits[:, -1, :]
    probs = torch.softmax(next_token_logits, dim=-1)
    top_probs, top_ids = torch.topk(probs, k=10)

for p, idx in zip(top_probs[0], top_ids[0]):
    print(tokenizer.decode(idx), float(p))
```

Preguntas avanzadas obligatorias.

- ¿Por qué GPT-2 no responde como un modelo instruct moderno?
- ¿Qué significa exactamente `outputs.logits[:, -1, :]`?
- ¿Por qué top-k y top-p no son equivalentes?
- ¿Cómo puede una temperatura alta aumentar diversidad, pero reducir precisión?
- ¿Por qué KV cache mejora inferencia, pero no cambia el significado matemático del modelo?.

### Proyecto 3: instruction tuning y evaluación de respuestas

**Cuaderno base:** `Cuaderno14-CC0C2.ipynb`

**Tema central:** formato instrucción-respuesta, SFT y evaluación de comportamiento.

El estudiante debe construir un mini dataset de 20 instrucciones, aplicar un template de instrucción-respuesta, evaluar respuestas de un modelo base o simulado, y comparar prompt sin estructura contra prompt estructurado.

La modificación obligatoria consiste en crear dos templates distintos y analizar cuál produce respuestas más controladas.

Código mínimo sugerido para mostrar en el video.

```python
def build_prompt(instruction, input_text=""):
    return f"""### Instrucción:
{instruction}

### Entrada:
{input_text}

### Respuesta:
"""
```

Preguntas avanzadas obligatorias.

- ¿Por qué SFT no garantiza alineamiento?
- ¿Qué diferencia hay entre aprender una tarea y obedecer un formato?
- ¿Cómo distinguirías una respuesta correcta de una respuesta solo bien redactada?
- ¿Por qué una evaluación puramente textual puede ser engañosa?
- ¿Qué sesgo introduces al crear tú mismo las instrucciones y respuestas esperadas?.

### Proyecto 4: fine-tuning de Transformer para clasificación

**Cuaderno base:** `Cuaderno15-CC0C2.ipynb`

**Tema central:** ajuste fino supervisado para clasificación de texto.

El estudiante debe cargar un dataset pequeño de clasificación, usar tokenizer y modelo preentrenado, entrenar o simular un fine-tuning reducido, reportar accuracy o loss, y analizar errores.

La modificación obligatoria puede ser comparar dos configuraciones de learning rate, batch size, congelamiento parcial, número de ejemplos o longitud máxima.

Código mínimo sugerido para mostrar en el video.

```python
for name, param in model.named_parameters():
    if "classifier" not in name:
        param.requires_grad = False

trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total = sum(p.numel() for p in model.parameters())

print("Parámetros entrenables:", trainable)
print("Parámetros totales:", total)
print("Porcentaje entrenable:", trainable / total * 100)
```

Preguntas avanzadas obligatorias.

- ¿Qué riesgo hay al hacer fine-tuning con pocos datos?
- ¿Por qué congelar capas puede mejorar estabilidad, pero reducir adaptación?
- ¿Qué representa cada dimensión de los logits en clasificación?
- ¿Por qué accuracy puede ocultar errores importantes?
- ¿Cómo detectarías sobreajuste si solo tienes pocas épocas?.

### Proyecto 5: continual pre-training, replay y olvido catastrófico

**Cuaderno base:** `Cuaderno16-CC0C2.ipynb`

**Tema central:** adaptación a dominio y riesgo de olvido.

El estudiante debe construir dos mini corpus, uno de dominio base y otro de dominio nuevo. Luego debe ejecutar una adaptación mínima, comparar generación o pérdida antes y después, y discutir olvido catastrófico.

La modificación obligatoria consiste en comparar adaptación solo con dominio nuevo contra adaptación con replay.

Código mínimo sugerido para mostrar en el video.

```python
def mix_replay(new_examples, old_examples, replay_ratio=0.3):
    n_old = int(len(new_examples) * replay_ratio)
    return new_examples + old_examples[:n_old]

mixed_data = mix_replay(new_data, old_data, replay_ratio=0.5)
print("Nuevos:", len(new_data))
print("Replay:", len(mixed_data) - len(new_data))
print("Total:", len(mixed_data))
```

Preguntas avanzadas obligatorias.

- ¿Por qué adaptar a un nuevo dominio puede degradar conocimiento anterior?
- ¿Qué evidencia mínima mostraría olvido catastrófico?
- ¿Por qué replay no garantiza conservación perfecta?
- ¿Qué diferencia hay entre memorizar frases nuevas y adaptarse a un dominio?
- ¿Cómo separarías mejora real de simple repetición del corpus?.

### Proyecto 6: LoRA desde PyTorch

**Cuaderno base:** `Cuaderno17-CC0C2.ipynb`

**Tema central:** adaptación de bajo rango.

El estudiante debe implementar o adaptar una capa LoRA, congelar pesos base, entrenar solo matrices de bajo rango y comparar parámetros totales contra parámetros entrenables.

La modificación obligatoria consiste en comparar dos valores de rank `r` y analizar el efecto sobre parámetros entrenables y resultado.

Código mínimo sugerido para mostrar en el video.

```python
class LoRALinear(nn.Module):
    def __init__(self, in_features, out_features, r=4, alpha=1.0):
        super().__init__()
        self.base = nn.Linear(in_features, out_features)
        self.base.weight.requires_grad = False
        self.base.bias.requires_grad = False

        self.A = nn.Parameter(torch.randn(in_features, r) * 0.01)
        self.B = nn.Parameter(torch.randn(r, out_features) * 0.01)
        self.alpha = alpha
        self.r = r

    def forward(self, x):
        base_out = self.base(x)
        lora_out = x @ self.A @ self.B
        return base_out + (self.alpha / self.r) * lora_out
```

Preguntas avanzadas obligatorias.

- ¿Por qué LoRA representa una actualización de bajo rango?
- ¿Qué se pierde si el rank es demasiado pequeño?
- ¿Qué riesgo aparece si el rank es demasiado grande?
- ¿Por qué congelar `W0` reduce memoria de entrenamiento?
- ¿Cómo se relaciona LoRA con la hipótesis de que las adaptaciones viven en subespacios de baja dimensión?.

### Proyecto 7: QLoRA, DPO y ORPO

**Cuaderno base:** `Cuaderno18-CC0C2.ipynb`

**Tema central:** PEFT con cuantización y entrenamiento por preferencias.

El estudiante debe explicar QLoRA, DPO y ORPO, construir un mini dataset de preferencias con pares chosen y rejected, implementar una pérdida DPO simplificada o una simulación controlada, y comparar SFT contra entrenamiento por preferencias.

La modificación obligatoria consiste en cambiar el parámetro `beta`, el margen o el criterio de preferencia, y analizar cómo cambia el score o la pérdida.

Código mínimo sugerido para mostrar en el video.

```python
def dpo_loss(logp_chosen, logp_rejected, ref_chosen, ref_rejected, beta=0.1):
    policy_diff = logp_chosen - logp_rejected
    ref_diff = ref_chosen - ref_rejected
    logits = beta * (policy_diff - ref_diff)
    return -torch.nn.functional.logsigmoid(logits).mean()
```

Preguntas avanzadas obligatorias.

- ¿Por qué DPO evita entrenar explícitamente un reward model separado?
- ¿Qué papel cumple la política de referencia?
- ¿Qué puede salir mal si las preferencias están mal construidas?
- ¿Por qué QLoRA reduce memoria, pero puede introducir degradación numérica?
- ¿Qué diferencia conceptual hay entre optimizar likelihood y optimizar preferencias?.

### Proyecto 8: adaptadores

**Cuaderno base:** `Cuaderno19-CC0C2.ipynb`

**Tema central:** adaptadores, congelamiento y parámetros entrenables.

El estudiante debe implementar adaptadores en una red pequeña, congelar el modelo base, entrenar solo adaptadores y clasificador, y comparar modelo base contra modelo con adaptadores.

La modificación obligatoria consiste en comparar dos tamaños de bottleneck y analizar exactitud, pérdida y porcentaje de parámetros entrenables.

Código mínimo sugerido para mostrar en el video.

```python
class Adapter(nn.Module):
    def __init__(self, hidden_dim, bottleneck_dim):
        super().__init__()
        self.down = nn.Linear(hidden_dim, bottleneck_dim)
        self.activation = nn.ReLU()
        self.up = nn.Linear(bottleneck_dim, hidden_dim)

    def forward(self, h):
        return h + self.up(self.activation(self.down(h)))
```

Preguntas avanzadas obligatorias.

- ¿Por qué el adaptador usa una conexión residual?
- ¿Qué representa el cuello de botella?
- ¿Qué diferencia hay entre adaptadores y LoRA?
- ¿Por qué entrenar pocos parámetros no garantiza mejor generalización?
- ¿Cómo decidirías el tamaño del bottleneck si tuvieras restricciones de memoria?.

#### Preguntas transversales obligatorias

Además de las preguntas específicas del proyecto, todo estudiante debe responder al menos cinco de las siguientes preguntas en el video.

- ¿Qué parte de tu trabajo corresponde a arquitectura, qué parte a entrenamiento y qué parte a inferencia?
- ¿Qué componente de tu notebook sería más difícil de detectar si estuviera mal implementado?
- ¿Qué resultado podría parecer bueno, pero ser técnicamente engañoso?
- ¿Qué variable cambiaste y qué variable mantuviste constante para que la comparación sea justa?
- ¿Qué parte de tu resultado depende del dataset y no del modelo?
- ¿Qué parte de tu resultado depende del prompt y no del aprendizaje?
- ¿Qué evidencia muestra que tu cambio no fue cosmético?
- ¿Qué error esperas si aumentas demasiado la longitud de secuencia?
- ¿Qué error esperas si reduces demasiado el número de ejemplos?
- ¿Qué significa que un modelo sea autoregresivo desde el punto de vista de la factorización de probabilidad?
- ¿Dónde aparece la distribución de probabilidad en tu notebook?
- ¿Dónde aparece la pérdida o criterio de optimización?
- ¿Qué parte de tu código controla memoria?
- ¿Qué parte de tu código controla diversidad?
- ¿Qué parte de tu código controla capacidad de adaptación?
- ¿Qué parte de tu código permite reproducibilidad?
- ¿Cómo distinguirías un error de implementación de una mala elección de hiperparámetros?
- ¿Qué resultado invalidaría tu conclusión?
- ¿Qué simplificación hiciste por limitaciones de cómputo?
- ¿Qué harías distinto si tuvieras una GPU y más datos?.

#### Requisitos mínimos del notebook

El notebook debe contener las siguientes secciones.

- Título del proyecto.
- Nombre del estudiante.
- Cuaderno base.
- Objetivo.
- Línea base.
- Modificación significativa.
- Configuración experimental.
- Dataset, prompts o corpus utilizado.
- Tabla de dimensiones.
- Evidencia de cálculo interno.
- Comparación línea base contra variante.
- Análisis de errores.
- Conclusión técnica.
- Declaración de autoría y uso de IA.
- Sección final llamada `Puente al curso`.

#### Celda de verificación personal

Cada notebook debe incluir una celda llamada `CELDA DE VERIFICACIÓN PERSONAL`.

La celda debe contener lo siguiente.

- Nombre completo del estudiante.
- Fecha de ejecución.
- Modelo usado.
- Semilla.
- Tamaño del dataset o lista de prompts.
- Frase técnica propia que explique el objetivo.
- Variante elegida según el proyecto.

Ejemplo sugerido.

```python
STUDENT_NAME = "Nombre completo"
EXECUTION_DATE = "AAAA-MM-DD"
BASE_NOTEBOOK = "CuadernoXX-CC0C2.ipynb"
MODEL_NAME = "modelo usado"
SEED = 42
VARIANT = "descripción breve de la variante"

print("Estudiante:", STUDENT_NAME)
print("Fecha:", EXECUTION_DATE)
print("Cuaderno base:", BASE_NOTEBOOK)
print("Modelo:", MODEL_NAME)
print("Semilla:", SEED)
print("Variante:", VARIANT)
```

#### Requisitos mínimos del README

El archivo `README.md` debe contener las siguientes secciones.

- Título.
- Objetivo.
- Cuaderno base.
- Resumen de la línea base.
- Modificación realizada.
- Cómo ejecutar el notebook.
- Principales resultados.
- Limitaciones.
- Qué se muestra en el video.
- Declaración de autoría y uso de IA.

#### Declaración de autoría y uso de IA

El estudiante debe incluir en el notebook y en el README una declaración breve con el siguiente contenido.

```text
Declaro que comprendo el código, los resultados y las explicaciones entregadas en esta práctica. 
Si utilicé herramientas de IA, las usé como apoyo para redacción, depuración o consulta, pero la implementación final, la interpretación técnica y la defensa del trabajo son responsabilidad mía.
```

Si el estudiante usó IA, debe indicar para qué la usó.

Ejemplos válidos.

- Usé IA para revisar redacción del README.
- Usé IA para depurar un error de forma de tensores.
- Usé IA para entender una advertencia de PyTorch.
- Usé IA para generar una primera versión de una función que luego modifiqué y expliqué.

Ejemplos no válidos.

- Usé IA para hacer todo el notebook.
- No sé qué partes hizo la IA.
- Solo ejecuté el código generado.
- No puedo explicar la función generada.

#### Rúbrica sobre 20 puntos

#### A. Video técnico y defensa asíncrona: 6 puntos

- 1 punto: explica el problema y el cuaderno base.
- 1 punto: explica la línea base.
- 1 punto: explica la modificación principal.
- 1 punto: interpreta resultados.
- 1 punto: responde preguntas avanzadas.
- 1 punto: conecta el trabajo con el curso.

#### B. Codificación en vivo: 5 puntos

- 1 punto: realiza una modificación común obligatoria.
- 1 punto: realiza una modificación específica del proyecto.
- 1 punto: predice el efecto antes de ejecutar.
- 1 punto: interpreta el resultado después de ejecutar.
- 1 punto: explica errores, cambios de forma, pérdida, parámetros o salida generada.

#### C. Evidencia interna y comprensión técnica: 4 puntos

- 1 punto: muestra tensores, matrices, logits, máscaras, parámetros o pérdida.
- 1 punto: explica dimensiones correctamente.
- 1 punto: conecta el cálculo interno con el código.
- 1 punto: justifica por qué su variante es técnicamente relevante.

#### D. Análisis experimental: 3 puntos

- 1 punto: compara línea base contra variante.
- 1 punto: incluye evidencia cuantitativa, visual o tabular.
- 1 punto: analiza limitaciones y errores.

#### E. Repositorio, notebook y README: 2 puntos

- 1 punto: notebook ordenado, ejecutable y reproducible.
- 1 punto: README claro con declaración de autoría y uso de IA.

#### Penalizaciones críticas

Estas penalizaciones tienen prioridad sobre la rúbrica.

- Video inexistente: 0/20.
- Video sin voz propia: 0/20.
- Video de 12 minutos exactos o menos: 0/20.
- Video sin codificación en vivo: 0/20.
- Video que solo lee texto o muestra celdas ya ejecutadas: 0/20.
- No responder preguntas avanzadas: máximo 10/20.
- No explicar dimensiones o parámetros centrales del proyecto: máximo 10/20.
- No comparar línea base contra variante: descuento de 3 puntos.
- No incluir README: descuento de 2 puntos.
- No declarar uso de IA: descuento de 2 puntos.
- Notebook generado automáticamente sin defensa técnica: 0/20.
- Código correcto sin explicación correcta: 0/20.
- Explicación genérica desconectada del notebook: 0/20.

#### Criterio de autenticidad

El objetivo no es impedir el uso de IA. El objetivo es impedir que el estudiante entregue un producto que no comprende.

La autenticidad se evaluará mediante la modificación en vivo, la explicación de errores, la predicción antes de ejecutar, la interpretación después de ejecutar, la explicación de dimensiones, la respuesta a preguntas avanzadas y la conexión entre notebook, código, resultado y teoría.

Un estudiante puede usar IA como apoyo, pero debe demostrar control técnico sobre el trabajo entregado.

#### Qué se considera una buena entrega

Una buena entrega parte de un cuaderno del curso, reconstruye una línea base, introduce una modificación real, compara resultados, muestra evidencia interna, explica dimensiones, analiza errores, reconoce limitaciones, usa vocabulario técnico correctamente y conecta código, matemática y resultado.

#### Qué se considera una mala entrega

Una mala entrega solo ejecuta celdas, cambia nombres o colores sin modificar el experimento, presenta texto genérico generado por IA, no explica el código, no explica tensores ni dimensiones, no interpreta resultados, no compara línea base contra variante, no muestra cálculo interno y no demuestra aprendizaje real.

#### Cierre obligatorio

Todo video y todo README deben terminar con dos secciones obligatorias.

#### Qué hice, por qué lo hice y qué significan mis resultados

El estudiante debe explicar en lenguaje propio qué implementó, qué modificó, por qué esa modificación es técnicamente relevante, qué evidencia obtuvo y qué significan los resultados.

#### Puente al curso

El estudiante debe conectar su proyecto con al menos dos temas relacionados.

- LLMs modernos.
- Fine-tuning.
- PEFT.
- LoRA.
- QLoRA.
- Alineamiento.
- DPO u ORPO.
- Agentes.
- Evaluación de LLMs.
- Eficiencia de inferencia.
- Seguridad y confiabilidad de modelos generativos.

#### Observación final para el estudiante

Esta práctica no evalúa solamente si el notebook funciona. Evalúa si el estudiante entiende el modelo, el código, los datos, la modificación realizada, los resultados obtenidos y las limitaciones del experimento.

La nota depende de la evidencia técnica mostrada en el notebook y defendida en el video.
