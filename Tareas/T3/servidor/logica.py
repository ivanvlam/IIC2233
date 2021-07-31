"""
Este módulo contiene la clase Logica
"""
import json
from os import listdir, path
from threading import Lock
from datetime import datetime
from random import choice, shuffle
from copy import copy
from funciones import manejar_mensajes
#from usuario import cargar_usuarios, leer_likes, leer_mensajes


class Logica:
    """
    Clase Logica: Funciona como "backend" del servidor. Posee métodos y atributos que describen
    y ejecutan la lógica del programa.

    Atributos:
        log_activado: bool, indica si se deben mostrar los logs en la consola
        usuarios_activos: diccionario de la forma { id : nombre_usuario }, donde el id corresponde
            al identificador de un cliente conectado, y nombre_usuario al usuario con el cual está
            logeado ese cliente
        diccionario_usuarios: diccionario de la forma { nombre_usuario : instancia_usuario }, que
            contiene y mantiene la información cargada de la base de datos.
    """

    # Evita que dos usuarios entren con el mismo nombre al mismo tiempo.
    ingreso_lock = Lock()
    # Administra el acceso a usuarios_activos para evitar que se produzcan errores.
    usuarios_activos_lock = Lock()

    def __init__(self, log_activado=True):
        self.log_activado = log_activado

        # Crear diccionario de usuarios activos de la forma { id : nombre_usuario }
        self.usuarios_activos = dict()
        self.lista_usuarios = []
        self.votos = {"ing": 0, "sj": 0}
        self.votaron = []
        '''
        # Cargar diccionario de usuarios y likes
        self.diccionario_usuarios = cargar_usuarios("./db/usuarios.json")
        leer_likes("./db/likes.csv", self.diccionario_usuarios)
        leer_mensajes("./db/mensajes.csv", self.diccionario_usuarios)
        '''
    def validar_nombre_usuario(self, nombre_usuario):
        """
        Recibe un nombre de usuario, y revisa si este ya está activo (conectado) o no.
        """
        with self.usuarios_activos_lock:
            # Revisar nombre en los usuarios activos
            if nombre_usuario in self.lista_usuarios:
                return False, 0
            # Revisar nombre en los usuarios registrados
            if len(nombre_usuario) >= 15 or len(nombre_usuario) == 0:
                return False, 1
            
            if len(self.usuarios_activos.values()) == 4:
                return False, 2

            return True, 0

    def desconectar_usuario(self, id_cliente):
        """
        Recibe una id de un cliente desde el servidor y la saca junto a su usuario asociado
        de el diccionario de usuarios activos.
        """
        with self.usuarios_activos_lock:
            try:
                self.lista_usuarios.remove(self.usuarios_activos[id_cliente])
                del self.usuarios_activos[id_cliente]
                self.log(f"Se ha eliminado al cliente {id_cliente} de la lista de usuarios activos")
            except KeyError:
                self.log(f"El cliente {id_cliente} no figura como usuario activo")

    def manejar_mensaje(self, mensaje, id_cliente):
        """
        Maneja un mensaje recibido desde el cliente.
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            self.log(f"ERROR: mensaje de cliente {id_cliente} no cumple el formato.")
            return dict()
        respuesta = dict()
        destinatarios = [key for key in self.usuarios_activos.keys()]
        destinatarios.append(id_cliente)
        if comando == "ingreso":
            nombre_usuario = mensaje["argumentos"]
            with self.ingreso_lock:
                resultado, motivo = self.validar_nombre_usuario(nombre_usuario)
                if resultado:
                    with self.usuarios_activos_lock:
                        self.lista_usuarios.append(nombre_usuario)
                        self.usuarios_activos[id_cliente] = nombre_usuario
                    respuesta = {
                        "comando": "ingreso",
                        "validado": True,
                        "nombre_usuario": nombre_usuario,
                        "nombres": self.lista_usuarios,
                        "motivo": 0,
                        "id_": id_cliente,
                        "votos_ing": self.votos["ing"],
                        "votos_sj": self.votos["sj"],
                        "indices": self.votaron
                    }
                else:
                    respuesta = {
                        "comando": "ingreso",
                        "validado": False,
                        "motivo": motivo
                    }
        
        elif comando == "voto":
            self.votos[mensaje["opcion"]] += 1
            indice = self.lista_usuarios.index(self.usuarios_activos[id_cliente])
            self.votaron.append(indice)
            respuesta = {
                "comando": "voto",
                "votos_ing": self.votos["ing"],
                "votos_sj": self.votos["sj"],
                "indices": self.votaron
            }
        
        elif comando == "iniciar":
            respuesta = {"comando": "iniciar", "mapa": mensaje["mapa"]}
            lista = self.elegir_fotos()
            lista[0]["comando"] = respuesta
            respuesta = lista
        
        return respuesta, destinatarios

    def elegir_fotos(self):
        orden_colores = {i: i + 1 for i in range(len(self.usuarios_activos.keys()))}
        diccionario_enviar = {}
        orden = list(range(int(self.votos['ing'] + int(self.votos['sj']))))
        shuffle(orden)
        orden_jugadores = {self.lista_usuarios[i]: orden[i] for i in range(len(orden))}
        for k, v in self.usuarios_activos.items():
            diccionario_enviar[k] = {
                "orden_colores": orden_colores,
                "orden_jugadores": orden_jugadores,
                "nombre": v
            }

        lista = [file for file in listdir(path.join('.', 'Avatares')) if file.endswith('.png')]
        lista = list(map(lambda x: path.join('Avatares', str(x)), lista))
        lista.append(diccionario_enviar)
        return lista[::-1]
        
    def log(self, mensaje_consola):
        """Imprime un mensaje a la consola, sólo si la funcionalidad está activada.

        Argumentos:
            mensaje_consola (str): mensaje a imprimir.
        """
        if self.log_activado:
            print(mensaje_consola)
