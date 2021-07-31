from PyQt5 import QtMultimedia
from PyQt5.QtCore import pyqtSignal, QObject


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def comprobar_nombre(self, nombre):
        if nombre.isalnum():
            self.senal_respuesta_validacion.emit(True)
        else:
            self.senal_respuesta_validacion.emit(False)



class Musica(QObject):
    # NO MODIFICAR ESTA CLASE

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion
        self.playing = False

    def comenzar(self):
        try:
            self.cancion = QtMultimedia.QSound(self.ruta_cancion)
            self.cancion.Loop()
            self.cancion.play()
            self.playing = True
        except Exception as error:
            print('No se pudo iniciar la cancion', error)

    def parar(self):
        if self.playing:
            self.cancion.stop()
    
    def evaluar(self, pausa):
        if pausa:
            self.parar()
        else:
            self.comenzar()
    
    def reiniciar(self):
        self.parar()
        self.comenzar()