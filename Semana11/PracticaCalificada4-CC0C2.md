### Práctica Calificada 4 - CC0C2 Procesamiento del Lenguaje Natural

**Tema general:** agentes basados en LLMs, arquitectura RAG, retrieval semántico, evaluación de sistemas de recuperación y generación fundamentada.

**Modalidad:** individual.

**Entrega:** repositorio con un notebook, README, video técnico y evidencia de ejecución.

**Duración del video:** estrictamente mayor que 12 minutos.

**Condición central:** no habrá exposición presencial por razones de tiempo. Por ello, el video será tratado como evidencia principal de autoría, comprensión técnica y defensa del trabajo.

#### Propósito de la evaluación

La Práctica Calificada 4 evalúa si el estudiante comprende y puede defender técnicamente los conceptos trabajados en los cuadernos 20, 21, 22 y 23 del curso CC0C2.

El objetivo no es premiar la simple ejecución de código ni la generación automática de notebooks mediante IA. El objetivo es verificar si el estudiante puede construir un sistema funcional, modificarlo de forma significativa, explicar el flujo interno del retrieval, justificar decisiones de arquitectura, interpretar métricas de evaluación y defender técnicamente su propio trabajo.

El uso de IA no está prohibido como apoyo. Sin embargo, una entrega producida con IA y no comprendida por el estudiante será considerada inválida.

El código correcto sin una explicación correcta no aprueba la Práctica.

#### Documentos base permitidos

Cada estudiante debe construir su trabajo a partir de uno o más de los siguientes cuadernos del curso.

- `Cuaderno20-CC0C2.ipynb`: agentes basados en LLMs, herramientas, memoria y planificación.
- `Cuaderno21-CC0C2.ipynb`: embeddings, búsqueda semántica, chunking y vector stores.
- `Cuaderno22-CC0C2.ipynb`: arquitectura RAG, `retrieve`, `rerank`, `refine` y `generate`.
- `Cuaderno23-CC0C2.ipynb`: evaluación de retrieval y grounded generation.

El estudiante puede reutilizar código del curso, pero debe identificar claramente qué parte proviene del cuaderno base, qué parte fue modificada, qué parte fue agregada por el estudiante y qué parte recibió apoyo de IA.

#### Entregables obligatorios

Cada estudiante debe entregar la dirección URL de su repositorio con los siguientes elementos.

- Un notebook `.ipynb` reproducible.
- Un archivo `README.md`.
- Un video técnico con voz propia.
- Evidencia de ejecución interna.
- Comparación entre línea base y variante.
- Registro de ejecución con semilla, entorno, librerías, modelo usado y datos usados.
- Una sección llamada `Declaración de autoría y uso de IA`.

#### Modalidad definitiva de evaluación

La Práctica se evaluará únicamente mediante la entrega del repositorio y el video técnico.

No habrá exposición presencial.

El video debe cumplir el rol de defensa asíncrona. Por esta razón, no debe ser una presentación superficial ni una lectura de texto. Debe mostrar al estudiante trabajando con su notebook, programando cambios, ejecutando celdas, prediciendo efectos, interpretando resultados y explicando técnicamente el código.

La duración debe ser estrictamente mayor que 12 minutos. Se recomienda una duración entre 14 y 18 minutos.

Un video de 12 minutos exactos o menos no será válido.

#### Regla habilitante de validez académica

La Práctica solo será calificada si el video contiene todos los elementos siguientes:

- Explicación del objetivo del proyecto.
- Identificación del cuaderno base usado.
- Explicación de la línea base.
- Explicación de la modificación principal.
- Codificación en vivo de al menos dos cambios.
- Ejecución de esos cambios.
- Predicción del efecto esperado antes de ejecutar.
- Interpretación del resultado obtenido después de ejecutar.
- Explicación de embeddings, chunks, vectores, scores de similitud, métricas de evaluación o flujo del agente, según corresponda.
- Respuesta a preguntas técnicas avanzadas.
- Cierre técnico sobre qué hizo, por qué lo hizo y qué significan sus resultados.

Si el video solo muestra celdas ya ejecutadas, solo lee texto, solo describe resultados o no incluye codificación en vivo, la práctica será inválida.

#### Regla frente a entregas generadas por IA

