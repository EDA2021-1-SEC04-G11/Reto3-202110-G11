
"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import datetime
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def conv(value):
    try:
        value=float(value)
    except ValueError:
        pass    
    return value

def loadData(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    loadEvents(analyzer)
    loadmusical_genre(analyzer)
    loadUserTrack_file(analyzer)
    loadSentiment(analyzer)

def loadEvents(analyzer):
    """
    Carga los eventos del archivo.  Por cada evento se toman sus características y por
    cada uno de ellos, se crea en la lista y árboles bianrios para 
    las categorías específicas
    """

    context_file = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(context_file, encoding="utf-8"),
                                delimiter=",")
    
    for event in input_file:
        for key,value in event.items():
            event[key] = conv(value)
        model.add_event(analyzer, event)
    

def loadUserTrack_file(analyzer):
    userTrack_file = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(userTrack_file, encoding="utf-8"),
                                    delimiter=",")
    for event in input_file:
        for key,value in event.items():
            event[key] = conv(value)
        model.add_userTrack(analyzer, event)

def loadSentiment(analyzer):
    userTrack_file = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(userTrack_file, encoding="utf-8"),
                                    delimiter=",")
    for event in input_file:
        for key,value in event.items():
            event[key] = conv(value)
        model.add_sentiment(analyzer, event)

def loadmusical_genre(analyzer):
    model.newUserGenre(analyzer,"reggae",60, 90)
    model.newUserGenre(analyzer,"down-tempo",70, 100)
    model.newUserGenre(analyzer,"chill-out",90, 120)
    model.newUserGenre(analyzer,"hip-hop",85, 115)
    model.newUserGenre(analyzer,"jazz_and_funk",120, 125)
    model.newUserGenre(analyzer,"pop",100, 130)
    model.newUserGenre(analyzer,"r&b",60, 80)
    model.newUserGenre(analyzer,"rock",110, 140)
    model.newUserGenre(analyzer,"metal",100, 160)
    

# ======================================
# Funciones de consulta sobre el catálogo
# ======================================

def getReproductions(analyzer, content_char, value_min,value_max):
    """
    Requerimiento 1 
    """
    return model.getReproductions(analyzer, content_char, value_min,value_max)

def partyMusic(analyzer, min_energy, max_energy,min_danceability,max_danceability):
    """
    Requirimiento 2
    """
    return model.partyMusic(analyzer, min_energy, max_energy,min_danceability,max_danceability)

def EstudyMusic(analyzer, min_instru, max_instru,min_tempo,max_tempo):
    return model.EstudyMusic(analyzer, min_instru, max_instru,min_tempo,max_tempo)

def newUserGenre(analyzer,new_genre,tempo_low,tempo_high):
    return model.newUserGenre(analyzer,new_genre,tempo_low,tempo_high)

def genreSearch(cont,genres):
    return model.genreSearch(cont,genres)


def getgeneromusicalmasescuchadoeneltiempo(analyzer, initialDate, finalDate):
    initialDate = datetime.datetime.strptime(initialDate, '%H:%M')
    
    

    
    finalDate = datetime.datetime.strptime(finalDate, '%H:%M')
    

    return model.getgeneromusicalmasescuchadoeneltiempo(analyzer, initialDate.time(), finalDate.time())

# ======================================
# Funciones de tamaño del catálogo
# ======================================
def videosSize(catalog):
    """
    Numero de videos cargados al catalogo
    """
    return model.videosSize(catalog)

def artistSize(catalog):
    """
    Número de libros en el catago
    """
    return model.artistSize(catalog)

def trackSize(catalog):
    """
    Número de libros en el catago
    """
    return model.trackSize(catalog)

# Funciones de impresión 

def printGenre(cont):
    return model.printGenre(cont)

def lastGenre(cont,new_genre):
    return model.lastGenre(cont,new_genre)

# ======================================
# Funciones de carga previas al catálogo 
# ======================================
def loadData0(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    loadEvents(analyzer)
    loadmusical_genre(analyzer)