## Práctica Calificada 2 - CC0C2 Procesamiento del Lenguaje Natural

> **Fecha de entrega:** 7 de mayo de 2026 a las 4:00 pm, entregando el URL del repositorio que contenga todo lo pedido.
>
> Si la práctica se publica en una fecha distinta, la entrega será exactamente **una semana después de la publicación**, a las 4:00 pm.
>
> **No se aceptan entregas tardías.**

### 1. Modalidad y propósito

La presente práctica calificada es **individual**. Cada estudiante desarrollará **un proyecto distinto** a partir de los cuadernos y workbooks trabajados en la segunda parte del curso.

Esta práctica ha sido diseñada para una duración de **una semana**. Por ello, el objetivo no es construir un sistema grande, sino producir una entrega **pequeña, técnicamente defendible y conceptualmente profunda**.

El objetivo de esta práctica **no** es premiar la simple ejecución de código, ni el llenado mecánico de celdas, ni la apariencia del notebook. El objetivo es verificar si el estudiante:

- comprende los mecanismos internos de RNN, atención, Transformers o Vision Transformers
- puede reconstruir una línea base,
- puede modificarla con criterio técnico,
- puede justificar sus decisiones experimentales,
- puede interpretar resultados, errores y limitaciones,
- puede conectar el código con los cálculos internos mostrados en los workbooks.

### 2. Documentos base permitidos

Los proyectos deben construirse a partir de los siguientes materiales del curso:

1. `Learner-RNN-Workbook.xlsx`
2. `Learner-Transformer-Workbook.xlsx`
3. `Learner-Vit-Workbook.xlsx`
4. Cuadernos del curso asociados a RNN, self-attention, Transformers, traducción, clasificación de texto y Vision Transformer, especialmente los cuadernos 7, 8, 9, 10 y 11.

El estudiante puede reutilizar código del curso, pero debe identificar con claridad:

- qué parte proviene del cuaderno base,
- qué parte proviene del workbook,
- qué parte fue modificada por el estudiante,
- qué parte corresponde a su análisis propio.

### 3. Entregables obligatorios

Cada estudiante debe entregar:

1. **Un notebook** (`.ipynb`) basado en el proyecto asignado.
2. **Un video narrado** de **más de 10 minutos**, con **voz propia del estudiante**.
3. **Un archivo breve** (`README.md` o PDF de una página) que incluya:
   - objetivo,
   - cuaderno o workbook base usado,
   - línea base implementada,
   - modificación realizada,
   - resultados principales,
   - errores o limitaciones,
   - conclusión técnica.
4. **Una evidencia de cálculo interno**, que puede ser:
   - captura o tabla del cálculo manual inspirado en el workbook,
   - impresión de matrices intermedias,
   - visualización de atención,
   - verificación de dimensiones,
   - comparación entre cálculo manual y salida del modelo.

### 4. Regla académica central

En esta práctica, la **sustentación oral es una condición de validez académica** del trabajo.

El notebook, las gráficas, las tablas, el código o las celdas del workbook **no generan puntaje por sí solos** si el estudiante no demuestra comprensión real en su explicación.

#### Regla habilitante

Para que la práctica pueda ser calificada normalmente, el estudiante debe cumplir simultáneamente estas condiciones en su video:

1. **Hilvanar y aplicar correctamente por lo menos 10 conceptos obligatorios** de su proyecto.
2. Responder de manera suficiente las preguntas obligatorias de su proyecto.
3. Justificar con claridad:
   - **qué hizo**,
   - **por qué lo hizo**,
   - **qué significan sus resultados**.
4. Explicar al menos una matriz, tensor, bloque, flujo o cálculo interno relacionado con el workbook usado.

#### Consecuencia directa

Si el estudiante no cumple esas condiciones, la práctica se considera **académicamente inválida** y la calificación final será **0/20**.

Además, el estudiante deberá completar durante el video una sección representativa del workbook asociado al proyecto. Esta parte será evaluada en la rúbrica específica del workbook y, si no se cumple, tendrá el descuento indicado en las penalizaciones.

#### Importante

