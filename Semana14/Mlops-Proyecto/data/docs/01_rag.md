### RAG y recuperación aumentada

Un sistema RAG combina recuperación de información con generación de respuestas.
Primero se dividen documentos en fragmentos, luego se construye un índice y después
se recuperan fragmentos relevantes para una consulta.

La calidad del sistema depende del chunking, del modelo de representación, de la
función de similitud y del número de documentos recuperados.

Un error común en RAG ocurre cuando el sistema recupera documentos relacionados
pero no suficientes para responder con fidelidad. Otro error ocurre cuando el modelo
genera información no sustentada en el contexto recuperado.
