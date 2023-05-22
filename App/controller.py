"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

import config as cf
import model
import csv
import tracemalloc
import time
import csv
import sys

csv.field_size_limit(2147483647)


# Inicialización del Catálogo de libros

def crear_catalogo():
    return model.crear_catalogo()

def loadData(catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    catalogo = model.crear_mapas(catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return delta_time,delta_memory,catalogo

#=========================================================
# requerimiento 1
#=========================================================
def consulta_aniopel(anio_consulta,catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista=model.consulta_aniopel(anio_consulta,catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory

#=========================================================
# requerimiento 2
#========================================================= 
def consulta_aniotv(anio_consulta,catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista=model.consulta_aniotv(anio_consulta,catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory

#=========================================================
# requerimiento 3
#=========================================================
def filtro_por_actor(nombre,catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista= model.filtro_por_actor(nombre, catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory


#=========================================================
# requerimiento 4
#=========================================================
def filtro_por_genero(nombre,catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista= model.filtro_por_genero(nombre,catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory


#=========================================================
# requerimiento 5
#=========================================================
def filtro_por_pais(nombre,catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista= model.filtro_por_pais(nombre,catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory



#=========================================================
# requerimiento 6
#=========================================================
def filtro_por_director(nombre,catalogo):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista=model.filtro_por_director(nombre,catalogo)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory


#=========================================================
# requerimiento 7
#=========================================================
def top_genero(catalogo,n):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    lista=model.top_genero(catalogo,n)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return lista, delta_time, delta_memory

#=========================================================
# requerimiento Bono
#=========================================================
#MEDIR TIEMPO--------------------------------------------------
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

# Funciones para medir la memoria utilizada
def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
