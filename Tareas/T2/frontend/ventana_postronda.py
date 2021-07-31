from PyQt5.QtWidgets import (
    QLabel, QWidget, QHBoxLayout,
    QVBoxLayout, QPushButton)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
import parametros as p


class VentanaPostronda(QWidget):

    senal_elegir_objeto = pyqtSignal()
    senal_continuar = pyqtSignal(dict)
    senal_reinciar_musica = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self.size = (p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.resize(p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.setMaximumHeight(p.VENTANA_ALTO)
        self.setMaximumWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))
        
        self.setMinimumHeight(p.VENTANA_ALTO)
        self.setMinimumWidth(p.VENTANA_ANCHO)

        self.setWindowTitle("Ventana post-ronda")

        self.init_gui()

        
    def init_gui(self):
        self.background = QLabel(self)
        self.background.resize(p.VENTANA_ANCHO, p.VENTANA_ALTO)

        self.background.setPixmap(QPixmap(p.PATH_BACKGROUND))
        self.background.setScaledContents(True)
        
        
        self.logo = QLabel(self)
        self.logo.resize(100, 100)
        self.logo.setMaximumWidth(100)
        self.logo.setMaximumHeight(100)
        
        
        self.title = QLabel(self)
        self.title.resize(self.title.sizeHint())

        self.title.setPixmap(QPixmap(p.PATH_RONDA_TITLE))
        self.title.setScaledContents(True)
        

        self.label_puntaje_ronda = QLabel(self)
        self.label_puntaje_ronda.setFont(QFont('Courier', 14, QFont.Bold))
        
        self.label_puntaje_acumulado = QLabel(self)
        self.label_puntaje_acumulado.setFont(QFont('Courier', 14, QFont.Bold))
        
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Courier', 14, QFont.Bold))
        
        self.label_items_buenos = QLabel(self)
        self.label_items_buenos.setFont(QFont('Courier', 14, QFont.Bold))
        
        self.label_items_malos = QLabel(self)
        self.label_items_malos.setFont(QFont('Courier', 14, QFont.Bold))
        
        self.label_continuar = QLabel(self)
        self.label_continuar.setMinimumWidth(p.VENTANA_ANCHO * 2 / 3)
        self.label_continuar.setMinimumHeight(60)
        self.label_continuar.setFont(QFont('Courier', 9, QFont.Bold))
        self.label_continuar.setAlignment(Qt.AlignCenter)
        
        self.boton_continuar = QPushButton('&Continuar jugando', self)
        self.boton_continuar.setMinimumWidth(p.VENTANA_ANCHO / 4)
        self.boton_continuar.setMaximumWidth(p.VENTANA_ANCHO / 4)
        self.boton_continuar.clicked.connect(self.continuar)
        self.boton_continuar.setFont(QFont('Courier', 10, QFont.Light))
        self.boton_continuar.setStyleSheet(p.ESTILO_BOTONES_NORMALES)
        
        self.boton_salir = QPushButton('&Salir', self)
        self.boton_salir.setMinimumWidth(p.VENTANA_ANCHO / 4)
        self.boton_salir.setMaximumWidth(p.VENTANA_ANCHO / 4)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_salir.setFont(QFont('Courier', 10, QFont.Light))
        self.boton_salir.setStyleSheet(p.ESTILO_BOTONES_NORMALES)
        
        
        hbox_titulo_logo = QHBoxLayout()
        hbox_titulo_logo.addStretch(2)
        hbox_titulo_logo.addWidget(self.title)
        hbox_titulo_logo.addStretch(1)
        hbox_titulo_logo.addWidget(self.logo)
        hbox_titulo_logo.addStretch(2)

        
        hbox_botones = QHBoxLayout()
        hbox_botones.addStretch(1)
        hbox_botones.addWidget(self.boton_continuar)
        hbox_botones.addStretch(1)
        hbox_botones.addWidget(self.boton_salir)
        hbox_botones.addStretch(1)
        

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_titulo_logo)
        vbox.addStretch(1)
    
        vbox.addWidget(self.label_puntaje_ronda, alignment = Qt.AlignCenter)
        vbox.addStretch(1)
        vbox.addWidget(self.label_puntaje_acumulado, alignment = Qt.AlignCenter)
        vbox.addStretch(1)
        vbox.addWidget(self.label_vida, alignment = Qt.AlignCenter)
        vbox.addStretch(1)
        vbox.addWidget(self.label_items_buenos, alignment = Qt.AlignCenter)
        vbox.addStretch(1)
        vbox.addWidget(self.label_items_malos, alignment = Qt.AlignCenter)
        
        vbox.addStretch(1)
        vbox.addWidget(self.label_continuar, alignment = Qt.AlignCenter)
        vbox.addStretch(1)
        vbox.addLayout(hbox_botones)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def continuar(self):
        self.senal_continuar.emit({
            'usuario': self.usuario,
            'vida': self.vida,
            'items_buenos_total': self.items_buenos_acumulados,
            'items_malos_total': self.items_malos_acumulados,
            'puntaje': int(self.puntaje),
            'ronda': self.ronda
        })
        self.senal_reinciar_musica.emit()
        self.close()

    def salir(self):
        self.close()
        
    def recibir_datos(self, diccionario):
        self.usuario = diccionario['usuario']
        self.vida = diccionario['vida']
        self.items_normales = diccionario['items_normales']
        self.items_buenos = diccionario['items_buenos']
        self.items_malos = diccionario['items_malos']
        self.items_x2 = diccionario['items_x2']
        self.puntaje = diccionario['puntaje']
        puntaje_ronda = diccionario['puntaje_ronda']
        self.items_buenos_acumulados = diccionario['items_buenos_total']
        self.items_malos_acumulados = diccionario['items_malos_total']
        self.ronda = diccionario['ronda']
        self.pillado = diccionario['pillado']
        
        self.label_puntaje_ronda.setText(f'Puntaje ronda: {int(puntaje_ronda)} puntos')
        self.label_puntaje_acumulado.setText(f'Puntaje acumulado: {int(self.puntaje)} puntos')
        self.label_vida.setText(f'Vida: {self.vida * 100}%')
        self.label_items_buenos.setText(f'Items buenos: {self.items_buenos}')
        self.label_items_malos.setText(f'Items malos: {self.items_malos}')
        
        if self.pillado:
            self.label_continuar.setText('Te ha atrapado el jefe Gorgory.\n' \
                'Fin del juego ¯\_(ツ)_/¯')
            self.label_continuar.setStyleSheet(p.ESTILO_LABEL_FIN)
            self.boton_continuar.setDisabled(True)
        elif self.vida == 0:
            self.label_continuar.setText('Te has quedado sin vida.\nFin del juego ¯\_(ツ)_/¯')
            self.label_continuar.setStyleSheet(p.ESTILO_LABEL_FIN)
            self.boton_continuar.setDisabled(True)
        else:
            self.label_continuar.setText('Bien jugado! Presiona el botón continuar\n' \
                'para volver a la ventana de preparación')
            self.label_continuar.setStyleSheet(p.ESTILO_LABEL_CONTINUAR)
        
    def cargar_objeto(self, path):
        self.logo.setPixmap(QPixmap(path))
        self.logo.setScaledContents(True)
    
    
    def mostrar_ventana(self):

        self.senal_elegir_objeto.emit()
        self.show()
    

    def clearvbox(self, L = False):
        if L is not None:
            while L.count():
                item = L.takeAt(0)
                
                widget = item.widget()
                
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearvbox(item.layout())