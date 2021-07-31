from funciones import desencriptar, encriptar, log
from random import uniform


def desencriptar_receta(metodo_original):
    """
    Este decorador debe hacer que el método "leer_recetas" retorne las recetas desencriptadas
    """
    def wrapper(*args, **kwargs):
        diccionario_recetas = metodo_original(*args, **kwargs)
        
        for k, v in diccionario_recetas.items():
            lista_ingredientes = []
            
            for ingrediente in v:
                nuevo_ingrediente = desencriptar(ingrediente)
                lista_ingredientes.append(nuevo_ingrediente)

            diccionario_recetas[k] = lista_ingredientes
            
        return diccionario_recetas
    return wrapper


def encriptar_receta(metodo_original):
    """
    Este decorador debe hacer que el método "escribir_recetas" encripte las
    recetas antes de escribirlas
    """
    def wrapper(*args):
        torta = args[1]
        
        for i in range(len(torta)):
            torta[i] = encriptar(torta[i])
        
        return metodo_original(args[0], torta)            

    return wrapper


def ingredientes_infectados(probabilidad_infectado):

    def decorador(metodo_original):
        """
        Este decorador debe hacer que el método "revisar_despensa" elmine los ingredientes
        que pueden estar infectados, según la probabilidad dada.
         """
        def wrapper(*args, **kwargs):
            
            diccionario_ingredientes = metodo_original(*args, **kwargs)
            for k in diccionario_ingredientes.keys():
                
                if diccionario_ingredientes[k] > 0:
                    if uniform(0.0, 1.0) < probabilidad_infectado:
                        log(f'Una unidad de {k} estaba infectada con progravirus!!', 'ingredientes')
                        
                        diccionario_ingredientes[k] -= 1
                        
            return diccionario_ingredientes
        
        return wrapper
    return decorador