- Mencionar conceptos solo de nombre **no cuenta**.
- Leer definiciones memorizadas sin conectarlas con el notebook **no cuenta**.
- Mostrar celdas ejecutadas sin interpretar sus valores **no cuenta**.
- Leer un texto generado por IA sin apropiación conceptual **no cuenta**.
- Explicar solo la salida final sin explicar el flujo interno **no cuenta**.
- Si el docente tiene que recordarle después qué conceptos debía explicar, ese aviso no recupera puntaje.

### 5. Regla frente al uso de IA

El uso de herramientas de IA **no está prohibido**, pero en esta práctica **no da puntaje por sí mismo**.

Lo que se evalúa es si el estudiante puede defender técnicamente su trabajo. En particular:

- Si el estudiante presenta código que no puede explicar, se asumirá que no hay evidencia suficiente de aprendizaje.
- Si el estudiante presenta resultados que no puede interpretar, se asumirá que no comprende el experimento.
- Si el estudiante usa discurso genérico que no se conecta con su notebook, se asumirá que no estudió el contenido del proyecto.
- Si el estudiante no puede explicar las dimensiones de sus tensores, matrices o embeddings, se asumirá que no domina el flujo del modelo.

En consecuencia, **código correcto sin explicación correcta no aprueba la práctica**.

### 6. Estructura obligatoria del video

El video debe seguir esta estructura mínima:

1. Presentación del problema.
2. Identificación del proyecto asignado.
3. Identificación del cuaderno o workbook base.
4. Explicación de la línea base.
5. Explicación de la modificación realizada.
6. Representación de entrada y salida.
7. Dimensiones principales de los tensores o matrices.
8. Arquitectura o flujo del modelo.
9. Función de pérdida y optimización, si corresponde.
10. Comparación entre línea base y variante.
11. Resultados y su interpretación.
12. Análisis de errores o limitaciones.
13. Explicación hilvanada de los conceptos obligatorios.
14. Explicación de una matriz, bloque o cálculo interno relacionado con el workbook.
15. Completar en pantalla una sección mínima del workbook asociado al proyecto.
16. Conectar ese cálculo del workbook con el resultado del notebook.
17. Sección final: **"Qué hice, por qué lo hice y qué significan mis resultados"**.
18. Sección final: **"Puente al curso"**.

### 7. Capa adicional obligatoria

Todos los proyectos deben incluir cuatro capas:

#### Capa A. Línea base identificable

El estudiante debe ejecutar, reconstruir o implementar una versión mínima del cuaderno o workbook base.

#### Capa B. Modificación significativa

El estudiante debe introducir una modificación real. No se aceptan cambios superficiales como:

- renombrar variables,
- cambiar colores de gráficos,
- mover celdas,
- alterar texto sin alterar el experimento,
- cambiar una semilla sin analizar el efecto,
- aumentar épocas sin justificar qué se está midiendo.

#### Capa C. Comparación y juicio técnico

El estudiante debe comparar línea base vs variante y emitir un juicio técnico sobre:

- qué cambió,
- por qué cree que cambió,
- qué limitación se mantiene,
- qué evidencia apoya su conclusión,
- qué tema posterior del curso podría superar esa limitación.

#### Capa D. Auditoría interna del modelo

El estudiante debe mostrar y explicar al menos uno de estos elementos:

- matriz de atención,
- tensores `Q`, `K`, `V`,
- estados ocultos de una RNN,
- efecto de una máscara,
- embeddings posicionales,
- salida de un bloque encoder o decoder,
- `class token` en ViT,
- pesos de softmax,
- verificación de dimensiones antes y después de un bloque.

### 8. Proyectos individuales

> El docente asignará **un proyecto por estudiante**. Hay **8 proyectos base**. Si hay más estudiantes, se pueden repetir proyectos siempre que cambie el dataset, la tarea, la variante o la pregunta experimental.


#### Proyecto 1. Self-attention desde producto punto, escalamiento y softmax

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, hoja `Attention_Blank`, y Cuaderno 8.
**Tema central:** reconstruir self-attention desde matrices `Q`, `K`, `V` y leer técnicamente la matriz de atención.

##### Trabajo mínimo

El estudiante debe implementar un ejemplo pequeño de self-attention con al menos 4 tokens.

Debe mostrar explícitamente:

- embeddings de entrada,
- matrices `Q`, `K`, `V`,
- scores por producto punto,
- escalamiento por `sqrt(dk)`,
- softmax,
- salida ponderada por `V`.

##### Capa adicional de dificultad

Debe comparar al menos dos variantes:

