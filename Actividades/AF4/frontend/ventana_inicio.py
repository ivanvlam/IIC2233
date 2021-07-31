import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton, QApplication,
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaInicio(QWidget):
    """
    Ventana de log-in para el juego. Consta de una imagen, un campo de texto y un boton para
    ingresar. Es la primera ventana que se ve en el programa
    """
    senal_abrir_eleccion_personaje = pyqtSignal(str)  # Señal que abre la ventana de eleccion
    senal_elegir_nombre = pyqtSignal(str)  # Señal para enviar el nombre al back-end para verificar

    def __init__(self, ancho, alto, ruta_logo):
        # NO MODIFICAR
        super().__init__()
        self.size = (ancho, alto)
        self.resize(ancho, alto)

        self.setWindowTitle("Ventana Inicio")

        self.init_gui(ruta_logo)  # Llamada a la funcion que inicia la interfaz

    def init_gui(self, ruta_logo):
        self.label1 = QLabel('Ingrese su nombre:', self)
        self.line_edit_nombre = QLineEdit('', self)
        self.line_edit_nombre.resize(100, 20)
        self.boton1 = QPushButton('Entrar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.clicked.connect(self.enviar_nombre)

        self.logo = QLabel(self)
        self.logo.resize(self.logo.sizeHint())

        pixeles = QPixmap(ruta_logo)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)

        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.logo)


        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.line_edit_nombre)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.boton1)

        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        

    def enviar_nombre(self):
        nombre_ingresado = self.line_edit_nombre.text()
        self.senal_elegir_nombre.emit(nombre_ingresado)

    def recibir_validacion(self, validado):
        # NO MODIFICAR
        """
        Este método recibe desde el back-end una señal que indica si el nombre enviado es
        valido o no. De ser valido, se sigue a la siguiente ventana. En el caso contrario, se borra
        el texto del QLine y se notifica que el nombre es invalido
        """
        if validado:
            self.hide()
            self.senal_abrir_eleccion_personaje.emit(self.line_edit_nombre.text())
        else:
            self.line_edit_nombre.clear()
            self.line_edit_nombre.setPlaceholderText("Nombre inválido")
