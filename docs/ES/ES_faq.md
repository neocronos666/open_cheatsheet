# Preguntas Frecuentes (FAQ)

## 1. ¿Qué es un archivo `.chsheet`?

Un archivo `.chsheet` es un archivo en formato JSON que contiene información estructurada sobre un tema específico, como fórmulas matemáticas, conceptos físicos, o cualquier otro contenido educativo. Estos archivos son utilizados por la aplicación para generar contenido dinámico.

## 2. ¿Cómo se crea un archivo `.chsheet`?

Puedes crear un archivo `.chsheet` manualmente utilizando un editor de texto o mediante herramientas específicas que generan estos archivos basándose en entradas estructuradas.

## 3. ¿Qué pasa si omito un campo en el archivo `.chsheet`?

Algunos campos son opcionales, como `cons_table` y `rel_forms`. Si omites estos campos, la aplicación simplemente no mostrará esa sección del contenido. Sin embargo, es importante asegurarse de que los campos esenciales como `title`, `forms`, y `description` estén presentes para evitar errores.

## 4. ¿Cómo se manejan los enlaces y referencias externas en un archivo `.chsheet`?

Puedes incluir enlaces y referencias externas en el campo `ref_webs`. Estos son utilizados por la aplicación para proporcionar recursos adicionales relacionados con el tema.

## 5. ¿Puedo usar LaTeX en los archivos `.chsheet`?

Sí, los archivos `.chsheet` soportan la inclusión de fórmulas en formato LaTeX en los campos `forms`, `var_table`, y `cons_table`.