- con escalamiento vs sin escalamiento,
- embeddings pequeños vs embeddings más grandes,
- attention uniforme vs attention concentrada,
- entrada con tokens similares vs tokens distintos,
- self-attention vs una representación recurrente simple.

##### Evidencias mínimas

- matriz de scores
- matriz de atención después de softmax
- visualización tipo heatmap o tabla
- interpretación token por token
- comparación línea base vs variante
- explicación de qué token atiende a cuál y por qué.

##### Conceptos obligatorios

En su exposición debe hilvanar por lo menos 10 de estos conceptos:

- token,
- embedding,
- query,
- key,
- value,
- producto punto,
- similitud,
- escalamiento,
- `sqrt(dk)`,
- softmax,
- peso de atención,
- matriz de atención,
- salida contextual,
- dependencia global,
- complejidad cuadrática.

##### Preguntas obligatorias que debe explicar

1. ¿Qué representan `Q`, `K` y `V` en tu ejemplo?
2. ¿Por qué se usa producto punto para calcular scores?
3. ¿Qué cambia cuando escalas por `sqrt(dk)`?
4. ¿Qué hace softmax sobre cada fila o columna de tu matriz?
5. ¿Qué significa que un token atienda fuertemente a otro?
6. ¿Qué patrón observaste en tu heatmap?
7. ¿Qué diferencia hubo entre la línea base y la variante?
8. ¿Dónde aparece la complejidad cuadrática?
9. ¿Qué limitación tiene este ejemplo respecto a un Transformer real?
10. ¿Cómo se relaciona tu cálculo con la hoja `Attention_Blank` del workbook?.



#### Proyecto 2. Bloque encoder Transformer con residual, LayerNorm y MLP

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, hoja `Transformer_Blank`, y Cuaderno 9.  
**Tema central:** construir y analizar un bloque encoder Transformer como composición de self-attention, residual connection, LayerNorm y feed-forward network.

##### Trabajo mínimo

El estudiante debe implementar un bloque encoder pequeño que incluya:

- self-attention,
- conexión residual,
- LayerNorm,
- MLP position-wise,
- segunda conexión residual,
- segunda normalización.

Debe comparar el bloque completo contra una versión incompleta.

##### Capa adicional de dificultad

Debe hacer una ablación con al menos dos de estos elementos:

- sin residual connection,
- sin LayerNorm,
- sin MLP,
- con diferente número de cabeceras,
- con diferente dimensión interna del MLP,
- con distinta inicialización o dropout.

##### Evidencias mínimas

- diagrama o tabla del flujo del bloque,
- verificación de dimensiones antes y después de cada subbloque,
- curva o tabla de resultados,
- comparación con y sin los componentes ablatados,
- explicación de estabilidad o degradación.

##### Conceptos obligatorios

En su exposición debe hilvanar por lo menos 10 de estos conceptos:

- encoder,
- self-attention,
- multi-head attention,
- residual connection,
- shortcut,
- LayerNorm,
- normalización,
- MLP position-wise,
- feed-forward network,
- estabilidad,
- flujo del gradiente,
- representación contextual,
- dimensión del modelo,
- dimensión interna,
- ablación.

##### Preguntas obligatorias que debe explicar

1. ¿Qué operación realiza primero tu bloque encoder?
2. ¿Por qué la salida de self-attention se suma con la entrada?
3. ¿Qué normaliza LayerNorm y por qué ayuda?
4. ¿Qué hace el MLP position-wise?
5. ¿Qué dimensiones se preservan dentro del bloque?
6. ¿Qué componente fue más importante según tu ablación?
7. ¿Qué ocurrió al retirar residual, LayerNorm o MLP?
8. ¿Cómo interpretas la estabilidad del entrenamiento?
9. ¿Por qué este bloque puede apilarse varias veces?
10. ¿Cómo se conecta tu implementación con la hoja `Transformer_Blank`?.

#### Proyecto 3. Encoder-decoder Transformer y cross-attention en una tarea pequeña

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, hoja `Transformer_Blank`, Cuaderno 10.  
**Tema central:** analizar el flujo encoder-decoder y diferenciar self-attention de cross-attention.

##### Trabajo mínimo

El estudiante debe implementar o adaptar una tarea pequeña de traducción, transformación de secuencia o mapeo simbólico.

