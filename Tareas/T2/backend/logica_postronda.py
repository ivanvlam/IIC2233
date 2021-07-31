from PyQt5.QtCore import pyqtSignal, QObject
import parametros as p
from random import choice


class LogicaPostronda(QObject):

    senal_enviar_ranking = pyqtSignal(list)
    senal_enviar_objeto = pyqtSignal(str)
    senal_datos = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        
        self.playing = False

    def trabajar_datos(self, diccionario):
        self.usuario = diccionario['usuario']
        self.puntaje = diccionario['puntaje']
        self.vida = diccionario['vida']
        self.items_normales = diccionario['items_normales']
        self.items_buenos = diccionario['items_buenos']
        self.items_x2 = diccionario['items_x2']
        self.items_malos = diccionario['items_malos']
        self.items_buenos_acumulados = diccionario['items_buenos_total']
        self.items_malos_acumulados = diccionario['items_malos_total']
        self.ronda = diccionario['ronda']
        self.pillado_gorgory = diccionario['pillado']
        
        puntaje_ronda = self.calcular_puntaje(self.vida, self.items_normales, self.items_x2)

        self.puntaje += puntaje_ronda
        
        self.senal_datos.emit({
            'usuario': self.usuario,
            'vida': self.vida,
            'items_normales': self.items_normales,
            'items_buenos': self.items_buenos,
            'items_malos': self.items_malos,
            'items_x2': self.items_x2,
            'puntaje': int(self.puntaje),
            'puntaje_ronda': puntaje_ronda,
            'items_malos_total': self.items_malos_acumulados,
            'items_buenos_total': self.items_buenos_acumulados,
            'ronda': self.ronda + 1,
            'pillado': self.pillado_gorgory
        })
        
        self.escribir_ranking()
        self.playing = True
        
    def calcular_puntaje(self, vida, normales, buenos):
        puntaje_normales = normales * p.PUNTOS_OBJETO_NORMAL
        puntaje_x2 = buenos * p.PUNTOS_OBJETO_NORMAL * 2
        
        return (puntaje_normales + puntaje_x2) * vida
    
    def escribir_ranking(self):
        try:
            with open(p.PATH_RANKING, 'r') as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            with open(p.PATH_RANKING, 'w') as archivo:
                archivo.write(f'{self.usuario},{int(self.puntaje)}')
        else:
            lista_puntajes = []
            if self.playing:
                lineas = lineas[:-1]
                
            for linea in lineas:
                lista_puntajes.append(linea.strip())
                
            with open(p.PATH_RANKING, 'w') as archivo:
                for linea in lista_puntajes:
                    print(linea, file = archivo)
                print(f'{self.usuario},{int(self.puntaje)}', file = archivo)

    def elegir_objeto(self):
        key = choice(list(p.DICCIONARIO_OBJETOS.keys()))
        
        if '_x2' in key:
            key = key[:-3]
            
        path = p.DICCIONARIO_OBJETOS[key]
        
        self.senal_enviar_objeto.emit(path)
            