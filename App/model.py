"""
Es la lógica del programa
Donde se calculan los porcentajes del indicador
 """



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

    return catalog

#=========================================================
# Llenamos el catalgo con la info
#=========================================================
def crear_mapas(catalogo):

    base_de_datos = cf.data_dir + 'Base de Datos DMAIC' + '.csv'
    
    input_file_datos = csv.DictReader(open(base_de_datos, encoding='utf-8'))

    datos = [input_file_datos]
    for dato in datos: 
        for empresa in dato:
            print(empresa("nombre"))
            agregarempresa(catalogo, empresa["nombre"], empresa, "nombre")
            agregarempresa(catalogo, empresa["toneladas_cana"], empresa, "toneladas_cana")
            agregarempresa(catalogo, empresa["cantidad_maquinas"], empresa, "cantidad_maquinas")
            agregarempresa(catalogo, empresa["operarios"], empresa, "operarios")
            agregarempresa(catalogo, empresa["porcentaje_deseado"], empresa, "porcentaje")

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
#  R. Intriducción al porgrama 
#=========================================================
def intro():
    intro = "A partir de las estadísticas del sector azucarero colombiano y de los datos brindados por el ingenio Riopaila y Castilla se realizó un programa para calcular y analizar el indicador de desempeño frente a distintas empresas.  "
    esp = "Con los valores se distintas empresas se puede calcular el porcentaje de desperdicio o para obtener un porcentaje desead se calcuan las cantidades de máquinas y de operarios necesariaos."
    cnc = "Se llegó a la conclusión que el la mejor distribución entre caña larga y caña mecanizada es la siguiente: \n"
    porc = " Caña larga: 35%\n"
    porc2 = "Caña mecanizada : 65%"
    resp = intro + esp + cnc + porc + porc2

    return resp

    


#=========================================================
# R. Análisis Indicador 
#=========================================================      
def analisis_indic():
    a = "El idicador de desempeño calcula la capacidad de desperdicio de caña por vagones al distribuir la caña entre un contre manual y uno mecanizado\n"
    b = "El cálculo del indicador es: Desperdicio = 1-(Capacidad de caña larga por vagón / Capacidad de caña mecanizada por vagón)\n"
    resp = a+b 
    return resp

#=========================================================
# R. Cálculo de porcentaje desperdiciado
#========================================================= 
def porcent_desperdicio(larga, mecanizada, nombre, catalogo):
    lista = lt.newList()
    desp = 1 - (larga/mecanizada)
    if mp.contains(catalogo["nombre"],nombre)==True:
        cantidad= mp.get(catalogo['cantidad_cana'],nombre)
        cantidad = cantidad * desp
  
    lt.addLast(lista,desp)
    lt.addLast(lista,cantidad)
    return lista


#==================================================================
# R. Requerimientos en máquinas y operarios para desperdicio mínimo
#==================================================================
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

