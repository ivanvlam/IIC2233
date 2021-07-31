from funciones import manejar_mensajes
from PyQt5.QtWidgets import (
    QLabel, QWidget, QButtonGroup, QRadioButton,
    QProgressBar, QComboBox, QPushButton, QLineEdit)
from PyQt5.QtCore import pyqtSignal, Qt, QPoint
from PyQt5.QtGui import QPixmap, QFont, QIcon, QPainter, QColor, QBrush, QPen
from funciones import construir_grafo

#54B4E6
ESTILO_BOTONES = '''
    background-color: white;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: black;
    font: bold 14px;
    min-width: 5em;
    min-height: 25 px;
    padding: 6px;
'''

ESTILO_LABEL = '''
    background-color : rgb(213, 238, 251);
    border-style: solid;
    border-width: 3px;
    border-radius: 20px;
    border-color: black;
'''

class VentanaJuego(QWidget):

    senal_salir = pyqtSignal()
    senal_teclas = pyqtSignal(dict)
    senal_posicion_personaje = pyqtSignal()
    senal_iniciar_partida = pyqtSignal(dict)
    senal_reiniciar_musica = pyqtSignal()

    def __init__(self, parametros):
        super().__init__()
        self.parametros = parametros
        #senal_mostrar.connect(self.mostrar_ventana)
        
        self.ancho = 2 * parametros["ancho_ventana"]
        self.alto = parametros["alto_ventana"]
        self.ruta_fondo = parametros["imagenes"]["ruta_fondo"]
        self.ruta_logo = parametros["imagenes"]["ruta_logo"]
        self.texto_camino = parametros["imagenes"]["texto_camino"]
        self.flecha = parametros["imagenes"]["flecha"]
        self.jugadores_text = parametros["imagenes"]["jugadores_juego"]
        self.imagenes = parametros["imagenes"]
        self.estilo_boton = ESTILO_BOTONES
        self.i = 0
        
        self.size = (self.ancho, self.alto)
        self.resize(self.ancho, self.alto)
        self.setMaximumHeight(self.alto)
        self.setMaximumWidth(self.ancho)
        
        self.setWindowIcon(QIcon(self.ruta_logo))
        
        self.setMinimumHeight(self.alto)
        self.setMinimumWidth(self.ancho)

        self.setWindowTitle("Sala de juego")

        self.init_gui()
        
    def init_gui(self):
        
        self.background = QLabel(self)
        self.background.setMinimumWidth(self.ancho)
        self.background.setMinimumHeight(self.alto)
        self.background.setPixmap(QPixmap(self.ruta_fondo))
        self.background.setScaledContents(True)
        
        self.top_label = QLabel(self)
        self.top_label.resize(self.ancho * 70 / 100, self.alto * 20 / 100)
        self.top_label.setStyleSheet(ESTILO_LABEL)
        self.top_label.move(self.ancho * 1 / 100, self.alto * 1 / 100)
        
        self.texto_camino_comprar = QLabel(self)
        self.texto_camino_comprar.resize(self.alto * 70 / 100, self.alto * 9 / 100)
        self.texto_camino_comprar.setPixmap(QPixmap(self.texto_camino))
        self.texto_camino_comprar.setScaledContents(True)
        self.texto_camino_comprar.move(self.ancho * 14 / 100, self.alto * 3 / 100)
        
        self.box_inicio = QComboBox(self)
        self.box_inicio.resize(55, 55)
        self.box_inicio.setFont(QFont('Courier', 14, QFont.Bold))
        self.box_inicio.move(self.ancho * 25 / 100, self.alto * 12 / 100)
        self.box_inicio.setStyleSheet("border: 2px solid black;")
        
        self.arrow_image = QLabel(self)
        self.arrow_image.resize(self.ancho * 9 / 100, self.ancho * 9 / 100)
        self.arrow_image.setPixmap(QPixmap(self.flecha))
        self.arrow_image.setScaledContents(True)
        self.arrow_image.move(self.ancho * 30 / 100, self.alto * 7.5 / 100)
        
        self.box_final = QComboBox(self)
        self.box_final.resize(55, 55)
        self.box_final.setFont(QFont('Courier', 14, QFont.Bold))
        self.box_final.move(self.ancho * 40 / 100, self.alto * 12 / 100)
        self.box_final.setStyleSheet("border: 2px solid black;")
        self.box_final.setDisabled(True)
        
        self.left_label = QLabel(self)
        self.left_label.setScaledContents(True)
        self.left_label.resize(self.ancho * 70 / 100, self.alto * 77 / 100)
        self.left_label.setStyleSheet("border: 3px solid black;")
        self.left_label.move(self.ancho * 1 / 100, self.alto * 22 / 100)
        
        painter = QPainter()
        painter.drawLine(30, 40, 80, 90);
        painter.drawLine(QPoint(200, 200), QPoint(400, 400))

        self.boton_comprar = QPushButton('&Comprar', self)
        self.boton_comprar.resize(self.boton_comprar.sizeHint())
        #self.boton_comprar.clicked.connect(self.enviar_nombre)
        self.boton_comprar.setFont(QFont('Courier', 12, QFont.Bold))
        self.boton_comprar.move(self.ancho * 61 / 100, self.alto * 13 / 100)
        self.boton_comprar.setStyleSheet(self.estilo_boton)
                        
        self.right_label = QLabel(self)
        self.right_label.resize(self.ancho * 27 / 100, self.alto * 52 / 100)
        self.right_label.setStyleSheet(ESTILO_LABEL)
        self.right_label.move(self.ancho * 72 / 100, self.alto * 22 / 100)
        
        self.texto_jugadores = QLabel(self)
        self.texto_jugadores.resize(self.alto * 38 / 100, self.alto * 8 / 100)
        self.texto_jugadores.setPixmap(QPixmap(self.jugadores_text))
        self.texto_jugadores.setScaledContents(True)
        self.texto_jugadores.move(self.ancho * 74.5 / 100, self.alto * 24 / 100)
        
        self.bottom_label = QLabel(self)
        self.bottom_label.resize(self.ancho * 27 / 100, self.alto * 24 / 100)
        self.bottom_label.setStyleSheet(ESTILO_LABEL)
        self.bottom_label.move(self.ancho * 72 / 100, self.alto * 75 / 100)
        
        self.boton_carta = QPushButton('&Sacar carta', self)
        self.boton_carta.setStyleSheet(self.estilo_boton)
        self.boton_carta.setMaximumHeight(15)
        #self.boton_carta.clicked.connect(self.enviar_nombre)
        self.boton_carta.setFont(QFont('Courier', 12, QFont.Bold))
        self.boton_carta.move(self.ancho * 73 / 100, self.alto * 91 / 100)
        
        self.top_right_label = QLabel(self)
        self.top_right_label.resize(self.ancho * 27 / 100, self.alto * 20 / 100)
        self.top_right_label.setStyleSheet(ESTILO_LABEL)
        self.top_right_label.move(self.ancho * 72 / 100, self.alto / 100)
        
        self.texto_mapa = QLabel(self)
        self.texto_mapa.resize(self.alto * 38 / 100, self.alto * 8 / 100)
        self.texto_mapa.setScaledContents(True)
        self.texto_mapa.move(self.ancho * 74.5 / 100, self.alto * 3.5 / 100)
        
        self.label_jugador_actual = QLabel('Jugador actual:\nIvan', self)
        self.label_jugador_actual.setFont(QFont('Courier', 14, QFont.Bold))
        self.label_jugador_actual.setAlignment(Qt.AlignCenter)
        self.label_jugador_actual.move(self.ancho * 76.5 / 100, self.alto * 11 / 100)
    
    def cargar_mapa(self, mensaje):
        diccionario = mensaje["comando"]
        mapa = diccionario["mapa"]
        self.grafo = construir_grafo(mapa)
        self.ruta_mapa = self.parametros["imagenes"]['mapa_' + str(mapa)]
        self.ruta_texto = self.parametros["imagenes"]['texto_' + str(mapa)]
        self.left_label.setPixmap(QPixmap(self.ruta_mapa))
        self.texto_mapa.setPixmap(QPixmap(self.ruta_texto))
        self.labels_grafo = {}
        self.orden_jugadores = mensaje['0']['orden_jugadores']
        self.orden_colores = mensaje['0']['orden_colores']
        
        for nodo in self.grafo.nodos:
            label = QLabel(self)
            x, y = nodo.posicion[0], nodo.posicion[1]
            label.move(self.ancho / 100 * (1 + 70 * x), self.alto / 100 * (22 + 77 * y))
            self.labels_grafo[nodo._id] = label
            self.box_inicio.addItem(nodo._id)
        
        self.labels_fotos = []

    def poner_fotos(self, bytes_):
        _bytes, color = manejar_mensajes(bytes_, 1)[0], manejar_mensajes(bytes_, 1)[1]
        
        self.fotos_jugadores = []

        if self.i < len(self.orden_colores.keys()):
            label = QLabel(self)
            label.resize(90, 90)
            pixmap = QPixmap()
            pixmap.loadFromData(_bytes)
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            label.show()
            label.raise_()
            label.move(self.ancho * 74 / 100, self.alto / 100 * (32 + self.i * 13))
            self.fotos_jugadores.append(label)
            self.i += 1
        
    def guardar_datos(self, diccionario):
        self._id = diccionario["id_"]
        self.nombre = diccionario["nombre_usuario"]
    
    def mostrar_ventana(self, diccionario):
        self.cargar_mapa(diccionario)
        self.show()
    