Se considerará entrega superficial o inválida aquella en la que el estudiante realice una o más de las siguientes acciones.

- Lee texto genérico sin conectarlo con su notebook.
- No puede explicar sus propias funciones.
- No puede explicar dimensiones de embeddings, scores de similitud, flujo de retrieval o métricas de evaluación.
- No puede justificar por qué eligió una variante.
- No puede interpretar los resultados.
- No modifica una celda simple durante el video.
- No explica una línea de código relevante.
- Presenta resultados sin reproducibilidad mínima.
- Presenta un notebook aparentemente correcto, pero sin defensa técnica real.

La IA puede usarse como apoyo. La evaluación se centra en apropiación conceptual, defensa técnica y trazabilidad del trabajo.

#### Estructura obligatoria del video

El video debe seguir esta estructura:

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
- Explicación de embeddings, chunks, vectores, scores de similitud, métricas o flujo del agente.
- Comparación entre línea base y variante.
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

Puede elegir una de las siguientes opciones:

- Cambiar el tamaño de chunk y explicar cómo afecta la granularidad del retrieval.
- Cambiar el número de documentos recuperados (top_k) y explicar su impacto en precisión y cobertura.
- Cambiar el modelo de embeddings y explicar cómo cambia la representación semántica.
- Cambiar la función de similitud (`cosine`, `dot`, `euclidean`) y explicar su efecto en el ranking.
- Cambiar el umbral de similitud y explicar cómo filtra resultados irrelevantes.
- Cambiar el prompt del agente o del sistema RAG y explicar cómo afecta la generación.
- Cambiar la estrategia de chunking (`fixed`, `recursive`, `semantic`) y explicar sus ventajas y limitaciones.
- Cambiar el número de ejemplos en el dataset de evaluación y explicar su efecto en las métricas.

#### Ejercicio B: modificación específica según el proyecto

Además del cambio común, el estudiante debe hacer una modificación técnica relacionada directamente con su proyecto.

La modificación debe ser visible en el video, debe ejecutarse y debe interpretarse.

### Proyecto 1: Agente basado en LLM con herramientas

**Cuaderno base:** `Cuaderno20-CC0C2.ipynb`

**Tema central:** diseño de agente, definición de herramientas, ciclo de razonamiento y ejecución.

El estudiante debe construir un agente basado en LLM que tenga al menos dos herramientas definidas por el estudiante. Debe mostrar el ciclo de pensamiento, decisión de herramienta, ejecución y observación. Debe comparar al menos dos estrategias de planificación.

La modificación obligatoria puede ser agregar una herramienta nueva, cambiar la estrategia de planificación, modificar el formato de memoria o alterar el prompt del sistema.

La evidencia interna mínima debe incluir el estado del agente en cada paso, la decisión de herramienta tomada, la entrada y salida de cada herramienta, y el texto generado por el LLM en cada iteración.

Código mínimo sugerido para mostrar en el video:

```python
print("Paso:", step)
print("Pensamiento:", thought)
print("Herramienta elegida:", tool_name)
print("Argumentos:", tool_args)
print("Resultado de herramienta:", tool_result)
print("Respuesta final:", final_answer)
```

Preguntas avanzadas obligatorias:

- Si el agente elige una herramienta incorrecta, ¿qué mecanismo podría detectar o corregir ese error?
- ¿Qué diferencia hay entre un agente reactivo y un agente con planificación explícita?
- ¿Por qué la memoria del agente es crítica para tareas de múltiples pasos?
- ¿Qué riesgo introduce permitir que el agente ejecute herramientas arbitrarias?
- ¿Cómo se relaciona el diseño de herramientas con la calidad del razonamiento del agente?.

### Proyecto 2: Embeddings y búsqueda semántica

**Cuaderno base:** `Cuaderno21-CC0C2.ipynb`

**Tema central:** representación vectorial, similitud semántica, indexación y recuperación.

El estudiante debe cargar un corpus de texto, generar embeddings con un modelo preentrenado, construir un índice de búsqueda, y comparar búsqueda por palabras clave contra búsqueda semántica. Debe analizar casos donde una funciona mejor que la otra.

La modificación obligatoria consiste en comparar dos modelos de embeddings distintos y analizar diferencias en calidad de retrieval para consultas específicas.

