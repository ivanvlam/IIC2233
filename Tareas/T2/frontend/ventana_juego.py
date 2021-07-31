from PyQt5.QtWidgets import (
    QLabel, QWidget, QProgressBar)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
import parametros as p
from backend.jefe_gorgory import ThreadGorgory
from clases import BotonPersonalizado, Objeto, FotoEstandar
from time import time

class VentanaJuego(QWidget):

    senal_teclas = pyqtSignal(dict)
    senal_posicion_personaje = pyqtSignal(list)
    senal_colocar_obstaculos = pyqtSignal()
    senal_creacion_timers = pyqtSignal(str)
    senal_tipo_objeto = pyqtSignal(dict)
    senal_pausar = pyqtSignal(bool)
    senal_terminar_ronda = pyqtSignal(dict)
    senal_thread = pyqtSignal(tuple)
    senal_pillar_gorgory = pyqtSignal(tuple)
    senal_reiniciar_musica = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.senal_thread.connect(self.mover_gorgory)
        
        self.size = (p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.resize(p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.setMaximumHeight(p.VENTANA_ALTO)
        self.setMaximumWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))
        
        self.setMinimumHeight(p.VENTANA_ALTO)
        self.setMinimumWidth(p.VENTANA_ANCHO)

        self.setWindowTitle("Ventana de Juego")
        
        self.obstaculos = []
        self.objetos = []
        self.eliminar = False
        self.duracion_saxofones = 0
        self.init_gui()

    def init_gui(self):
        self.top_label = FotoEstandar(self, p.VENTANA_ANCHO, p.VENTANA_ALTO / 6, 0, 0, None)
        self.top_label.setStyleSheet("QLabel {background-color : rgb(243, 243, 150)}")
        
        self.top_middle = FotoEstandar(self, p.VENTANA_ANCHO * 49 / 50, p.VENTANA_ALTO * 9 / 60, \
            p.VENTANA_ANCHO / 100, p.VENTANA_ALTO / 120, None)
        self.top_middle.setStyleSheet(p.ESTILO_LABEL_TOP)

        self.logo = FotoEstandar(self, p.VENTANA_ALTO * 1 / 6, p.VENTANA_ALTO * 1 / 6 * 541 / 622,
            p.VENTANA_ANCHO / 100, p.VENTANA_ALTO / 120, p.PATH_LOGO)

        self.barra_vida = QProgressBar(self)
        self.barra_vida.resize(p.VENTANA_ANCHO / 7, p.VENTANA_ALTO * 1 / 30)
        self.barra_vida.move(p.VENTANA_ANCHO / 100 + self.logo.width() * 17 / 10, \
            p.VENTANA_ALTO / 30)
        self.barra_vida.setAlignment(Qt.AlignCenter)
        self.barra_vida.setFont(QFont('Courier', 12))
        
        self.barra_tiempo = QProgressBar(self)
        self.barra_tiempo.resize(p.VENTANA_ANCHO / 7, p.VENTANA_ALTO * 1 / 30)
        self.barra_tiempo.move(p.VENTANA_ANCHO / 100 + self.logo.width() * 17 / 10, \
            p.VENTANA_ALTO / 30 + self.barra_vida.height() * 2)
        self.barra_tiempo.setAlignment(Qt.AlignCenter)
        self.barra_tiempo.setFont(QFont('Courier', 12))
        
        self.label_vida = QLabel('VIDA:', self)
        self.label_vida.setFont(QFont('Courier', 9))
        self.label_vida.move(p.VENTANA_ANCHO / 100 + self.logo.width() * 11 / 10, \
            p.VENTANA_ALTO / 28)
        
        self.label_tiempo = QLabel('TIEMPO:', self)
        self.label_tiempo.setFont(QFont('Courier', 9, QFont.Light))
        self.label_tiempo.move(p.VENTANA_ANCHO / 100 + self.logo.width(), \
            p.VENTANA_ALTO / 28 + self.barra_vida.height() * 2)
        
        self.label_items_buenos = QLabel('ITEMS BUENOS: ', self)
        self.label_items_buenos.setFont(QFont('Courier', 9))
        self.label_items_buenos.move(p.VENTANA_ANCHO / 100 + self.barra_vida.width() * 2.7, \
            p.VENTANA_ALTO / 28)
        self.label_items_buenos.setMinimumWidth(200)
        
        self.label_items_malos = QLabel('ITEMS MALOS: ', self)
        self.label_items_malos.setFont(QFont('Courier', 9, QFont.Light))
        self.label_items_malos.move(p.VENTANA_ANCHO / 100 + self.barra_vida.width() * 2.7, \
            p.VENTANA_ALTO / 28 + self.barra_vida.height() * 2)
        
        self.label_ronda = QLabel('RONDA: 1', self)
        self.label_ronda.setFont(QFont('Courier', 9))
        self.label_ronda.move(self.label_items_buenos.x() 
                              + self.label_items_buenos.width() * 1.1,
                            p.VENTANA_ALTO / 28)
        self.label_ronda.raise_()
        
        self.label_puntaje = QLabel('PUNTAJE: ', self)
        self.label_puntaje.setFont(QFont('Courier', 9, QFont.Light))
        self.label_puntaje.move(self.label_items_buenos.x() 
                                + self.label_items_buenos.width() * 1.1, 
                            p.VENTANA_ALTO / 28 + self.barra_vida.height() * 2)
        self.label_puntaje.setMinimumWidth(250)
        
        self.boton_pausar = BotonPersonalizado('&Pausar', self, p.VENTANA_ANCHO / 7, \
            p.VENTANA_ALTO * 1 / 30, p.VENTANA_ANCHO * 83 / 100, p.VENTANA_ALTO / 30, 'chico')
        self.boton_pausar.clicked.connect(self.pausar)
        
        self.boton_salir = BotonPersonalizado('&Salir', self, p.VENTANA_ANCHO / 7, \
            p.VENTANA_ALTO * 1 / 30, p.VENTANA_ANCHO * 83 / 100, \
            p.VENTANA_ALTO / 30 + self.barra_vida.height() * 1.95, 'chico')
        self.boton_salir.clicked.connect(self.salir)

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if valor > 1:
            self.__vida = 1
        elif valor < 0:
            self.__vida = 0
        else:
            self.__vida = round(valor, 1)
    
    def keyPressEvent(self, event):
        
        diccionario = {
            'obstaculos': self.obstaculos,
            'movimientos': self.movimientos,
            'personaje': self.personaje,
            'posicion': self.posicion,
            'velocidad': self.velocidad_personaje,
            'objetos': self.objetos,
            'vida': self.vida,
            'seguidos': self.seguidos,
            'items_normales': self.items_normales,
            'items_buenos': self.items_buenos,
            'items_malos': self.items_malos,
            'items_x2': self.items_x2,
        }
        self.enviar = True
        if event.key() == Qt.Key_P:
            self.pausar()
            diccionario['tecla'] = 'P'
        elif event.key() == Qt.Key_A:
            diccionario['tecla'] = 'A'
        elif event.key() == Qt.Key_D:
            diccionario['tecla'] = 'D'
        elif event.key() == Qt.Key_W:
            diccionario['tecla'] = 'W'
        elif event.key() == Qt.Key_S:
            diccionario['tecla'] = 'S'
        elif event.key() == Qt.Key_V:
            diccionario['tecla'] = 'V'
        elif event.key() == Qt.Key_I:
            diccionario['tecla'] = 'I'
        elif event.key() == Qt.Key_N:
            diccionario['tecla'] = 'N'
        else:
            self.enviar = False
                    
        if not self.pausa and self.enviar:
            self.senal_teclas.emit(diccionario)
    
    def actualizar_sprite(self, path):
        self.label_personaje.setPixmap(QPixmap(path))
            
    def mover_personaje(self, posicion):
        self.posicion = posicion
        self.label_personaje.move(*posicion)
    
    def pausar(self):
        self.senal_pausar.emit(not self.pausa)
        if self.pausa:
            for objeto in self.objetos:
                diff = self.tiempo_actual - objeto.tiempo_inicio
                objeto.timer.start((objeto.tiempo_duracion - diff) * 1000)
        else:
            self.tiempo_actual = time()
            for objeto in self.objetos:
                objeto.timer.stop()
        self.pausa = not self.pausa

    def tiempo_saxofones(self, valor):
        self.duracion_saxofones += valor
    
    def actualizar_vida(self, vida):
        self.vida = vida
        self.barra_vida.setValue(int(self.vida / vida))
    
    def actualizar_tiempo(self, tiempo):
        self.barra_tiempo.setValue(tiempo)
        
        if tiempo <= 0:
            self.terminar_ronda()
    
    def salir(self):
        self.close()
    
    def colocar_personaje(self, posicion):
        self.label_personaje.move(*posicion)
        self.posicion = posicion
    
    def setear_mapa(self):
        path = p.DICCIONARIO_MAPAS[self.mapa]['path']
        self.background = FotoEstandar(self, p.VENTANA_ANCHO, p.VENTANA_ALTO * 5 / 6, 0, \
            p.VENTANA_ALTO / 6, path)

        self.barra_vida.setValue(self.vida * 100)
        self.label_puntaje.setText(f'PUNTAJE: {int(self.puntaje)}')
        self.label_items_buenos.setText(f'ITEMS BUENOS: {self.items_buenos}')
        self.label_items_malos.setText(f'ITEMS MALOS: {self.items_malos}')
    
    def recolectar_objeto(self, lista):
        for indice in lista:
            objeto_recolectado = self.objetos[indice]
            objeto_recolectado.hide()
    
    def limpiar_mapa(self):
        for label in self.obstaculos + self.objetos:
            label.clear()
        
        self.objetos = []
        self.posicion_objetos = []
    
    def actualizar_labels(self, diccionario):
        self.vida = diccionario['vida']
        self.seguidos = diccionario['seguidos']
        self.items_normales = diccionario['items_normales']
        self.items_buenos = diccionario['items_buenos']
        self.items_malos = diccionario['items_malos']
        self.items_x2 = diccionario['items_x2']
        
        if self.vida == 0:
            self.terminar_ronda()
        
        self.barra_vida.setValue(self.vida * 100)
        self.label_puntaje.setText(f'PUNTAJE: {self.puntaje}')
        self.label_items_buenos.setText(f'ITEMS BUENOS: {self.items_buenos}')
        self.label_items_malos.setText(f'ITEMS MALOS: {self.items_malos}')

    def terminar_ronda(self):
        self.items_buenos_acumulados += self.items_buenos
        self.items_malos_acumulados += self.items_malos
        
        self.senal_terminar_ronda.emit({
            'usuario': self.usuario,
            'vida': self.vida,
            'puntaje': self.puntaje,
            'items_normales': self.items_normales,
            'items_buenos': self.items_buenos,
            'items_malos': self.items_malos,
            'items_x2': self.items_x2,
            'items_malos_total': self.items_malos_acumulados,
            'items_buenos_total': self.items_buenos_acumulados,
            'ronda': self.ronda,
            'pillado': self.pillado_gorgory
        })
        self.senal_reiniciar_musica.emit()
        
        for objeto in self.objetos:
            objeto.timer.stop()
            objeto.clear()
        
        if len(self.threads) > 0:
            for thread in self.threads:
                if thread.isRunning():
                    thread.terminate()
            
        self.threads = []
        
        self.close()
    
    def pillado(self):
        self.vida = 0
        self.pillado_gorgory = True
        self.terminar_ronda()
    
    def colocar_obstaculos(self, lista):
        self.senal_posicion_personaje.emit(lista)
        
        self.obstaculos = []
        self.posicion_obstaculos = lista
        
        obstaculos_disponibles = p.DICCIONARIO_MAPAS[self.mapa]['obstaculos']
        for obstaculo, posicion in zip(obstaculos_disponibles, lista):
            if self.mapa == 'Planta_nuclear':
                posicion_y = p.VENTANA_ALTO - ( 8 - posicion[1]) * p.ALTO_BALDOSA * 0.96
            else:
                posicion_y = p.VENTANA_ALTO - ( 8 - posicion[1]) * p.ALTO_BALDOSA
            label = FotoEstandar(self, p.ANCHO_BALDOSA * 0.8, p.ALTO_BALDOSA * 0.9, \
                (posicion[0] + 0.1) * p.ANCHO_BALDOSA, posicion_y, obstaculo)

            self.obstaculos.append(label)
            label.show()
        
        self.label_personaje.raise_()
    
    def pedir_objeto(self):
        self.senal_tipo_objeto.emit({
            'personaje': self.personaje,
            'posiciones_obstaculos': self.posicion_obstaculos,
            'posiciones_objetos': self.posicion_objetos
        })
        
    def colocar_objeto(self, diccionario):
        path = diccionario['path']
        posicion = diccionario['posicion']
        tipo = diccionario['tipo']
        
        if tipo == 'normal' and self.personaje == 'lisa':
            label = Objeto(self, tipo, self.dificultad, posicion, p.ANCHO_BALDOSA * 0.7, \
                p.ALTO_BALDOSA * 0.8, self.mapa, self.duracion_saxofones, path)
        
        else:
            label = Objeto(self, tipo, self.dificultad, posicion, p.ANCHO_BALDOSA * 0.7, \
                p.ALTO_BALDOSA * 0.8, self.mapa, 0, path)

        self.objetos.append(label)
        self.objetos = list(filter(lambda x: x.vivo, self.objetos))
        self.posicion_objetos = self.lista_posiciones()
        label.show()
        self.label_personaje.raise_()
    
    def ejecutar_thread(self, tupla):
        thread = ThreadGorgory(self.senal_thread, *tupla)
        thread.start()
        self.threads.append(thread)
        
    def mover_gorgory(self, tupla):
        posicion = tupla[0]
        sprite = tupla[1]
        self.label_gorgory.move(*posicion)
        self.label_gorgory.setPixmap(QPixmap(sprite))
        self.label_gorgory.show()
        self.senal_pillar_gorgory.emit((self.posicion, self.label_gorgory))
        self.label_gorgory.raise_()
    
    def lista_posiciones(self):
        lista = list(map(lambda x: x.posicion, self.objetos))
        return lista
    
    def eliminar_objeto(self, objeto):
        self.objetos.remove(objeto)
        objeto.clear()
        
    def mostrar_ventana(self, diccionario):
        self.usuario = diccionario['usuario']
        self.personaje = diccionario['personaje']
        self.puntaje = diccionario['puntaje']
        self.dificultad = diccionario['dificultad']
        self.__vida = diccionario['vida']
        self.mapa = diccionario['mapa']
        self.items_normales = 0
        self.items_buenos_acumulados = diccionario['items_buenos']
        self.items_malos_acumulados = diccionario['items_malos']
        self.ronda = diccionario['ronda']
        self.items_malos = 0
        self.items_buenos = 0
        self.items_x2 = 0
        self.seguidos = 0
        self.pausa = False
        self.threads = []
        self.pillado_gorgory = False
        self.label_ronda.setText(f'RONDA: {self.ronda}')
        self.setear_mapa()
        self.limpiar_mapa()
        
        self.velocidad_personaje = p.DICCIONARIO_VELOCIDADES[self.personaje]
        self.movimientos = p.DICCIONARIO_MOVIMIENTOS[self.personaje]
        self.label_personaje = FotoEstandar(self, p.ANCHO_PERSONAJE, p.ALTO_PERSONAJE, \
            0, 0, self.movimientos['abajo_1'])
        
        self.label_gorgory = FotoEstandar(self, p.ANCHO_PERSONAJE, p.ALTO_PERSONAJE, \
            0, 0, p.DICCIONARIO_MOVIMIENTOS['gorgory']['abajo_1'])
        self.label_gorgory.hide()
        
        self.senal_colocar_obstaculos.emit()
        self.senal_creacion_timers.emit(self.dificultad.lower())
        
        self.show()