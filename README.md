# Examen-2-DesWeb
Agua y drenaje

Archivos principales:

main.py: Es el archivo que corre la API y conecta todo.

models.py: Tiene las validaciones de los datos.

storage.py: Funciona como nuestra base de datos guardando las listas.

routers/: Carpeta donde están los archivos de clientes, consumos, tarifas y reportes.

Instalacion:
Para que el proyecto funcione, se necesita instalar la siguiente libreria en la terminal:
pip install fastapi uvicorn pydantic

Como correr el proyecto:
Abrir la terminal en la carpeta del proyecto y corre el siguiente comando:
py -m uvicorn main:app --reload

Como probarlo:
Cuando el servidor este corriendo, abrir el navegador y entrar a esta direccion:
http://127.0.0.1:8000/docs

Aparecera la pagina de Swagger donde puedes probar que funcionan los metodos GET, POST, PUT y DELETE de todas las partes del proyecto.