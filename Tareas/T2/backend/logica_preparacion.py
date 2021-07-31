from PyQt5.QtCore import pyqtSignal, QObject
from random import randint
import parametros as p
from collections import deque

class LogicaPreparacion(QObject):

    senal_posicion_inicial = pyqtSignal(tuple)
    senal_sprite_acutal = pyqtSignal(str)
    senal_actualizar_posicion = pyqtSignal(tuple)
    senal_entrar_mapa = pyqtSignal(str)
    senal_vida_trampa = pyqtSignal(float)
    senal_no_entrar = pyqtSignal(bool)

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
        
        self.sprite_actual = 1
        self.aumentando = True
        self.teclas_presionadas = deque()

    def comprobar_nombre(self, nombre):
        if nombre.isalnum():
            self.senal_respuesta_validacion.emit(True)
        else:
            self.senal_respuesta_validacion.emit(False)
    
    def posicion_inicial(self):
        baldosa_horizontal = (randint(0, 11) + 0.25) * p.ANCHO_BALDOSA 
        baldosa_vertical = randint(0, 7) * p.ALTO_BALDOSA + p.ALTO_MURALLA * 0.92

        self.senal_posicion_inicial.emit((baldosa_horizontal, baldosa_vertical))
    
    def avanzar(self, diccionario):
        posicion_x, posicion_y = diccionario['posicion'][0], diccionario['posicion'][1]
        ancho_personaje = p.ANCHO_PERSONAJE
        velocidad = diccionario['velocidad']
        personaje = diccionario['personaje']
        vida = diccionario['vida']
        
        if diccionario['tecla'] == 'A':
            if posicion_x - velocidad > 0:
                self.senal_actualizar_posicion.emit((posicion_x - velocidad, posicion_y))
            else:
                self.senal_actualizar_posicion.emit((0, posicion_y))
        
        elif diccionario['tecla'] == 'D':
            if posicion_x + 3 + ancho_personaje < p.VENTANA_ANCHO:
                self.senal_actualizar_posicion.emit((posicion_x + velocidad, posicion_y))
        
        elif diccionario['tecla'] == 'W':
            if posicion_y - velocidad > p.ALTURA_CALLE - p.ALTO_PERSONAJE * 0.9:
                self.senal_actualizar_posicion.emit((posicion_x, posicion_y - velocidad))
            else:
                self.senal_actualizar_posicion.emit((
                    posicion_x,
                    p.ALTURA_CALLE - p.ALTO_PERSONAJE * 0.9
                ))
                
                if posicion_x < p.PRIMER_LIMITE:
                    if personaje == 'homero':
                        self.senal_entrar_mapa.emit('Planta_nuclear')
                    else:
                        self.senal_no_entrar.emit(True)
                elif posicion_x < p.SEGUNDO_LIMITE:
                    if personaje == 'lisa':
                        self.senal_entrar_mapa.emit('Primaria')
                    else:
                        self.senal_no_entrar.emit(True)
                elif posicion_x < p.TERCER_LIMITE:
                    if personaje == 'moe':
                        self.senal_entrar_mapa.emit('Bar')
                    else:
                        self.senal_no_entrar.emit(True)
                else:
                    if personaje == 'krusty':
                        self.senal_entrar_mapa.emit('Krustyland')
                    else:
                        self.senal_no_entrar.emit(True)
        
        elif diccionario['tecla'] == 'S':
            if posicion_y + velocidad < p.VENTANA_ALTO - 1.1 * p.ALTO_PERSONAJE:
                self.senal_actualizar_posicion.emit((posicion_x, posicion_y + velocidad))
            else:
                tupla = (posicion_x, p.VENTANA_ALTO - 1.1 * p.ALTO_PERSONAJE)
                self.senal_actualizar_posicion.emit(tupla)
        
        if diccionario['tecla'] != 'W':
            self.senal_no_entrar.emit(False)
        
        self.teclas_presionadas.append(diccionario['tecla'])
        if len(self.teclas_presionadas) > 3:
            self.teclas_presionadas.popleft()

        if list(self.teclas_presionadas) == ['V', 'I', 'D']:
            vida += p.VIDA_TRAMPA
            self.senal_vida_trampa.emit(vida)
    
    def cambiar_sprite(self, diccionario):
        
        tecla_presionada = diccionario['tecla']
        if tecla_presionada in ['W', 'A', 'S', 'D']:
            sprite = self.diccionario_teclas[tecla_presionada]
            
            path = diccionario['movimientos'][sprite + str(self.sprite_actual)]
            
            if self.aumentando:
                if self.sprite_actual == 3:
                    self.aumentando = False
                self.sprite_actual = self.diccionario_aumento[self.sprite_actual]
            
            else:
                if self.sprite_actual == 1:
                    self.aumentando = True
                self.sprite_actual = self.diccionario_disminucion[self.sprite_actual]
            
            self.senal_sprite_acutal.emit(path)