Debe identificar:

- secuencia de entrada,
- secuencia de salida desplazada a la derecha,
- salida esperada,
- encoder output,
- self-attention del decoder,
- cross-attention entre decoder y encoder.

##### Capa adicional de dificultad

Debe comparar dos variantes entre:

- con cross-attention vs sin cross-attention,
- secuencia corta vs secuencia más larga,
- vocabulario pequeño vs vocabulario ampliado,
- teacher forcing alto vs bajo,
- una capa vs dos capas,
- máscara causal correcta vs incorrecta.

##### Evidencias mínimas

- ejemplo completo entrada-salida,
- explicación de shifted-right,
- tabla de dimensiones del encoder y decoder,
- visualización o impresión de pesos de cross-attention,
- comparación de errores,
- discusión de por qué el decoder necesita mirar al encoder.

##### Conceptos obligatorios

En su exposición debe hilvanar por lo menos 10 de estos conceptos:

- encoder,
- decoder,
- self-attention,
- cross-attention,
- query,
- key,
- value,
- máscara causal,
- shifted-right,
- teacher forcing,
- vocabulario,
- token objetivo,
- distribución de salida,
- pérdida por token,
- alineamiento,
- dependencia entre secuencias.

##### Preguntas obligatorias que debe explicar

1. ¿Qué procesa el encoder y qué procesa el decoder?
2. ¿Qué significa desplazar la salida a la derecha?
3. ¿Por qué el decoder usa máscara causal?
4. ¿Qué diferencia hay entre self-attention y cross-attention?
5. ¿De dónde vienen `Q`, `K` y `V` en la cross-attention?
6. ¿Qué patrón observaste en los pesos de cross-attention?
7. ¿Qué errores aparecen cuando el decoder no usa bien el contexto del encoder?
8. ¿Qué cambió entre tu línea base y tu variante?
9. ¿Por qué este esquema es útil para traducción?
10. ¿Cómo se relaciona tu flujo con el workbook de Transformer?.


#### Proyecto 4. Transformer decoder-only para modelado autoregresivo

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, Cuaderno 9 y Cuaderno 11.  
**Tema central:** comprender un Transformer tipo decoder-only como modelo que predice el siguiente token usando máscara causal.

##### Trabajo mínimo

El estudiante debe entrenar o adaptar un modelo pequeño decoder-only para predicción de siguiente token.

Debe mostrar:

- tokenización,
- embeddings,
- codificación posicional,
- máscara causal,
- predicción del siguiente token,
- pérdida autoregresiva.

##### Capa adicional de dificultad

Debe comparar al menos dos estrategias:

- temperatura baja vs alta,
- greedy decoding vs sampling,
- top-k vs top-p,
- longitud corta vs larga,
- embedding pequeño vs mayor,
- una cabecera vs varias cabeceras.

##### Evidencias mínimas

- muestra de texto o secuencia generada
- curva o tabla de pérdida
- ejemplo de predicción de siguiente token
- explicación de la máscara causal
- comparación de estrategias de decodificación
- análisis de errores o repeticiones.

##### Conceptos obligatorios

En su exposición debe hilvanar por lo menos 10 de estos conceptos:

- decoder-only,
- autoregresión,
- siguiente token,
- máscara causal,
- contexto,
- embedding,
- codificación posicional,
- logits,
- softmax,
- entropía o incertidumbre,
- temperatura,
- top-k,
- top-p,
- sampling,
- repetición,
- pérdida cross-entropy.

##### Preguntas obligatorias que debe explicar

1. ¿Qué significa predecir el siguiente token?
2. ¿Por qué el modelo no debe ver tokens futuros?
3. ¿Cómo funciona la máscara causal en tu implementación?
4. ¿Qué representa la distribución de salida?
5. ¿Qué efecto tuvo la temperatura?
6. ¿Qué diferencia observaste entre greedy, top-k o top-p?
7. ¿Qué tipo de errores o repeticiones aparecieron?
8. ¿Qué limitaciones tiene tu dataset o vocabulario?
9. ¿Cómo se relaciona este proyecto con un LLM?
10. ¿Qué parte del cálculo del workbook ayuda a entender tu decoder?.

#### Proyecto 5. Vision Transformer desde imagen a tokens

