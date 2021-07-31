"""
Modulo contiene implementación principal del servidor
"""
import json
import socket
import threading
from logica import Logica
from funciones import manejar_mensajes

class Servidor:
    """
    Clase Servidor: Administra la conexión y la comunicación con los clientes

    Atributos:
        host: string que representa la dirección del host (como una URL o una IP address).
        port: int que representa el número de puerto en el cual el servidor recibirá conexiones.
        log_activado: booleano, controla si el programa "printea" en la consola (ver método log).
        socket_servidor: socket del servidor, encargado de recibir conexiones.
        clientes_conectados: diccionario que mantiene los sockets de los clientes actualmente
            conectados, de la forma { id : socket_cliente }.
        logica: instancia de Logica que maneja el funcionamiento interno del programa
    """

    _id_cliente = 0
    # Administra el acceso a clientes_conectados para evitar que se produzcan errores.
    clientes_conectados_lock = threading.Lock()

    def __init__(self, host, port, log_activado=True):
        self.host = host
        self.port = port
        self.log_activado = log_activado

        # Crear atributo para el socket del servidor, pero vacío
        self.socket_servidor = None

        self.log("Inicializando servidor...")
        self.iniciar_servidor()

        # Crear diccionario de clientes de la forma { id : socket }
        self.clientes_conectados = dict()

        self.logica = Logica(log_activado)

        # Crea y comienza thread encargado de aceptar clientes
        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()

    def aceptar_clientes(self):
        """Ciclo principal que acepta clientes."""
        while True:
            socket_cliente, address = self.socket_servidor.accept()
            with self.clientes_conectados_lock:
                id_cliente = self._id_cliente
                self.clientes_conectados[id_cliente] = socket_cliente
                self._id_cliente += 1
                self.log(f'El cliente {id_cliente} se ha conectado')
            thread_cliente = threading.Thread(target = self.escuchar_cliente, args = (id_cliente, ))
            thread_cliente.start()

    def escuchar_cliente(self, id_cliente):
        """Ciclo principal que escucha a un cliente.

        Recibe mensajes de un cliente, y genera una respuesta adecuada o levanta
        una acción según el mensaje recibido.

        Argumentos:
            id_cliente (int): La id del cliente a escuchar.
        """
        try:
            socket_cliente = self.clientes_conectados[id_cliente]
            while True:
                mensaje = self.recibir(socket_cliente)
                if not mensaje:
                    raise ConnectionResetError
                respuesta, targets = self.logica.manejar_mensaje(mensaje, id_cliente)
                if respuesta:
                    for target in targets:
                        if isinstance(respuesta, list):
                            for resp in respuesta:
                                self.enviar(resp, self.clientes_conectados[target])
                        else:
                            self.enviar(respuesta, self.clientes_conectados[target])

        except ConnectionResetError:
            self.log(...)
        self.eliminar_cliente(id_cliente)
            
    def enviar(self, mensaje, socket_cliente):
        """Envía un mensaje a un cliente.

        Argumentos:
            mensaje (dict): Contiene la información a enviar.
            socket_cliente (socket): El socket objetivo al cual enviar el mensaje.
        """
        codificado = manejar_mensajes(mensaje, 0)
        socket_cliente.sendall(codificado)
    
    def recibir(self, socket_cliente):
        """Recibe un mensaje del cliente.

        Recibe el mensaje, lo decodifica usando el protocolo establecido,
        y lo des-serializa (via decodificar_mensaje).

        Argumentos:
            socket_cliente (socket): El socket del cliente del cual recibir.

        Retorna:
            dict: contiene el mensaje, después de ser decodificado.
        """
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = socket_cliente.recv(4)
        bytes_mensaje.extend(bytes_largo_mensaje)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder = 'big')
        
        bytes_tipo_mensaje = socket_cliente.recv(4)
        bytes_mensaje.extend(bytes_tipo_mensaje)
        tipo_mensaje = int.from_bytes(bytes_tipo_mensaje, byteorder = 'little')
        
        if tipo_mensaje == 1:
            bytes_color = self.socket_cliente.recv(4)
            bytes_mensaje.extend(bytes_color)
            
            while len(bytes_mensaje) < (largo_mensaje // 100 + 1) * 104:
                bytes_mensaje.extend(socket_cliente.recv(104))
        
        else:
            while len(bytes_mensaje) < (largo_mensaje // 60 + 1) * 64:
                bytes_mensaje.extend(socket_cliente.recv(64))

        return manejar_mensajes(bytes_mensaje, 1)

    def log(self, mensaje_consola):
        """Imprime un mensaje a la consola, sólo si la funcionalidad está activada.

        Argumentos:
            mensaje_consola (str): mensaje a imprimir.
        """
        if self.log_activado:
            print(mensaje_consola)

    def eliminar_cliente(self, id_cliente):
        """Elimina un cliente de clientes_conectados.

        Argumentos:
            id_cliente (int): la id del cliente a eliminar del diccionario.
        """
        with self.clientes_conectados_lock:
            self.log(f"Borrando socket del cliente {id_cliente}.")
            # Obtener socket
            socket_cliente = self.clientes_conectados[id_cliente]
            # Cerrar socket
            socket_cliente.close()
            # Borrar entrada del diccionario
            del self.clientes_conectados[id_cliente]
            # Borrar usuario de los usuarios activos (Logica)
            self.logica.desconectar_usuario(id_cliente)

    def cerrar_servidor(self):
        """
        Ejecuta las acciones necesarias para cerrar el servidor:
         - Desconecta los clientes
         - Cierra su socket
         - Persiste variables en memoria
        """
        self.log("Desconectando clientes...")
        for id_cliente in list(self.clientes_conectados.keys()):
            self.eliminar_cliente(id_cliente)
        self.log("Cerrando socket de recepción...")
        self.socket_servidor.close()
        self.log("Guardando variables en memoria...")

'''
if __name__ == '__main__':
    p = cargar_parametros('parametros.json')
    servidor = Server(p["port"], p["host"])
'''