from os import name
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton, QGridLayout)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QFont, QIcon
import parametros as p
from random import choice


class VentanaRanking(QWidget):

    senal_cargar_ranking = pyqtSignal()
    senal_volver_inicio = pyqtSignal()
    senal_elegir_objeto = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self.ranking_cargado = False
        
        self.size = (p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.resize(p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.setMaximumHeight(p.VENTANA_ALTO)
        self.setMaximumWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))
        
        self.setMinimumHeight(p.VENTANA_ALTO)
        self.setMinimumWidth(p.VENTANA_ANCHO)

        self.setWindowTitle("Ventana de Ranking")

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

        self.title.setPixmap(QPixmap(p.PATH_RANKING_TITLE))
        self.title.setScaledContents(True)

        
        self.boton_volver = QPushButton('&Volver', self)
        self.boton_volver.setMinimumWidth(p.VENTANA_ANCHO / 4)
        self.boton_volver.setMaximumWidth(p.VENTANA_ANCHO / 4)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_volver.setFont(QFont('Courier', 10, QFont.Light))
        
        self.boton_volver.setStyleSheet(p.ESTILO_BOTONES_NORMALES)
        
        
        hbox_titulo_logo = QHBoxLayout()
        hbox_titulo_logo.addStretch(2)
        hbox_titulo_logo.addWidget(self.title)
        hbox_titulo_logo.addStretch(1)
        hbox_titulo_logo.addWidget(self.logo)
        hbox_titulo_logo.addStretch(2)

        
        hbox_volver = QHBoxLayout()
        hbox_volver.addStretch(0.5)
        hbox_volver.addWidget(self.boton_volver)
        hbox_volver.addStretch(0.5)
        

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_titulo_logo)
        vbox.addStretch(1)
        
        self.vboxs_ranking = []
        hbox_ranking = QHBoxLayout()
        hbox_ranking.addStretch(1)
        
        for _ in range(3):
            vbox_ranking = QVBoxLayout()
            self.vboxs_ranking.append(vbox_ranking)
            hbox_ranking.addLayout(vbox_ranking)
            hbox_ranking.addStretch(1)
        
        
        vbox.addLayout(hbox_ranking)
        vbox.addStretch(1)
        vbox.addLayout(hbox_volver)
        vbox.addStretch(1)
        self.setLayout(vbox)


    def volver(self):
        self.senal_volver_inicio.emit()
        self.hide()
    
    def mostrar_ranking(self, ranking):

        numeros = [str(i + 1) + '.' for i in range(min(5, len(ranking)))]
        nombres = [ranking[i].nombre for i in range(min(5, len(ranking)))]
        puntajes = [ranking[i].puntaje for i in range(min(5, len(ranking)))]
        
        lista_datos = [numeros, nombres, puntajes]
        lista_labels = ['Posición', 'Nombre de usuario', 'Puntaje']
        
        for i in range(len(self.vboxs_ranking)):
            
            vbox = self.vboxs_ranking[i]
            
            self.clearvbox(vbox)
            
            texto = QLabel(f'{str(lista_labels[i]): ^17s}', self)  
            texto.setFont(QFont('Courier', 50, QFont.Bold))
            
            vbox.addWidget(texto)
            
            texto_vacio = QLabel('', self)
            vbox.addWidget(texto_vacio)

            datos = lista_datos[i]
            vbox.addStretch(2)
            
            for j in range(min(5, len(ranking))):
                elemento = datos[j]
                
                texto_vacio = QLabel('', self)
                vbox.addWidget(texto_vacio)

                if i == 2:
                    elemento = str(elemento) + ' puntos'
                    
                texto = QLabel(f'{str(elemento): ^17s}', self)
                    
                texto.setFont(QFont('Courier', 40, QFont.Bold))
                
                vbox.addWidget(texto)
                vbox.addStretch(1)
                
            vbox.addStretch(2)

    def no_hay_ranking(self):
        for i in range(len(self.vboxs_ranking)):
            
            vbox = self.vboxs_ranking[i]
            self.clearvbox(vbox)
            
        label = QLabel('Aún no hay puntajes registrados ¯\_(ツ)_/¯')
        label.setFont(QFont('Courier', 40, QFont.Bold))
        label.setStyleSheet(p.ESTILO_LABEL_TOP)
        label.setMinimumWidth(p.VENTANA_ANCHO * 2 / 3)
        label.setMinimumHeight(50)
        
        self.vboxs_ranking[1].addStretch(1)
        self.vboxs_ranking[1].addWidget(label)
        self.vboxs_ranking[1].addStretch(1)
        
    def cargar_objeto(self, path):
        self.logo.setPixmap(QPixmap(path))
        self.logo.setScaledContents(True)
    
    
    def mostrar_ventana(self):

        self.senal_elegir_objeto.emit()

        self.senal_cargar_ranking.emit()
        self.ranking_cargado = True
            
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
            