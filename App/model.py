"""
Es la lógica del programa
Donde se calculan los porcentajes del indicador
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
def crear_catalogo():
    catalog={}
    catalog['id_empresa'] = mp.newMap(9688, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    catalog['nombre'] = mp.newMap(9688, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    catalog['toneladas_cana'] = mp.newMap(9688, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    catalog['cantidad_maquinas'] = mp.newMap(9688, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    catalog['operarios'] = mp.newMap(200, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    catalog['porcentaje_deseado']=mp.newMap(10000, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    """
    catalog['pais']=mp.newMap(200, maptype = "CHAINING",
                        loadfactor = 0.8)
    #Mapa para el requerimiento 6
    catalog['director_generos']=mp.newMap(2, 
                        maptype = "CHAINING",
                        loadfactor = 0.8)
    """
    return catalog

#=========================================================
# Llenamos el catalgo con la info
#=========================================================
def crear_mapas(catalogo):
    """
    peliculas_amazon = cf.data_dir + 'amazon_prime_titles-utf8-' + tamanio + '.csv'
    peliculas_disney = cf.data_dir + "disney_plus_titles-utf8-" + tamanio + ".csv"
    peliculas_hulu = cf.data_dir + "hulu_titles-utf8-" + tamanio + ".csv"
    peliculas_netflix = cf.data_dir + "netflix_titles-utf8-" + tamanio + ".csv"
    """
    base_de_datos = cf.data_dir + 'Base de Datos DMAIC-utf8' + '.csv'
    
    input_file_datos = csv.DictReader(open(base_de_datos, encoding='utf-8'))
    """
    input_file_amazon = csv.DictReader(open(peliculas_amazon, encoding='utf-8'))
    input_file_disney = csv.DictReader(open(peliculas_disney, encoding='utf-8'))
    input_file_hulu= csv.DictReader(open(peliculas_hulu, encoding='utf-8'))
    input_file_netflix= csv.DictReader(open(peliculas_netflix, encoding='utf-8'))
    
    archivos=[input_file_amazon,input_file_disney,input_file_hulu,input_file_netflix]
    """
    datos = [input_file_datos]
    for empresa in datos: 
        agregarempresa(catalogo, empresa["id_empresa"], empresa, "id")
        agregarempresa(catalogo, empresa["toneladas_cana"], empresa, "toneladas_cana")
        agregarempresa(catalogo, empresa["cantidad_maquinas"], empresa, "cantidad_maquinas")
        agregarempresa(catalogo, empresa["operarios"], empresa, "operarios")
        agregarempresa(catalogo, empresa["porcentaje_deseado"], empresa, "porcentaje")

    """
    for archivo in archivos:  
        for pelicula in archivo:
            if archivo==input_file_amazon:
                pelicula['plataforma']='amazon'
            elif archivo==input_file_disney:
                pelicula['plataforma']='disney'
            elif archivo==input_file_hulu:
                pelicula['plataforma']='hulu'
            elif archivo==input_file_netflix:
                pelicula['plataforma']='netflix'

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
            """



    return  catalogo

def agregarempresa(catalogo, llave, valor, clase):
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
    if mp.contains(catalogo["año"],anio_consulta)==True:
        resp= mp.get(catalogo['año'],anio_consulta)
    else:
        resp= False
   
    return resp
def porcent_cana(indicador, catalogo):
    


#=========================================================
# requerimiento 2
#=========================================================      
 def consulta_aniotv(anio_consulta,catalogo): 
    if mp.contains(catalogo["año"],anio_consulta)==True:
        resp= mp.get(catalogo['año'],anio_consulta)
    else:
        resp= False
   
    return resp

#=========================================================
# requerimiento 3  S
#========================================================= 
def filtro_por_actor(nombre,catalogo):
    if mp.contains(catalogo["actor"],nombre)==True:
        resp= mp.get(catalogo['actor'],nombre)
    else:
        resp= False
    return resp


#=========================================================
# requerimiento 4
#=========================================================
def filtro_por_genero(nombre,catalogo):
    if mp.contains(catalogo["genero"],nombre)==True:
        resp= mp.get(catalogo['genero'],nombre)
      
    else:
        resp= False
    return resp

#=========================================================
# requerimiento 5
#=========================================================
def filtro_por_pais(nombre,catalogo):
    if mp.contains(catalogo["pais"],nombre)==True:
        resp= mp.get(catalogo['pais'],nombre)
    else:
        resp= False
    return resp


#=========================================================
# requerimiento 6
#=========================================================
def filtro_por_director(nombre,catalogo):
    lista_generos=mp.keySet(catalogo['genero'])
    iterador=lt.iterator(lista_generos)
    dic={}
    for genero in iterador:
        dic[genero]= 0
        movie=0
        tv=0
        ama=0
        net=0
        hul=0
        dis=0

    if mp.contains(catalogo["director"],nombre)==True:
        lista= mp.get(catalogo['director'],nombre)['value']['elements']

        for pelicula in lista:
            generos = (pelicula["listed_in"]).split(",")
            for gen in generos:
                dic[gen]+=1
            if pelicula['type']=='Movie':
                movie+=1
            elif pelicula['type']=='TV Show':
                tv+=1
            if pelicula['plataforma']=='amazon':
                ama+=1
            elif pelicula['plataforma']=='netflix':
                net+=1
            elif pelicula['plataforma']=='hulu':
                hul+=1
            else:
                dis+=1
    else:
        lista_grande=False

    lista_grande=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic.keys():
        if dic[llave]>0:
            lt.addLast(lista_grande,(llave,dic[llave],movie,tv,ama,net,hul,dis))

    qs.sort(lista_grande,cmpsort)

    


    return lista_grande


#=========================================================
# requerimiento 7    S
#========================================================= 

def top_genero(catalogo,n):
    lista_generos=mp.keySet(catalogo['genero'])
    iterador=lt.iterator(lista_generos)

    lista=lt.newList(datastructure="ARRAY_LIST")
    for genero in iterador:
        lista_pelicula_genero=mp.get(catalogo['genero'],genero)['value']
        tamanio=lt.size(lista_pelicula_genero)
        movie=0
        tv=0
        ama=0
        net=0
        hul=0
        dis=0
        iterador2=lt.iterator(lista_pelicula_genero)
        for pelicula in iterador2:
            if pelicula['type']=='Movie':
                movie+=1
            elif pelicula['type']=='TV Show':
                tv+=1
            if pelicula['plataforma']=='amazon':
                ama+=1
            elif pelicula['plataforma']=='netflix':
                net+=1
            elif pelicula['plataforma']=='hulu':
                hul+=1
            else:
                dis+=1

       
        lt.addLast(lista,(genero,tamanio,movie,tv,ama,net,hul,dis))
    
    qs.sort(lista,cmpsort)

    lista=lt.subList(lista,1,int(n))

    return lista


    



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

