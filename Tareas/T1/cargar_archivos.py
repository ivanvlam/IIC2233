from parametros import PATH_BARCOS, PATH_CANALES, PATH_MERCANCIA, PATH_TRIPULANTES
from barcos import BarcoDePasajeros, BarcoCarguero, Buque
from tripulantes import DCCapitan, DCCocinero, DCCarguero
from mercancia import Mercancia
from canales import Canal


# Retorna una lista de instancias de tipo DCCapitan, DCCocinero y DCCarguero
# A partir del path señalado en parametros.py
def cargar_tripulantes():

    diccionario_tripulantes = {'DCCapitán': DCCapitan, 'DCCocinero': DCCocinero, \
        'DCCarguero': DCCarguero}
    
    lista_tripulantes = []

    with open(PATH_TRIPULANTES, 'r', encoding = 'UTF-8') as archivo:
        lineas = archivo.readlines()[1:]
    
    for linea in lineas:
        lista = linea.strip().split(',')
        nombre, tipo, agnos_de_experiencia = lista[0], lista[1], lista[2]
        tripulante = diccionario_tripulantes[tipo](nombre, agnos_de_experiencia)

        lista_tripulantes.append(tripulante)
    
    return lista_tripulantes


# Retorna una lista de instancias de tipo Mercancia
# A partir del path señalado en parametros.py
def cargar_mercancia():
    
    lista_mercancia = []

    with open(PATH_MERCANCIA, 'r', encoding = 'UTF-8') as archivo:
        lineas = archivo.readlines()[1:]
    
    for linea in lineas:
        lista = linea.strip().split(',')
        lote, tipo, tiempo_de_expiracion, peso = lista[0], lista[1], lista[2], lista[3]
        mercancia = Mercancia(lote, tipo, tiempo_de_expiracion, peso)

        lista_mercancia.append(mercancia)
    
    return lista_mercancia


# Retorna una lista de instancias de tipo BarcoDePasajeros, BarcoCarguero y Buque
# A partir del path señalado en parametros.py
def cargar_barcos():

    # Para poder almacenar mercancia y tripulacion como una lista de instancias,
    # se llama a las funciones definidas anteriormente 

    lista_tripulantes = cargar_tripulantes()
    lista_mercancia = cargar_mercancia()

    diccionario_barcos = {'Pasajero': BarcoDePasajeros, 'Carguero': BarcoCarguero, \
        'Buque': Buque}
    
    lista_barcos = []

    with open(PATH_BARCOS, 'r', encoding = 'UTF-8') as archivo:
        lineas = archivo.readlines()[1:]
    
    for linea in lineas:
        lista = linea.strip().split(',')
        nombre, tipo, costo_de_mantencion, velocidad_base, pasajeros, carga_maxima, \
        moneda_de_origen, tripulacion, carga = lista[0], lista[1], lista[2], lista[3], \
        lista[4], lista[5], lista[6], lista[7], lista[8]
        
        tripulacion_barco = []
        mercancia_barco = []

        lista_tripulantes_linea = tripulacion.split(';')
        lista_mercancia_linea = carga.split(';')


        # Se buscan las instancias de tripulantes a partir de los nombres almacenados
        # en el archivo barcos.csv
        for tripulante in lista_tripulantes:
            if tripulante.nombre in lista_tripulantes_linea:
                tripulacion_barco.append(tripulante)


        # Se buscan las instancias de mercancia a partir de los números
        # de lote almacenados en el archivo barcos.csv
        for caja in lista_mercancia:
            if str(caja.numero_de_lote) in lista_mercancia_linea:
                mercancia_barco.append(caja)

        # Se instacia el barco con todos sus atributos
        barco = diccionario_barcos[tipo](nombre, costo_de_mantencion, velocidad_base, \
            pasajeros, carga_maxima, moneda_de_origen, tripulacion_barco, mercancia_barco)

        lista_barcos.append(barco)
    
    return lista_barcos


# Retorna una lista de instancias de tipo Canal
# A partir del path señalado en parametros.py
def cargar_canales():
    
    lista_canales = []

    with open(PATH_CANALES, 'r', encoding = 'UTF-8') as archivo:
        lineas = archivo.readlines()[1:]
    
    for linea in lineas:
        lista = linea.strip().split(',')
        nombre, largo, dificultad = lista[0], lista[1], lista[2]
        canal = Canal(nombre, largo, dificultad)

        lista_canales.append(canal)
    
    return lista_canales


# Reinicia los atributos del barco luego de salir del canal
def reiniciar_barco(barco_reiniciar, barcos_disponibles):
    barcos_default = cargar_barcos()
    for barco_default in barcos_default:
        if barco_reiniciar.nombre == barco_default.nombre:
            barco_nuevo = barco_default
    
    for i in range(len(barcos_disponibles)):
        if barcos_disponibles[i].nombre == barco_nuevo.nombre:
            barcos_disponibles[i] = barco_nuevo


# Testeo carga de archivos
if __name__ == '__main__':
    barcos = cargar_barcos()
    canal = cargar_canales()
    canal = canal[0]
    for barco in barcos:
        print(barco, '\n')
    
    print(cargar_canales())
