from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QFont
import parametros as p
from time import time

class Objeto(QLabel):
    
    def __init__(self, parent, tipo, dificultad, posicion, ancho, alto, mapa, \
        duracion, path, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.tipo = tipo
        self.posicion = posicion
        self.vivo = True
        self.tiempo_duracion = p.DICCIONARIO_DIFICULTADES[dificultad.lower()]['duracion']
        self.timer = QTimer()
        self.timer.setInterval(1000 * (self.tiempo_duracion + duracion))
        self.timer.timeout.connect(self.eliminar)
        self.timer.start()
        
        self.tiempo_inicio = time()

        self.resize(ancho, alto)
        self.setPixmap(QPixmap(path))
        self.setScaledContents(True)
        
        if mapa == 'Planta_nuclear':
            self.move(
                (posicion[0] + 0.15) * p.ANCHO_BALDOSA,
                p.VENTANA_ALTO - ( 8 - posicion[1]) * p.ALTO_BALDOSA * 0.96
            )
            
        else:
            self.move(
                (posicion[0] + 0.15) * p.ANCHO_BALDOSA,
                p.VENTANA_ALTO - ( 8 - posicion[1]) * p.ALTO_BALDOSA
            )
        
    def eliminar(self):
        self.vivo = False
        self.clear()

class FotoEstandar(QLabel):
    
    def __init__(self, parent, ancho, alto, posicion_x, posicion_y, path, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.setMaximumWidth(ancho)
        self.setMaximumHeight(alto)
        self.setMinimumWidth(ancho)
        self.setMinimumHeight(alto)
        self.resize(ancho, alto)
        self.move(posicion_x, posicion_y)
        
        if path != None:
            self.setPixmap(QPixmap(path))
            self.setScaledContents(True)

class BotonPersonalizado(QPushButton):
    
    diccionario_tamanos = {
        'chico': p.ESTILO_BOTONES_CHICOS,
        'normal': p.ESTILO_BOTONES_NORMALES
    }
    
    def __init__(self, text, parent, ancho, alto, posicion_x, posicion_y, type, *args, **kwargs):
        
        super().__init__(text, parent, *args, **kwargs)
        
        self.resize(ancho, alto)
        self.move(posicion_x, posicion_y)
        self.setStyleSheet(BotonPersonalizado.diccionario_tamanos[type])
        
        if type == 'chico':
            self.setFont(QFont('Courier', 9, QFont.Light))