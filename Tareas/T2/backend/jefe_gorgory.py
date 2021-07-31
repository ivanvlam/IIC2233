from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread
import parametros as p
from time import sleep


class JefeGorgory(QLabel):
    
    def __init__(self):
        super().__init__()

        self.diccionario_aumento = {1: 2, 2: 3, 3: 2}
        self.diccionario_disminucion = {3: 2, 2: 1, 1: 2}
        self.diccionario_teclas = {
            'A': 'izquierda_',
            'D': 'derecha_',
            'W': 'arriba_',
            'S': 'abajo_'
        }
        
        self.movimientos = p.DICCIONARIO_MOVIMIENTOS['gorgory']
        
        self.sprite_actual = 1
        self.aumentando = True
        self.sprites = []
        self.sprite = self.movimientos['abajo_1']
        self.posiciones = []

    def cambiar_sprite(self, tecla):
        
        sprite = self.diccionario_teclas[tecla]
        
        path = self.movimientos[sprite + str(self.sprite_actual)]
        
        if self.aumentando:
            if self.sprite_actual == 3:
                self.aumentando = False
            self.sprite_actual = self.diccionario_aumento[self.sprite_actual]
        
        else:
            if self.sprite_actual == 1:
                self.aumentando = True
            self.sprite_actual = self.diccionario_disminucion[self.sprite_actual]
        
        self.sprites.append(path)
    
    def moverse(self):
        self.posicion = self.posiciones.pop(0)
        self.sprite = self.sprites.pop(0)
        return (self.posicion, self.sprite)
    
class ThreadGorgory(QThread):
    
    def __init__(self, senal, posicion, sprite, delay):
        super().__init__()
        
        self.senal = senal

        self.posicion = posicion
        self.sprite = sprite
        self.delay = delay

    def run(self):
        sleep(self.delay)
        self.senal.emit((self.posicion, self.sprite))