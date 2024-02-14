# ptinchcapeyesidp
proposed technical test
Proceso de realización
Para le realización de la presente prueba técnica, inicialmente se orientó el enfoque a un servicio en Python que consuma la API REST https://jsonplaceholder.typicode.com/posts y muestre la información como respuesta, para lograr esto se utilizaron las librerías:

requests: Para realizar peticiones HTTP a la API.
Flask: Para crear una aplicación web simple que muestre la respuesta.
Definido el enfoque a dar, se desarrollo el código correspondiente para desplegar la infraestructura necesaria por medio de Terraform en la plataforma Cloud AWS.

Enlace repositorio github: https://github.com/yesidpuerto/iaac-pt-inchcape-yesidp.git 

Estructurados los repositorios del código mencionado previamente, se procedió con la integración y el despliegue continuo por medio de un pipeline a implementar dentro de Azure DevOps.

*Tanto la cuenta de AWS como la cuenta de Azure DevOps se manejaron con las capas gratuitas.

Dadas las limitantes de la capa gratuita de Azure DevOps, referente a los trabajos paralelos, se desarrollo el YAML correspondiente al apartado de CI/CD, dentro de los repositorios de Github y Azure DevOps en las cuentas gratuitas, sin embargo su ejecución y su validación se tuvo que realizar en la cuenta paga.

La lógica implementada dentro de CI/CD, se fundamento en la ejecución y construcción del servicio solicitado, y su posterior montaje con docker, desarrollando el Dockerfile necesario para el montaje de la imagen para su posterior envío hacia el ECR de AWS, y el uso de la misma en un archivo deploy previamente configurado para el lanzamiento de pods en un clouster de kubernetes, de ser el caso, o para este caso puntual, para ser utilizada para correr el servicio por medio de esta imagen en un container dentro de la instancia desplegada previamente por medio de Terraform (IaaC).

Para finalizar el proceso de despliegue, al finalizar el mismo, se da un tiempo de 15 segundos de tal forma que se garantice el levantamiento del servicio, para así ejecutar una prueba unitaria del mismo a través del archivo test.py obteniendo la respuesta del estado del servicio, finalizando de esta forma el proceso de CI/CD de manera exitosa.

Se lanza inicialmente el pipeline con la configuración para construir por primera vez la imagen de docker y correr el container correspondiente.

Luego se estructuró, el yaml con detención y eliminación de container para actualización correspondiente dentro de la integración y el despliegue continuos.

Para lograr esta conexión a través de uno de los agentes hospedados por Microsoft, previamente se configuró la conexión al servidor / instancia de AWS, por medio de la configuración del proyecto dentro de Azure DevOps en la sección, service connections.

Cabe resaltar que dentro de mis conocimientos, esta el manejo de CI/CD por medio de Releases en el apartado de Azure DevOps, en donde se puede dar manejos diferentes a esta funcionalidad, por stages, aprobaciones, etc.

Limitaciones capa gratuita:
Aunque se desarrollaron diferentes opciones de yaml para la ejecución dentro de la capa gratuita, no fue posible tener una ejecución exitosa dado el limitante de trabajos paralelos.

Referente a seguridad, por medio de terraform se configuro el grupo de seguridad / FW para la instancia lanzada, de tal forma que se garantizara el trafico por los puertos 443 y 80 y unicamente autorizado el acceso a la conexión ssh por el puerto 22 para mi ip pública.

Dado que el servicio se expone en el puerto 5000, se habilito este dentro de las reglas del grupo de seguridad / FW .

Finalmente de manera temporal, para el proceso de CI/CD se habilito el puerto 22 para todo el mundo aunque claramente es una falla de seguridad, se tenia que aperturar por el uso de los agentes hospedados de Microsoft, esta regla se quito al momento de finalizar la ejecución y para mitigar este tipo de aperturas / vulnerabilidades, se implementa el uso de agentes autohospedados los cuales son manejados por el encargado o encargados de la organización de Azure DevOps, tanto para mitigar la vulnerabilidad de seguridad como para contar con mas de un agente que permita las canalizaciones en simultanea para diferentes proyectos dentro de la plataforma.

Con lo anterior, se realiza la Technical Test , agradeciendo su tiempo y la consideración de mi postulación para la vacante de DevOps Engineer en la compañía Inchcape Digital, aprecio sus comentarios y consideraciones. 
