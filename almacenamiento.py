
#Tarea corta 09
#Analisis de algoritmos
#Jose Alexander Artavia Quesada
#2015098028

#----------------------------------------------------------------#

def maximizar(As, D):
    
    """
    Funcion que ordena un conjunto de tuplas (archivos) segun
    su tamano, para luego llamar la funcion auxiliar
    
    E: Un conjunto de tuplas (AS) con un texto(nombre)
       y un tamanio, ademas de un almacenamiento (D)
    S: Retorna las tuplas ordenadas segun el tamano del archivo y
       el almacenamiento
    R: Tuplas con dos elementos en ellas, tipo str y tipo int
    """ 

    #Se ordenan las tuplas con la funcion de python
    resultado = sorted(As, key=lambda elemento:elemento[1])
    
    #El almacenamiento no es un numero
    if isinstance(D,int) != True:
        return []

    else:
        return maximizarAux(resultado, D)

#----------------------------------------------------------------#

def maximizarAux(archivos, almacenamiento):
    
    """
    Funcion que recorre los archivos ya ordenados y toma los
    primeros archivos que en su tamanio total sean menores o
    iguales que el almacenamiento
    
    E: Un conjunto archivos ordenados por tamanio y un
       almacenamiento
    S: Retorna un conjunto de tuplas que su suma total de
       tamanios sea igual o menor que el almacenamiento
    R: Tipo str, tipo int
    """

    largoArchivos = len(archivos)
    resultado = []
    total = 0
    i = 0

    #Mientras aun exista almacenamiento
    while total < almacenamiento and i < (largoArchivos - 1):

        #Si el siguiente archivo entra en el almacenamiento
        if total + archivos[i][1] <= almacenamiento:
            resultado.append(archivos[i])
            total = total + archivos[i][1]
            i += 1

        #El siguiente archivo no entra, se retornan los que si
        else:
            return resultado
    

#----------------------------------------------------------------#

"""
As = [('archivo1', 10), ('archivo2', 5), ('archivo3', 3),
     ('archivo4', 8), ('archivo5', 9), ('archivo6', 1)]
D = 10

print(maximizar(As,D))
"""

#raise NotImplementedError()


#Nota para el portafolio, se agrega i < (largoArchivos - 1) para evitar
#error de fuera de indice en el test

