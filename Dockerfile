# Usa la imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación Flask al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 en el contenedor
EXPOSE 5000

# Define la variable de entorno FLASK_APP para indicar el punto de entrada de la aplicación
ENV FLASK_APP=app.py

# Define el comando para ejecutar la aplicación Flask cuando se inicie el contenedor
CMD ["flask", "run", "--host=0.0.0.0"]
