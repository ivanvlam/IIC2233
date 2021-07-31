from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon

ESTILO_BOTONES = '''
    background-color: white;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: black;
    font: bold 16px;
    min-width: 10em;
    min-height: 25 px;
    padding: 6px;
'''

class VentanaInicio(QWidget):

    senal_abrir_sala_espera = pyqtSignal(dict)  
    senal_elegir_nombre = pyqtSignal(dict)  
    senal_mostrar_ranking = pyqtSignal()

    def __init__(self, parametros):
        super().__init__()
        
        self.ancho = parametros["ancho_ventana"]
        self.alto = parametros["alto_ventana"]
        self.ruta_fondo = parametros["imagenes"]["ruta_fondo"]
        self.ruta_logo = parametros["imagenes"]["ruta_logo"]
        self.estilo_boton = ESTILO_BOTONES
        
        self.size = (self.ancho, self.alto)
        self.resize(self.ancho, self.alto)
        self.setMaximumHeight(self.alto)
        self.setMaximumWidth(self.ancho)
        
        self.setWindowIcon(QIcon(self.ruta_logo))
        
        self.setMinimumHeight(self.alto)
        self.setMinimumWidth(self.ancho)

        self.setWindowTitle("Ventana de Inicio")

        self.init_gui()
        

    def init_gui(self):
        self.background = QLabel(self)
        self.background.resize(self.background.sizeHint())
        self.background.setMaximumWidth(self.ancho)
        self.background.setMaximumHeight(self.alto)
        self.background.setMinimumWidth(self.ancho)
        self.background.setMinimumHeight(self.alto)

        self.background.setPixmap(QPixmap(self.ruta_fondo))
        self.background.setScaledContents(True)
        
        self.logo = QLabel(self)
        self.logo.resize(self.logo.sizeHint())
        self.logo.setMaximumWidth(self.alto * 3/4)
        self.logo.setMaximumHeight(self.alto * 3/4)
        self.logo.setMinimumWidth(self.alto * 3/4)
        self.logo.setMinimumHeight(self.alto * 3/4)

        self.logo.setPixmap(QPixmap(self.ruta_logo))
        self.logo.setScaledContents(True)
        
        self.label_nombre = QLabel('Escribe tu nombre de usuario:', self)
        self.label_nombre.setFont(QFont('Courier', 10))
        
        self.line_edit_nombre = QLineEdit('', self)
        self.line_edit_nombre.setMinimumWidth(self.ancho / 5 * 3)
        self.line_edit_nombre.setMinimumHeight(35)
        self.line_edit_nombre.setFont(QFont('Courier', 9, QFont.Light))

        self.boton_partida = QPushButton('&Ingresar', self)
        self.boton_partida.resize(self.boton_partida.sizeHint())
        self.boton_partida.setMinimumWidth(self.ancho / 4)
        self.boton_partida.setMaximumWidth(self.ancho / 4)
        self.boton_partida.clicked.connect(self.enviar_nombre)
        self.boton_partida.setFont(QFont('Courier', 12, QFont.Bold))
        
        self.boton_partida.setStyleSheet(self.estilo_boton)
    
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
        

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_logo)
        vbox.addLayout(hbox_label_nombre)
        vbox.addLayout(hbox_line_edit)
        vbox.addStretch(0.5)
        vbox.addLayout(hbox_partida)
        vbox.addStretch(0.5)
        self.setLayout(vbox)
    
        
    def enviar_nombre(self):
        nombre_ingresado = self.line_edit_nombre.text()
        diccionario = {
            "comando": "ingreso",
            "argumentos": nombre_ingresado
        }
        self.senal_elegir_nombre.emit(diccionario)
    
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.enviar_nombre()

    
    def recibir_validacion(self, diccionario):

        validado, motivo = diccionario["validado"], diccionario["motivo"]
        
        if validado:
            self.hide()
            self.senal_abrir_sala_espera.emit(diccionario)
        
        elif motivo == 0:
            self.line_edit_nombre.setPlaceholderText("Nombre ya en uso")
        
        elif motivo == 1:
            self.line_edit_nombre.setPlaceholderText("Nombre inválido")
        
        else:
            self.line_edit_nombre.setPlaceholderText("Sala llena")
            
        self.line_edit_nombre.clear()
    
    def cerrar_ventana(self):
        self.close()    

    def mostrar_ventana(self):
        self.show()