Código mínimo sugerido para mostrar en el video:

```python
print("Query:", query)
print("Embedding shape:", query_embedding.shape)
print("Top 5 similitudes:", similarities[:5])
for idx, score in zip(top_indices, top_scores):
    print(f"Doc {idx}: score={score:.4f} | {corpus[idx][:100]}")
```

Preguntas avanzadas obligatorias:

- ¿Por qué embeddings de oraciones cortas pueden capturar significado incluso sin contexto extenso?
- ¿Qué limitación tiene la similitud coseno cuando los embeddings no están normalizados?
- ¿Cómo afecta el tamaño del vocabulario del modelo de embeddings a la calidad de la representación?
- ¿Por qué una búsqueda semántica puede devolver resultados irrelevantes que son numéricamente similares?
- ¿Qué diferencia hay entre un embedding de promedio de tokens y un embedding de pooling especializado?.

### Proyecto 3: Chunking y construcción de un vector store

**Cuaderno base:** `Cuaderno21-CC0C2.ipynb`

**Tema central:** estrategias de segmentación, vectorización de chunks y persistencia de índice.

El estudiante debe implementar al menos dos estrategias de chunking sobre un corpus largo, vectorizar los chunks, construir un vector store en memoria o persistente, y comparar la calidad de retrieval entre las dos estrategias.

La modificación obligatoria consiste en comparar dos estrategias de chunking (por ejemplo, fixed size vs recursive) y analizar cómo afectan la recuperación de respuestas completas.

Código mínimo sugerido para mostrar en el video:

```python
print("Estrategia:", strategy_name)
print("Número de chunks:", len(chunks))
print("Tamaño promedio de chunk:", avg_chunk_size)
print("Chunk de ejemplo:", chunks[0][:200])
print("Top retrieval:", retrieved_chunks[0][:200])
```

Preguntas avanzadas obligatorias:

- ¿Por qué un chunk demasiado grande puede degradar la precisión del retrieval?
- ¿Por qué un chunk demasiado pequeño puede perder contexto necesario?
- ¿Qué información se pierde al dividir un documento en chunks sin solapamiento?
- ¿Cómo decidirías el tamaño de chunk si el corpus contiene tanto párrafos cortos como tablas extensas?
- ¿Qué rol cumple el overlap entre chunks y cuándo es contraproducente?.

### Proyecto 4: Arquitectura RAG básica

**Cuaderno base:** `Cuaderno22-CC0C2.ipynb`

**Tema central:** pipeline de retrieval y generación, integración de contexto recuperado en el prompt.

El estudiante debe construir un pipeline RAG completo: carga de documentos, chunking, embedding, retrieval y generación con un LLM. Debe comparar respuestas del LLM con y sin contexto recuperado para las mismas consultas.

La modificación obligatoria puede ser cambiar el número de documentos recuperados, el modelo de generación, la forma de integrar el contexto en el prompt, o agregar un paso de reranking.

Código mínimo sugerido para mostrar en el video:

```python
print("Query:", query)
print("Documentos recuperados:", len(retrieved_docs))
for i, doc in enumerate(retrieved_docs):
    print(f"Doc {i+1} (score={scores[i]:.4f}): {doc[:150]}")
print("Prompt con contexto:", prompt[:300])
print("Respuesta generada:", response)
```

Preguntas avanzadas obligatorias:

- ¿Por qué RAG puede generar respuestas incorrectas aunque el retrieval sea correcto?
- ¿Qué riesgo introduce incluir demasiados documentos en el prompt de generación?
- ¿Cómo se relaciona la calidad del chunking con la calidad de la respuesta final?
- ¿Por qué un LLM puede ignorar el contexto recuperado y generar basado en su conocimiento paramétrico?
- ¿Qué diferencia hay entre retrieval denso y retrieval híbrido (denso + esparso)?.

### Proyecto 5: RAG avanzado con rerank y refine

**Cuaderno base:** `Cuaderno22-CC0C2.ipynb`

**Tema central:** mejora de calidad de retrieval mediante reranking y refinamiento de contexto.

El estudiante debe implementar un pipeline RAG que incluya un paso de reranking después del retrieval inicial. Debe comparar la calidad de las respuestas con y sin reranking, y analizar casos donde el reranking mejora o empeora los resultados.

