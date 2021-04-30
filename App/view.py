"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

cont = None

# ___________________________________________________
#  funciones de impresión
# ___________________________________________________
def print5(analyzer):
    print("Primeras 5 posiciones: \n")
    for x in range(1,6):
        
        print(lt.getElement(analyzer,x))

    print("\nÚltimas 5 posiciones: \n")
    for y in range(-5,0):
        
        print(lt.getElement(analyzer,y))

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar los Datos")
    print("2- Cargar información al analizador")
    print("3- Requerimiento 1: Caracterizar las reproducciones")
    print("4- Requerimiento 2: Música para festejar")
    print("5- Requerimiento 3: Música según el ánimo")
    print("6- Requerimiento 4: Música para estudiar")
    print("7- Requerimiento 5: Indicar el género musical más escuchado en un tiempo")
    print("0- Salir")
    print("*******************************************")
# ___________________________________________________
#  Menu Requerimiento 4
# ___________________________________________________

def printreq4():
    print("*******************************************")
    print("Bienvenido a estimar las reproducciones de géneros musicales")
    print("1- Cargar nuevo género musical")
    print("2- Conocer canciones por Tempo y artistas")
    print("3- Salir")
    print("*******************************************")
# ___________________________________________________
#  Funciones de inicialización
# ___________________________________________________

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.init()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) ==1:
        print("\nCargando Datos y comparando....")
        cont = controller.init()
        answer = controller.loadData0(cont)

    elif int(inputs[0]) == 2:
        print("\nCargando información del analizador ....")

        cont = controller.init()
        answer = controller.loadData(cont)
        print('Total de registros de eventos de escucha cargados:' + str(controller.videosSize(cont)))
        print('Total de ártistas únicos cargados:' + str(controller.artistSize(cont)))
        print('Total de pistas de audio únicas cargadas:' + str(controller.trackSize(cont)))
        print('Estos son los primeros 5 y últimos 5 eventos de escucha cargados: \n')
        print(print5(cont["events"]))


    elif int(inputs[0]) ==3:
        content_char = str(input("Característica de contenido a evaluar:"))
        value_min = float(input("Valor mínimo de la característica del contenido:"))
        value_max = float(input("Valor mínimo de la característica del contenido:"))

        result = controller.getReproductions(cont, content_char, value_min,value_max)
        
        print("++++++ Req 1. Results... ++++++")
        print("\nInstrumentalness is between {} and {}\n".format(value_min, value_max))
        print(result)
    elif int(inputs[0]) == 4: 
        min_energy= float(input("Ingrese el valor mínimo para la característica Energy:"))
        max_energy= float(input("Ingrese el valor máximo para la característica Energy:"))
        min_danceability= float(input("Ingrese el valor mínimo para la característica Danceability:"))
        max_danceability= float(input("Ingrese el valor m para la característica danceability:"))

        result = controller.partyMusic(cont, min_energy, max_energy,min_danceability,max_danceability)
        print("Energy is between {} and {}".format(min_energy,max_energy))
        print("Danceability is between {} and {}".format(min_danceability,max_danceability))
        
        print("--- Unique track_id ---")
        for x in lt.iterator(result):
            print("Track:{} with energy of {} and danceability of {}".format(x["track_id"],x["energy"],x["danceability"]))
            
    elif int(inputs[0]) == 5:

        min_instru= float(input("Ingrese el valor mínimo para la característica Instrumentalness:"))
        max_instru= float(input("Ingrese el valor máximo para la característica Instrumentalness:"))
        min_tempo= float(input("Ingrese el valor mínimo para la característica Tempo:"))
        max_tempo= float(input("Ingrese el valor m para la característica Tempo:"))

        result = controller.EstudyMusic(cont, min_instru, max_instru,min_tempo,max_tempo)
        print("Instrumentalness is between {} and {}".format(min_instru,max_instru))
        print("Tempo is between {} and {}".format(min_tempo,max_tempo))
        
        print("--- Unique track_id ---")
        for x in lt.iterator(result):
            print("Track:{} with instrumentalness of {} and tempo of {}".format(x["track_id"],x["instrumentalness"],x["tempo"]))

        
    elif int(inputs[0]) == 6:
        value = True
        while value == True:
            printreq4()

            inputs = input('Seleccione una opción para continuar\n')
            if int(inputs[0]) == 1:
                print("Géneros Cargados:\n-------")
                print(str(controller.printGenre(cont)))

                new_genre = input("Ingrese el nuevo género que le gustaría insertar")
                tempo_low = int(input("Ingrese el valor mínimo del tempo"))
                tempo_high = int(input("Ingrese el valor máximo del tempo"))
                result = controller.newUserGenre(cont,new_genre,tempo_low,tempo_high)

                print("último género cargado:" + str(controller.lastGenre(cont,new_genre)))

            elif int(inputs[0]) == 2:
                print("Géneros Cargados:")
                print(str(controller.printGenre(cont)))
                print("Para insertar géneros ejemplo: chill-out,hip-hop")
                genres= input("Ingrese los géneros que le gustaría buscar separados por coma...").replace(" ","").split(",")
                result = controller.genreSearch(cont,genres)
                print(result)
            else:
                value= False 
    elif int(inputs[0]) == 7:
        pass
    else:
        sys.exit(0)
sys.exit(0)