**Documentos base:** `Learner-Vit-Workbook.xlsx`  
**Tema central:** entender cómo una imagen se transforma en una secuencia de patches y cómo un Transformer puede clasificarla.

##### Trabajo mínimo

El estudiante debe implementar o adaptar una versión pequeña de Vision Transformer para clasificación simple.

Debe mostrar explícitamente:

- división de imagen en patches,
- aplanamiento de patches,
- proyección lineal,
- token `[class]`,
- embeddings posicionales,
- bloque de self-attention,
- MLP final,
- softmax de clases.

##### Capa adicional de dificultad

Debe comparar al menos dos variantes:

- patch pequeño vs patch grande,
- con token `[class]` vs pooling promedio,
- con embedding posicional vs sin embedding posicional,
- una cabecera vs múltiples cabeceras,
- una capa vs dos capas,
- diferente dimensión de embedding.

##### Evidencias mínimas

- imagen o ejemplo de entrada
- visualización de patches
- tabla de dimensiones desde imagen hasta tokens
- comparación de variantes
- curva o tabla de resultados
- explicación de qué representa el token `[class]`
- análisis de errores de clasificación.

##### Conceptos obligatorios

En su exposición debe hilvanar por lo menos 10 de estos conceptos:

- patch,
- IM2COL,
- flatten,
- proyección lineal,
- token `[class]`,
- embedding posicional,
- secuencia visual,
- self-attention,
- multi-head attention,
- Add & Norm,
- LayerNorm,
- MLP feed-forward,
- logits,
- softmax,
- cross-entropy,
- clasificación.

##### Preguntas obligatorias que debe explicar

1. ¿Cómo conviertes una imagen en una secuencia de tokens?
2. ¿Qué representa cada patch?
3. ¿Qué hace la proyección lineal de patches?
4. ¿Para qué sirve el token `[class]`?
5. ¿Qué aporta el embedding posicional?
6. ¿Qué ocurre si cambias el tamaño del patch?
7. ¿Qué diferencia hubo entre tus variantes?
8. ¿Qué errores de clasificación observaste?
9. ¿Por qué ViT usa atención sobre patches y no convoluciones tradicionales?
10. ¿Cómo se relaciona tu implementación con el `Learner-Vit-Workbook.xlsx`?.

#### Proyecto 6. Transformer encoder para clasificación de texto

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, hoja `Transformer_Blank`, y Cuaderno 11
**Tema central:** usar un Transformer encoder para clasificar textos y analizar cómo una secuencia de tokens se convierte en una predicción de clase.

##### Trabajo mínimo

El estudiante debe implementar o adaptar un clasificador de texto pequeño usando `TransformerEncoder`.

Puede usar:

* AG_NEWS,
* frases cortas construidas manualmente,
* mini dataset de noticias,
* mini dataset de sentimientos,
* clasificación binaria o multiclase.

Debe mostrar:

* tokenización,
* vocabulario,
* padding,
* embeddings,
* codificación posicional,
* bloque encoder,
* pooling o token especial,
* logits,
* softmax,
* predicción de clase.

##### Capa adicional de dificultad

Debe comparar al menos una variante:

* pooling promedio vs primer token,
* con codificación posicional vs sin codificación posicional,
* una capa encoder vs dos capas,
* una cabecera vs varias cabeceras,
* embedding pequeño vs embedding mayor,
* dropout bajo vs dropout alto.

##### Evidencias mínimas

* ejemplo de texto de entrada y etiqueta esperada,
* tabla de dimensiones: tokens, embeddings, salida del encoder, logits,
* curva o tabla de accuracy/loss,
* matriz de atención o salida intermedia del encoder,
* comparación línea base vs variante,
* análisis de errores de clasificación.

##### Conceptos obligatorios

Debe hilvanar por lo menos 10 de estos conceptos:

* tokenización,
* vocabulario,
* padding,
* embedding,
* codificación posicional,
* Transformer encoder,
* self-attention,
* representación contextual,
* pooling,
* logits,
* softmax,
* cross-entropy,
* clasificación multiclase,
* overfitting,
* matriz de atención,
* dimensión del modelo.

##### Preguntas obligatorias

