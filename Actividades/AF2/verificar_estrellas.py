from cargar_datos import cargar_estrellas, cargar_nombres_estrellas_cercanas


def verificar_alias_estrella(estrella):
    letras = estrella.alias[:2]

    if not letras.isalpha():
        raise ValueError('El alias de la estrella es incorrecto.', 0)
    
    elif 'F' in letras:
        raise ValueError('El alias de la estrella es incorrecto.', 1)


def corregir_alias_estrella(estrella):
    try:
        verificar_alias_estrella(estrella)

    except ValueError as error:
        print(f'Error: {error.args[0]}')

        estrella.alias = estrella.alias.replace('F', 'T')

        if error.args[1] == 0:
            letras = estrella.alias[:2]
            numeros = estrella.alias[2:]
            estrella.alias = numeros + letras

        print(f'El alias de {estrella.nombre} fue correctamente corregido.\n')


def verificar_distancia_estrella(estrella):
    if estrella.distancia < 0:
        raise ValueError('Distancia negativa.')


def corregir_distancia_estrella(estrella):
    try:
        verificar_distancia_estrella(estrella)

    except ValueError as error:
        print(f'Error: {error}')

        estrella.distancia *= -1

        print(f'La distancia de la estrella {estrella.nombre} fue corregida.\n')


def verificar_magnitud_estrella(estrella):
    if not isinstance(estrella.magnitud, float):
        raise TypeError('Magnitud no es del tipo correcto.')


def corregir_magnitud_estrella(estrella):
    try:
        verificar_magnitud_estrella(estrella)
        
    except TypeError as error:
        print(f'Error: {error}')

        if ';' in estrella.magnitud:
            estrella.magnitud = estrella.magnitud.replace(';', '.')
        
        estrella.magnitud = float(estrella.magnitud)

        print(f'La magnitud de la estrella {estrella.nombre} fue corregida.\n')


def dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas):
    try:
        alias_estrella = diccionario_estrellas[nombre_estrella].alias

    except KeyError:
        print(f'Estrella {nombre_estrella} NO está en nuestra base de datos.' \
            '\n¡Alerta, puede ser una trampa de algún extraterrestre!')
    
    else:
        print(f'Estrella {nombre_estrella} está en nuestra base de datos.', \
            f'Su alias es {alias_estrella}.')



if __name__ == "__main__":
    diccionario_estrellas = cargar_estrellas("estrellas.csv")
    nombres_estrellas = cargar_nombres_estrellas_cercanas("estrellas_cercanas.txt")

    # Descomenta las funciones que quieras probar de la actividad
    print("Revisando posibles errores en las estrellas...\n")
    for estrella in diccionario_estrellas.values():
        corregir_alias_estrella(estrella)
        corregir_distancia_estrella(estrella)
        corregir_magnitud_estrella(estrella)
        pass

    print("Revisando estrellas inexistentes...\n")
    for nombre_estrella in nombres_estrellas:
        dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas)
        pass
