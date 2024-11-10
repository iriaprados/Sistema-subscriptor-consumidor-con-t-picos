# Emisor-Suscriptor con RabbitMQ y Docker
Este proyecto implementa un sistema de mensajería Emisor-Suscriptor utilizando RabbitMQ y Docker en un entorno AMQP. Con varios productores que publican mensajes sobre distintos temas o topics, que van a ser "deportes", "noticias", y tiempo. Mientras que los consumidores se suscriben a esos topics específicos para recibir únicamente los mensajes relevantes a su interés.

## Requisitos previos 
Para la ejecución correcta de este proyecto es necesaro: 
- Tener Docker instalado.
- La imagen de RabbitMQ, de la consola activada.
### Instalación y configuración de RabbitMQ 
Para iniciar RabbitMQ en Docker, ejecuta el siguiente comando en tu terminal:
**docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management**

Este comando inicia un contenedor de RabbitMQ que expone los puertos necesarios. 

## Descripción del sistema 
Este sistema permite que múltiples productores y consumidores se comuniquen a través de topics en una cola de mensajes. La configuración utiliza un exchange de tipo topic llamado exchange_topic, que enruta los mensajes en función de los nombres de los topics.

Cada productor publica mensajes que incluyen un contador incremental, y cada consumidor escucha los mensajes de la cola asociada al topic que le interesa.
