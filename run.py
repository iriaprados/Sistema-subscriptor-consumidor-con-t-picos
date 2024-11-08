import rabbitpy
import threading
from consumidor import consumidor 
from productor import productor


# Introducir para cargar el servidor rabbitmq: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management 


def configuracion(topics): 
    conexion = rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2F')
    channel = conexion.channel()

    try: 
        exchange= rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
        exchange.declare()

        print('')
        for topic in topics: 
            cola= rabbitpy.Queue(channel, topic)
            cola.declare()
            cola.bind(exchange, topic)
            print(f'La cola de {topic}, se ha configurado y enlazado con {exchange.name}')
        print(' ')
           

    except Exception as e:
        print(f'Error en la configuración de Exchange o de las colas: {e}')
    finally: 
        channel.close()
        conexion.close()


if __name__ == '__main__': 
    temas= ['Deportes', 'Noticas', 'Tiempo']

    configuracion(temas)
    for tema in temas: 
        threading.Thread(target=productor, args=(f'productor1',tema)).start()