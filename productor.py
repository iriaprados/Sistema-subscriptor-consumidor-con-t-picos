import rabbitpy
from time import sleep

def productor(name, topic): 
    conexion = rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2F')
    channel = conexion.channel()

    # Configurar el exchange de tipo topic
    exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
    exchange.declare()

    # Crear la cola para el topic y enlazarla al exchange
    cola = rabbitpy.Queue(channel, topic)
    cola.declare()
    cola.bind(exchange, topic)

    print(f"[{name}] Productor enviando mensajes al topic '{topic}'...")

    contador = 1  # Inicializar el contador

    # Emisión de mensajes al topic correspondiente
    try: 
        while True: 
            # Crear el contenido del mensaje con el contador y la información solicitada
            contenido = f"Productor: {name}, Topic: {topic}, Mensaje: Información relevante, Contador: {contador}"
            
            # Crear el mensaje en RabbitMQ
            mensaje = rabbitpy.Message(channel, contenido)

            # Publicar el mensaje en el exchange usando el topic como clave de enrutamiento
            mensaje.publish(exchange, topic)
            print(f"{name} ha enviado el mensaje: '{contenido}'")
                
            contador += 1  # Incrementar el contador en cada mensaje enviado
            sleep(1)  # Esperar un segundo antes de enviar otro mensaje

    except KeyboardInterrupt:
        print(f"{name} ha detenido el envío de mensajes al topic '{topic}'.")
        
    finally:
        # Cerrar el canal y la conexión al finalizar
        channel.close()
        conexion.close()
