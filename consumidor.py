import rabbitpy
from time import sleep

def consumidor(topic): 
    conexion= rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2F')
    channel = conexion.channel()

    # Configurar el exchange topic
    exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
    exchange.declare()

    # Crear la cola para los topic y enlazarla a exchange y topic
    cola = rabbitpy.Queue(channel, topic)
    cola.declare()
    cola.bind(exchange, topic) # Enlazar la cola, con exchange y topic 

    print(f"[{topic}] Consumidor escuchando mensajes en el topic '{topic}'...")

    # Recepción para el mensaje según el topic 
    try: 
        while True: 
            if len(cola) > 0: # Si hay mensajes en la cola 
                mensaje= cola.get() # Se obtienen los
                print(f'El mensaje ha sido recibido en [{topic}] {mensaje.body.decode()}.')
                mensaje.ack() # Comprobar que se ha recibido el mensaje 
            sleep(5) # Esperar cinco segundos antes de verificar de nuevo
    except KeyboardInterrupt: # Si se interrumpe la ejecucción con una tecla
        print(f'El topic [{topic}], ha sido detenido.') 
    finally:
        channel.close()
        conexion.close()

    
