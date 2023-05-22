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
# Funcion para imprimir
#=========================================================
def imprimir_3_primeros_y_ultimos(lista):
    #imprime para el caso especial de consulta entre años
    if lt.size(lista)>=6:
        lista_imprimir=[]
        for i in range(1,4):
            dic=lt.getElement(lista,i)
            """
            if len(dic['description'])>50:
                dic['description']=dic['description'][0:50]
            """
            lista_pequeña=[dic["id"],dic["nombre"],dic["toneladas_cana"],dic["cantidad_maquinas"],dic["operarios"],dic["porcentaje"]]
            lista_imprimir.append(lista_pequeña)
        for i in range(lt.size(lista)-2,lt.size(lista)+1):
            dic=lt.getElement(lista,i)
            """
            if len(dic['description'])>50:
                dic['description']=dic['description'][0:50]
            """
            lista_pequeña=[dic["id"],dic["nombre"],dic["toneladas_cana"],dic["cantidad_maquinas"],dic["operarios"],dic["porcentaje"]]
            lista_imprimir.append(lista_pequeña)
        print(tabulate(lista_imprimir,headers=["ID" , "NOMBRE", "TONELADAS CAÑA","CANTIDAD MAQUINAS","OPERARIOS","PORCENTAJE DESEADO"],tablefmt="fancy_grid",maxcolwidths=[10,10,10,10,10,10]  ))
        print("\n")
    else:
        lista_imprimir=[]
        for i in range(1,lt.size(lista)+1):
            dic=lt.getElement(lista,i)
            """
            if len(dic['description'])>50:
                dic['description']=dic['description'][0:50]
            """
            lista_pequeña=[dic["id"], dic["nombre"],dic["toneladas_cana"],dic["cantidad_maquinas"],dic["operarios"],dic["porcentaje"]]
            lista_imprimir.append(lista_pequeña)
        print(tabulate(lista_imprimir,headers=["ID", "NOMBRE", "TONELADAS CAÑA","CANTIDAD MAQUINAS","OPERARIOS","PORCENTAJE DESEADO"],tablefmt="fancy_grid",maxcolwidths=[10,10,10,10,10,10]  ))
        print("\n")

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
        delta_time, deltamemory, catalogo=controller.loadData(catalogo)

        #imprimit la primera tabla donde está el numero de peliculas
       
        print('Impresión carga de datos')
       
        empresas = lt.size(mp.get(catalogo['nombre'],empresa)['value'])
        for empresa in empresas:
            
            imprimir_3_primeros_y_ultimos(mp.get(catalogo['nombre'],empresa)['value'])
        
        print ("Tiempo de ejecución: " , delta_time)
        print ("Memoria utilizada: ", deltamemory)
        
    if int(inputs[0]) == 1:
        #organizar los datos en un periodo de tiempo dado
        anio_consulta=input("Digite el año que desea consultar: ")
        print (type(anio_consulta))
        resp=consulta_aniopel(anio_consulta,catalogo)
        lista =resp[0]['value']
        movie=0
        for dic_peli in lt.iterator(lista):
            if dic_peli['type']=='Movie':
                movie+=1
        if lista==False:
            print("Lo sentimos, el actor buscado no se encuentra en la base de datos")
        else:
            lista
            print(tabulate([["Movies",movie]],headers=["type", "count"],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista)

    if int(inputs[0]) == 2:
        fecha = (input("Escriba la fecha de agregado de programas de televisión a examinar (como 'november 16, 2019'): "))
        anio_consulta = str(fecha[-4:])
        print (type(anio_consulta))
        resp = consulta_aniotv(anio_consulta,catalogo)
        lista = resp[0]['value']
        tv=0
        for dic_peli in lt.iterator(lista):
            if dic_peli['type']=='TV Show':
                tv+=1
        if lista==False:
            print("Lo sentimos, el año de la fecha buscada no se encuentra en la base de datos")
        else:
            print(tabulate([['TV Show',tv]],headers=["type", "count"],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista)

    if int(inputs[0]) == 3:
        nombre=input("Escriba el nombre y el apellido del actor que desea buscar: ")
        resp = filtro_por_actor(nombre,catalogo)
        lista = resp[0]
        lista= lista['value']
        movie=0
        tv=0
        for dic_peli in lt.iterator(lista):
            if dic_peli['type']=='Movie':
                movie+=1
            else:
                tv+=1
        if lista==False:
            print("Lo sentimos, el actor buscado no se encuentra en la base de datos")
        else:
            print(tabulate([["Movies",movie],['TV Show',tv]],headers=["type", "count"],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista)

    if int(inputs[0]) == 4:
        nombre=input("Inserte el género por el que desea buscar: ")
        resp = filtro_por_genero(nombre,catalogo)
        lista = resp[0]
        lista= lista['value']
        movie=0
        tv=0
        for dic_peli in lt.iterator(lista):
            if dic_peli['type']=='Movie':
                movie+=1
            else:
                tv+=1
        if lista==False:
            print("Lo sentimos, el género buscado no se encuentra en la base de datos")
        else:
            print(tabulate([["Movies",movie],['TV Show',tv]],headers=["type", "count"],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista)

printMenu()