1. ¿Cómo conviertes un texto en una secuencia de índices?
2. ¿Qué representa cada embedding antes de entrar al encoder?
3. ¿Por qué necesitas padding en un batch?
4. ¿Qué aporta la codificación posicional?
5. ¿Qué produce el Transformer encoder para cada token?
6. ¿Cómo conviertes la salida secuencial en una sola predicción?
7. ¿Qué representan los logits?
8. ¿Qué mide la pérdida cross-entropy?
9. ¿Qué cambió entre la línea base y la variante?
10. ¿Qué errores de clasificación observaste y cómo los interpretas?
11. ¿Qué matriz, tensor o bloque interno conectaste con el workbook?.

#### Proyecto 7. Codificación posicional en Transformers

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, hoja `Transformer_Blank`, Cuaderno 9 y Cuaderno 11
**Tema central:** estudiar por qué un Transformer necesita información de posición y qué ocurre cuando se cambia o elimina la codificación posicional.

##### Trabajo mínimo

El estudiante debe implementar una tarea pequeña donde el orden importe. Por ejemplo:

* clasificar secuencias como "correctas" o "invertidas",
* detectar si una palabra aparece antes que otra,
* clasificar frases donde el orden cambia el significado,
* predecir una etiqueta según la posición de un token clave.

Debe comparar:

* modelo con codificación posicional,
* modelo sin codificación posicional.

##### Capa adicional de dificultad

Debe agregar una variante adicional:

* codificación posicional sinusoidal vs aprendida,
* secuencia corta vs secuencia larga,
* posición absoluta vs sin posición,
* embedding pequeño vs grande,
* con una cabecera vs varias cabeceras.

##### Evidencias mínimas

* ejemplos donde el orden cambia la etiqueta,
* tabla de dimensiones de tokens, embeddings y posiciones,
* visualización o tabla de embeddings posicionales,
* comparación de resultados con/sin posición,
* análisis de errores cuando el modelo no recibe información posicional,
* conexión con el bloque Transformer del workbook.

##### Conceptos obligatorios

Debe hilvanar por lo menos 10 de estos conceptos:

* orden secuencial,
* token,
* embedding,
* embedding posicional,
* codificación sinusoidal,
* codificación aprendida,
* suma embedding + posición,
* self-attention,
* permutación,
* representación contextual,
* dimensión del modelo,
* secuencia,
* generalización a longitudes mayores,
* matriz de atención,
* clasificación.

##### Preguntas obligatorias

1. ¿Por qué self-attention por sí sola no distingue el orden de los tokens?
2. ¿Qué información agrega la codificación posicional?
3. ¿Cómo se suma la posición al embedding del token?
4. ¿Qué dimensiones deben coincidir para poder sumar token embedding y positional embedding?
5. ¿Qué pasó cuando retiraste la codificación posicional?
6. ¿Qué diferencia viste entre codificación sinusoidal y aprendida, si comparaste ambas?
7. ¿Qué errores aparecen cuando dos secuencias tienen los mismos tokens pero distinto orden?
8. ¿Cómo se refleja la posición en la matriz de atención?
9. ¿Qué limitación mantiene tu experimento?
10. ¿Cómo conecta este proyecto con el Transformer encoder del curso?.


#### Proyecto 8. Máscara causal y predicción del siguiente token

**Documentos base:** `Learner-Transformer-Workbook.xlsx`, hoja `Attention_Blank`, hoja `Transformer_Blank`, y Cuaderno 9.
**Tema central:** demostrar qué hace una máscara causal dentro de self-attention y por qué es necesaria para predicción autoregresiva.

#### Trabajo mínimo

El estudiante debe construir un ejemplo pequeño de predicción del siguiente token usando un Transformer decoder-only o una capa de atención causal.

Debe mostrar:

* secuencia de entrada,
* secuencia objetivo desplazada,
* embeddings,
* matriz de scores,
* máscara causal,
* softmax después de la máscara,
* predicción del siguiente token.

#### Capa adicional de dificultad

Debe comparar al menos dos variantes:

* con máscara causal vs sin máscara causal,
* máscara correcta vs máscara incorrecta,
* secuencia corta vs secuencia más larga,
* greedy decoding vs sampling,
* temperatura baja vs temperatura alta,
* una cabecera vs varias cabeceras.

#### Evidencias mínimas

* matriz de atención antes y después de aplicar la máscara,
* visualización tipo heatmap de la máscara causal,
* ejemplo de predicción paso a paso,
* comparación entre modelo con fuga de información y modelo causal,
* tabla de pérdida o errores por token,
* explicación de por qué el modelo no debe mirar tokens futuros.

