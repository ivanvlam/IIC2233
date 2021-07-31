from excepciones_estrellas import RutaPeligrosa


# No modificar esta función
def verificar_condiciones_estrella(estrella):
    if estrella.luminosidad > 15500:
        raise RutaPeligrosa("luz", estrella.nombre)
    elif estrella.magnitud > 4:
        raise RutaPeligrosa("tamaño", estrella.nombre)
    elif estrella.temperatura > 7200:
        raise RutaPeligrosa("calor", estrella.nombre)


# Completar
def generar_ruta_estrellas(estrellas):
    ruta_estrellas = []
    for estrella in estrellas:
        try:
            verificar_condiciones_estrella(estrella)

        except RutaPeligrosa as error:
            error.dar_alerta_peligro()

        else:
            print(f'¡La estrella {estrella.nombre} se ha agregado a tu ruta!'+ u'\x02' + '\n')
            ruta_estrellas.append(estrella.nombre)
    
    return ruta_estrellas

