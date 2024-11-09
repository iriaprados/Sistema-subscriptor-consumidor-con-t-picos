import time
import rabbitpy

def consumidor(topic):
    with rabbitpy.Connection() as conexion:
        with conexion.channel() as channel:
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
               
                for mensaje in queue.consume_messages():
                    print(f"\n[Consumidor][{time.strftime('%Y-%m-%d %H:%M:%S')}] | Topic: '{topic}' | Recibido: {mensaje.body.decode('utf-8')}")
                    # print(f'Se ha recibido el topic {mensaje.body}')
                    mensaje.ack()
                
                time.sleep(5)  # Esperar cinco segundos antes de revisar de nuevo

 