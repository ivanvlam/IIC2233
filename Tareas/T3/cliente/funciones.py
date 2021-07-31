import json
from os.path import join
from clases import Nodo, Grafo
from codificacion import codificar_imagen, codificar_mensaje, \
    decodificar_imagen, decodificar_mensaje

def cargar_parametros():
    with open('parametros.json', 'r') as archivo:
        parametros = json.load(archivo)
    
    imagenes = dict()
    for k, v in parametros["imagenes"].items():
        imagenes[k] = join(*tuple(v))
    
    parametros["imagenes"] = imagenes
    
    return parametros

def construir_grafo(mapa_short):
    if mapa_short == "sj":
        mapa = "san_joaquin"
    else: 
        mapa = "ingenieria"

    with open('mapa.json', 'r') as archivo:
        grafo = json.load(archivo)["mapa"][mapa]

    diccionario = {}
    for k, v in grafo['posiciones'].items():
        nodo = Nodo(k, tuple(v.values()))
        diccionario[k] = nodo
    
    for k, v in diccionario.items():
        for elemento in grafo['caminos'][k]:
            v.agregar_vecino(diccionario[elemento[0]], elemento[1])
    
    grafo = Grafo()
    for v in diccionario.values():
        grafo.agregar_nodo(v)
    
    return grafo
    
def manejar_mensajes(mensaje, num):
    if num == 0:
        if isinstance(mensaje, str):
            if '.png' in mensaje:
                return codificar_imagen(mensaje)
            else:
                return codificar_mensaje(mensaje)
        else:
            return codificar_mensaje(mensaje)
    else:
        if int.from_bytes(mensaje[4:8], byteorder = 'little') == 1:
            return decodificar_imagen(mensaje)
        else:
            return decodificar_mensaje(mensaje)

if __name__ == '__main__':
    codificado = manejar_mensajes({'hola': 'adios'}, 0)
    print(codificado)
    decodificado = manejar_mensajes(codificado, 1)
    print(decodificado)
    #print(construir_grafo('sj'))