from collections import deque
import parametros as p


# Funciones que revisan todos los nodos para desmantelar la organización


def recorrer_mafia(inicio):
    visitados = set()
    lugares = deque()
    lugares.append(inicio)
    
    lugares_lideres = []
    
    while len(lugares) > 0:
        lugar = lugares.popleft()
        
        if lugar not in visitados:
            visitados.add(lugar)
            
            print(f'Se ha desmantelado {lugar.nombre}')

            for mafioso in lugar.mafiosos:
                if mafioso.frase == p.frase_lider_1 or mafioso.frase == p.frase_lider_2:
                    lugares_lideres.append(lugar)
            
            for conexion in lugar.conexiones:
                if conexion.vecino not in lugares:
                    lugares.append(conexion.vecino)
    
    return lugares_lideres


# BONUS
# Recibe como inicio el nodo en el que está uno de los líderes de la mafia
# y como termino el nodo en el que esta el otro lider
def minima_peligrosidad(inicio, termino):
    # COMPLETAR
    pass