#### Conceptos obligatorios

Debe hilvanar por lo menos 10 de estos conceptos:

* autoregresión,
* siguiente token,
* máscara causal,
* token futuro,
* fuga de información,
* self-attention,
* query,
* key,
* value,
* scores,
* softmax,
* logits,
* cross-entropy,
* shifted-right,
* decoding,
* temperatura,
* greedy decoding,
* sampling.

#### Preguntas obligatorias

1. ¿Qué significa predecir el siguiente token?
2. ¿Cuál es la entrada y cuál es el objetivo desplazado?
3. ¿Por qué el modelo no debe ver tokens futuros?
4. ¿Cómo se construye la máscara causal?
5. ¿Qué valores de la matriz quedan bloqueados?
6. ¿Qué cambia en softmax antes y después de aplicar la máscara?
7. ¿Qué ocurre si entrenas o evalúas sin máscara causal?
8. ¿Qué diferencia observaste entre greedy decoding y sampling?
9. ¿Qué errores o repeticiones aparecieron?
10. ¿Cómo se conecta este cálculo con las hojas `Attention_Blank` y `Transformer_Blank`?.

### 9. Requisitos mínimos del notebook

El notebook debe contener, como mínimo:

1. título del proyecto
2. objetivo
3. identificación del documento base
4. línea base implementada
5. modificación realizada
6. configuración experimental
7. descripción del dataset o secuencia usada
8. tabla de dimensiones de los tensores principales
9. comparación entre línea base y variante
10. al menos una figura, tabla o resumen numérico
11. al menos una evidencia de cálculo interno
12. análisis de errores o limitaciones
13. conclusión técnica
14. sección final llamada **"Puente al curso"**.

### 10. Requisitos mínimos del video

El video debe:

- durar **más de 10 minutos**
- tener **voz propia del estudiante**
- mostrar el notebook o los resultados mientras explica
- incluir los **conceptos obligatorios** de su proyecto
- responder las **preguntas obligatorias** de su proyecto
- explicar al menos un cálculo interno o matriz relacionada con el workbook
- terminar con las secciones:
  - **"Qué hice, por qué lo hice y qué significan mis resultados"**
  - **"Puente al curso"**.
- completar en pantalla una sección mínima del workbook asociado al proyecto, explicando el cálculo y conectándolo con el notebook.

### 11. Rúbrica de evaluación sobre 20 puntos

#### A. Sustentación oral técnica y uso de conceptos - 8 puntos

Este criterio es **habilitante**.

##### Para acceder a esta parte de la rúbrica, el estudiante debe:

- explicar correctamente **al menos 10 conceptos obligatorios** de su proyecto
- responder las preguntas obligatorias de forma suficiente
- justificar qué hizo, por qué lo hizo y qué significan sus resultados
- explicar una matriz, tensor, bloque o cálculo interno relacionado con el workbook.

Si no cumple eso, la práctica se califica con **0/20**.

##### Desglose

- **1 pts:** explica correctamente el problema, los datos y la representación.
- **1 pts:** explica arquitectura, tensores, bloques y flujo interno.
- **2 pts:** explica entrenamiento, pérdida, optimización o criterio de comparación.
- **2 pts:** analiza errores, límites o resultados inesperados.
- **2 pts:** conecta su trabajo con temas posteriores del curso.

#### B. Workbook completado y explicado durante el video - 5 puntos
- **1 pts:** completa una sección correcta del workbook asociado al proyecto
- **1 pts:** explica dimensiones de matrices, tensores o embeddings
- **1.5 pts:** desarrolla correctamente el cálculo interno.
- **1 pts:** conecta el cálculo con una celda o resultado del notebook
- **0.5 pts:** interpreta qué significa el resultado obtenido.

#### C. Análisis experimental - 4 puntos

- **2 pts:** comparación clara entre línea base y variante.
- **1 pt:** evidencia cuantitativa o visual suficiente.
- **1 pt:** interpretación razonada de resultados.

#### D. Notebook y calidad técnica - 2 puntos

- **1 pt:** orden, claridad, reproducibilidad y estructura.
- **1 pt:** evidencia suficiente de modificación propia y experimento real.

#### E. Claridad expositiva - 1 punto

