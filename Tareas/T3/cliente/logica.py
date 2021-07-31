from PyQt5.QtCore import QObject, pyqtSignal

class Logica(QObject):
    
    senal_actualizar_labels = pyqtSignal(dict)
    senal_validacion = pyqtSignal(dict)
    senal_cerrar_espera = pyqtSignal(dict)
    senal_para_fotos = pyqtSignal(bytearray)
    
    def __init__(self):
        super().__init__()
        self.en_espera = False
    
    def espera(self, _):
        self.en_espera = True
    
    def manejar_mensaje(self, mensaje):
        """
        Maneja un mensaje recibido desde el servidor.
        Genera la respuesta y los cambios en la interfaz correspondientes.

        Argumentos:
            mensaje (dict): Mensaje ya decodificado recibido desde el servidor
        """
        if isinstance(mensaje, dict):
        
            if mensaje["comando"] == "ingreso":
                if self.en_espera:
                    self.senal_actualizar_labels.emit(mensaje)
                else:
                    self.senal_validacion.emit(mensaje)

            elif mensaje["comando"] == "voto":
                self.senal_actualizar_labels.emit(mensaje)
            
            elif mensaje["comando"] == "iniciar":
                self.senal_cerrar_espera.emit(mensaje)
            
            elif mensaje["comando"]["comando"] == "iniciar":
                self.senal_cerrar_espera.emit(mensaje)
        
        else:
            self.senal_para_fotos.emit(mensaje[0])
            #print(mensaje[0])
