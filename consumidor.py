import time 
import rabbitpy
# import rabbitpy.channel 

def consumidor(topic): 
    with rabbitpy.Connection() as conexion: 
        with conexion.channel() as channel: 
            # Declarar el exchange de tipo topic 
            exchange = rabbitpy.Exchange(channel, "exchange_topic", exchange_type='topic')
            exchange.declare()
            # Declarar la cola, y enclazarla con el exchange 
            queue= rabbitpy.Queue(channel, topic)
            queue.declare()
            queue.bind(exchange, routing_key=topic)
            print(f'\nSe espera un mensaje del topic: ', {topic})

            while True: 
                for contenido in queue: # Recorre la cola para ver que halla mensajes 
                    print(f'Mensaje recibido en {topic}: {contenido.body}')
                    contenido.ack()
                time.sleep(5) # Esperar cinco segundos hasta revisar de nuevo