La modificación obligatoria consiste en comparar dos estrategias de reranking (por ejemplo, cross-encoder vs score de similitud ajustado) y analizar su efecto en la calidad final.

Código mínimo sugerido para mostrar en el video:

```python
print("Documentos antes de rerank:", len(initial_docs))
print("Documentos después de rerank:", len(reranked_docs))
for i, (doc, score) in enumerate(zip(reranked_docs, rerank_scores)):
    print(f"Rank {i+1}: score={score:.4f} | {doc[:100]}")
print("Respuesta con rerank:", response_rerank)
print("Respuesta sin rerank:", response_no_rerank)
```

Preguntas avanzadas obligatorias:

- ¿Por qué un cross-encoder puede mejorar el ranking respecto a un bi-encoder?
- ¿Qué costo computacional introduce el reranking y cuándo no vale la pena?
- ¿Cómo puede el reranking introducir sesgos que empeoren la diversidad de fuentes?
- ¿Qué relación hay entre el número de candidatos para rerank y la calidad final?
- ¿Por qué refine no es lo mismo que rerank y qué aporta cada uno?.

### Proyecto 6: Evaluación de retrieval

**Cuaderno base:** `Cuaderno23-CC0C2.ipynb`

**Tema central:** métricas de evaluación para sistemas de recuperación de información.

El estudiante debe construir un dataset de evaluación con consultas y documentos relevantes conocidos, implementar métricas como precision@k, recall@k, MRR y nDCG, y comparar al menos dos configuraciones de retrieval usando estas métricas.

La modificación obligatoria consiste en cambiar el tamaño de top_k y analizar cómo evolucionan precisión y recall, o comparar dos modelos de embeddings usando las métricas calculadas.

Código mínimo sugerido para mostrar en el video:

```python
print("Métricas de retrieval:")
print(f"Precision@5: {precision_at_5:.4f}")
print(f"Recall@5: {recall_at_5:.4f}")
print(f"MRR: {mrr:.4f}")
print(f"nDCG@10: {ndcg_at_10:.4f}")
print("Comparación configuración A vs. B:")
print(f"A: P@5={p_a:.4f}, R@5={r_a:.4f}")
print(f"B: P@5={p_b:.4f}, R@5={r_b:.4f}")
```

Preguntas avanzadas obligatorias:

- ¿Por qué precisión y recall están en tensión y como se relacionan con top_k?
- ¿Qué limitación tiene MRR cuando hay múltiples documentos relevantes?
- ¿Por qué nDCG es más informativo que precision para rankings ordenados?
- ¿Cómo se relaciona la calidad métrica de retrieval con la calidad de la respuesta generada?
- ¿Qué sesgo introduce construir tu propio dataset de evaluación?.

### Proyecto 7: evaluación de grounded generation

**Cuaderno base:** `Cuaderno23-CC0C2.ipynb`

**Tema central:** verificación de fidelidad de respuestas generadas respecto al contexto recuperado.

El estudiante debe construir un pipeline RAG y evaluar las respuestas generadas usando métricas de grounded generation como faithfulness, answer relevance y context relevance. Debe comparar al menos dos configuraciones de generación y analizar dónde el modelo alucina o se desvía del contexto.

La modificación obligatoria consiste en cambiar el prompt de generación o la temperatura y analizar cómo cambia la métrica de faithfulness.

Código mínimo sugerido para mostrar en el video:

```python
print("Evaluación de grounded generation:")
print(f"Faithfulness: {faithfulness_score:.4f}")
print(f"Answer Relevance: {relevance_score:.4f}")
print(f"Context Relevance: {context_score:.4f}")
print("Ejemplo de alucinación:")
print(f"Contexto: {context[:200]}")
print(f"Respuesta: {answer}")
print(f"Veredicto: {verdict}")
```

Preguntas avanzadas obligatorias:

- ¿Por qué una respuesta puede ser correcta en general pero no faithful al contexto?
- ¿Qué diferencia hay entre faithfulness y factual correctness?
- ¿Cómo puede un prompt de sistema reducir la tasa de alucinación?
- ¿Por qué métricas automáticas de grounded generation pueden ser engañosas?
- ¿Qué relación hay entre la temperatura de generación y la fidelidad al contexto?.

