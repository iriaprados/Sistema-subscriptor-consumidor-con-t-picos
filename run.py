# RUN PARA EL PRODUCTOR Y EL CONSUMIDOR    

# IMPORTAR LIBRERÍAS 
import threading
import rabbitpy
from time import sleep
from productor import productor 
from consumidor import consumidor

# ALMACENAMIENTO DE LOS HILOS PARA EL PRODUCTOR Y EL CONSUMIDOR 
hilos_productor = []
hilos_consumidor= []

# FUNCIONES PARA LLAMAR A ARGUMENTOS DEL PRODUCTOR Y EL CONSUMIDOR
def iniciarp(name, topic): 
    productor(name, topic)

def iniciarc(topic):
    consumidor(topic)

# FUNCIÓN PRINCIPAL DEL MENÚ 
def menu(): 
    while True: 
        # Mostrar y pedir al usuario que seleccione una opción del menú 
        print('\nSeleccione un opción:')
        print('\n1. Enviar mensaje. \n2. Recibir mensaje. \n3. Salir.')
        opcion= input('\nOpción:')

        # Primera opción; envío del mensaje por el productor 
        if opcion == '1': 
            nproductop= input('\nAñade el nombre del productor: ')
            topic= input('Elige un topic, entre deportes, noticias y tiempo: ')

            if topic in ['deportes', 'noticias', 'tiempo']: # Si introducidos se encuentran entre los posibles 
                hilo =threading.Thread(target= productor, args=(nproductop, topic)) # Hilo, que ejecuta la función del productor, con sus argumentos 
                hilo.start()
                hilos_productor.append(hilo) # Introducir hilo en la lista de hilos del productor 
            else: # El topic seleccionando no se encuentra entre los posibles, se sale del programa 
                print('Topic no válido, debe seleccionar entre: deportes, noticias o tiempo')

        # Segunda opción; recibimiento del mensaje por el consumidor  
        elif opcion == '2': 
            topic= input('Elige un topic, entre deportes, noticias y tiempo: ')

            if topic in ['deportes', 'noticias', 'tiempo']: # Si introducidos se encuentran entre los posibles 
                hilo= threading.Thread(target= consumidor, args=(topic, )) # Hilo, que ejecuta la función del productor, con sus argumentos 
                hilo.start()
                hilos_consumidor.append(hilo) # Introducir hilo en la lista de hilos del consumidor  
            else: # El topic seleccionando no se encuentra entre los posibles, se sale del programa 
                print('Topic no válido, debe seleccionar entre: deportes, noticias o tiempo')

        elif opcion == '3': # Opción para salirse del programa 
            print('Se ha seleccionado salirse del programa ...')
            return
        
        else: # Si no se ha seleccionado una opción disponible, se indica y se sale del programa 
            print('La opción seleccionada debe estar entre el 1 y el 3. Intentelo de nuevo')

        # Recorrer las listas de los hilos ejecutador por el consumidor y el productor, para esperar ejecutar los hilos cuando hallan finalizado los anteriores 
        for hilop in hilos_productor:
            hilop.join()
        for hiloc in hilos_consumidor: 
            hiloc.join()

# LLAMADA DE LA FUNCIÓN MENÚ 
if __name__ == "__main__": 
    menu()