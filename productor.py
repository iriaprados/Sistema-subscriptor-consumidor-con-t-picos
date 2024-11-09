import time
import rabbitpy

def productor (nproductor, topic): 
    with rabbitpy.Connection() as conexion: 
        with conexion.channel() as channel: 
            # Declaración de exchange, del tipo tópico 
            exchange= rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
            exchange.declare()
            contador = 1 # Inciar el contador de mensajes 

            while True: 
                contenido = f'{nproductor} envía el mensaje {contador} en el topic {topic} '
                # mensaje= rabbitpy.Message(channel, mensaje, {topic: topic}) # Creación y publicación del mensaje 
                mensaje= rabbitpy.Message(channel, contenido) # Creación y publicación del mensaje 
                mensaje.publish(exchange, routing_key=topic)
                print(f'\nEnviando el mensaje: {contenido}')
                contador+=  1
                time.sleep(1) # Se envía un mensaje cada segundo 