from os.path import join
RUTA_LOGO = join("frontend", "assets", "logo.jpg")

# Archivos
PATH_RANKING = 'ranking.txt'
PATH_LOGO = join('sprites', 'Logo.png')
PATH_BACKGROUND = join('imagenes', 'Background.jpg')
PATH_RANKING_TITLE = join('imagenes', 'Ranking_text.png')
PATH_RONDA_TITLE = join('imagenes', 'Resumen_text.png')
PATH_CANCION = join('canciones', 'musica.wav')

# Ventana
VENTANA_ANCHO = 960
VENTANA_ALTO = 720
LOGO_ALTO = 541
LOGO_ANCHO = 622

ALTO_MURALLA = VENTANA_ALTO / 6 + VENTANA_ALTO / 6 * 5 * (1 - 0.7178)
ALTO_BALDOSA = VENTANA_ALTO * 5 * 0.7116 / 48
ANCHO_BALDOSA = VENTANA_ANCHO / 12

# Preparación
PATH_PREPARACION = join('sprites', 'Mapa', 'Mapa_Preparación', 'MapaCompleto.png')
PRIMER_LIMITE = VENTANA_ANCHO * 800 / 2846
SEGUNDO_LIMITE = VENTANA_ANCHO * 1790 / 2846
TERCER_LIMITE = VENTANA_ANCHO * 2325 / 2846
ALTURA_CALLE = (((1 - (566 / 1600)) * 3 / 5) + 2 / 5) * VENTANA_ALTO

# Homero
VELOCIDAD_HOMERO = 5 # int
PONDERADOR_VIDA_HOMERO = None # float

# Lisa
VELOCIDAD_LISA = 13 # int
PONDERADOR_TIEMPO_LISA = 5 # int

# Otros personajes
VELOCIDAD_MOE = 6 #int
VELOCIDAD_KRUSTY = 10 #int

DICCIONARIO_VELOCIDADES = {
    'homero': VELOCIDAD_HOMERO,
    'lisa': VELOCIDAD_LISA,
    'moe': VELOCIDAD_MOE,
    'krusty': VELOCIDAD_KRUSTY
}

# Objetos
APARICION_INTRO = 2 # int
TIEMPO_OBJETO_INTRO = 5 # int
APARICION_AVANZADA = 3 # int
TIEMPO_OBJETO_AVANZADA = 5 # int

PUNTOS_OBJETO_NORMAL = 50 #int
PROB_NORMAL = 0.8 #float

PROB_BUENO = 0.1 #float
PONDERADOR_CORAZON = 0.1 #int

PROB_VENENO = 0.1 #float
PONDERADOR_VENENO = 0.2 #float

TIEMPO_DELAY_INTRO = 5 #int
TIEMPO_DELAY_AVANZADA = 3 #int
VIDA_TRAMPA = 0.1 #float

DURACION_INTRO = 45
DURACION_AVANZADA = 60

DICCIONARIO_DIFICULTADES = {
    'intro': {
        'aparicion': APARICION_INTRO,
        'duracion': TIEMPO_OBJETO_INTRO,
        'delay': TIEMPO_DELAY_INTRO,
        'tiempo_ronda': DURACION_INTRO
    },
    
    'avanzada': {
        'aparicion': APARICION_AVANZADA,
        'duracion': TIEMPO_OBJETO_AVANZADA,
        'delay': TIEMPO_DELAY_AVANZADA,
        'tiempo_ronda': DURACION_AVANZADA
    }
}

MAPA_BAR = {
    'path': join('sprites', 'Mapa', 'Bar', 'Mapa.png'),
    'obstaculos': [
        join('sprites', 'Mapa', 'Bar', 'Obstaculo1.png'),
        join('sprites', 'Mapa', 'Bar', 'Obstaculo2.png'),
        join('sprites', 'Mapa', 'Bar', 'Obstaculo3.png'),
    ]
}

MAPA_KRUSTY = {
    'path': join('sprites', 'Mapa', 'Krustyland', 'Mapa.png'),
    'obstaculos': [
        join('sprites', 'Mapa', 'Krustyland', 'Obstaculo1.png'),
        join('sprites', 'Mapa', 'Krustyland', 'Obstaculo2.png'),
        join('sprites', 'Mapa', 'Krustyland', 'Obstaculo3.png'),
    ]
}

MAPA_PLANTA = {
    'path': join('sprites', 'Mapa', 'Planta_nuclear', 'Mapa.png'),
    'obstaculos': [
        join('sprites', 'Mapa', 'Planta_nuclear', 'Obstaculo1.png'),
        join('sprites', 'Mapa', 'Planta_nuclear', 'Obstaculo2.png'),
        join('sprites', 'Mapa', 'Planta_nuclear', 'Obstaculo3.png'),
    ]
}

