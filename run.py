import threading
import rabbitpy
from time import sleep
from productor import productor 
from consumidor import consumidor

hilos_productor = []
hilos_consumidor= []

def iniciarp(name, topic): 
    productor(name, topic)

def iniciarc(topic):
    consumidor(topic)

def menu(): 
    while True: 
        print('\nSeleccione un opción:')
        print('\n1. Enviar mensaje. \n2. Recibir mensaje. \n3. Salir.')
        opcion= input('\nOpción:')

        if opcion == '1': 
            nproductop= input('\nAñade el nombre del productor: ')
            topic= input('Elige un topic, entre deportes, noticias y tiempo: ')

            if topic in ['deportes', 'noticias', 'tiempo']:
                hilo =threading.Thread(target= productor, args=(nproductop, topic))
                hilo.start()
                hilos_productor.append(hilo)
            else: 
                print('Topic no válido, debe seleccionar entre: deportes, noticias o tiempo')

        elif opcion == '2': 
            topic= input('Elige un topic, entre deportes, noticias y tiempo: ')

            if topic in ['deportes', 'noticias', 'tiempo']:
                hilo= threading.Thread(target= consumidor, args=(topic, ), daemon=True)
                hilo.start()
                hilos_consumidor.append(hilo)
            else:
                print('Topic no válido, debe seleccionar entre: deportes, noticias o tiempo')

        elif opcion == '3': 
            print('Se ha seleccionado salirse del programa ...')
            return
        
        else: 
            print('La opción seleccionada debe estar entre el 1 y el 3. Intentelo de nuevo')

        for hilop in hilos_productor:
            hilop.join()
        for hiloc in hilos_consumidor: 
            hiloc.join()

if __name__ == "__main__": 
    menu()