from collections import defaultdict
from cargar import cargar_platos

# Separar por los platos por categoria
def platos_por_categoria(platos):
    categorias = defaultdict(list)
    for nombre in platos.keys():
        plato = platos[nombre]
        categoria_plato = plato.categoria
        categorias[categoria_plato].append(plato)
    return dict(categorias)


# Retorna los platos que no incluyan los ingredientes descartados
def descartar_platos(ingredientes_descartados, platos):
    platos_descartados = defaultdict(list)
    for nombre in platos.keys():
        plato = platos[nombre]
        ingredientes_plato = plato.ingredientes
        for ingrediente_descartado in ingredientes_descartados:
            if ingrediente_descartado not in ingredientes_plato:
                platos_descartados[ingrediente_descartado].append(plato)
    return platos_descartados


# Recibe un plato, comprueba si hay ingredientes suficientes y los descuenta
def ordenar_plato(plato, ingredientes):
    ingredientes_plato = plato.ingredientes
    for ingrediente in ingredientes_plato:
        print(ingrediente)
        if ingredientes[ingrediente] == 0:
            return False
    for ingrediente in ingredientes_plato:
        ingredientes[ingrediente] -= 1
    return True


# Recibe una lista de platos y retorna el resumen de esa orden
def resumen_orden(lista_platos):
    resumen = {'precio total': 0, \
                'tiempo total': 0, \
                'cantidad de platos': 0, \
                'platos': []}
    for plato in lista_platos:
        resumen['precio total'] += plato.precio
        resumen['tiempo total'] += plato.tiempo_preparacion
        resumen['cantidad de platos'] += 1
        resumen['platos'].append(plato.nombre)
    return resumen


if __name__ == "__main__":
    # ================== PUEDES PROBAR TUS FUNCIONES AQUÍ =====================
    print(" PRUEBA CONSULTAS ".center(80, "="))
    platos = cargar_platos('platos.csv')
    print(platos_por_categoria(platos))
    ingredientes_descartados = {'Salsa tamarindo', 'Lechuga', 'Queso', 'Tomate'}
    print(descartar_platos(ingredientes_descartados, platos))
