# ptinchcapeyesidp
proposed technical test


Comandos para construir imagen de docker y correr el contenedor correspondiente.
*Para construir imagen con base en el archivo Dockerfile:
docker build -t my-flask-app .
*Para correr contenedor:
docker run -d --name app-pt-yesidp -p 5000:5000 my-flask-app
