# CONSUMIDOR  

# IMPORTAR LIBRERÍAS
import time
import rabbitpy

# FUNCIÓN PARA EL CONSUMIDOR 
def consumidor(topic): # Añadir como argumento el topic seleccionado
    with rabbitpy.Connection() as conexion: # Establecer conexión con rabbitpy
        with conexion.channel() as channel: # Abrir canales de la comunicación 

            # Declarar el exchange de tipo topic
            exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
            exchange.declare()

            # Crear y enlazar la cola con el exchange usando el topic como clave de enrutamiento
            queue = rabbitpy.Queue(channel, f'queue_{topic}')
            queue.declare()
            queue.bind(exchange, routing_key=topic)

            print(f'\nSe espera un mensaje del topic: {topic}')

            while True:
                print('Revisando el contenido de la cola...')
               
                for mensaje in queue.consume_messages(): # Extrear mensaje de la cola uno por uno 
                    print(f"\n[Consumidor][{time.strftime('%Y-%m-%d %H:%M:%S')}] | Topic: '{topic}' | Recibido: {mensaje.body.decode('utf-8')}")
                    mensaje.ack() # Revisar el envio correcto del mensaje 
                
                time.sleep(5)  # Esperar cinco segundos antes de revisar de nuevo

 