- **0.5 pt:** secuencia lógica del video.
- **0.5 pt:** audio claro, organización y cierre entendible.

### 12. Penalizaciones obligatorias

Estas penalizaciones tienen prioridad sobre la rúbrica.

#### Penalizaciones críticas

- **Código o notebook sin video:** **0/20**.
- **Video sin voz propia del estudiante:** **0/20**.
- **Video menor o igual a 10 minutos:** **0/20**.
- **Video que solo muestra ejecución sin explicación conceptual:** **0/20**.
- **No responder las preguntas obligatorias del proyecto:** **0/20**.
- **No completar durante el video una sección mínima del workbook asociado: descuento de 5 puntos, siempre que la sustentación siga siendo válida**.
- **Mostrar el workbook ya lleno sin explicar el cálculo: se considera equivalente a no haber explicado el cálculo interno.**
- **No justificar qué hizo, por qué lo hizo y qué significan sus resultados:** **0/20**.
- **No explicar ningún cálculo interno del modelo:** **0/20**.

> No se puntúa como 0, sino como 1, si el sistema de notas no acepta 0 como calificación.

#### Penalizaciones por conceptos

- **No hilvanar por lo menos 10 conceptos obligatorios del proyecto:** **0/20**.
- **Mencionar conceptos solo de nombre, sin aplicarlos al notebook:** se considera equivalente a no haberlos explicado.
- **Usar términos técnicos de manera reiteradamente incorrecta:** puede invalidar la sustentación.
- **Confundir dimensiones, matrices o flujo del modelo sin corregirse:** puede invalidar la sustentación.
- **Si el docente tiene que avisarle al estudiante qué conceptos debía explicar, ese aviso no recupera puntaje ni valida la sustentación.**

#### Penalizaciones por entrega superficial

- **No comparar línea base vs variante:** descuento de **4 puntos**, siempre que la sustentación siga siendo válida.
- **No analizar errores o limitaciones:** descuento de **3 puntos**, siempre que la sustentación siga siendo válida.
- **No incluir evidencia de cálculo interno:** descuento de **3 puntos**, siempre que la sustentación siga siendo válida.
- **No incluir la sección "Puente al curso":** descuento de **2 puntos**, siempre que la sustentación siga siendo válida.
- **No identificar qué parte proviene del cuaderno/workbook base y qué parte fue modificación propia:** descuento de **1 punto**, siempre que la sustentación siga siendo válida.
- **No reportar dimensiones de tensores o matrices principales:** descuento de **1 punto**, siempre que la sustentación siga siendo válida.

### 13. Qué se considera una buena entrega

Se considera buena entrega aquella que:

- parte de un cuaderno o workbook base
- construye una línea base clara
- introduce una modificación real
- compara resultados
- muestra una evidencia interna del cálculo del modelo
- analiza errores
- usa con precisión el vocabulario técnico
- responde las preguntas de su proyecto
- explica dimensiones, tensores y flujo
- y demuestra que el estudiante **entiende lo que hizo**.

### 14. Qué se considera una mala entrega

Se considera mala entrega aquella que:

- solo ejecuta celdas
- solo llena tablas del workbook sin interpretarlas
- recita definiciones sin conexión con el notebook
- muestra gráficos sin interpretarlos
- usa IA para generar código o discurso sin comprensión
- no identifica la diferencia entre línea base y variante
- no explica al menos 10 conceptos obligatorios
- no responde las preguntas del proyecto
- no explica dimensiones ni matrices
- no puede justificar qué hizo, por qué lo hizo y qué significan sus resultados.

### 15. Recomendación de alcance

Como la práctica dura una semana, se recomienda:

- usar datasets pequeños
- entrenar modelos pequeños
- limitar el número de épocas
- priorizar comprensión sobre tamaño
- guardar resultados en tablas simples
- incluir pocas gráficas, pero bien interpretadas
- elegir una sola modificación principal y una ablación pequeña
- no intentar entrenar un modelo grande desde cero.

### 16. Observación final

La práctica ha sido diseñada para que sea **realizable en una semana**. La exigencia principal no estará en implementar un sistema enorme, sino en producir una entrega **pequeña pero defendible**, con comprensión real de RNN, atención, Transformers o Vision Transformers.

El estudiante debe demostrar que entiende no solo la salida final del modelo, sino también el flujo interno que la produce.
