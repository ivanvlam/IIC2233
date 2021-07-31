import cargar_archivos as c
import parametros as p
from collections import namedtuple


class NodoLugar:
    # NO MODIFICAR
    def __init__(self, nombre):
        self.nombre = nombre
        # Lista de namedtuples del tipo mafioso (definido en cargar_archivos.py)
        self.mafiosos = []
        # Lista de namedtuples del tipo conexion, con los atributos vecino
        # y peso, que guardan el nodo vecino y el peso de dicha conexion
        self.conexiones = []

    def agregar_conexion(self, destino, peso):
        Conexion = namedtuple("Conexion", ["vecino", "peso"])
        self.conexiones.append(
            Conexion(vecino=destino, peso=peso)
        )

    def __str__(self):
        # Puedes imprimir el nodo :D
        texto = ""
        nombres = ", ".join([habitante.nombre for habitante in self.mafiosos])
        texto += f"En {self.nombre} se encuentran los mafiosos {nombres}.\n"
        conexiones = ", ".join([f"{conexion.vecino.nombre} de peso {conexion.peso}"
                                for conexion in self.conexiones])
        texto += f"Desde aqui puedes ir a {conexiones}.\n"
        return texto
     

def crear_grafo(dic_lugares, conexiones):
    
    lista_nodos = []
    
    for k, v in dic_lugares.items():
        nodo = NodoLugar(k)
        nodo.mafiosos = v
        
        lista_nodos.append(nodo)
    
    for nodo in lista_nodos:
        lista_origen = list(filter(lambda x: x[0] == nodo.nombre, conexiones))
        
        for elemento in lista_origen:
            lista_nodos_filtrada = list(filter(lambda x: x.nombre == elemento[1], lista_nodos))
            nodo.agregar_conexion(lista_nodos_filtrada[0], elemento[2])
        
        lista_destino = list(filter(lambda x: x[1] == nodo.nombre, conexiones))
        for elemento in lista_destino:
            lista_nodos_filtrada = list(filter(lambda x: x.nombre == elemento[0], lista_nodos))
            for nodo_origen in lista_nodos_filtrada:
                nodo_origen.agregar_conexion(nodo, elemento[2])
                nodo.agregar_conexion(nodo_origen, elemento[2])
    
    return nodo


if __name__ == "__main__":
    diccionario_mafiosos, nombre_cabeza = c.cargar_mafiosos(p.path_mafioso)
    
    diccionario_lugares, arcos = c.cargar_lugares(
        p.path_lugares, p.path_conexiones, diccionario_mafiosos
    )
    nodo_inicial = crear_grafo(diccionario_lugares, arcos)

    for arco in arcos:
        print(arco)
    
    print("Mapa cargado en forma de grafo!!")
    print("Ahora... a acabar con la mafia!!\n")
