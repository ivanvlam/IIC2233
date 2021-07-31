import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from backend.logica_inicio import LogicaInicio, Musica
from frontend.ventana_ranking import VentanaRanking
from backend.logica_ranking import LogicaRanking
from frontend.ventana_preparacion import VentanaPreparacion
from backend.logica_preparacion import LogicaPreparacion
from frontend.ventana_juego import VentanaJuego
from backend.logica_juego import LogicaJuego
from frontend.ventana_postronda import VentanaPostronda
from backend.logica_postronda import LogicaPostronda
from parametros import PATH_CANCION

def hook(type_error, traceback):
    print(type_error)
    print(traceback)
    

if __name__ == '__main__':
    
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    
    ventana_inicio = VentanaInicio()
    logica_inicio = LogicaInicio()

    ventana_inicio.senal_elegir_nombre.connect(logica_inicio.comprobar_nombre)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)

    ventana_inicio.show()
    
    ventana_ranking = VentanaRanking()
    logica_ranking = LogicaRanking()
    
    ventana_preparacion = VentanaPreparacion()
    logica_preparacion = LogicaPreparacion()
    
    ventana_juego = VentanaJuego()
    logica_juego = LogicaJuego()
    
    ventana_postronda = VentanaPostronda()
    logica_postronda = LogicaPostronda()
    
    musica = Musica(PATH_CANCION)
    musica.comenzar()
    
    ventana_inicio.senal_mostrar_ranking.connect(ventana_ranking.mostrar_ventana)
    ventana_ranking.senal_volver_inicio.connect(ventana_inicio.mostrar_ventana)
    
    ventana_inicio.senal_abrir_eleccion_personaje.connect(ventana_preparacion.mostrar_ventana)
    ventana_inicio.senal_abrir_eleccion_personaje.connect(musica.reiniciar)
    
    ventana_preparacion.senal_teclas.connect(logica_preparacion.cambiar_sprite)
    logica_preparacion.senal_sprite_acutal.connect(ventana_preparacion.actualizar_sprite)
    logica_preparacion.senal_vida_trampa.connect(ventana_preparacion.sumar_vida)    
    logica_preparacion.senal_no_entrar.connect(ventana_preparacion.label_no_entrar)
    
    ventana_preparacion.senal_teclas.connect(logica_preparacion.avanzar)
    logica_preparacion.senal_actualizar_posicion.connect(ventana_preparacion.mover_personaje)
    
    logica_preparacion.senal_entrar_mapa.connect(ventana_preparacion.entrar_mapa)
    ventana_preparacion.senal_iniciar_partida.connect(ventana_juego.mostrar_ventana)
    ventana_preparacion.senal_reiniciar_musica.connect(musica.reiniciar)
    
    ventana_ranking.senal_cargar_ranking.connect(logica_ranking.leer_ranking)
    logica_ranking.senal_enviar_ranking.connect(ventana_ranking.mostrar_ranking)
    logica_ranking.senal_sin_ranking.connect(ventana_ranking.no_hay_ranking)
    
    ventana_ranking.senal_elegir_objeto.connect(logica_ranking.elegir_objeto)
    logica_ranking.senal_enviar_objeto.connect(ventana_ranking.cargar_objeto)
    
    ventana_juego.senal_posicion_personaje.connect(logica_juego.posicion_inicial)
    logica_juego.senal_posicion_inicial.connect(ventana_juego.colocar_personaje)
    
    ventana_juego.senal_teclas.connect(logica_juego.cambiar_sprite)
    logica_juego.senal_sprite_acutal.connect(ventana_juego.actualizar_sprite)
    
    ventana_juego.senal_teclas.connect(logica_juego.avanzar)
    logica_juego.senal_actualizar_posicion.connect(ventana_juego.mover_personaje)
    
    ventana_juego.senal_colocar_obstaculos.connect(logica_juego.posicion_obstaculos)
    logica_juego.senal_posicion_obstaculos.connect(ventana_juego.colocar_obstaculos)
    
    ventana_juego.senal_creacion_timers.connect(logica_juego.creacion_timers)
    logica_juego.senal_aparicion_objeto.connect(ventana_juego.pedir_objeto)
    
    ventana_juego.senal_tipo_objeto.connect(logica_juego.elegir_objeto)
    logica_juego.senal_info_objeto.connect(ventana_juego.colocar_objeto)
    logica_juego.senal_objeto_recolectado.connect(ventana_juego.recolectar_objeto)
    logica_juego.senal_cheat_ronda.connect(ventana_juego.terminar_ronda)
    
    logica_juego.senal_tiempo.connect(ventana_juego.actualizar_tiempo)
    logica_juego.senal_labels.connect(ventana_juego.actualizar_labels)
    logica_juego.senal_eliminar_objeto.connect(ventana_juego.eliminar_objeto)
    logica_juego.senal_lisa.connect(ventana_juego.tiempo_saxofones)
    logica_juego.senal_gorgory.connect(ventana_juego.ejecutar_thread)
    
    ventana_juego.senal_pillar_gorgory.connect(logica_juego.comprobar_pillar)
    logica_juego.senal_pillado.connect(ventana_juego.pillado)
    
    ventana_juego.senal_pausar.connect(logica_juego.pausar)
    ventana_juego.senal_pausar.connect(musica.evaluar)
    ventana_juego.senal_terminar_ronda.connect(logica_juego.terminar_ronda)
    ventana_juego.senal_terminar_ronda.connect(logica_postronda.trabajar_datos)
    ventana_juego.senal_terminar_ronda.connect(ventana_postronda.mostrar_ventana)
    ventana_juego.senal_reiniciar_musica.connect(musica.reiniciar)
    
    ventana_postronda.senal_elegir_objeto.connect(logica_postronda.elegir_objeto)
    logica_postronda.senal_enviar_objeto.connect(ventana_postronda.cargar_objeto)
    logica_postronda.senal_datos.connect(ventana_postronda.recibir_datos)
    ventana_postronda.senal_continuar.connect(ventana_preparacion.seguir_jugando)
    ventana_postronda.senal_reinciar_musica.connect(musica.reiniciar)
    
    sys.exit(app.exec_())