MAPA_PRIMARIA = {
    'path': join('sprites', 'Mapa', 'Primaria', 'Mapa.png'),
    'obstaculos': [
        join('sprites', 'Mapa', 'Primaria', 'Obstaculo1.png'),
        join('sprites', 'Mapa', 'Primaria', 'Obstaculo2.png'),
        join('sprites', 'Mapa', 'Primaria', 'Obstaculo3.png'),
    ]
}

DICCIONARIO_MAPAS = {
    'Bar': MAPA_BAR,
    'Krustyland': MAPA_KRUSTY,
    'Planta_nuclear': MAPA_PLANTA,
    'Primaria': MAPA_PRIMARIA
}

# Estilos
ESTILO_BOTONES_NORMALES = '''
    background-color: white;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: pink;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
'''

ESTILO_BOTONES_CHICOS = '''
    background-color: white;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: pink;
    font: bold 14px;
    min-width: 6em;
    padding: 6px;
'''

ESTILO_LABEL_TOP = '''
    background-color : rgb(147, 222, 244);
    border-style: solid;
    border-width: 3px;
    border-radius: 20px;
    border-color: rgb(27, 91, 191);
'''

ESTILO_LABEL_CONTINUAR = '''
    background-color : rgb(165, 251, 180);
    border-style: solid;
    border-width: 3px;
    border-radius: 10px;
    border-color: rgb(60, 250, 1);
'''

ESTILO_LABEL_FIN = '''
    background-color : rgb(250, 133, 120);
    border-style: solid;
    border-width: 3px;
    border-radius: 10px;
    border-color: rgb(215, 19, 1);
'''

# Objetos
DICCIONARIO_OBJETOS = {
    'cerveza': join('sprites', 'Objetos', 'Cerveza.png'),
    'cerveza_x2': join('sprites', 'Objetos', 'CervezaX2.png'),
    'corazon': join('sprites', 'Objetos', 'Corazon.png'),
    'dona': join('sprites', 'Objetos', 'Dona.png'),
    'dona_x2': join('sprites', 'Objetos', 'DonaX2.png'),
    'krusty': join('sprites', 'Objetos', 'Krusty.png'),
    'krusty_x2': join('sprites', 'Objetos', 'KrustyX2.png'),
    'saxofon': join('sprites', 'Objetos', 'Saxofon.png'),
    'saxofon_x2': join('sprites', 'Objetos', 'SaxofonX2.png'),
    'veneno': join('sprites', 'Objetos', 'Veneno.png')
}

OBJETOS_HOMERO = {
    'normales': ['dona'],
    'buenos': ['dona_x2', 'corazon']
}

OBJETOS_LISA = {
    'normales': ['saxofon'],
    'buenos': ['saxofon_x2', 'corazon']
}

OBJETOS_MOE = {
    'normales': ['cerveza'],
    'buenos': ['cerveza_x2', 'corazon']
}

OBJETOS_KRUSTY = {
    'normales': ['krusty'],
    'buenos': ['krusty_x2', 'corazon']
}

OBJETOS_PERSONAJES = {
    'homero': OBJETOS_HOMERO,
    'lisa': OBJETOS_LISA,
    'moe': OBJETOS_MOE,
    'krusty': OBJETOS_KRUSTY
}

# Movimientos personajes
ALTO_PERSONAJE = VENTANA_ALTO / 11
ANCHO_PERSONAJE = ALTO_PERSONAJE * 166 / 271

MOVIMIENTOS_GORGORY = {
    'abajo_1': join('sprites', 'Personajes', 'Gorgory', 'down_3.png'),
    'abajo_2': join('sprites', 'Personajes', 'Gorgory', 'down_2.png'),
    'abajo_3': join('sprites', 'Personajes', 'Gorgory', 'down_1.png'),
    'izquierda_1': join('sprites', 'Personajes', 'Gorgory', 'left_1.png'),
    'izquierda_2': join('sprites', 'Personajes', 'Gorgory', 'left_2.png'),
    'izquierda_3': join('sprites', 'Personajes', 'Gorgory', 'left_3.png'),
    'derecha_1': join('sprites', 'Personajes', 'Gorgory', 'right_1.png'),
    'derecha_2': join('sprites', 'Personajes', 'Gorgory', 'right_2.png'),
    'derecha_3': join('sprites', 'Personajes', 'Gorgory', 'right_3.png'),
    'arriba_1': join('sprites', 'Personajes', 'Gorgory', 'up_1.png'),
    'arriba_2': join('sprites', 'Personajes', 'Gorgory', 'up_2.png'),
    'arriba_3': join('sprites', 'Personajes', 'Gorgory', 'up_3.png')
}