### Proyecto 8: sistema híbrido agente-RAG

**Cuaderno base:** `Cuaderno20-CC0C2.ipynb` y `Cuaderno22-CC0C2.ipynb`

**Tema central:** integración de capacidades de agente con pipeline RAG para tareas complejas.

El estudiante debe construir un sistema que combine un agente con capacidad de razonamiento y un pipeline RAG. El agente debe poder decidir cuándo consultar la base de conocimiento, cómo formular la consulta, y cómo integrar la información recuperada en su razonamiento final.

La modificación obligatoria consiste en comparar dos estrategias de decisión: agente que siempre consulta RAG vs agente que decide dinámicamente si consultar basado en la consulta.

Código mínimo sugerido para mostrar en el video:

```python
print("Consulta del usuario:", user_query)
print("Decisión del agente:", decision)
print("Consulta a vector store:", rewritten_query)
print("Documentos recuperados:", len(docs))
print("Razonamiento con contexto:", reasoning)
print("Respuesta final:", final_answer)
```

Preguntas avanzadas obligatorias:

- ¿Por qué un agente que siempre consulta RAG puede ser ineficiente?
- ¿Qué criterios podría usar un agente para decidir si necesita consultar conocimiento externo?
- ¿Cómo se relaciona la calidad de la consulta reformulada con la calidad del retrieval?
- ¿Qué riesgo introduce que el agente confíe ciegamente en los documentos recuperados?
- ¿Cómo mantendrías la coherencia del razonamiento cuando el retrieval devuelve información contradictoria?.

#### Preguntas transversales obligatorias

Además de las preguntas específicas del proyecto, todo estudiante debe responder al menos cinco de las siguientes preguntas en el video.

- ¿Qué parte de tu trabajo corresponde a retrieval, qué parte a generación y qué parte a razonamiento del agente?
- ¿Qué componente de tu notebook sería más difícil de detectar si estuviera mal implementado?
- ¿Qué resultado podría parecer bueno, pero ser técnicamente engañoso?
- ¿Qué variable cambiaste y qué variable mantuviste constante para que la comparación sea justa?
- ¿Qué parte de tu resultado depende del corpus y no del modelo?
- ¿Qué parte de tu resultado depende del prompt y no del retrieval?
- ¿Qué evidencia muestra que tu cambio no fue cosmético?
- ¿Qué error esperas si aumentas demasiado el tamaño de los chunks?
- ¿Qué error esperas si reduces demasiado el número de documentos recuperados?
- ¿Qué significa que un sistema RAG sea autorregresivo desde el punto de vista de la generación?
- ¿Dónde aparece la distribución de probabilidad en tu notebook?
- ¿Dónde aparece la función de similitud o métrica de evaluación?
- ¿Qué parte de tu código controla la granularidad del retrieval?
- ¿Qué parte de tu código controla la diversidad de respuestas?
- ¿Qué parte de tu código controla la capacidad de adaptación a nuevo conocimiento?
- ¿Qué parte de tu código permite reproducibilidad?
- ¿Cómo distinguirías un error de implementación de una mala elección de hiperparámetros?
- ¿Qué resultado invalidaría tu conclusión?
- ¿Qué simplificación hiciste por limitaciones de cómputo?
- ¿Qué harías distinto si tuvieras una GPU y más datos?.

#### Requisitos mínimos del notebook

El notebook debe contener las siguientes secciones:

- Título del proyecto.
- Nombre del estudiante.
- Cuaderno base.
- Objetivo.
- Línea base.
- modificación significativa.
- Configuración experimental.
- Corpus, consultas o dataset utilizado.
- Tabla de dimensiones o estructuras de datos.
- Evidencia de cálculo interno.
- Comparación entre línea base y variante.
- Análisis de errores.
- Conclusión técnica.
- Declaración de autoría y uso de IA.
- Sección final llamada `Puente al curso`.

#### Celda de verificación personal

Cada notebook debe incluir una celda llamada `CELDA DE VERIFICACIÓN PERSONAL`.

La celda debe contener lo siguiente:

