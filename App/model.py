
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
import datetime
import random
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -instrumentalidad
    - acousticness
    - liveness
    - speechiness
    - energy
    - danceability
    - valence
    Retorna el analizador inicializado.
    """
    analyzer = {'events': None,
                "musical_genre":None,
                'artist_ID': None,
                "track_ID": None,
                "instrumentalness": None,
                "acousticness": None,
                "liveness": None,
                "speechiness": None,
                "energy":None,
                "danceability": None,
                "valence": None
                }
    # Listas
    analyzer['events'] = lt.newList('ARRAY_LIST', compareIds)

    # RBT 
    analyzer["instrumentalness"] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['acousticness'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['liveness'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['speechiness'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['energy'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['danceability'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['valence'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['tempo'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['dates_c'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    analyzer['dates_u'] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    

    # Tablas de Hash 
    analyzer['artist_ID'] = mp.newMap(10000,maptype='PROBING',loadfactor=0.5, comparefunction=compareByName)
    analyzer['track_ID'] = mp.newMap(10000,maptype='PROBING',loadfactor=0.5, comparefunction=compareByName)
    analyzer["musical_genre"] = mp.newMap(15,maptype='PROBING',loadfactor=0.5, comparefunction=compareByName)
    analyzer["hashtag"] = mp.newMap(15,maptype='PROBING',loadfactor=0.5, comparefunction=compareByName)

    return analyzer

# ==============================
# Funciones para agregar informacion al catalogo
# ==============================

def add_event(analyzer, event):
    lt.addLast(analyzer['events'], event)

    addArtist_ID(analyzer,event["artist_id"].strip(),event)
    addTrack_ID(analyzer,event["track_id"].strip(),event)
    addHashTag(analyzer,event["hashtag"].strip(),event)
    
    
    for key in analyzer.keys():
        if analyzer[key]["type"] == "RBT":
            update_keys(analyzer,event,key)

    updateDateIndex(analyzer["dates_c"], event)

            
 def add_userTrack(analyzer, event):

     updateDateIndex(analyzer["dates_u"], event)


# ==============================
# Funciones para creación
# ==============================
def new_musical_genre(name,lower,upper):
    genre ={"genre_type": "", 
            "lower":0, 
            "upper":0,
            "totchar":0,
            "events":None}
    genre["genre_type"] = name
    genre["lower"] = int(lower)
    genre["upper"] = int(upper)
    genre["events"] = om.newMap(omaptype='RBT',comparefunction=compareDates)
    return genre
# ==============================
# Funciones para add
# ==============================

def addArtist_ID(analyzer, artist_n,event):
    """
    param analyzer: el catálogo de videos subidos con loadData()
    param artist_n: nombre del artista que se va a guardar 
    param video: c/ video 
    returns: Adicional por país específico
    """
    artist= analyzer['artist_ID']
    moj= mp.contains(artist,artist_n)
    if moj:
        valoactual = mp.get(artist,artist_n) 
        valor = me.getValue(valoactual)
    else:
        mp.put(artist,artist_n,lt.newList("ARRAY_LIST"))
        artsta = mp.get(artist,artist_n)
        valor= me.getValue(artsta)
    lt.addLast(valor,event)

def addTrack_ID(analyzer, artist_n,event):
    """
    param analyzer: el catálogo de videos subidos con loadData()
    param artist_n: nombre del artista que se va a guardar 
    param video: c/ video 
    returns: Adicional por país específico
    """
    artist = analyzer['track_ID']
    moj= mp.contains(artist,artist_n)
    if moj:
        valoactual = mp.get(artist,artist_n) 
        valor = me.getValue(valoactual)
    else:
        mp.put(artist,artist_n,lt.newList("ARRAY_LIST"))
        artsta = mp.get(artist,artist_n)
        valor= me.getValue(artsta)
    lt.addLast(valor,event)

def addHashTag(analyzer, artist_n,event):
    """
    param analyzer: el catálogo de videos subidos con loadData()
    param artist_n: nombre del artista que se va a guardar 
    param video: c/ video 
    returns: Adicional por país específico
    """
    artist = analyzer["hashtag"]
    moj= mp.contains(artist,artist_n)
    if moj:
        valoactual = mp.get(artist,artist_n) 
        valor = me.getValue(valoactual)
    else:
        mp.put(artist,artist_n.lower(),lt.newList("ARRAY_LIST"))
        artsta = mp.get(artist,artist_n)
        valor= me.getValue(artsta)
    lt.addLast(valor,event)

def add_music_genre(analyzer, tag):
    newtag = new_musical_genre(tag['\ufeff"genero"'],tag["bpm_min"],tag["bpm_max"])
    mp.put(analyzer["musical_genre"] ,tag['\ufeff"genero"'], newtag)
# ==============================
# Funciones para update
# ==============================
def update_keys(analyzer, track_n,key):
    
    analyzer_rbt = analyzer[key]
    moj = track_n[key] # El valor numérico de la característica

    if om.contains(analyzer_rbt,moj):
        entry = om.get(analyzer_rbt,moj)
        valor = me.getValue(entry)
    else:
        valor = {key: moj, "events": lt.newList("ARRAY_LIST")}
        om.put(analyzer_rbt,moj,valor) 
    lt.addLast(valor["events"],track_n)

def updateDateIndex(map, event):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = event['created_at']
    eventdate = datetime.datetime.strptime(occurreddate, '%H:%M')
    entry = om.get(map, crimedate.date())
    if entry is None:
        datentry = newDataEntry(event)
        om.put(map, eventdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, event)
    return map

def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'created_at': None, 'value': None}
    entry['offenseIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareOffenses)
    entry['lstcrimes'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry



    


# ==============================
# Funciones de consulta
# ==============================

#-------------------------------
# REQUERIMIENTO 1
#-------------------------------

def getReproductions(analyzer, content_char, value_min,value_max):
    """
    Requerimiento 1
    """
    # Creación de una lista 
    videosct = lt.newList("ARRAY_LIST")
    # filtro 1: por minKey y MaxKey 
    lst = om.values(analyzer[content_char], value_min, value_max)
    totchar = 0 # contador 
    for lstdate in lt.iterator(lst):
        # cuenta el número de tracks y las suma 
        totchar += lt.size(lstdate['events'])
        # filtro 2: crea una list con artist_id y saca lt.size()
        for element in lt.iterator(lstdate["events"]):
            if lt.isPresent(videosct, element['artist_id'])==0: 
                lt.addLast(videosct, element['artist_id'])

    return {"Total of reproductions":totchar, "Total of unique artists": lt.size(videosct)} 


#-------------------------------
# REQUERIMIENTO 2
#-------------------------------
def partyMusic(analyzer, min_energy, max_energy,min_danceability,max_danceability):
    """
    Requerimiento 2
    """
    # Creación de un map y lista
    track_map = om.newMap(omaptype='RBT',comparefunction=compareDates)
    videosct = lt.newList("ARRAY_LIST")
    
    # filtro 1: por minKey y MaxKey de energy 
    lst = om.values(analyzer["energy"], min_energy, max_energy)
    for lstdate in lt.iterator(lst):
        
        for element in lt.iterator(lstdate["events"]):
            if (element["danceability"] > min_danceability) and (element["danceability"]< max_danceability):
                if om.contains(track_map,element["track_id"])== False:
                    om.put(track_map,element["track_id"],
                    {"danceability":element["danceability"],"energy":element["energy"]})
    size= om.size(track_map)
    print("Total of unique track events: ", size)
    for pos in random.sample(range(1, size), 5):
        key = om.select(track_map,pos)
        item = om.get(track_map,key)
        value = me.getValue(item)
        lt.addLast(videosct,{"track_id": key, "danceability": value["danceability"],"energy": value["energy"]})
    return videosct

#-------------------------------
# REQUERIMIENTO 3
#-------------------------------
def EstudyMusic(analyzer, min_instru, max_instru,min_tempo,max_tempo):
    track_map = om.newMap(omaptype='RBT',comparefunction=compareDates)
    videosct = lt.newList("ARRAY_LIST")
    track_map = om.newMap(omaptype='RBT',comparefunction=compareDates)
    videosct = lt.newList("ARRAY_LIST")
    
    # filtro 1: por minKey y MaxKey de energy 
    lst = om.values(analyzer["instrumentalness"], min_instru, max_instru)
    for lstdate in lt.iterator(lst):
        
        for element in lt.iterator(lstdate["events"]):
            if (element["tempo"] > min_tempo) and (element["tempo"]< max_tempo):
                if om.contains(track_map,element["track_id"])== False:
                    om.put(track_map,element["track_id"],
                    {"instrumentalness":element["instrumentalness"],"tempo":element["tempo"]})
    size= om.size(track_map)
    print("Total of unique track events: ", size)
    for pos in random.sample(range(1, size), 5):
        key = om.select(track_map,pos)
        item = om.get(track_map,key)
        value = me.getValue(item)
        lt.addLast(videosct,{"track_id": key, "instrumentalness": value["instrumentalness"],"tempo": value["tempo"]})
    return videosct


#-------------------------------
# REQUERIMIENTO 4
#-------------------------------
def newUserGenre(analyzer,new_genre,tempo_low,tempo_high):
    newtag = new_musical_genre(new_genre,tempo_low,tempo_high)
    mp.put(analyzer["musical_genre"] ,new_genre, newtag)

def genreSearch(analyzer,genres):
    videosct = lt.newList("ARRAY_LIST")
    for every_genre in genres: 
        tagg=mp.get(analyzer["musical_genre"],every_genre) 
        taggg=me.getValue(tagg) 
        
        minor = taggg["lower"]
        mayor = taggg["upper"]

        # filtro 1: por minKey y MaxKey 
        lst = om.values(analyzer["tempo"], minor, mayor)
        totchar = 0 # contador

        for lstdate in lt.iterator(lst):
        # cuenta el número de tracks y las suma 
            totchar += lt.size(lstdate['events'])
            taggg["totchar"]= totchar
            for element in lt.iterator(lstdate["events"]):
                if om.contains(taggg["events"],element["artist_id"]) == False:
                    om.put(taggg["events"],element["artist_id"],None)
        
        different_artist = om.size(taggg["events"])
        reproductions = taggg["totchar"]
        
        print("========{}========".format(every_genre))
        print("For {} the tempo is between {} and {} BPM".format(every_genre,minor,mayor))
        print("{} reproductions: {} with {} different artists".format(every_genre,reproductions,different_artist))
        
        print("---- Some artists for {}----".format(every_genre))
        for pos in random.sample(range(1, different_artist), 10):
            key = om.select(taggg["events"],pos)
            print("Artist {}:{}".format(pos,key))
    return "-"
        

    
#-------------------------------
# REQUERIMIENTO 5
#-------------------------------
# ==============================
def getgeneromusicalmasescuchadoeneltiempo(analyzer, initialDate, finalDate):
    lst = om.values(analyzer['dates_c'], initialDate, finalDate)
    lst1 = om.values(analyzer['dates_u'], initialDate, finalDate) 

    videosct = lt.newList("ARRAY_LIST")
    videosct1 = lt.newList("ARRAY_LIST")
    videosct2 = lt.newList("ARRAY_LIST")
    # filtro 1: por minKey y MaxKey 
    
    totchar = 0 # contador 
    for lstdate in lt.iterator(lst):
        # cuenta el número de tracks y las suma 
        totchar += lt.size(lstdate['events'])
        # filtro 2: crea una list con artist_id y saca lt.size()
        for element in lt.iterator(lstdate["events"]):
            if lt.isPresent(videosct, element['artist_id'])==0: 
                lt.addLast(videosct, element['artist_id'])
    
    totchar = 0 # contador 
    for lstdate in lt.iterator(lst):
        # cuenta el número de tracks y las suma 
        totchar += lt.size(lstdate['events'])
        # filtro 2: crea una list con artist_id y saca lt.size()
        for element in lt.iterator(lstdate["events"]):
            if lt.isPresent(videosct1, element['track_id'])==0: 
                lt.addLast(videosct1, element['track_id'])

    for videos in lt.iterator(videosct):
        if lt.isPresent(videosct1,videos):
            lt.addLast(videosct2,videos)









# Funciones de Comparacion
# ==============================

def compareByName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

# Funciones de Tamaño

def videosSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer["events"])

def artistSize(analyzer):
    """
    Número de libros en el catago
    """
    return mp.size(analyzer['artist_ID'])

def trackSize(analyzer):
    """
    Número de libros en el catago
    """
    return mp.size(analyzer['track_ID'])

# Funciones de impresión 

def printGenre(analyzer):
    
    llaves = mp.keySet(analyzer["musical_genre"])
    for every_key in lt.iterator(llaves):
        if every_key != None: 
            item = mp.get(analyzer["musical_genre"],every_key)
        llave = me.getKey(item)
        print(llave)
    return "-------"
def lastGenre(analyzer,new_genre):
    
    llaves = mp.keySet(analyzer["musical_genre"])
    for every_key in lt.iterator(llaves):
        if every_key != None: 
            item = mp.get(analyzer["musical_genre"],every_key)
        llave = me.getKey(item)
        if llave == new_genre:
            answer = llave
    return answer