import threading
import rabbitpy
from time import sleep
from productor import productor 
from consumidor import consumidor

# exchange= rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')

def menu(): 
    while True: 
        print('\nSeleccione un opción:')
        print('\n1. Enviar mensaje. \n2. Recibir mensaje. \n3. Salir.')
        opcion= input('\nOpción: ')

        if opcion == '1': 
            nproductop= input('Añade el nombre del productor: ')
            topic= input('Elige un topic: ')
            if topic in ['deportes', 'noticias', 'tiempo']:
                threading.Thread(target= productor, args=(nproductop, topic)).start()
            else: 
                print('Topic no válido, debe seleccionar entre: deportes, noticias o tiempo')

        elif opcion == '2': 
            topic= input('Elige un topic: ')
            if topic in ['deportes', 'noticias', 'tiempo']:
                threading.Thread(target= consumidor, args=(topic, )).start()
            else:
                print('Topic no válido, debe seleccionar entre: deportes, noticias o tiempo')
                
        elif opcion == '3': 
            print('Se ha seleccionado salirse del programa ...')
            return
        else: 
            print('La opción seleccionada debe estar entre el 1 y el 3. Intentelo de nuevo')

if __name__ == "__main__": 
    menu()