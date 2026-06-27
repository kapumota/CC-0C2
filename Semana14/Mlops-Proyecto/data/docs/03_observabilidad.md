### Observabilidad y métricas

La observabilidad permite entender cómo se comporta un sistema durante la operación.
En una API de lenguaje se pueden medir latencia, cantidad de requests, errores,
consultas vacías, documentos recuperados, uso de fallback y tiempo de respuesta.

Prometheus permite exponer métricas mediante un endpoint como /metrics. Estas métricas
ayudan a detectar degradación, errores y cambios en el comportamiento del sistema.

En un sistema RAG también conviene observar la edad del índice, el número de chunks,
los scores promedio de similitud y la frecuencia de resultados sin evidencia suficiente.
