from PyQt5.QtCore import pyqtSignal, QObject
from collections import namedtuple
import parametros as p
from random import choice


class LogicaRanking(QObject):

    senal_enviar_ranking = pyqtSignal(list)
    senal_enviar_objeto = pyqtSignal(str)
    senal_sin_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()

    def leer_ranking(self):
        try:
            with open(p.PATH_RANKING, 'r') as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            self.senal_sin_ranking.emit()
        else:
            Usuario = namedtuple('Usuario', ['nombre', 'puntaje'])
            ranking = list()
            
            for linea in lineas:
                if len(linea) > 1:
                    datos = linea.strip().split(',')
                    nombre = datos[0]
                    puntaje = int(datos[1])
                    usuario = Usuario(nombre, puntaje)
                    ranking.append(usuario)
                    
            ranking.sort(reverse = True, key = sortear_por_puntaje)
            self.senal_enviar_ranking.emit(ranking[:(min(len(ranking), 5))])
    
    def elegir_objeto(self):
        key = choice(list(p.DICCIONARIO_OBJETOS.keys()))
        
        if '_x2' in key:
            key = key[:-3]
            
        path = p.DICCIONARIO_OBJETOS[key]
        
        self.senal_enviar_objeto.emit(path)
            

def sortear_por_puntaje(usuario):
    return usuario.puntaje