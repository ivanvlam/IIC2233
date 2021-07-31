from PyQt5.QtWidgets import (
    QLabel, QWidget, QButtonGroup, QRadioButton,
    QProgressBar, QComboBox, QPushButton)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from random import choice

ESTILO_BOTONES = '''
    background-color: white;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: black;
    font: bold 16px;
    min-width: 10em;
    min-height: 25 px;
    padding: 6px;
'''

ESTILO_LABEL = '''
    background-color : rgb(213, 238, 251);
    border-style: solid;
    border-width: 3px;
    border-radius: 20px;
    border-color: balck;
'''

class VentanaEspera(QWidget):

    senal_votar = pyqtSignal(dict)
    senal_iniciar_partida = pyqtSignal(dict)
    senal_juego = pyqtSignal(dict)

    def __init__(self, parametros):
        super().__init__()
        
        self.ancho = 2 * parametros["ancho_ventana"]
        self.alto = parametros["alto_ventana"]
        self.ruta_fondo = parametros["imagenes"]["ruta_fondo"]
        self.ruta_logo = parametros["imagenes"]["ruta_logo"]
        self.imagenes = parametros["imagenes"]
        self.estilo_boton = ESTILO_BOTONES
        
        self.size = (self.ancho, self.alto)
        self.resize(self.ancho, self.alto)
        self.setMaximumHeight(self.alto)
        self.setMaximumWidth(self.ancho)
        
        self.setWindowIcon(QIcon(self.ruta_logo))
        
        self.setMinimumHeight(self.alto)
        self.setMinimumWidth(self.ancho)

        self.setWindowTitle("Sala de espera")
        
        self.host = False
        
        self.init_gui()
        
    def init_gui(self):
        
        self.background = QLabel(self)
        self.background.setMinimumWidth(self.ancho)
        self.background.setMinimumHeight(self.alto)
        self.background.setPixmap(QPixmap(self.ruta_fondo))
        self.background.setScaledContents(True)
        
        self.left_label = QLabel(self)
        self.left_label.setMaximumWidth(self.ancho * 44 / 100)
        self.left_label.setMaximumHeight(self.alto * 70 / 100)
        self.left_label.setMinimumWidth(self.ancho * 44 / 100)
        self.left_label.setMinimumHeight(self.alto * 70 / 100)
        self.left_label.setStyleSheet(ESTILO_LABEL)
        self.left_label.move(self.ancho * 4 / 100, self.alto * 15 / 100)
        
        self.texto_jugadores = QLabel(self)
        self.texto_jugadores.resize(self.alto * 68 / 100, self.alto * 9 / 100)
        self.texto_jugadores.setPixmap(QPixmap(self.imagenes["texto_jugadores"]))
        self.texto_jugadores.setScaledContents(True)
        self.texto_jugadores.move(self.ancho * 5.5 / 100, self.alto * 20 / 100)
        
        self.labels_jugadores = []
        self.labels_listos = []
        posicion = self.alto * 35 / 100
        
        for i in range(4):
            label_jugador = QLabel(f'{i + 1}. Pendiente...', self)
            label_jugador.setFont(QFont('Courier', 15, QFont.Bold))
            label_jugador.move(self.ancho * 8 / 100, posicion)
            
            label_listo = QLabel('PENDIENTE', self)
            label_listo.setFont(QFont('Courier', 15, QFont.Bold))
            label_listo.move(self.ancho * 32 / 100, posicion)
            label_listo.setStyleSheet("color: red")
            
            posicion += self.alto * 10 / 100
            self.labels_jugadores.append(label_jugador)
            self.labels_listos.append(label_listo)
                        
        self.right_label = QLabel(self)
        self.right_label.setMaximumWidth(self.ancho * 44 / 100)
        self.right_label.setMaximumHeight(self.alto * 70 / 100)
        self.right_label.setMinimumWidth(self.ancho * 44 / 100)
        self.right_label.setMinimumHeight(self.alto * 70 / 100)
        self.right_label.setStyleSheet(ESTILO_LABEL)
        self.right_label.move(self.ancho * 52 / 100, self.alto * 15 / 100)
        
        self.texto_votar = QLabel(self)
        self.texto_votar.resize(self.alto * 68 / 100, self.alto * 9 / 100)
        self.texto_votar.setPixmap(QPixmap(self.imagenes["texto_votar"]))
        self.texto_votar.setScaledContents(True)
        self.texto_votar.move(self.ancho * 54 / 100, self.alto * 20 / 100)
        
        self.mapa_ing = QLabel(self)
        self.mapa_ing.resize(self.alto * 29 / 100, self.alto * 21 / 100)
        self.mapa_ing.setPixmap(QPixmap(self.imagenes["mapa_ing"]))
        self.mapa_ing.setScaledContents(True)
        self.mapa_ing.move(self.ancho * 55 / 100, self.alto * 30 / 100)
        self.mapa_ing.setStyleSheet("border: 2px solid black;")
        
        self.label_ing = QLabel('Ingeniería', self)
        self.label_ing.setFont(QFont('Courier', 12, QFont.Bold))
        self.label_ing.move(self.ancho * 74.5 / 100, self.alto * 38 / 100)
        
        self.boton_ing = QRadioButton(self)
        self.boton_ing.move(self.ancho * 79 / 100, self.alto * 42 / 100)
        self.boton_ing.clicked.connect(self.activar_boton)
        
        self.mapa_sj = QLabel(self)
        self.mapa_sj.resize(self.alto * 29 / 100, self.alto * 21 / 100)
        self.mapa_sj.setPixmap(QPixmap(self.imagenes["mapa_sj"]))
        self.mapa_sj.setScaledContents(True)
        self.mapa_sj.move(self.ancho * 55 / 100, self.alto * 56 / 100)
        self.mapa_sj.setStyleSheet("border: 2px solid black;")
        
        self.label_sj = QLabel('San Joaquín', self)
        self.label_sj.setFont(QFont('Courier', 12, QFont.Bold))
        self.label_sj.move(self.ancho * 74 / 100, self.alto * 63 / 100)
        
        self.boton_sj = QRadioButton(self)
        self.boton_sj.move(self.ancho * 79 / 100, self.alto * 67 / 100)
        self.boton_sj.clicked.connect(self.activar_boton)
        
        self.grupo_botones = QButtonGroup()
        self.grupo_botones.addButton(self.boton_ing)
        self.grupo_botones.addButton(self.boton_sj)
        
        self.boton_votar = QPushButton('&Votar', self)
        self.boton_votar.resize(self.boton_votar.sizeHint())
        self.boton_votar.clicked.connect(self.votar)
        self.boton_votar.setFont(QFont('Courier', 12, QFont.Bold))
        self.boton_votar.move(self.ancho * 77.5 / 100, self.alto * 77 / 100)
        self.boton_votar.setStyleSheet(self.estilo_boton)
        self.boton_votar.setDisabled(True)
        
        self.linea = QLabel(self)
        self.linea.resize(2, self.alto * 44 / 100)
        self.linea.move(self.ancho * 87 / 100, self.alto * 31 / 100)
        self.linea.setStyleSheet("background: 2px solid black;")
        
        self.texto_votos = QLabel('VOTOS', self)
        self.texto_votos.setFont(QFont('Courier', 14, QFont.Bold))
        self.texto_votos.move(self.ancho * 88 / 100, self.alto * 30 / 100)
        
        self.votos_ing = QLabel('0', self)
        self.votos_ing.setFont(QFont('Courier', 16, QFont.Bold))
        self.votos_ing.move(self.ancho * 90.5 / 100, self.alto * 39 / 100)
        
        self.votos_sj = QLabel('0', self)
        self.votos_sj.setFont(QFont('Courier', 16, QFont.Bold))
        self.votos_sj.move(self.ancho * 90.5 / 100, self.alto * 64 / 100)

    def activar_boton(self):
        self.boton_votar.setEnabled(True)
    
    def salir(self):
        self.senal_salir.emit()
        self.close()
    
    def actualizar_labels(self, diccionario):
        if diccionario["comando"] == "voto":
            self.votos_ing.setText((str(diccionario["votos_ing"])))
            self.votos_sj.setText((str(diccionario["votos_sj"])))
            
            for i in diccionario["indices"]:
                self.labels_listos[i].setText('  LISTO  ')
                self.labels_listos[i].setStyleSheet("color: green")
            
        elif diccionario["validado"]:
            for i in range(len(diccionario["nombres"])):
                self.labels_jugadores[i].setText(f'{i + 1}. {diccionario["nombres"][i]}')

            for i in diccionario["indices"]:
                self.labels_listos[i].setText('  LISTO  ')
                self.labels_listos[i].setStyleSheet("color: green")
            
            self.votos_ing.setText(str(diccionario["votos_ing"]))
            self.votos_sj.setText(str(diccionario["votos_sj"]))

            if len(diccionario["nombres"]) == 1:
                self.host = True
                self.boton_iniciar = QPushButton('&Iniciar', self)
                self.boton_iniciar.resize(self.boton_iniciar.sizeHint())
                self.boton_iniciar.setFont(QFont('Courier', 12, QFont.Bold))
                self.boton_iniciar.move(self.ancho * 17 / 100, self.alto * 77 / 100)
                self.boton_iniciar.setStyleSheet(self.estilo_boton)
                self.boton_iniciar.setEnabled(False)
                self.boton_iniciar.clicked.connect(self.iniciar_partida)
                
        votos = int(self.votos_ing.text()) + int(self.votos_sj.text())
        func = lambda x: True if 'Pendiente...' not in x.text() else False
        
        lista_numeros = list(filter(func, self.labels_jugadores))
        
        if votos == len(lista_numeros) and self.host and len(lista_numeros) > 1:
            self.boton_iniciar.setEnabled(True)
        
    def seguir_jugando(self, diccionario):
        self.usuario = diccionario['usuario']
        self.vida = diccionario['vida']
        self.puntaje = diccionario['puntaje']
        self.items_buenos = diccionario['items_buenos_total']
        self.items_malos = diccionario['items_malos_total']
        self.ronda = diccionario['ronda']
        
        self.mostrar_ventana(self.usuario)
     
    def votar(self):
        if self.boton_ing.isChecked():
            diccionario = {"comando": "voto", "opcion": "ing"}
        else:
            diccionario = {"comando": "voto", "opcion": "sj"}
        
        self.senal_votar.emit(diccionario)
        
        self.boton_ing.setDisabled(True)
        self.boton_sj.setDisabled(True)
        self.boton_votar.setDisabled(True)
    
    def iniciar_partida(self):
        if int(self.votos_ing.text()) > int(self.votos_sj.text()):
            mapa = "ing"
        elif int(self.votos_ing.text()) < int(self.votos_sj.text()):
            mapa = "sj"
        else:
            mapa = choice(["ing", "sj"])
        self.senal_iniciar_partida.emit({"comando": "iniciar", "mapa": mapa})
    
    def mostrar_ventana(self, diccionario):
        self.actualizar_labels(diccionario)
        self.show()
    
    def cerrar_ventana(self, mensaje):
        self.senal_juego.emit(mensaje)
        self.close()