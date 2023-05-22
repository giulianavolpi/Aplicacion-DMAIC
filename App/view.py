﻿"""
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
# requerimiento 1
#=========================================================
def consulta_aniopel(anio_consulta,catalogo):
    lista=controller.consulta_aniopel(anio_consulta,catalogo)
    return lista
#=========================================================
# requerimiento 2
#=========================================================
def consulta_aniotv(anio_consulta,catalogo):
    lista=controller.consulta_aniotv(anio_consulta,catalogo)
    return lista

#=========================================================
# requerimiento 3
#=========================================================
def filtro_por_actor(nombre,catalogo):
    lista=controller.filtro_por_actor(nombre,catalogo)
    return lista

#=========================================================
# requerimiento 4
#=========================================================
def filtro_por_genero(nombre,catalogo):
    lista=controller.filtro_por_genero(nombre,catalogo)
    return lista

#=========================================================
# requerimiento 5
#=========================================================
def filtro_por_pais(nombre,catalogo):
    lista=controller.filtro_por_pais(nombre,catalogo)
    return lista
#=========================================================
# requerimiento 6
#=========================================================
def filtro_por_director(nombre,catalogo):
    lista=controller.filtro_por_director(nombre,catalogo)
    return lista
#=========================================================
# requerimiento 7
#=========================================================
def top_genero(catalogo,n):
    lista=controller.top_genero(catalogo,n)
    return lista

#=========================================================
# MENU COMPLETO
#=========================================================
def printMenu():
    print("Bienvenido")
    print("0- Cargar datos")
    print("1- Introducción Aplicación")
    print("2- Análisis Indicador")
    print("3- Cálculo de porcentajes caña")
    print("4- Impresión resultados obtenidos")
    print("5- x")
    print("6- x")
    print("7- x")
    print("8- x")
    print("11- Salir ")

catalog = None

#=========================================================
# Menu principal
#=========================================================
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')  
    
    if int(inputs[0]) == 0:
        """
        print("Seleccione el tamaño de la muestra: ")
        print("a- small")
        print("b- 5pct")
        print("c- 10pct")
        print("d- 20pct")
        print("e- 30pct")
        print("f- 50pct")
        print("g- 80pct")
        print("h- large")

        tamano = input("Digite su selección: ")
        if tamano == "a":
            tamano = "small"
        elif tamano == "b":
            tamano = "5pct"
        elif tamano == "c":
            tamano = "10pct"
        elif tamano == "d":
            tamano = "20pct"
        elif tamano == "e":
            tamano = "30pct"
        elif tamano == "f":
            tamano = "50pct"
        elif tamano == "g":
            tamano = "80pct"
        elif tamano=="h":
            tamano="large"
        """
        #cargar los archivos
        print("Cargando información de los archivos ....\n")
        catalogo= controller.crear_catalogo()
        delta_time, deltamemory, catalogo=controller.loadData(catalogo)

        #imprimit la primera tabla donde está el numero de peliculas
        """
        tabla_numero_peliculas=[["Netflix",lt.size(mp.get(catalogo['plataforma'],'netflix')['value'])],
        ["Amazon",lt.size(mp.get(catalogo['plataforma'],'amazon')['value'])],
        ["Hulu",lt.size(mp.get(catalogo['plataforma'],'hulu')['value'])],
        ["Disney",lt.size(mp.get(catalogo['plataforma'],'disney')['value'])]]
        print(tabulate(tabla_numero_peliculas,headers=["Plataforma", "Numero peliculas"],tablefmt="fancy_grid" ))
        plataforma=['netflix','hulu','disney','amazon']
        """
        print('Impresicarga de datos')
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

    if int(inputs[0]) == 5:
        nombre=input("Inserte el país por el que desea buscar: ") 
        resp= filtro_por_pais(nombre,catalogo)
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
            print("Lo sentimos, el país buscado no se encuentra en la base de datos")
        else:
            print(tabulate([["Movies",movie],['TV Show',tv]],headers=["type", "count"],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista)

    if int(inputs[0]) == 6:
        nombre=input("Inserte el director el que desea buscar: ")
        lista, delta_time, delta_memory= filtro_por_director(nombre,catalogo)

        if lista==False:
            print("Lo sentimos, el director buscado no se encuentra en la base de datos")
        else:
            movie=0
            tv=0
            ama=0
            net=0
            hul=0
            dis=0
            lista_imprimir3=[]
            for tup in lt.iterator(lista):
                lista_imprimir3.append([tup[0],tup[1]])
                movie+=tup[2]
                tv+=tup[3]
                ama+=tup[4]
                net+=tup[5]
                hul+=tup[6]
                dis+=tup[7]

            lista_imprimir1=[['Movie',movie],['Tv show',tv]]
            lista_imprimir2=[['amazon',ama],['netflix',net],['hulu',hul],['disney',dis]]
            lista30= mp.get(catalogo['director'],nombre)['value']
            
            print(tabulate(lista_imprimir1,headers=['type','count'],tablefmt="fancy_grid" ))
            print(tabulate(lista_imprimir2,headers=['service name','count'],tablefmt="fancy_grid" ))
            print(tabulate(lista_imprimir3,headers=['listed in','count'],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista30)


        
    if int(inputs[0]) == 7:
        top=input("Escriba cuantas posiciones desea que aparezcan ")
        resp=top_genero(catalogo,top)
        lista = resp[0]
        lista_imprimir=[]

        for i in range(1,lt.size(lista)+1):
            tupla=lt.getElement(lista,i)
            lista_pequeña=[tupla[0],tupla[1]]
            lista_imprimir.append(lista_pequeña)
        print(tabulate(lista_imprimir,headers=['genero','cantidad que aparecen'],tablefmt="fancy_grid" ))
        print("\n")

        lista_imprimi=[]
        for i in range(1,lt.size(lista)+1):
            tupla=lt.getElement(lista,i)
            lista_pe=[tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7]]
            lista_imprimi.append(lista_pe)
        print(tabulate(lista_imprimi,headers=['genero','cantidad que aparecen','conteo movie','conteo tv show','amazon','netflix','hulu','disney'],tablefmt="fancy_grid" ))
        print("\n")


printMenu()



