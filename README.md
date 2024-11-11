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

### Productores
Cada productor envía mensajes al topic correspondiente, con las siguientes características:
- Envían mensajes cada segundo
- Cada mensaje contienen:
    - Nómbre del productor (introcucido por el usuario)
    - Topic (a seleccionar por el usuario entre "deportes", "noticias", "tiempo")
    - Información del mensaje
    - Contador de mensajes (inicia en uno y aumenta un valor cada mensaje)

### Consumidor 
- Escucha los mensajes de la cola asociada a su topic.
- Procesa los mensajes de forma periódica, cada cinco segundos.
- Solo hay un consumidor por topic, ejecutado en un hilo independiente.

## Función prinicipal main
El programa principal despliega un menú interactivo que permite al usuario seleccionar entre las siguientes opciones:

1. **Enviar mensajes**: Permite agregar un nuevo productor que envía mensajes a un topic específico. Para ello, el usuario ingresa:

- Nombre del productor
- Nombre del topic
- Cada productor se ejecuta en un hilo independiente.
  
2. **Recibir mensajes**: Permite agregar un nuevo consumidor para recibir mensajes de un topic específico. El usuario ingresa:

- Nombre del topic
. Cada consumidor se ejecuta en un hilo independiente.
  
3. **Salir**: Finaliza la ejecución del programa.

### Ejecucción 
Para iniciar el programa, ejecuta el archivo principal (main.py). En el menú interactivo:

- Si seleccionas **1**, puedes enviar mensajes.
- Si seleccionas **2**, puedes recibir mensajes.
- Si seleccionas **3**, el programa se cierra.
- Si seleccionas una **opción no válida**, el menú te volverá a preguntar

## Ejemplo de uso 
Para ejecutar un **productor**:

Seleccione una opción:
1. Enviar mensajes
2. Recibir mensajes
3. Salir
> 1
Ingrese el nombre del productor: Productor_1
Ingrese el topic: noticias 

Para ejecutar un **consumidor**: 
Seleccione una opción:
1. Enviar mensajes
2. Recibir mensajes
3. Salir
> 2
Ingrese el topic: noticias




