### Seguridad básica en sistemas LLMOps

Un sistema LLMOps debe controlar accesos, proteger endpoints administrativos y evitar
la exposición de secretos. El reindexado no debería quedar abierto al público porque
puede modificar la base de conocimiento usada por el sistema.

También se deben revisar logs para evitar almacenar datos sensibles. Un sistema que
maneja consultas de usuarios debe tener límites de tamaño, manejo de errores y
políticas claras sobre privacidad.

La seguridad mínima incluye variables de entorno, tokens de administración, validación
de entrada y separación entre endpoints públicos y administrativos.
