"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#from DISClib.ADT import list as lt
import model as mod
from tabulate import tabulate 
#=========================================================
# R. Intriducción al porgrama 
#=========================================================
def intro():
    lista=mod.intro()
    return lista
#=========================================================
# R. Análisis Indicador 
#=========================================================
def analisis_indic():
    lista=mod.analisis_indic()
    return lista

#=========================================================
# R. Cálculo de porcentaje desperdiciado
#=========================================================
def porcent_desperdicio(larga, mecanizada, nombre, catalogo):
    lista=mod.porcent_desperdicio(larga, mecanizada, nombre, catalogo)
    return lista

#===================================================================
# R. Requerimientos en máquinas y operarios para desperdicio mínimo
#===================================================================
def para_porcent(nombre,catalogo):
    lista=mod.para_porcent(nombre,catalogo)
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


#=========================================================
# Menu principal
#=========================================================
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')  
    
    if int(inputs[0]) == 0:
        #cargar el archivo
        print("Cargando información de los archivos ....\n")
        catalogo= mod.crear_catalogo()
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
        larga=float(input("Digíte la capacidad de caña larga de su vagón: "))
        mecanizada=float(input("Digíte la capacidad de caña mecanizada de su vagón: "))
        resp = porcent_desperdicio(larga, mecanizada, nombre, catalogo)
        
        desperdicio = resp[0]
        cantidad = resp[1]
        lista_imprimir = []
        lista_imprimir.append(desperdicio)
        lista_imprimir.append(cantidad )
        lista_imprimir=[["Porcentaje Desperdicio","Cantidad de Caña Desperdiciada"],[desperdicio, cantidad]]
       
        print("El porcentaje de desperdicio de la empresa " + nombre + "  y su cantidad de caña desperdiciada es de: ")
       
        print(tabulate(lista_imprimir,headers='firstrow', tablefmt='fancy_grid'))

    if int(inputs[0]) == 4:
        
        nombre=input("Digíte el nombre de la empresa: ")
        resp = para_porcent(nombre,catalogo)

        personas = resp[0]
        maquinas = resp[1]

        print("Para obenter un porcentaje de desperdicio deseado, siguiendo el indicador.")
        print("Los requisitos para la empresa " + nombre + " son los siguientes: ")
    
        lista_imprimir = []
        lista_imprimir.append(personas)
        lista_imprimir.append(maquinas )
        lista_imprimir=[["Operarios","Máquinas"],[personas, maquinas]]
        print(tabulate(lista_imprimir,headers='firstrow', tablefmt='fancy_grid'))

printMenu()

