from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
import parametros as p


class VentanaInicio(QWidget):


    senal_abrir_eleccion_personaje = pyqtSignal(str)  
    senal_elegir_nombre = pyqtSignal(str)  
    senal_mostrar_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.size = (p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.resize(p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.setMaximumHeight(p.VENTANA_ALTO)
        self.setMaximumWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))
        
        self.setMinimumHeight(p.VENTANA_ALTO)
        self.setMinimumWidth(p.VENTANA_ANCHO)

        self.setWindowTitle("Ventana de Inicio")

        self.init_gui()
        

    def init_gui(self):
        self.background = QLabel(self)
        self.background.resize(self.background.sizeHint())
        self.background.setMaximumWidth(p.VENTANA_ANCHO)
        self.background.setMaximumHeight(p.VENTANA_ALTO)
        self.background.setMinimumWidth(p.VENTANA_ANCHO)
        self.background.setMinimumHeight(p.VENTANA_ALTO)

        self.background.setPixmap(QPixmap(p.PATH_BACKGROUND))
        self.background.setScaledContents(True)
        
        self.logo = QLabel(self)
        self.logo.resize(self.logo.sizeHint())
        self.logo.setMaximumWidth(p.LOGO_ANCHO)
        self.logo.setMaximumHeight(p.LOGO_ALTO)
        self.logo.setMinimumWidth(p.LOGO_ANCHO)
        self.logo.setMinimumHeight(p.LOGO_ALTO)

        self.logo.setPixmap(QPixmap(p.PATH_LOGO))
        self.logo.setScaledContents(True)
        
        self.label_nombre = QLabel('Escribe tu nombre de usuario:', self)
        self.label_nombre.setFont(QFont('Courier', 11))
        
        self.line_edit_nombre = QLineEdit('', self)
        self.line_edit_nombre.setMinimumWidth(p.VENTANA_ANCHO / 2)
        self.line_edit_nombre.setFont(QFont('Courier', 10, QFont.Light))
        
        self.boton_partida = QPushButton('&Iniciar Partida', self)
        self.boton_partida.resize(self.boton_partida.sizeHint())
        self.boton_partida.setMinimumWidth(p.VENTANA_ANCHO / 4)
        self.boton_partida.setMaximumWidth(p.VENTANA_ANCHO / 4)
        self.boton_partida.clicked.connect(self.enviar_nombre)
        self.boton_partida.setFont(QFont('Courier', 10, QFont.Light))
        
        self.boton_partida.setStyleSheet(p.ESTILO_BOTONES_NORMALES)
        
        self.boton_ranking = QPushButton('&Ver ranking', self)
        self.boton_ranking.setMinimumWidth(p.VENTANA_ANCHO / 4)
        self.boton_ranking.setMaximumWidth(p.VENTANA_ANCHO / 4)
        self.boton_ranking.clicked.connect(self.mostrar_ranking)
        self.boton_ranking.setFont(QFont('Courier', 10, QFont.Light))

        self.boton_ranking.setStyleSheet(p.ESTILO_BOTONES_NORMALES)
        
        hbox_logo = QHBoxLayout()
        hbox_logo.addStretch(1)
        hbox_logo.addWidget(self.logo)
        hbox_logo.addStretch(1)
        
        hbox_label_nombre = QHBoxLayout()
        hbox_label_nombre.addStretch(1)
        hbox_label_nombre.addWidget(self.label_nombre)
        hbox_label_nombre.addStretch(1)
        
        hbox_line_edit = QHBoxLayout()
        hbox_line_edit.addStretch(1)
        hbox_line_edit.addWidget(self.line_edit_nombre)
        hbox_line_edit.addStretch(1)


        hbox_partida = QHBoxLayout()
        hbox_partida.addStretch(0.5)
        hbox_partida.addWidget(self.boton_partida)
        hbox_partida.addStretch(0.5)
        
        hbox_ranking = QHBoxLayout()
        hbox_ranking.addStretch(0.5)
        hbox_ranking.addWidget(self.boton_ranking)
        hbox_ranking.addStretch(0.5)
        

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_logo)
        vbox.addStretch(0.5)
        vbox.addLayout(hbox_label_nombre)
        vbox.addLayout(hbox_line_edit)
        vbox.addStretch(0.5)
        vbox.addLayout(hbox_partida)
        vbox.addLayout(hbox_ranking)
        vbox.addStretch(0.5)
        self.setLayout(vbox)
        
        
    def enviar_nombre(self):
        nombre_ingresado = self.line_edit_nombre.text()
        self.senal_elegir_nombre.emit(nombre_ingresado)
        
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.enviar_nombre()


    def recibir_validacion(self, validado):

        if validado:
            self.hide()
            self.senal_abrir_eleccion_personaje.emit(self.line_edit_nombre.text())
            self.line_edit_nombre.setPlaceholderText("")
            
        else:
            self.line_edit_nombre.setPlaceholderText("Nombre inválido")
        
        self.line_edit_nombre.clear()
            
            
    def mostrar_ranking(self):
        self.line_edit_nombre.setPlaceholderText("")
        self.line_edit_nombre.clear()
        self.senal_mostrar_ranking.emit()
        
        
    def mostrar_ventana(self):
        self.show()
