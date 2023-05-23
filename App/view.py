"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



from time import strptime
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
assert cf
from tabulate import tabulate
import datetime as dt
import model

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

#=========================================================
# R. Intriducción al porgrama 
#=========================================================
def intro():
    lista=controller.intro()
    return lista
#=========================================================
# R. Análisis Indicador 
#=========================================================
def analisis_indic():
    lista=controller.analisis_indic()
    return lista

#=========================================================
# R. Cálculo de porcentaje desperdiciado
#=========================================================
def porcent_desperdicio(larga, mecanizada, nombre, catalogo):
    lista=controller.porcent_desperdicio(larga, mecanizada, nombre, catalogo)
    return lista

#===================================================================
# R. Requerimientos en máquinas y operarios para desperdicio mínimo
#===================================================================
def para_porcent(nombre,catalogo):
    lista=controller.para_porcent(nombre,catalogo)
    return lista


#=========================================================
# MENU
#=========================================================
def printMenu():
    print("Bienvenido")
    print("0- Cargar datos")
    print("1- Introducción Aplicación")
    print("2- Análisis Indicador")
    print("3- Cálculo de porcentajes de desperdicio")
    print("4- Requisitos para desperdicio mínimo")
    print("11- Salir ")

catalog = None

#=========================================================
# Menu principal
#=========================================================
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')  
    
    if int(inputs[0]) == 0:
        #cargar los archivos
        print("Cargando información de los archivos ....\n")
        catalogo= controller.crear_catalogo()
       
        print('Datos cargados correctamente')
       
        

        
    if int(inputs[0]) == 1:
        
        print ("Bienvenido a la Aplicación DMAIC")
        print ("Se calculará el desperdicio en el manejo de caña larga y caña mecanizada en los vagones")
        resp=intro()
        print (resp[0])
        print (resp[1])
        print (resp[2])
     


    if int(inputs[0]) == 2:
        
        print ("Análisis del Indicador")
        resp = analisis_indic()
        print(resp[0]) 
        print(resp[1])


    if int(inputs[0]) == 3:
        nombre=input("Digíte el nombre de la empresa: ")
        larga=input("Digíte la cantidad de caña larga: ")
        mecanizada=input("Digíte la cantidad de caña larga: ")
        resp = porcent_desperdicio(larga, mecanizada, nombre, catalogo)
        
        desperdicio = resp[0]
        cantidad = resp[1]
        
        print("El porcentaje de desperdicio de la empresa: " + nombre + " es de " + desperdicio)
        print("La cantdad de caña desperdiciada actualmente es de: " + cantidad)

    if int(inputs[0]) == 4:
        nombre=input("Digíte el nombre de la empresa: ")
        resp = para_porcent(nombre,catalogo)

        personas = resp[0]
        maquinas = resp[1]

        print("Para obenter un porcentaje de desperdicio deseado, siguiendo el indicador.")
        print("Los requisitos para la empresa " + nombre + " son los siguientes: ")
        print ("Cantidad de personas: " + personas)
        print ("Cantidad de máquinas: " + maquinas)
printMenu()



