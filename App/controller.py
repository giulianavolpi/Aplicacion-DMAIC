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
    catalogo = model.crear_mapas(catalogo)

    return catalogo

#=========================================================
# R. Intriducción al porgrama 
#=========================================================
def intro():
    lista=model.intro()
    return lista 

#=========================================================
# R. Análisis Indicador 
#========================================================= 
def analisis_indic():
    lista=model.analisis_indic()
    
    return lista

#=========================================================
# R. Cálculo de porcentaje desperdiciado
#=========================================================
def porcent_desperdicio(larga, mecanizada, nombre, catalogo):
   
    lista= model.porcent_desperdicio(larga, mecanizada, nombre, catalogo)
    
    return lista


#===================================================================
# R. Requerimientos en máquinas y operarios para desperdicio mínimo 
#===================================================================
def para_porcent(nombre,catalogo):
  
    lista= model.para_porcent(nombre,catalogo)
   
    return lista
