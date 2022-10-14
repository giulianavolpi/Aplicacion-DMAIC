"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#=========================================================
# Funcion para imprimir
#=========================================================
def imprimir_3_primeros_y_ultimos(lista):
    #imprime para el caso especial de consulta entre años
    if lt.size(lista)>=6:
        lista_imprimir=[]
        for i in range(1,4):
            dic=lt.getElement(lista,i)
            if len(dic['description'])>50:
                dic['description']=dic['description'][0:50]
            lista_pequeña=[dic["title"],dic["release_year"],dic["director"],dic["duration"],dic["cast"],dic["country"],dic["listed_in"], dic["description"]]
            lista_imprimir.append(lista_pequeña)
        for i in range(lt.size(lista)-2,lt.size(lista)+1):
            dic=lt.getElement(lista,i)
            if len(dic['description'])>50:
                dic['description']=dic['description'][0:50]
            lista_pequeña=[dic["title"],dic["release_year"],dic["director"],dic["duration"],dic["cast"],dic["country"],dic["listed_in"], dic["description"]]
            lista_imprimir.append(lista_pequeña)
        print(tabulate(lista_imprimir,headers=["TÍTULO", "LANZAMIENTO","DIRECTOR","DURACIÓN","CASTING","PAÍS","GÉNERO","DESCRIPCIÓN"],tablefmt="fancy_grid",maxcolwidths=[10,10,10,10,10,10,10,10]  ))
        print("\n")
    else:
        lista_imprimir=[]
        for i in range(1,lt.size(lista)+1):
            dic=lt.getElement(lista,i)
            if len(dic['description'])>50:
                dic['description']=dic['description'][0:50]
            lista_pequeña=[dic["title"],dic["release_year"],dic["director"],dic["duration"],dic["cast"],dic["country"],dic["listed_in"], dic["description"]]
            lista_imprimir.append(lista_pequeña)
        print(tabulate(lista_imprimir,headers=["TÍTULO", "LANZAMIENTO","DIRECTOR","DURACIÓN","CASTING","PAÍS","GÉNERO","DESCRIPCIÓN"],tablefmt="fancy_grid",maxcolwidths=[10,10,10,10,10,10,10,10] ))
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
# requerimiento Bono
#=========================================================
def printMenu():
    print("Bienvenido")
    print("0- Cargar datos")
    print("1- Listar peliculas en un periodo")
    print("2- Listar programas de televisión en un periodo")
    print("3- Encontrar contenido donde participa un actor")
    print("4- Contenido filtrado por género específico")
    print("5- Contenido filtrado por país específico")
    print("6- Contenido filtrado por director específico")
    print("7- Top n elementos")
    print("8- Tipo de ordenamiento")
    print("11- Salir ")

catalog = None

#=========================================================
# Menu principal
#=========================================================
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')  
    
    if int(inputs[0]) == 0:

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

        #cargo los archivos
        print("Cargando información de los archivos ....\n")
        catalogo= controller.crear_catalogo()
        delta_time, deltamemory, catalogo=controller.loadData(catalogo, tamano)

        #imprimo la primera tabla donde está el numero de peliculas
        tabla_numero_peliculas=[["Netflix",lt.size(mp.get(catalogo['plataforma'],'netflix')['value'])],
        ["Amazon",lt.size(mp.get(catalogo['plataforma'],'amazon')['value'])],
        ["Hulu",lt.size(mp.get(catalogo['plataforma'],'hulu')['value'])],
        ["Disney",lt.size(mp.get(catalogo['plataforma'],'disney')['value'])]]
        print(tabulate(tabla_numero_peliculas,headers=["Plataforma", "Numero peliculas"],tablefmt="fancy_grid" ))
        plataforma=['netflix','hulu','disney','amazon']
        for plat in plataforma:
            print('lista para la plataforma '+plat)
            imprimir_3_primeros_y_ultimos(mp.get(catalogo['plataforma'],plat)['value'])
        print ("Tiempo de ejecución: " , delta_time)
        print ("Memoria utilizada: ", deltamemory)
        
    if int(inputs[0]) == 1:
        #organizar los datos en un periodo de tiempo dado
        anio_consulta=input("Digite el año que desea consultar: ")
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
        fecha = str(input("Escriba la fecha de agregado de programas de televisión a examinar (como 'november 16, 2019'): "))
        anio_consulta = fecha[-5:]
        resp = consulta_aniotv(anio_consulta,catalogo)
        lista = resp[0]['value']
        tv=0
        for dic_peli in lt.iterator(lista):
            if dic_peli['type']=='TV Show':
                tv+=1
        if lista==False:
            print("Lo sentimos, el año de la fecha buscada no se encuentra en la base de datos")
        else:
            print(tabulate([["Movies",movie]],headers=["type", "count"],tablefmt="fancy_grid" ))
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
        resp= filtro_por_director(nombre,catalogo)
        lista = resp[0]
        lista= lista['value']
        movie=0
        tv=0
        for dic_peli in lt.iterator(lista):
            if dic_peli['type']=='Movie':
                movie+=1
            else:
                tv+=1
        generos = catalogo["genero"]
        keys_generos = mp.keySet(generos)
        generos_lista = lt.newList("ARRAY LIST")
        for i in lt.iterator(keys_generos):
            lt.addLast(generos_lista,i)
        num_gen = lt.size(generos_lista)
            

        if lista==False:
            print("Lo sentimos, el director buscado no se encuentra en la base de datos")
        else:
            print(tabulate([["Movies",movie],['TV Show',tv]],headers=["type", "count"],tablefmt="fancy_grid" ))
            imprimir_3_primeros_y_ultimos(lista)

        
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
            lista_pe=[tupla[0],tupla[1],tupla[2],tupla[3]]
            lista_imprimi.append(lista_pe)
        print(tabulate(lista_imprimi,headers=['genero','cantidad que aparecen','conteo movie','conteo tv show'],tablefmt="fancy_grid" ))
        print("\n")


printMenu()



