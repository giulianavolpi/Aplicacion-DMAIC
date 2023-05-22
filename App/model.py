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
    base_de_datos = cf.data_dir + 'Base de Datos DMAIC' + '.csv'
    
    input_file_datos = csv.DictReader(open(base_de_datos, encoding='utf-8'))
    """
    input_file_amazon = csv.DictReader(open(peliculas_amazon, encoding='utf-8'))
    input_file_disney = csv.DictReader(open(peliculas_disney, encoding='utf-8'))
    input_file_hulu= csv.DictReader(open(peliculas_hulu, encoding='utf-8'))
    input_file_netflix= csv.DictReader(open(peliculas_netflix, encoding='utf-8'))
    
    archivos=[input_file_amazon,input_file_disney,input_file_hulu,input_file_netflix]
    """
    datos = [input_file_datos]
    for dato in datos: 
        for empresa in dato:
            print(empresa("nombre"))
            agregarempresa(catalogo, empresa["nombre"], empresa, "nombre")
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

def intro():
    intro = "A partir de las estadísticas del sector azucarero colombiano y de los datos brindados por \n el ingenio Riopaila y Castilla se realizó un programa para calcular y analizar el indicador de desempeño frente a distintas empresas.  "
    esp = "Con los valores se distintas empresas se puede calcular el porcentaje de desperdicio o para obtener un porcentaje desead \n se calcuan las cantidades de máquinas y de operarios necesariaos."
    cnc = "Se llegó a la conclusión que el la mejor distribución entre caña larga y caña mecanizada es la siguiente: \n"
    porc = " Caña larga: 35%\n"
    porc2 = "Caña mecanizada : 65%"
    resp = intro + esp + cnc + porc + porc2

    return resp

    


#=========================================================
# requerimiento 2
#=========================================================      
def consulta_aniotv(anio_consulta,catalogo): 
    if mp.contains(catalogo["año"],anio_consulta)==True:
        resp= mp.get(catalogo['año'],anio_consulta)
    else:
        resp= False
   
    return resp
def analisis_indic():
    a = "El idicador de desempeño calcula la capacidad de desperdicio de caña por vagones al distribuir la caña entre un contre manual y uno mecanizado\n"
    b = "El cálculo del indicador es: Desperdicio = 1-(Capacidad de caña larga por vagón / Capacidad de caña mecanizada por vagón)\n"
    resp = a+b 
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
def porcent_desperdicio(larga, mecanizada, nombre, catalogo):
    lista = lt.newList()
    desp = 1 - (larga/mecanizada)
    if mp.contains(catalogo["nombre"],nombre)==True:
        cantidad= mp.get(catalogo['cantidad_cana'],nombre)
        cantidad = cantidad * desp
  
    lt.addLast(lista,desp)
    lt.addLast(lista,cantidad)
    return lista


#=========================================================
# requerimiento 4
#=========================================================
def filtro_por_genero(nombre,catalogo):
    if mp.contains(catalogo["genero"],nombre)==True:
        resp= mp.get(catalogo['genero'],nombre)
      
    else:
        resp= False
    return resp

def para_porcent(nombre, catalogo):
    lista = lt.newList()
    if mp.contains(catalogo["nombre"],nombre)==True:
        cantidad= mp.get(catalogo['cantidad_cana'],nombre)

        larga = cantidad * 0.35
        mecan = cantidad * 0.65

        personas = round((larga/5.5),0)
        maquinas = round((mecan/160),0)
        lt.addLast(lista,personas)
        lt.addLast(lista,maquinas)
    
    return lista 

#=========================================================
# Funciones de comparación
#=========================================================
def cmpsort(tupla1, tupla2):
    resp=False
    if tupla1[1]>tupla2[1]:
        resp=True
    return resp

