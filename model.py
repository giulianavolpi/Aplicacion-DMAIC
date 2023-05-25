"""
Es la lógica del programa
Donde se calculan los porcentajes del indicador
 """
#=========================================================
# Llenamos el catalgo con la info
#=========================================================

def crear_catalogo():
    archivo = open ("base_datos.csv", 'r', encoding='utf-8')
    datos=[]
    encabezados=archivo.readline().strip().split (",")

    for linea in archivo:
        informacion = linea.strip().split(",")
        
        empresa={
            "id_empresa":informacion [0],
            encabezados [1]:informacion [1], 
            encabezados [2]:int(informacion [2]),
            encabezados [3]:int(informacion [3]),
            encabezados [4]:int(informacion [4]),
            encabezados [5]:float(informacion [5])}
     
        datos.append(empresa)
        
    archivo.close()
    return datos


#=========================================================
#  R. Intriducción al porgrama 
#=========================================================
def intro():
    intro = "A partir de las estadísticas del sector azucarero colombiano y de los datos brindados por el ingenio Riopaila y Castilla se realizó un programa para calcular y analizar el indicador de desempeño frente a distintas empresas. \nCon los valores se distintas empresas se puede calcular el porcentaje \nde desperdicio o para obtener un porcentaje desead se calcuan las cantidades de máquinas y de operarios necesariaos.\n Se llegó a la conclusión que el la mejor distribución entre caña larga y caña mecanizada es la siguiente: \n"
    porc = " Caña larga: 35%\n"
    porc2 = "Caña mecanizada : 65%"
    
    return intro, porc, porc2 

#=========================================================
# R. Análisis Indicador 
#=========================================================      
def analisis_indic():
    
    a = "El idicador de desempeño calcula la capacidad de desperdicio de caña por vagones al distribuir la caña entre un contre manual y uno mecanizado\n"
    b = "El cálculo del indicador es: Desperdicio = 1-(Capacidad de caña larga por vagón / Capacidad de caña mecanizada por vagón)\n"
    
    return a,b 

#=========================================================
# R. Cálculo de porcentaje desperdiciado
#========================================================= 
def porcent_desperdicio(larga, mecanizada, nombre, catalogo):
    desp = 1- (larga/mecanizada)
    for empresa in catalogo:
        if empresa["nombre"] == nombre:
            cantidad = empresa["toneladas_cana"]
            cantidad = cantidad * desp
   
    return desp, cantidad

#==================================================================
# R. Requerimientos en máquinas y operarios para desperdicio mínimo
#==================================================================
def para_porcent(nombre, catalogo):

    for empresa in catalogo:
        if empresa["nombre"] == nombre:
            cantidad = empresa["toneladas_cana"]
            larga = cantidad * 0.35
            mecan = cantidad * 0.65

    personas = round((larga/5.5),0)
    maquinas = round((mecan/160),0)
    
    return personas, maquinas 

