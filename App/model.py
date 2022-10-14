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


import tracemalloc
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
import csv
from datetime import time


#=========================================================
# Creamos el catalogo vacio
#=========================================================
def crear_catalogo(tipo_hash):
    catalog={}
    catalog['tipo'] = mp.newMap(9688, 
                        maptype = tipo_hash,
                        loadfactor = 0.8)
    catalog['director'] = mp.newMap(9688, 
                        maptype = tipo_hash,
                        loadfactor = 0.8)
    catalog['actor'] = mp.newMap(9688, 
                        maptype = tipo_hash,
                        loadfactor = 0.8)
    catalog['plataforma'] = mp.newMap(9688, 
                        maptype = tipo_hash,
                        loadfactor = 0.8)
    catalog['año'] = mp.newMap(200, 
                        maptype = tipo_hash,
                        loadfactor = 0.8)
    catalog['genero']=mp.newMap(10000, 
                        maptype = tipo_hash,
                        loadfactor = 0.8)
    catalog['pais']=mp.newMap(200, maptype = tipo_hash,
                        loadfactor = 0.8)

    return catalog

#=========================================================
# Llenamos el catalgo con la info
#=========================================================
def crear_mapas(tamanio,catalogo):

    peliculas_amazon = cf.data_dir + 'amazon_prime_titles-utf8-' + tamanio + '.csv'
    peliculas_disney = cf.data_dir + "disney_plus_titles-utf8-" + tamanio + ".csv"
    peliculas_hulu = cf.data_dir + "hulu_titles-utf8-" + tamanio + ".csv"
    peliculas_netflix = cf.data_dir + "netflix_titles-utf8-" + tamanio + ".csv"

    input_file_amazon = csv.DictReader(open(peliculas_amazon, encoding='utf-8'))
    input_file_disney = csv.DictReader(open(peliculas_disney, encoding='utf-8'))
    input_file_hulu= csv.DictReader(open(peliculas_hulu, encoding='utf-8'))
    input_file_netflix= csv.DictReader(open(peliculas_netflix, encoding='utf-8'))

    archivos=[input_file_amazon,input_file_disney,input_file_hulu,input_file_netflix]
    for archivo in archivos:  
        for pelicula in archivo:
            #esta linea agrega al mapa del año la info
            agregarpelicula(catalogo, pelicula['release_year'],pelicula,'año')
            #esta linea agrega al mapa del director la info
            agregarpelicula(catalogo, pelicula['director'],pelicula,'director')
            #esta linea agrega al mapa del pais la info
            agregarpelicula(catalogo, pelicula['country'],pelicula,'pais')
            #esta linea agrega al mapa del actor la info
            actores=pelicula['cast'].split(',')
            for actor in actores:
                agregarpelicula(catalogo, actor,pelicula,'actor')

            #esta linea agrega al mapa del tipo la info
            agregarpelicula(catalogo, pelicula['type'],pelicula,'tipo')
            #esta linea agrega al mapa del plataforma la info
            if archivo==input_file_amazon:
                agregarpelicula(catalogo, 'amazon',pelicula, 'plataforma')
            elif archivo==input_file_disney:
                agregarpelicula(catalogo, 'disney',pelicula, 'plataforma')
            elif archivo==input_file_hulu:
                agregarpelicula(catalogo, 'hulu',pelicula, 'plataforma')
            elif archivo==input_file_netflix:
                agregarpelicula(catalogo, 'netflix',pelicula, 'plataforma')

            #esta linea agrega al mapa de los generos la info
            generos=pelicula['listed_in'].split(',')
            for genero in generos:
                agregarpelicula(catalogo, genero,pelicula,'genero')



    return  catalogo

def agregarpelicula(catalogo, llave, valor, clase):
    if mp.contains(catalogo[clase],llave)==True:
        pareja=mp.get(catalogo[clase],llave)
        lista=pareja['value']
        lt.addLast(lista,valor)
        mp.put(catalogo[clase],llave, lista )
    else:
        lista=lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista,valor)
        mp.put(catalogo[clase],llave, lista )
    


#=========================================================
# requerimiento 1   S
#=========================================================
def consulta_aniopel(anio_consulta,catalogo): 
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    if mp.contains(catalogo["año"],anio_consulta)==True:
        resp= mp.get(catalogo['año'],anio_consulta)
    else:
        resp= False
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return resp, delta_memory, delta_time


#=========================================================
# requerimiento 2
#=========================================================      
def consulta_aniotv(anio_consulta,catalogo): 
    start_time = getTime()
    start_memory = getMemory()
    if mp.contains(catalogo["año"],anio_consulta)==True:
        resp= mp.get(catalogo['año'],anio_consulta)
    else:
        resp= False
    stop_memory = getMemory()
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return resp, delta_memory, delta_time

#=========================================================
# requerimiento 3  S
#========================================================= 
def filtro_por_actor(nombre,catalogo):
    start_time = getTime()
    start_memory = getMemory()
    if mp.contains(catalogo["actor"],nombre)==True:
        resp= mp.get(catalogo['actor'],nombre)
    else:
        resp= False
    stop_memory = getMemory()
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return resp, delta_memory, delta_time


#=========================================================
# requerimiento 4
#=========================================================
def filtro_por_genero(nombre,catalogo):
    start_time = getTime()
    start_memory = getMemory()
    if mp.contains(catalogo["genero"],nombre)==True:
        resp= mp.get(catalogo['genero'],nombre)
      
    else:
        resp= False
    stop_memory = getMemory()
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return resp, delta_memory, delta_time

#=========================================================
# requerimiento 5
#=========================================================
def filtro_por_pais(nombre,catalogo):
    start_time = getTime()
    start_memory = getMemory()
    if mp.contains(catalogo["pais"],nombre)==True:
        resp= mp.get(catalogo['pais'],nombre)
    else:
        resp= False
    stop_memory = getMemory()
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return resp, delta_memory, delta_time


#=========================================================
# requerimiento 6
#=========================================================
def filtro_por_director(nombre,catalogo):
    start_time = getTime()
    start_memory = getMemory()
    if mp.contains(catalogo["director"],nombre)==True:
        resp= mp.get(catalogo['director'],nombre)
    else:
        resp= False
    stop_memory = getMemory()
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return resp, delta_memory, delta_time

#=========================================================
# requerimiento 7    S
#========================================================= 

def top_genero(catalogo,n):
    start_time = getTime()
    start_memory = getMemory()
    lista_generos=mp.keySet(catalogo['genero'])
    iterador=lt.iterator(lista_generos)

    lista=lt.newList(datastructure="ARRAY_LIST")
    for genero in iterador:
        lista_pelicula_genero=mp.get(catalogo['genero'],genero)['value']
        tamanio=lt.size(lista_pelicula_genero)
        movie=0
        tv=0
        iterador2=lt.iterator(lista_pelicula_genero)
        for pelicula in iterador2:
            if pelicula['type']=='Movie':
                movie+=1
            elif pelicula['type']=='TV Show':
                tv+=1

       
        lt.addLast(lista,(genero,tamanio,movie,tv))
    
    qs.sort(lista,cmpsort)

    lista=lt.subList(lista,1,int(n))

    stop_memory = getMemory()
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_memory, delta_time


    



#=========================================================
# requerimiento Bono
#=========================================================


#=========================================================
# Funciones de comparación
#=========================================================
def cmpsort(tupla1, tupla2):
    resp=False
    if tupla1[1]>tupla2[1]:
        resp=True
    return resp