MOVIMIENTOS_HOMERO = {
    'abajo_1': join('sprites', 'Personajes', 'Homero', 'down_3.png'),
    'abajo_2': join('sprites', 'Personajes', 'Homero', 'down_2.png'),
    'abajo_3': join('sprites', 'Personajes', 'Homero', 'down_1.png'),
    'izquierda_1': join('sprites', 'Personajes', 'Homero', 'left_1.png'),
    'izquierda_2': join('sprites', 'Personajes', 'Homero', 'left_2.png'),
    'izquierda_3': join('sprites', 'Personajes', 'Homero', 'left_3.png'),
    'derecha_1': join('sprites', 'Personajes', 'Homero', 'right_1.png'),
    'derecha_2': join('sprites', 'Personajes', 'Homero', 'right_2.png'),
    'derecha_3': join('sprites', 'Personajes', 'Homero', 'right_3.png'),
    'arriba_1': join('sprites', 'Personajes', 'Homero', 'up_3.png'),
    'arriba_2': join('sprites', 'Personajes', 'Homero', 'up_2.png'),
    'arriba_3': join('sprites', 'Personajes', 'Homero', 'up_1.png')
}

MOVIMIENTOS_KRUSTY = {
    'abajo_1': join('sprites', 'Personajes', 'Krusty', 'down_1.png'),
    'abajo_2': join('sprites', 'Personajes', 'Krusty', 'down_2.png'),
    'abajo_3': join('sprites', 'Personajes', 'Krusty', 'down_3.png'),
    'izquierda_1': join('sprites', 'Personajes', 'Krusty', 'left_1.png'),
    'izquierda_2': join('sprites', 'Personajes', 'Krusty', 'left_2.png'),
    'izquierda_3': join('sprites', 'Personajes', 'Krusty', 'left_3.png'),
    'derecha_1': join('sprites', 'Personajes', 'Krusty', 'right_1.png'),
    'derecha_2': join('sprites', 'Personajes', 'Krusty', 'right_2.png'),
    'derecha_3': join('sprites', 'Personajes', 'Krusty', 'right_3.png'),
    'arriba_1': join('sprites', 'Personajes', 'Krusty', 'up_1.png'),
    'arriba_2': join('sprites', 'Personajes', 'Krusty', 'up_2.png'),
    'arriba_3': join('sprites', 'Personajes', 'Krusty', 'up_3.png')
}

MOVIMIENTOS_LISA = {
    'abajo_1': join('sprites', 'Personajes', 'Lisa', 'down_1.png'),
    'abajo_2': join('sprites', 'Personajes', 'Lisa', 'down_2.png'),
    'abajo_3': join('sprites', 'Personajes', 'Lisa', 'down_3.png'),
    'izquierda_1': join('sprites', 'Personajes', 'Lisa', 'left_1.png'),
    'izquierda_2': join('sprites', 'Personajes', 'Lisa', 'left_2.png'),
    'izquierda_3': join('sprites', 'Personajes', 'Lisa', 'left_3.png'),
    'derecha_1': join('sprites', 'Personajes', 'Lisa', 'right_1.png'),
    'derecha_2': join('sprites', 'Personajes', 'Lisa', 'right_2.png'),
    'derecha_3': join('sprites', 'Personajes', 'Lisa', 'right_3.png'),
    'arriba_1': join('sprites', 'Personajes', 'Lisa', 'up_1.png'),
    'arriba_2': join('sprites', 'Personajes', 'Lisa', 'up_2.png'),
    'arriba_3': join('sprites', 'Personajes', 'Lisa', 'up_3.png')
}

MOVIMIENTOS_MOE = {
    'abajo_1': join('sprites', 'Personajes', 'Moe', 'down_1.png'),
    'abajo_2': join('sprites', 'Personajes', 'Moe', 'down_2.png'),
    'abajo_3': join('sprites', 'Personajes', 'Moe', 'down_3.png'),
    'izquierda_1': join('sprites', 'Personajes', 'Moe', 'left_1.png'),
    'izquierda_2': join('sprites', 'Personajes', 'Moe', 'left_2.png'),
    'izquierda_3': join('sprites', 'Personajes', 'Moe', 'left_3.png'),
    'derecha_1': join('sprites', 'Personajes', 'Moe', 'right_1.png'),
    'derecha_2': join('sprites', 'Personajes', 'Moe', 'right_2.png'),
    'derecha_3': join('sprites', 'Personajes', 'Moe', 'right_3.png'),
    'arriba_1': join('sprites', 'Personajes', 'Moe', 'up_3.png'),
    'arriba_2': join('sprites', 'Personajes', 'Moe', 'up_2.png'),
    'arriba_3': join('sprites', 'Personajes', 'Moe', 'up_1.png')
}

DICCIONARIO_MOVIMIENTOS = {
    'gorgory': MOVIMIENTOS_GORGORY,
    'homero': MOVIMIENTOS_HOMERO,
    'krusty': MOVIMIENTOS_KRUSTY,
    'lisa': MOVIMIENTOS_LISA,
    'moe': MOVIMIENTOS_MOE
}