- Nombre completo del estudiante.
- Fecha de ejecución.
- Modelo usado.
- Semilla.
- Tamaño del corpus o lista de consultas.
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
- modificación realizada.
- Cómo ejecutar el notebook.
- Principales resultados.
- Limitaciones.
- Qué se muestra en el video.
- Declaración de autoría y uso de IA.

#### Declaración de autoría y uso de IA

El estudiante debe incluir en el notebook y en el README una declaración breve con el siguiente contenido.

```
Declaro que comprendo el código, los resultados y las explicaciones entregadas en esta Práctica.
Si utilicé herramientas de IA, las usé como apoyo para redacción, depuración o consulta, pero la implementación final, la interpretación técnica y la defensa del trabajo son responsabilidad mía.
```

Si el estudiante usó IA, debe indicar para qué la usó.

Ejemplos válidos:

- Usé IA para revisar redacción del README.
- Usé IA para depurar un error de dimensión de embeddings.
- Usé IA para entender una advertencia de la librería de vector store.
- Usé IA para generar una primera versión de una función de evaluación que luego modifiqué y expliqué.

Ejemplos no válidos:

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

- 1 punto: realiza una Modificación común obligatoria.
- 1 punto: realiza una Modificación específica del proyecto.
- 1 punto: predice el efecto antes de ejecutar.
- 1 punto: interpreta el resultado después de ejecutar.
- 1 punto: explica errores, cambios de forma, scores, métricas o flujo del agente.

#### C. Evidencia interna y comprensión técnica: 4 puntos

- 1 punto: muestra embeddings, chunks, vectores, scores de similitud, métricas o flujo del agente.
- 1 punto: explica dimensiones o estructuras correctamente.
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
- No explicar dimensiones o estructuras centrales del proyecto: máximo 10/20.
- No comparar línea base contra variante: descuento de 3 puntos.
- No incluir README: descuento de 2 puntos.
- No declarar uso de IA: descuento de 2 puntos.
- Notebook generado automáticamente sin defensa técnica: 0/20.
- Código correcto sin explicación correcta: 0/20.
- Explicación genérica desconectada del notebook: 0/20.

#### Criterio de autenticidad

El objetivo no es impedir el uso de IA. El objetivo es impedir que el estudiante entregue un producto que no comprende.

La autenticidad se evaluará mediante la modificación en vivo, la explicación de errores, la predicción antes de ejecutar, la interpretación después de ejecutar, la explicación de dimensiones y estructuras, la respuesta a preguntas avanzadas y la conexión entre notebook, código, resultado y teoría.

Un estudiante puede usar IA como apoyo, pero debe demostrar control técnico sobre el trabajo entregado.

#### Qué se considera una buena entrega

Una buena entrega parte de un cuaderno del curso, reconstruye una línea base, introduce una modificación real, compara resultados, muestra evidencia interna, explica dimensiones, analiza errores, reconoce limitaciones, usa vocabulario técnico correctamente y conecta código, matemática y resultado.

#### Qué se considera una mala entrega

Una mala entrega solo ejecuta celdas, cambia nombres o colores sin modificar el experimento, presenta texto genérico generado por IA, no explica el código, no explica embeddings ni chunks ni scores, no interpreta resultados, no compara línea base contra variante, no muestra cálculo interno y no demuestra aprendizaje real.

#### Cierre obligatorio

Todo video y todo README deben terminar con dos secciones obligatorias.

#### Qué hice, por qué lo hice y qué significan mis resultados

El estudiante debe explicar en lenguaje propio qué implementó, qué modificó, por qué esa modificación es técnicamente relevante, qué evidencia obtuvo y qué significan los resultados.

#### Puente al curso

El estudiante debe conectar su proyecto con al menos dos temas relacionados.

- Agentes basados en LLMs.
- Búsqueda semántica.
- Chunking y vectorización.
- Arquitectura RAG.
- Reranking y refine.
- Evaluación de retrieval.
- Grounded generation.
- Sistemas híbridos.
- Memoria en agentes.
- Seguridad y confiabilidad de sistemas generativos.

#### Observación final para el estudiante

Esta práctica no evalúa solamente si el notebook funciona. Evalúa si el estudiante entiende el sistema, el código, los datos, la modificación realizada, los resultados obtenidos y las limitaciones del experimento.

La nota depende de la evidencia técnica mostrada en el notebook y defendida en el video.
