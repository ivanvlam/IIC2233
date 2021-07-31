import pyrematch as re


# ------------------------------------------------------------------------------------------------
# DEFINIR AQUI LOS PATRONES PARA CONSTRUIR CADA EXPRESION REGULAR
# NO CAMBIAR LOS NOMBRES DE LAS VARIABLES
PATRON_1 = "(^|\n)# !titulo{[^\n]+}($|\n)"
PATRON_2 = "(^|\n)#{2,3} !subseccion{[^\n]+}($|\n)"
PATRON_3 = "<img src='!link{([^']|\s)+}($|')"
PATRON_4 = "(^|\n)```!lenguaje{\w+}\n!codigo{[^`]+}($|```)"
PATRON_5 = "(^|\n)[*-]{1} \[[xX]\] !elemento{[^\n]+}($|\n)"
PATRON_6 = "(^|\n)!texto{[^\n]*\[[^\n]+\]\(!link{[^\n ]+}\)[^\n]*}($|\n)"


# ------------------------------------------------------------------------------------------------
# Completar a continuación el código de cada consulta. Cada consulta recibe el patrón
# correspondiente para construir la expresión regular, y el texto sobre el cual se aplicará.
# Cada consulta debe retornar una lista de diccionarios, donde cada diccionario contiene dos
# llaves: "contenido" (el texto del match encontrado) y "posicion" (lista con dos elementos: la
# posición de inicio y la posición de término del match encontrado).


# CONSULTA 1
def consulta_1(texto, patron):
    regex = re.compile(patron)
    lista = []
    
    for match in regex.finditer(texto):
        
        diccionario = {
            "contenido": match.group('titulo'),
            "posicion": match.span('titulo')
        }

        lista.append(diccionario)

    return lista

# CONSULTA 2
def consulta_2(texto, patron):
    regex = re.compile(patron)
    lista = []
    
    for match in regex.finditer(texto):
        
        diccionario = {
            "contenido": match.group('subseccion'),
            "posicion": match.span('subseccion')
        }

        lista.append(diccionario)

    return lista
    
# CONSULTA 3
def consulta_3(texto, patron):
    regex = re.compile(patron)
    lista = []
    
    for match in regex.finditer(texto):
        
        diccionario = {
            "contenido": match.group('link'),
            "posicion": match.span('link')
        }

        lista.append(diccionario)

    return lista

# CONSULTA 4
def consulta_4(texto, patron):
    regex = re.compile(patron)
    lista = []
    
    for match in regex.finditer(texto):
        
        diccionario = {
            "contenido": match.group('lenguaje'),
            "posicion": match.span('codigo')
        }

        lista.append(diccionario)

    return lista


# CONSULTA 5
def consulta_5(texto, patron):
    regex = re.compile(patron)
    lista = []
    
    for match in regex.finditer(texto):
        
        diccionario = {
            "contenido": match.group('elemento'),
            "posicion": match.span('elemento')
        }

        lista.append(diccionario)

    return lista


# CONSULTA 6
def consulta_6(texto, patron):
    regex = re.compile(patron)
    lista = []
    
    for match in regex.finditer(texto):
        
        diccionario = {
            "contenido": (
                match.group('texto')
            ),
            "posicion": match.span('link')
        }

        lista.append(diccionario)
    
    return lista
