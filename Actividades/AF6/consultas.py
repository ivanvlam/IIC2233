from functools import reduce
from cargar import cargar_comidas, cargar_mascotas
from copy import copy
from parametros import RUTA_ANIMALES, RUTA_COMIDAS, TAMANOS


def obtener_comidas():
    '''
    Retorna una lista con todos los nombres de las comidas
    '''
    comidas = cargar_comidas(RUTA_COMIDAS)
    mapeo = map(lambda x: x.nombre, comidas)
    return list(mapeo)


def agrupar_por_tamano(tamanos):
    '''
    Recibe los un diccionario con los tamaños desde parametros.py
    Retorna una lista de listas con las instancias de mascota agrupadas
    '''
    mascotas = list(cargar_mascotas(RUTA_ANIMALES))
    
    pequenos = tamanos['PEQUENO']
    medianos = tamanos['MEDIANO']
    grandes = tamanos['GRANDE']
    
    lista = [
        list(filter(lambda x: x.estatura > pequenos[0] and x.estatura <= pequenos[1], copy(mascotas))),
        list(filter(lambda x: x.estatura > medianos[0] and x.estatura <= medianos[1], copy(mascotas))),
        list(filter(lambda x: x.estatura > grandes[0] and x.estatura <= grandes[1], mascotas))
    ]
    
    return lista


def precio_total(especie):
    '''
    Recibe una especie
    Retorna precio total mascotas + comidas
    '''
    mascotas = cargar_mascotas(RUTA_ANIMALES)
    comidas = cargar_comidas(RUTA_COMIDAS)

    mascotas_filtradas = filter(lambda x: x.especie == especie, mascotas)
    comida_filtrada = filter(lambda x: x.especie == especie, comidas)
    
    precio_mascotas = map(lambda x: x.precio, mascotas_filtradas)
    precio_comida = map(lambda x: x.precio, comida_filtrada)
    
    precio_mascotas_final = reduce(lambda x, y: x + y, precio_mascotas, 0)
    precio_comida_final = reduce(lambda x, y: x + y, precio_comida, 0)
    
    return precio_mascotas_final + precio_comida_final
    

def comida_ideal(raza, especie):
    '''
    FUNCION GENERADORA
    Recibe una raza y una especie
    Retorna instancias de comida
    '''
    comidas = cargar_comidas(RUTA_COMIDAS)
    for comida in comidas:
        if comida.especie == especie and comida.raza == raza:
            yield comida


def precio_comidas(raza, especie):
    '''
    Debes usar la funcion generadora comida_ideal
    Retorna el precio total de las comidas ideales
    '''
    generador_comida = comida_ideal(raza, especie)
    precio_comida = map(lambda x: x.precio, generador_comida)
    return reduce(lambda x, y: x + y, precio_comida, 0)
    


if __name__ == '__main__':
    print(obtener_comidas())
    
    contador = 0
    lista_animales = list(map(lambda x: x.nombre, list(cargar_mascotas(RUTA_ANIMALES))))
    for lista in agrupar_por_tamano(TAMANOS):
        for mascota in lista:
            contador += 1
            if mascota.nombre not in lista_animales:
                print(mascota.nombre)
    
    for mascota in list(cargar_mascotas(RUTA_ANIMALES)):
        if mascota.estatura > 90:
            print(mascota.nombre)
            
    print(precio_total('perro'))
    
    for comida in comida_ideal('Poodle', 'perro'):
        print(comida.nombre)
        
    print(precio_comidas('Poodle', 'perro'))
    
    for lista in agrupar_por_tamano(TAMANOS):
        print(lista, len(lista))