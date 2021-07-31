from collections import namedtuple
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from time import sleep

class Nodo:
    
    def __init__(self, _id, posicion):
        self._id = _id
        self.posicion = posicion
        self.vecinos = {}
        self.caminos = []
    
    def agregar_vecino(self, vecino, valor):
        Camino = namedtuple('camino', 'destino peso')
        self.vecinos[vecino] = valor
        camino = Camino(vecino, valor)
        self.caminos.append(camino)
    
    def __repr__(self):
        return f'Soy el nodo {self._id} y mi posicion es {self.posicion}'
        
class Grafo:
    
    def __init__(self):
        self.nodos = []
    
    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)
    
    def __repr__(self):
        txt = ''
        for nodo in self.nodos:
            txt += str(nodo) + '\n'
            for vecino in nodo.vecinos:
                txt += f'    {str(vecino)}\n'
        return txt

class MegaThread(QThread):
    
    def __init__(self, target = sleep, args = ()):
        super().__init__()
        self.function = target
        self.args = args
    
    def run(self):
        self.function(*self.args)