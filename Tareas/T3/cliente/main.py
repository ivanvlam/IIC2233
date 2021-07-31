import sys
from os.path import join
from PyQt5.QtWidgets import QApplication
from cliente import Cliente
from funciones import cargar_parametros
from ventanas.ventana_juego import VentanaJuego


def hook(type_error, traceback):
    print(type_error)
    print(traceback)

if __name__ == '__main__':
    
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    
    p = cargar_parametros()
    '''
    ventana_inicio = VentanaInicio(p["ancho_ventana"], p["alto_ventana"], p["imagenes"])
    logica_inicio = LogicaInicio()
    cliente = Cliente(p["host"], p["port"])
    
    ventana_inicio.senal_elegir_nombre.connect(logica_inicio.comprobar_nombre)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)
    
    ventana_inicio.show()
    '''
    cliente = Cliente(p["host"], p["port"], p)
    #ventana = VentanaJuego(p)
    #ventana.show()
    
    sys.exit(app.exec_())
    