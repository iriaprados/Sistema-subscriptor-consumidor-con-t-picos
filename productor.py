import time
import rabbitpy

def productor(nproductor, topic):
    with rabbitpy.Connection() as conexion:
        with conexion.channel() as channel:
            # Declaración del exchange de tipo topic
            exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
            exchange.declare()

            contador = 1  # Iniciar el contador de mensajes

            while True:
                contenido = f'{nproductor} manda el mensaje {contador} en el topic {topic}'
                mensaje = rabbitpy.Message(channel, contenido)
                
                # Publicación del mensaje en el exchange con la clave de enrutamiento del topic
                mensaje.publish(exchange, routing_key=topic)
                print(f'\nEnviando el mensaje: {contenido}')
                
                contador += 1
                time.sleep(1)  # Se envía un mensaje cada segundo
