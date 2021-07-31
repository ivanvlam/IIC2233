from PyQt5.QtWidgets import (
    QLabel, QWidget, QButtonGroup, QRadioButton,
    QProgressBar, QComboBox)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
import parametros as p


class VentanaPreparacion(QWidget):

    senal_salir = pyqtSignal()
    senal_teclas = pyqtSignal(dict)
    senal_posicion_personaje = pyqtSignal()
    senal_iniciar_partida = pyqtSignal(dict)
    senal_reiniciar_musica = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.size = (p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.resize(p.VENTANA_ANCHO, p.VENTANA_ALTO)
        self.setMaximumHeight(p.VENTANA_ALTO)
        self.setMaximumWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))
        
        self.setMinimumHeight(p.VENTANA_ALTO)
        self.setMinimumWidth(p.VENTANA_ANCHO)

        self.setWindowTitle("Ventana de Preparación")
        
        self.vida = 1
        self.puntaje = 0
        self.items_buenos = 0
        self.items_malos = 0
        self.items_normales = 0
        self.seguidos = 0
        
        self.vida = 1
        self.puntaje = 0
        self.items_normales = 0
        self.items_buenos = 0
        self.items_malos = 0
        self.items_x2 = 0
        self.tiempo = 1
        self.ronda = 1

        self.init_gui()
        

    def init_gui(self):
        self.label_amarillo = QLabel(self)
        self.label_amarillo.setMaximumWidth(p.VENTANA_ANCHO)
        self.label_amarillo.setMaximumHeight(p.VENTANA_ALTO * 2 / 5)
        self.label_amarillo.setMinimumWidth(p.VENTANA_ANCHO)
        self.label_amarillo.setMinimumHeight(p.VENTANA_ALTO * 2 / 5)
        self.label_amarillo.setStyleSheet("QLabel {background-color : rgb(243, 243, 150)}")
        self.label_amarillo.move(0, 0)
        
        self.top_left = QLabel(self)
        self.top_left.setMaximumWidth(p.VENTANA_ANCHO * 22 / 100)
        self.top_left.setMaximumHeight(p.VENTANA_ALTO * 24 / 100)
        self.top_left.setMinimumWidth(p.VENTANA_ANCHO * 22 / 100)
        self.top_left.setMinimumHeight(p.VENTANA_ALTO * 24 / 100)
        self.top_left.setStyleSheet(p.ESTILO_LABEL_TOP)
        self.top_left.move(p.VENTANA_ANCHO / 100, p.VENTANA_ALTO / 120)
        
        self.top_middle = QLabel(self)
        self.top_middle.setMaximumWidth(p.VENTANA_ANCHO * 45 / 100)
        self.top_middle.setMaximumHeight(p.VENTANA_ALTO * 24 / 100)
        self.top_middle.setMinimumWidth(p.VENTANA_ANCHO * 45 / 100)
        self.top_middle.setMinimumHeight(p.VENTANA_ALTO * 24 / 100)
        self.top_middle.setStyleSheet(p.ESTILO_LABEL_TOP)
        self.top_middle.move(p.VENTANA_ANCHO / 50 + self.top_left.width(), p.VENTANA_ALTO / 120)
        
        self.top_right = QLabel(self)
        self.top_right.setMaximumWidth(p.VENTANA_ANCHO * 29 / 100)
        self.top_right.setMaximumHeight(p.VENTANA_ALTO * 24 / 100)
        self.top_right.setMinimumWidth(p.VENTANA_ANCHO * 29 / 100)
        self.top_right.setMinimumHeight(p.VENTANA_ALTO * 24 / 100)
        self.top_right.setStyleSheet(p.ESTILO_LABEL_TOP)
        self.top_right.move(p.VENTANA_ANCHO / 100 + self.top_middle.width() + self.top_middle.x(), 
            p.VENTANA_ALTO / 120)
        
        self.middle_lable = QLabel(self)
        self.middle_lable.setMaximumWidth(p.VENTANA_ANCHO * 49 / 50)
        self.middle_lable.setMaximumHeight(p.VENTANA_ALTO * 13 / 100)
        self.middle_lable.setMinimumWidth(p.VENTANA_ANCHO * 49 / 50)
        self.middle_lable.setMinimumHeight(p.VENTANA_ALTO * 13 / 100)
        self.middle_lable.setStyleSheet(p.ESTILO_LABEL_TOP)
        self.middle_lable.move(p.VENTANA_ANCHO / 100, p.VENTANA_ALTO / 50 + self.top_left.height())
        
        self.background = QLabel(self)
        self.background.setMaximumWidth(p.VENTANA_ANCHO)
        self.background.setMaximumHeight(p.VENTANA_ALTO * 3 / 5)
        self.background.setMinimumWidth(p.VENTANA_ANCHO)
        self.background.setMinimumHeight(p.VENTANA_ALTO * 3 / 5)
        
        self.background.setPixmap(QPixmap(p.PATH_PREPARACION))
        self.background.setScaledContents(True)
        self.background.move(0, p.VENTANA_ALTO * 2 / 5)

        self.logo = QLabel(self)
        self.logo.resize(p.VENTANA_ALTO * 27 / 100, p.VENTANA_ALTO * 27 / 100 * 541 / 622)

        self.logo.setPixmap(QPixmap(p.PATH_LOGO))
        self.logo.setScaledContents(True)
        self.logo.move(p.VENTANA_ANCHO / 45, p.VENTANA_ALTO / 120)
        
        self.label_seleccion = QLabel('SELECCIONA PERSONAJE:', self)
        self.label_seleccion.setFont(QFont('Courier', 14, QFont.Bold))
        self.label_seleccion.move(self.top_middle.x() + self.top_middle.width() / 7, 
                            p.VENTANA_ALTO / 30)
        
        self.boton_homero = QRadioButton(self, text = 'HOMERO')
        self.boton_homero.setFont(QFont('Courier', 8))
        self.boton_lisa = QRadioButton(self, text = 'LISA')
        self.boton_lisa.setFont(QFont('Courier', 8))
        self.boton_moe = QRadioButton(self, text = 'MOE')
        self.boton_moe.setFont(QFont('Courier', 8))
        self.boton_krusty = QRadioButton(self, text = 'KRUSTY')
        self.boton_krusty.setFont(QFont('Courier', 8))
        
        self.grupo_botones = QButtonGroup()
        self.grupo_botones.addButton(self.boton_homero)
        self.grupo_botones.addButton(self.boton_lisa)
        self.grupo_botones.addButton(self.boton_moe)
        self.grupo_botones.addButton(self.boton_krusty)
        
        self.boton_homero.move(
            self.top_middle.x() + self.top_middle.width() / 20, 
            self.top_middle.height() * 8 / 10
        )
        self.boton_lisa.move(
            self.top_middle.x() + self.top_middle.width() / 20 + self.boton_homero.width() * 1.1, 
            self.top_middle.height() * 8 / 10
        )
        self.boton_moe.move(
            self.top_middle.x() + self.top_middle.width() / 20 + self.boton_homero.width() * 2.1, 
            self.top_middle.height() * 8 / 10
        )
        self.boton_krusty.move(
            self.top_middle.x() + self.top_middle.width() / 20 + self.boton_homero.width() * 2.95, 
            self.top_middle.height() * 8 / 10
        )
        
        self.boton_homero.toggled.connect(self.colocar_personaje)
        self.boton_lisa.toggled.connect(self.colocar_personaje)
        self.boton_moe.toggled.connect(self.colocar_personaje)
        self.boton_krusty.toggled.connect(self.colocar_personaje)
        
        self.label_homero = QLabel(self)
        self.label_homero.resize(p.ANCHO_PERSONAJE * 1.1, p.ALTO_PERSONAJE * 1.1)
        self.label_homero.setPixmap(QPixmap(p.DICCIONARIO_MOVIMIENTOS['homero']['abajo_1']))
        self.label_homero.setScaledContents(True)
        self.label_homero.move(
            self.top_middle.x() + self.top_middle.width() / 9, 
            self.top_middle.height() * 7 / 20
        )
        
        self.label_lisa = QLabel(self)
        self.label_lisa.resize(p.ANCHO_PERSONAJE * 1.1, p.ALTO_PERSONAJE * 1.1)
        self.label_lisa.setPixmap(QPixmap(p.DICCIONARIO_MOVIMIENTOS['lisa']['abajo_1']))
        self.label_lisa.setScaledContents(True)
        self.label_lisa.move(
            self.top_middle.x() + self.top_middle.width() / 10 + self.boton_homero.width() * 1, 
            self.top_middle.height() * 7 / 20
        )
        
        self.label_moe = QLabel(self)
        self.label_moe.resize(p.ANCHO_PERSONAJE * 1.1, p.ALTO_PERSONAJE * 1.1)
        self.label_moe.setPixmap(QPixmap(p.DICCIONARIO_MOVIMIENTOS['moe']['abajo_1']))
        self.label_moe.setScaledContents(True)
        self.label_moe.move(
            self.top_middle.x() + self.top_middle.width() / 10 + self.boton_homero.width() * 2, 
            self.top_middle.height() * 7 / 20
        )
        
        self.label_krusty = QLabel(self)
        self.label_krusty.resize(p.ANCHO_PERSONAJE * 1.1, p.ALTO_PERSONAJE * 1.1)
        self.label_krusty.setPixmap(QPixmap(p.DICCIONARIO_MOVIMIENTOS['krusty']['abajo_1']))
        self.label_krusty.setScaledContents(True)
        self.label_krusty.move(
            self.top_middle.x() + self.top_middle.width() / 10 + self.boton_homero.width() * 2.95, 
            self.top_middle.height() * 7 / 20
        )
        
        self.label_dificultad = QLabel('DIFICULTAD:', self)
        self.label_dificultad.setFont(QFont('Courier', 14, QFont.Bold))
        self.label_dificultad.move(self.top_right.x() + self.top_right.width() / 5, 
                            p.VENTANA_ALTO / 30)
        
        self.box_dificultad = QComboBox(self)
        self.box_dificultad.resize(self.top_right.width() * 3 / 5 , 35)
        self.box_dificultad.addItem('Intro')
        self.box_dificultad.addItem('Avanzada')
        
        self.box_dificultad.setEditable(True)
        line_edit = self.box_dificultad.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.box_dificultad.setFont(QFont('Courier', 10, QFont.Light))
        self.box_dificultad.move(self.top_right.x() + self.top_right.width() / 5, 
                            p.VENTANA_ALTO / 40 + self.label_dificultad.height() * 7 / 4)
        
        self.label_ronda = QLabel('RONDA: 1', self)
        self.label_ronda.setFont(QFont('Courier', 14, QFont.Bold))
        self.label_ronda.move(self.top_right.x() + self.top_right.width() / 4, 
                            p.VENTANA_ALTO / 40 + self.label_dificultad.height() * 4)
        
        self.label_vida = QLabel('VIDA:', self)
        self.label_vida.setFont(QFont('Courier', 16, QFont.Bold))
        self.label_vida.move(p.VENTANA_ANCHO / 25, \
            p.VENTANA_ALTO / 45 + self.top_left.height() + self.middle_lable.height() / 3)
        
        self.barra_vida = QProgressBar(self)
        self.barra_vida.resize(p.VENTANA_ANCHO / 7, p.VENTANA_ALTO * 1 / 25)
        self.barra_vida.move(p.VENTANA_ANCHO / 40 + self.label_vida.width(), \
            p.VENTANA_ALTO / 50 + self.top_left.height() + self.middle_lable.height() / 3)
        self.barra_vida.setAlignment(Qt.AlignCenter)
        self.barra_vida.setFont(QFont('Courier', 12))
        
        self.barra_vida.setValue(70)
        
        self.label_puntaje = QLabel('PUNTAJE: 10000', self)
        self.label_puntaje.setFont(QFont('Courier', 16, QFont.Bold))
        self.label_puntaje.move(p.VENTANA_ANCHO / 25 + 1.85 * self.barra_vida.width(), \
            p.VENTANA_ALTO / 45 + self.top_left.height() + self.middle_lable.height() / 3)
        self.label_puntaje.setMinimumWidth(300)
        
        self.label_items = QLabel('ITEMS RECOLECTADOS', self)
        self.label_items.setFont(QFont('Courier', 16, QFont.Bold))
        self.label_items.move(p.VENTANA_ANCHO / 25 + 4 * self.barra_vida.width(), \
            p.VENTANA_ALTO / 45 + self.top_left.height() + self.middle_lable.height() / 6)
        
        self.label_items_buenos = QLabel('BUENOS: 20', self)
        self.label_items_buenos.setFont(QFont('Courier', 16, QFont.Bold))
        self.label_items_buenos.move(p.VENTANA_ANCHO / 25 + 3.75 * self.barra_vida.width(), \
            p.VENTANA_ALTO / 45 + self.top_left.height() + self.middle_lable.height() / 7 * 4)
        self.label_items_buenos.setMinimumWidth(200)
        
        self.label_items_malos = QLabel('MALOS: 20', self)
        self.label_items_malos.setFont(QFont('Courier', 16, QFont.Bold))
        self.label_items_malos.move(p.VENTANA_ANCHO / 25 + 5.25 * self.barra_vida.width(), \
            p.VENTANA_ALTO / 45 + self.top_left.height() + self.middle_lable.height() / 7 * 4)
        self.label_items_malos.setMinimumWidth(200)

        self.label_no = QLabel('', self)
        self.label_no.setFont(QFont('Courier', 14, QFont.Bold))
        self.label_no.move(p.VENTANA_ANCHO / 50, p.VENTANA_ALTO * 46 / 50)
        self.label_no.setMinimumWidth(300)
        
    def keyPressEvent(self, event):
        self.enviar = True
        if self.personaje != '':
        
            diccionario = {
                'movimientos': self.movimientos,
                'posicion': self.posicion,
                'velocidad': self.velocidad_personaje,
                'personaje': self.personaje,
                'vida': self.vida
            }
            
            if event.key() == Qt.Key_A:
                diccionario['tecla'] = 'A'
            elif event.key() == Qt.Key_D:
                diccionario['tecla'] = 'D'
            elif event.key() == Qt.Key_W:
                diccionario['tecla'] = 'W'
            elif event.key() == Qt.Key_S:
                diccionario['tecla'] = 'S'
            elif event.key() == Qt.Key_V:
                diccionario['tecla'] = 'V'
            elif event.key() == Qt.Key_I:
                diccionario['tecla'] = 'I'
            else:
                self.enviar = False
            
            if self.enviar:
                self.senal_teclas.emit(diccionario)
    
    def actualizar_sprite(self, path):
        self.label_personaje.setPixmap(QPixmap(path))
            
    def mover_personaje(self, posicion):
        self.posicion = posicion
        self.label_personaje.move(*posicion)

    def salir(self):
        self.senal_salir.emit()
        self.close()
    
    def actualizar_labels(self):
        self.barra_vida.setValue(self.vida * 100)
        self.label_puntaje.setText(f'PUNTAJE: {int(self.puntaje)}')
        self.label_items_buenos.setText(f'BUENOS: {self.items_buenos}')
        self.label_items_malos.setText(f'MALOS: {self.items_malos}')
        self.label_ronda.setText(f'RONDA: {self.ronda}')
        
    def seguir_jugando(self, diccionario):
        self.usuario = diccionario['usuario']
        self.vida = diccionario['vida']
        self.puntaje = diccionario['puntaje']
        self.items_buenos = diccionario['items_buenos_total']
        self.items_malos = diccionario['items_malos_total']
        self.ronda = diccionario['ronda']
        
        self.mostrar_ventana(self.usuario)
        
    def colocar_personaje(self):
        self.label_personaje.clear()
        radioBtn = self.sender()
        if radioBtn.isChecked():
            if self.personaje != radioBtn.text().lower():
                
                self.personaje = radioBtn.text().lower()
                self.movimientos = p.DICCIONARIO_MOVIMIENTOS[self.personaje]
                self.label_personaje = QLabel(self)
                self.label_personaje.resize(p.ANCHO_PERSONAJE, p.ALTO_PERSONAJE)
                
                pixeles = QPixmap(self.movimientos['arriba_1'])
                self.label_personaje.setPixmap(pixeles)
                self.label_personaje.setScaledContents(True)


                self.label_personaje.move(
                    (p.VENTANA_ANCHO - self.label_personaje.width()) / 2,
                    p.VENTANA_ALTO - self.label_personaje.height() * 1.1
                )
                self.label_personaje.show()
                self.posicion = (self.label_personaje.x(), self.label_personaje.y())
                self.velocidad_personaje = p.DICCIONARIO_VELOCIDADES[self.personaje]
    
    def label_no_entrar(self, no_entrar):
        if no_entrar:
            self.label_no.setText('NO PUEDES ENTRAR AHÍ')
        else:
            self.label_no.setText('')
    
    def entrar_mapa(self, mapa):
        diccionario = {
            'personaje': self.personaje,
            'usuario': self.usuario,
            'puntaje': self.puntaje,
            'mapa': mapa,
            'dificultad': self.box_dificultad.currentText(),
            'vida': self.vida,
            'items_buenos': self.items_buenos,
            'items_malos': self.items_malos,
            'ronda': self.ronda
        }
        self.senal_iniciar_partida.emit(diccionario)
        self.senal_reiniciar_musica.emit()
        self.label_personaje.clear()
        
        self.grupo_botones.setExclusive(False)
        self.boton_homero.setChecked(False)
        self.boton_lisa.setChecked(False)
        self.boton_moe.setChecked(False)
        self.boton_krusty.setChecked(False)
        self.grupo_botones.setExclusive(True)
        
        self.close()
    
    def sumar_vida(self, valor):
        if valor <= 1:
            self.vida = valor
        else:
            self.vida = 1
        self.barra_vida.setValue(self.vida * 100)
    
    def mostrar_ventana(self, usuario):
        self.usuario = usuario
        self.personaje = ''
        self.label_personaje = QLabel(self)
        
        self.actualizar_labels()
        
        self.show()