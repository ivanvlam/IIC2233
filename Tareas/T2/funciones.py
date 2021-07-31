import parametros as p

def comprobar_colisiones(movimiento, lista, posicion_x, posicion_y, velocidad):
    if movimiento == 'A':
        for obstaculo in lista:
            
            condicion_1 = abs(obstaculo.x() + obstaculo.width() - posicion_x) < velocidad
            condicion_2 = posicion_y + p.ALTO_PERSONAJE > obstaculo.y()
            condicion_3 = posicion_y + p.ALTO_PERSONAJE < obstaculo.y() + obstaculo.height()
            condicion_4 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 < \
                obstaculo.y() + obstaculo.height()
            condicion_5 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 > obstaculo.y()
            
            if condicion_1 and ((condicion_2 and condicion_3) or (condicion_4 and condicion_5)):
                return (obstaculo.x() + obstaculo.width(), posicion_y)
        if posicion_x - velocidad < 0:
            return (0, posicion_y)
        
        return (posicion_x - velocidad, posicion_y)

    elif movimiento == 'D':
        for obstaculo in lista:
            
            condicion_1 = abs(posicion_x + p.ANCHO_PERSONAJE - obstaculo.x()) < velocidad
            condicion_2 = posicion_y + p.ALTO_PERSONAJE > obstaculo.y()
            condicion_3 = posicion_y + p.ALTO_PERSONAJE < obstaculo.y() + obstaculo.height()
            condicion_4 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 < \
                obstaculo.y() + obstaculo.height()
            condicion_5 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 > obstaculo.y()
                
            if condicion_1 and ((condicion_2 and condicion_3) or (condicion_4 and condicion_5)):
                return (obstaculo.x() - p.ANCHO_PERSONAJE, posicion_y)
        if posicion_x + velocidad + p.ANCHO_PERSONAJE > p.VENTANA_ANCHO:
            return (p.VENTANA_ANCHO - p.ANCHO_PERSONAJE, posicion_y)
        
        return (posicion_x + velocidad, posicion_y)

    elif movimiento == 'S':
        for obstaculo in lista:
            
            condicion_1 = abs(posicion_y + p.ALTO_PERSONAJE - obstaculo.y()) < velocidad
            condicion_2 = posicion_x + p.ANCHO_PERSONAJE > obstaculo.x()
            condicion_3 = posicion_x + p.ANCHO_PERSONAJE < obstaculo.x() + obstaculo.width()
            condicion_4 = posicion_x > obstaculo.x()
            condicion_5 = posicion_x < obstaculo.x() + obstaculo.width()
            
            if condicion_1 and ((condicion_2 and condicion_3) or (condicion_4 and condicion_5)):
                return (posicion_x, obstaculo.y() - p.ALTO_PERSONAJE)
        if posicion_y + velocidad + p.ALTO_PERSONAJE > p.VENTANA_ALTO:
            return (posicion_x, p.VENTANA_ALTO - p.ALTO_PERSONAJE * 1.1)
        
        return (posicion_x, posicion_y + velocidad)

    else:
        for obstaculo in lista:
            '''
            print(
                'obstaculo.x', obstaculo.x(),
                '\nobstaculo.y', obstaculo.y(),
                '\nobstaculo.width', obstaculo.width(),
                '\nposicion.x', posicion_x,
                '\nposicion.y', posicion_y,
                '\nobstaculo.height', p.ALTO_BALDOSA,
                '\n'
            )
            '''
            
            condicion_1 = abs(posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA - \
                obstaculo.y() - obstaculo.height()) < velocidad
            condicion_2 = posicion_x + p.ANCHO_PERSONAJE > obstaculo.x()
            condicion_3 = posicion_x + p.ANCHO_PERSONAJE < obstaculo.x() + obstaculo.width()
            condicion_4 = posicion_x > obstaculo.x()
            condicion_5 = posicion_x < obstaculo.x() + obstaculo.width()
            
            if condicion_1 and ((condicion_2 and condicion_3) or (condicion_4 and condicion_5)):
                return (
                    posicion_x,
                    obstaculo.y() + obstaculo.height() + p.ALTO_BALDOSA - p.ALTO_PERSONAJE
                )
        if posicion_y - velocidad < p.ALTO_MURALLA * 0.95:
            return (posicion_x, p.ALTO_MURALLA * 0.95)
        
        return (posicion_x, posicion_y - velocidad)

def comprobar_objetos(posicion_x, posicion_y, lista):
    lista_indices = []
    lista_objetos = []
    for i, elemento in enumerate(lista):
        condicion_1 = posicion_x < elemento.x() + elemento.width()
        condicion_2 = posicion_x > elemento.x()
        condicion_3 = posicion_x + p.ANCHO_PERSONAJE < elemento.x() + elemento.width()
        condicion_4 =  posicion_x + p.ANCHO_PERSONAJE > elemento.x()
        condicion_5 = posicion_y + p.ALTO_PERSONAJE / 2 > elemento.y()
        condicion_6 = posicion_y + p.ALTO_PERSONAJE / 2 < elemento.y() + elemento.height()
        condicion_7 = posicion_y + p.ALTO_PERSONAJE > elemento.y()
        condicion_8 = posicion_y + p.ALTO_PERSONAJE < elemento.y() + elemento.height()
        condicion_9 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 < \
            elemento.y() + elemento.height()
        condicion_0 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 > elemento.y()
        
        condicion_h = (condicion_1 and condicion_2) or (condicion_3 and condicion_4)
        condicion_v = (condicion_5 and condicion_6) or (condicion_7 and condicion_8) or \
            (condicion_9 and condicion_0)
        
        if condicion_h and condicion_v:
            lista_indices.append(i)
            lista_objetos.append(elemento)
    
    return lista_indices, lista_objetos

def colision_gorgory(posicion, elemento):
    
    posicion_x, posicion_y = posicion[0],posicion[1]

    condicion_1 = posicion_x < elemento.x() + elemento.width()
    condicion_2 = posicion_x > elemento.x()
    condicion_3 = posicion_x + p.ANCHO_PERSONAJE < elemento.x() + elemento.width()
    condicion_4 =  posicion_x + p.ANCHO_PERSONAJE > elemento.x()
    condicion_5 = posicion_y + p.ALTO_PERSONAJE / 2 > elemento.y()
    condicion_6 = posicion_y + p.ALTO_PERSONAJE / 2 < elemento.y() + elemento.height()
    condicion_7 = posicion_y + p.ALTO_PERSONAJE > elemento.y()
    condicion_8 = posicion_y + p.ALTO_PERSONAJE < elemento.y() + elemento.height()
    condicion_9 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 < \
        elemento.y() + elemento.height()
    condicion_0 = posicion_y + p.ALTO_PERSONAJE - p.ALTO_BALDOSA * 0.9 > elemento.y()
    
    condicion_h = (condicion_1 and condicion_2) or (condicion_3 and condicion_4)
    condicion_v = (condicion_5 and condicion_6) or (condicion_7 and condicion_8) or \
        (condicion_9 and condicion_0)
    
    if condicion_h and condicion_v:
        return True
    return False