from parametros import MULTA_PETROLEO, MULTA_ROPA, MULTA_ALIMENTOS

class Mercancia:

    # Atributo de clase porque es común a todas las mercancías
    tipo_multa = {'petróleo': MULTA_PETROLEO, 'ropa': MULTA_ROPA, 'alimentos': MULTA_ALIMENTOS}

    def __init__(self, numero_de_lote, tipo, tiempo_expiracion, peso):
        self.numero_de_lote = int(numero_de_lote) # int
        self.tipo = tipo # str
        self.tiempo_expiracion = int(tiempo_expiracion) # int Si es < 0 se considera EXPIRADO
        self.peso = int(peso) # int

    # Retorna el dinero de la multa
    def expirar(self):
        return Mercancia.tipo_multa[self.tipo]
    
    def __repr__(self):
        return f'[Número({self.numero_de_lote}), Tipo({self.tipo}),' \
            + f' Tiempo({self.tiempo_expiracion}), Peso({self.peso})]'
