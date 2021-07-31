from decoradores_cocina import ingredientes_infectados
from funciones import encontrar_preferencia, log


# Debes completar este archivo

def improvisar_toppings(metodo_original):
    """
    Este decorador se encarga de escoger un topping nuevo en caso de que no quede del
    que pide el método original
    """
    def wrapper(*args):
        chef, nombre_ingrediente, torta = args
        
        if chef.ingredientes_disponibles[nombre_ingrediente] > 0:   
            ingrediente_nuevo = nombre_ingrediente
        
        else:
            ingrediente_nuevo = encontrar_preferencia(nombre_ingrediente)
            log(f'No queda {nombre_ingrediente}, se reemplazará con {ingrediente_nuevo}', \
                'ingredientes')
            
            return wrapper(chef, ingrediente_nuevo, torta)
        
        return metodo_original(chef, ingrediente_nuevo, torta)
        
    return wrapper


def capa_relleno(tipo_relleno):
    def decorador(metodo_original):
        """
        Este decorador chequea que quede del relleno pedido, si los hay, lo agrega,
        si no, termina la torta
        """
        def wrapper(*args):
            
            chef, nombre_ingrediente, torta = args
        
            if chef.relleno_restante > 0:   
                chef.relleno_restante -= 1
                log(f"Agregando relleno de {tipo_relleno}.", 'relleno')
                torta.append(tipo_relleno)
                return metodo_original(*args)
            
            else:
                torta.finalizada = True
                log(f"No queda suficiente relleno de {tipo_relleno}. " \
                    "Se procederá a terminar la torta.", 'relleno')
                  
        return wrapper

    return decorador


def revisar_ingredientes(metodo_original):
    """
    Este decorador revisa que hayan suficientes ingredientes antes de empezar una torta.
    En caso contrario, debe levantar una excepción del tipo ValueError
    """
    def wrapper(*args):
        chef, nombre_torta, lista_ingredientes = args
        
        numero_ingredientes_torta = len(lista_ingredientes)
        numero_total_ingredientes = sum(chef.ingredientes_disponibles.values())
        
        if numero_total_ingredientes >= numero_ingredientes_torta:
            return(metodo_original(*args))
        
        else:
            log('¡No hay suficientes ingredientes para cocinar la torta!', 'ingredientes')
            raise ValueError()
        
    return wrapper
