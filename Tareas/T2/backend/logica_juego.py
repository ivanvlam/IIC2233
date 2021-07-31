from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from random import randint
import parametros as p
from collections import deque
from random import uniform, choice
from backend.jefe_gorgory import JefeGorgory
from time import time
from funciones import comprobar_colisiones, comprobar_objetos, colision_gorgory

class LogicaJuego(QObject):

    senal_posicion_inicial = pyqtSignal(tuple)
    senal_posicion_obstaculos = pyqtSignal(list)
    senal_sprite_acutal = pyqtSignal(str)
    senal_actualizar_posicion = pyqtSignal(tuple)
    senal_aparicion_objeto = pyqtSignal()
    senal_info_objeto = pyqtSignal(dict)
    senal_desaparicion_objeto = pyqtSignal()
    senal_objeto_recolectado = pyqtSignal(list)
    senal_tiempo = pyqtSignal(float)
    senal_labels = pyqtSignal(dict)
    senal_eliminar_objeto = pyqtSignal(object)
    senal_lisa = pyqtSignal(float)
    senal_cheat_ronda = pyqtSignal()
    senal_gorgory = pyqtSignal(tuple)
    senal_pillado = pyqtSignal()
    
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
        self.teclas_totales = []
    
    def posicion_inicial(self, lista):
        encontrada = False
        while not encontrada:
            posicion = (randint(0, 11), randint(0, 7))
            if self.comprobar_posiciones(lista, posicion):
                encontrada = True

        baldosa_horizontal = (posicion[0] + 0.25) * p.ANCHO_BALDOSA 
        baldosa_vertical = posicion[1] * p.ALTO_BALDOSA + p.ALTO_MURALLA * 0.92

        self.senal_posicion_inicial.emit((baldosa_horizontal, baldosa_vertical))
    
    def avanzar(self, diccionario):
        posicion_x, posicion_y = diccionario['posicion'][0], diccionario['posicion'][1]
        velocidad = diccionario['velocidad']
        obstaculos = diccionario['obstaculos']
        personaje = diccionario['personaje']
        objetos = diccionario['objetos']
        tecla = diccionario['tecla']
        vida = diccionario['vida']
        seguidos = diccionario['seguidos']
        items_normales = diccionario['items_normales']
        items_buenos = diccionario['items_buenos']
        items_malos = diccionario['items_malos']
        items_x2 = diccionario['items_x2']
        
        if tecla in ['W', 'A', 'S', 'D']:    
            tupla = comprobar_colisiones(tecla, obstaculos, posicion_x, posicion_y, velocidad)        
            self.senal_actualizar_posicion.emit(tupla)
            self.gorgory.posiciones.append(tupla)
            self.gorgory.cambiar_sprite(tecla)
            self.mover_gorgory()
            
        lista, objetos = comprobar_objetos(posicion_x, posicion_y, objetos)
        if len(lista) > 0:
            self.senal_objeto_recolectado.emit(lista)
            
            for objeto in objetos:
                self.senal_eliminar_objeto.emit(objeto)
                if objeto.tipo == 'normal':
                    seguidos += 1
                    items_normales += 1
                            
                elif objeto.tipo == 'bueno':
                    items_buenos += 1
                    items_x2 += 1
                    
                elif objeto.tipo == 'corazon':
                    vida += p.PONDERADOR_CORAZON
                    items_buenos += 1
                
                else:
                    items_malos += 1
                    vida -= p.PONDERADOR_VENENO
                    seguidos = 0
                    
                if seguidos == 10:
                    seguidos = 0
                    
                    if personaje == 'homero':
                        vida += p.PONDERADOR_VIDA_HOMERO
                        
                    elif personaje == 'lisa':
                        duracion_saxofones = p.PONDERADOR_TIEMPO_LISA
                        self.senal_lisa.emit(float(duracion_saxofones))
                    
                    elif personaje == 'moe':
                        self.timer_aparicion.stop()
                        self.tiempo_aparicion /= 2
                        self.timer_aparicion = QTimer()
                        self.timer_aparicion.setInterval(1000 * self.tiempo_aparicion)
                        self.timer_aparicion.timeout.connect(self.aparicion_objetos)
                        self.timer_aparicion.start()
                    
                    else:
                        diff = self.tiempo_actual - self.tiempo_ronda
                        if diff < self.delay:
                            self.delay *= 2


            self.senal_labels.emit({
                'vida': vida,
                'seguidos': seguidos,
                'items_normales': items_normales,
                'items_buenos': items_buenos,
                'items_malos': items_malos,
                'items_x2': items_x2
            })
                
        self.teclas_presionadas.append(diccionario['tecla'])
        
        if len(self.teclas_presionadas) > 3:
            self.teclas_presionadas.popleft()

        if list(self.teclas_presionadas) == ['V', 'I', 'D']:
            vida += p.VIDA_TRAMPA
            self.senal_labels.emit({
                'vida': vida,
                'seguidos': seguidos,
                'items_normales': items_normales,
                'items_buenos': items_buenos,
                'items_malos': items_malos,
                'items_x2': items_x2
            })
        elif list(self.teclas_presionadas) == ['N', 'I', 'D']:
            self.senal_cheat_ronda.emit()
            
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

    def posicion_obstaculos(self):
        lista = []
        while len(lista) < 3:
            posicion = (randint(0, 11), randint(0, 7))
            if self.comprobar_posiciones(lista, posicion):
                lista.append(posicion)
        
        self.senal_posicion_obstaculos.emit(lista)

    def comprobar_posiciones(self, lista, tupla):
        if len(lista) == 0:
            return True
        if tupla in lista:
            return False
        for elemento in lista:
            if elemento == tupla:
                return False
            elif elemento[0] == tupla[0] or elemento[1] == tupla[1]:
                if (elemento[0] - tupla[0]) ** 2 + (elemento[1] - tupla[1]) ** 2 < 2:
                    return False
                return True
            elif (elemento[0] - tupla[0]) ** 2 + (elemento[1] - tupla[1]) ** 2 <= 2:
                return False
        return True
    
    def comprobar_pillar(self, tupla):
        if colision_gorgory(*tupla):
            self.senal_pillado.emit()
    
    def creacion_timers(self, dificultad):
        self.gorgory = JefeGorgory()

        self.tiempo_aparicion = p.DICCIONARIO_DIFICULTADES[dificultad]['aparicion']
        self.timer_aparicion = QTimer()
        self.timer_aparicion.setInterval(1000 * self.tiempo_aparicion)
        self.timer_aparicion.timeout.connect(self.aparicion_objetos)
        self.timer_aparicion.start()
        self.tiempo_ultima_aparicion = time()
        
        self.tiempo_ronda = p.DICCIONARIO_DIFICULTADES[dificultad]['tiempo_ronda']
        self.timer_ronda = QTimer()
        self.timer_ronda.setInterval(100)
        self.timer_ronda.timeout.connect(self.cambiar_tiempo)
        self.timer_ronda.start()
        self.tiempo = self.tiempo_ronda
        
        self.delay = p.DICCIONARIO_DIFICULTADES[dificultad]['delay']
    
    def mover_gorgory(self):
        tupla = self.gorgory.moverse()
        self.senal_gorgory.emit((tupla[0], tupla[1], self.delay))
    
    def terminar_ronda(self, _):
        self.timer_aparicion.stop()
        self.timer_ronda.stop()
    
    def pausar(self, estado):
        if estado:
            self.tiempo_actual = time()
            self.timer_aparicion.stop()
            self.timer_ronda.stop()

        else:
            self.timer_ronda.start(100)
            diff = self.tiempo_actual - self.tiempo_ultima_aparicion
            
            self.timer_single = QTimer()
            self.timer_single.setSingleShot(True)
            self.timer_single.setInterval((self.tiempo_aparicion - diff) * 1000)
            self.timer_single.timeout.connect(self.reanudar_timer_aparicion)
            self.timer_single.start()
            
            
    def reanudar_timer_aparicion(self):
        self.senal_aparicion_objeto.emit()
        self.tiempo_ultima_aparicion = time()
        self.timer_aparicion.start(self.tiempo_aparicion * 1000)
    
    def cambiar_tiempo(self):
        self.tiempo -= 0.1
        self.senal_tiempo.emit(self.tiempo / self.tiempo_ronda * 100)
        
    def aparicion_objetos(self):
        self.senal_aparicion_objeto.emit()
        self.tiempo_ultima_aparicion = time()
    
    def elegir_objeto(self, diccionario):
        personaje = diccionario['personaje']
        posiciones_obstaculos = diccionario['posiciones_obstaculos']
        posiciones_objetos = diccionario['posiciones_objetos']
        probabilidad = uniform(0, 1)
        objetos_personaje = p.OBJETOS_PERSONAJES[personaje]
        objetos_normales = objetos_personaje['normales']
        objetos_buenos = objetos_personaje['buenos']
        
        if probabilidad < p.PROB_NORMAL:
            objeto = choice(objetos_normales)
            path = p.DICCIONARIO_OBJETOS[objeto]
            tipo = 'normal'
            
        elif probabilidad < p.PROB_NORMAL + p.PROB_BUENO:
            objeto = choice(objetos_buenos)
            path = p.DICCIONARIO_OBJETOS[objeto]
            
            if 'Corazon' in path:
                tipo = 'corazon'
            else:
                tipo = 'bueno'
            
        else:
            path = p.DICCIONARIO_OBJETOS['veneno']
            tipo = 'veneno'
        
        lista = posiciones_objetos + posiciones_obstaculos
        
        encontrada = False        
        while not encontrada:
            posicion = (randint(0, 11), randint(0, 7))
            if self.comprobar_posiciones(lista, posicion):
                encontrada = True
        
        diccionario_enviar = {
            'path': path,
            'posicion': posicion,
            'tipo': tipo
        }
            
        self.senal_info_objeto.emit(diccionario_enviar)
