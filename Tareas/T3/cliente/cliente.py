"""
Modulo contiene implementación principal del cliente
"""
import json
import threading
import socket

from PyQt5.QtCore import pyqtSignal, QObject
from funciones import manejar_mensajes
from clases import MegaThread
from logica import Logica
from ventanas.ventana_inicio import VentanaInicio
from ventanas.ventana_espera import VentanaEspera
from ventanas.ventana_juego import VentanaJuego

class Cliente(QObject):
    """
    Clase Cliente: Administra la conexión y la comunicación con el servidor.

    Atributos:
        host: string que representa la dirección del host (como una URL o una IP address).
        port: int que representa el número de puerto al cual conectarse.
        log_activado: booleano, controla si el programa "printea" en la consola (ver método log).
        controlador: instancia de Controlador, maneja la interfaz gráfica del programa.
        conectado: booleano, indica si el cliente se encuentra conectado al servidor.
        socket_cliente: socket del cliente, conectado al servidor.
    """
    senal_mostrar_login = pyqtSignal()
    senal_actualizar_labels = pyqtSignal(dict)
    senal_validacion = pyqtSignal(dict)
    senal_cerrar_espera = pyqtSignal(dict)
    senal_datos = pyqtSignal(dict)
    
    def __init__(self, host, port, parametros, log_activado=True):
        super().__init__()
        self.host = host
        self.port = port
        self.log_activado = log_activado

        self.en_espera = False

        self.logica = Logica()
        self.ventana_inicio = VentanaInicio(parametros)
        self.ventana_espera = VentanaEspera(parametros)
        self.ventana_juego = VentanaJuego(parametros)
        
        self.senal_mostrar_login.connect(self.ventana_inicio.mostrar_ventana)
        
        self.logica.senal_cerrar_espera.connect(self.ventana_espera.cerrar_ventana)
        self.logica.senal_validacion.connect(self.ventana_inicio.recibir_validacion)
        self.logica.senal_actualizar_labels.connect(self.ventana_espera.actualizar_labels)
        
        self.ventana_inicio.senal_elegir_nombre.connect(self.enviar)
        self.ventana_inicio.senal_abrir_sala_espera.connect(self.ventana_espera.mostrar_ventana)
        self.ventana_inicio.senal_abrir_sala_espera.connect(self.logica.espera)
        self.ventana_inicio.senal_abrir_sala_espera.connect(self.guardar_datos)
        
        self.ventana_espera.senal_votar.connect(self.enviar)
        self.ventana_espera.senal_iniciar_partida.connect(self.enviar)
        self.ventana_espera.senal_juego.connect(self.ventana_juego.mostrar_ventana)
        self.senal_datos.connect(self.ventana_juego.guardar_datos)
        
        self.logica.senal_para_fotos.connect(self.ventana_juego.poner_fotos)
        
        # Crear socket IPv4, TCP
        
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.iniciar_cliente()
    
    def guardar_datos(self, diccionario):
        self._id = diccionario["id_"]
        self.nombre = diccionario["nombre_usuario"]
        self.senal_datos.emit(diccionario)
    
    def iniciar_cliente(self):
        # Completar
        # IMPORTANTE: Si la conexión es exitosa, además de hacer lo que indica 
        # en el enunciado, debes invocar al método mostrar_login de self.controlador
        # self.controlador.mostrar_login()
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            thread = MegaThread(target = self.escuchar_servidor)
            thread.start()
            self.senal_mostrar_login.emit()
        
        except ConnectionResetError:
            self.log(...)
            self.socket_cliente.close()

    def escuchar_servidor(self):
        """Ciclo principal que escucha al servidor.

        Recibe mensajes desde el servidor, y genera una respuesta adecuada.
        """
        try:
            while self.conectado:
                mensaje = self.recibir()
                if not mensaje:
                    raise ConnectionResetError
                self.logica.manejar_mensaje(mensaje)
        
        except ConnectionResetError:
            self.log(...)
        
        finally:
            self.socket_cliente.close()
            
    def enviar(self, mensaje):
        """Envía un mensaje a un cliente.

        Argumentos:
            mensaje (dict): Contiene la información a enviar.
        """
        codificado = manejar_mensajes(mensaje, 0)
        self.socket_cliente.sendall(codificado)

    def recibir(self):
        """Recibe un mensaje del servidor.

        Recibe el mensaje, lo decodifica usando el protocolo establecido,
        y lo des-serializa (via decodificar_mensaje).

        Retorna:
            dict: contiene el mensaje, después de ser decodificado.
        """
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = self.socket_cliente.recv(4)
        bytes_mensaje.extend(bytes_largo_mensaje)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder = 'big')
        
        bytes_tipo_mensaje = self.socket_cliente.recv(4)
        bytes_mensaje.extend(bytes_tipo_mensaje)
        tipo_mensaje = int.from_bytes(bytes_tipo_mensaje, byteorder = 'little')
        
        if tipo_mensaje == 1:
            bytes_color = self.socket_cliente.recv(4)
            bytes_mensaje.extend(bytes_color)
            
            while len(bytes_mensaje) < (largo_mensaje // 100 + 1) * 104:
                bytes_mensaje.extend(self.socket_cliente.recv(104))
        
        else:
            while len(bytes_mensaje) < (largo_mensaje // 60 + 1) * 64:
                bytes_mensaje.extend(self.socket_cliente.recv(64))

        decodificado = manejar_mensajes(bytes_mensaje, 1)
        if not isinstance(decodificado, dict):
            return [bytes_mensaje]
        return decodificado

    def log(self, mensaje_consola):
        """Imprime un mensaje a la consola, sólo si la funcionalidad está activada.

        Argumentos:
            mensaje_consola (str): mensaje a imprimir.
        """
        if self.log_activado:
            print(mensaje_consola)
