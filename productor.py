# PRODUCTOR

# IMPORTAR LIBRERÍAS 
import time
import rabbitpy

def productor(nproductor, topic): # Se añaden como argumentos de la función el nombre del productor y el tópico
    with rabbitpy.Connection() as conexion: # Establecer conexión con rabbitpy
        with conexion.channel() as channel: # Abrir canales de la comunicación 
            # Declaración del exchange de tipo topic
            exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
            exchange.declare()

            contador = 1  # Iniciar el contador de mensajes

            while True:
                
                contenido = f'Mensaje {contador} del productor {nproductor} en el topic {topic}'
                mensaje = rabbitpy.Message(channel, contenido) # Mensaje en rabbytpy, con el contenido indicado, y la cola creada 
                
                # Publicación del mensaje en el exchange con la clave de enrutamiento del topic
                mensaje.publish(exchange, routing_key=topic)
                
                print(f'\n[Productor] Enviando el mensaje: {contenido}')
                
                contador += 1 # Aumentar un valor del contador cuando se crea un nuevo mensaje 
                time.sleep(1)  # Se envía un mensaje cada segundo