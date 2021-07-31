from collections import namedtuple

Plato = namedtuple('Plato', \
        ['nombre', 'categoria', \
        'tiempo_preparacion', \
        'precio', 'ingredientes'])

def cargar_platos(ruta_archivo):
    platos = dict()
    with open(ruta_archivo, 'rt') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        lista_datos = linea.strip().split(',')
        ingredientes = set()
        for i in range(4, len(lista_datos)):
            ingredientes.add(lista_datos[i])
        caracteristicas = Plato(lista_datos[0], \
                    lista_datos[1], \
                    int(lista_datos[2]), \
                    int(lista_datos[3]), \
                    ingredientes)
        platos[lista_datos[0]] = caracteristicas
    return platos


def cargar_ingredientes(ruta_archivo):
    ingredientes = dict()
    with open(ruta_archivo, 'rt') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        lista_datos = linea.strip().split(',')
        ingredientes[lista_datos[0]] = int(lista_datos[1])
    return ingredientes


if __name__ == "__main__":
    # ================== PUEDES PROBAR TUS FUNCIONES AQUÍ =====================
    print(" PRUEBA CARGAR ".center(80, "="))
    print(cargar_platos('platos.csv'))
    print(cargar_ingredientes('ingredientes.csv'))
    platos = cargar_platos('platos.csv')
    for nombre in platos.keys():
        plato = platos[nombre]
        print(plato.categoria)