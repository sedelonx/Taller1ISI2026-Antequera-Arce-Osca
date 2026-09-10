El verbo GET solo se usa para leer informacion del servidor, osea que la información del servidor permanece igual.
El verbo POST se utiliza para decirle al servidor que cree información en su memoria, osea que el estado del servidor cambia.
el verbo PATCH se utiliza para decirle al servidor que altere información que ya existe, cambiando el estado del servidor.
el verbo DELETE se utiliza para decirle al servidor que elimine informacion dentro de Él. Cambia su estado.

El GET NO es idempotente porque el mismo request no siempre da el mismo resultado, por ejemplo el servidor de este taller podría tener 2 tasks definidas en un momento, pero en otro podría tener 3. Ejecutar GET en estos momentos daría distintos resultados.