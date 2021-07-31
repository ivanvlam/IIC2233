from abc import ABC, abstractmethod
from parametros import TENDENCIA_ENCALLAR_PASAJEROS, TENDENCIA_ENCALLAR_CARGUERO, \
        TENDENCIA_ENCALLAR_BUQUE, PROBABILIDAD_EVENTO_ESPECIAL, CARGA_EXTRA_CARGUERO, \
        TIEMPO_AVERIA_BUQUE, DINERO_INTOXICACION
from currency_converter import CurrencyConverter
from random import random

c = CurrencyConverter()


# Se define la clase abstracta de la cual heredarán 
# los distintos tipos de barco
class Barco(ABC):

    def __init__(self, nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia):
        
        self.nombre = nombre # str
        self.costo_de_mantencion = float(costo_de_mantencion) # float
        self.velocidad_base = int(velocidad_base) # int
        self.pasajeros = int(pasajeros) # int
        self.carga_maxima = int(carga_maxima) # int
        self.moneda_de_origen = moneda_de_origen # str
        self.tripulacion = tripulacion # list
        self.mercancia = mercancia # list
    

    # Se define el peso total como una property
    @property
    def peso(self):
        return sum(caja.peso for caja in self.mercancia)


    # Se define la experiencia total como una property
    @property
    def experiencia(self):
        return sum(tripulante.agnos_de_experiencia for tripulante in self.tripulacion)


    # Se define la habilidad del DCCapitán como una property que retorna un booleano,
    # la ejecución de la habilidad se realiza desde canales.py
    @property
    def habilidad_capitan(self):
        return 'DCCapitan' in (type(tripulante).__name__ for tripulante in self.tripulacion)
    

    # Se define la distancia recorrida en cada hora como property, ya que es variable
    # según la ocurrencia del evento especial "Ataque de piratas"
    @property
    def distancia(self):
        comparador = (self.carga_maxima - self.peso - 0.3 * self.pasajeros) / self.carga_maxima
        distancia = max(0.1, min(1, comparador)) * self.velocidad_base
        return distancia


    # Se define la ejecución de habilidades del DCCocinero y DCCarguero como
    # un método no abstracto, ya que es igual para todos los tipos de barco
    def ejecutar_habilidades(self):
        if 'DCCocinero' in (type(tripulante).__name__ for tripulante in self.tripulacion):
            for caja in self.mercancia:
                if caja.tipo == 'alimentos':
                    caja.tiempo_expiracion = 2 * caja.tiempo_expiracion
        
        if 'DCCarguero' in (type(tripulante).__name__ for tripulante in self.tripulacion):
            self.carga_maxima += CARGA_EXTRA_CARGUERO


    # Se definen los métodos abstractos desplazarse, encallar y ejecutar_evento_especial,
    # debido a que existen diferencias entre los métodos de los distintos tipos de barco
    @abstractmethod
    def desplazarse(self):
        pass

    @abstractmethod
    def encallar(self, canal):
        pass

    @abstractmethod
    def ejecutar_evento_especial(self, canal):
        pass
    

    # Se define el __repr__ para poder probar la creación de instancias
    # al ejecutar el test en cargar_archivos.py
    def __repr__(self):
        return f'Tipo({type(self).__name__}), Nombre({self.nombre}),' \
            + f' Costo({self.costo_de_mantencion}), Velocidad({self.velocidad_base}),' \
            + f' Pasajeros({self.pasajeros}), Carga Máxima({self.carga_maxima}),' \
            + f' Moneda({self.moneda_de_origen}), Tripulación({self.tripulacion}),' \
            + f' Mercancía({self.mercancia})'


class BarcoDePasajeros(Barco):
    
    def __init__(self, nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia):
        super().__init__(nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia)
        self.desplazamiento = 0
        self.salida = True
        self.evento_disponible = True
        
        # Se ejecutan las habilidades de los tripulantes, es decir, los alimentos
        # tienen el doble de tiempo y aumenta la carga máxima
        self.ejecutar_habilidades()


    def desplazarse(self):
        self.desplazamiento += self.distancia

    def probabilidad(self, canal):
        comparador = (self.velocidad_base + self.peso - self.experiencia) / 120
        return max(0, min(1, comparador) * TENDENCIA_ENCALLAR_PASAJEROS * canal.ponderador)

    def encallar(self, canal):
        return random() < self.probabilidad(canal)

    def ejecutar_evento_especial(self, canal):
        if self.evento_disponible:
            if random() < PROBABILIDAD_EVENTO_ESPECIAL and self.salida:

                # Se convierte el dinero a USD y se retorna para que se haga el
                # descuento al dinero del canal en canales.py
                dinero = c.convert(DINERO_INTOXICACION, self.moneda_de_origen, 'USD')
                print(f'Las personas del barco de pasajeros {self.nombre} se han intoxicado, ' \
                    f'por lo que el barco tendrá que pagarle ${round(dinero, 2)} al canal')
                self.evento_disponible = False
                return dinero


class BarcoCarguero(Barco):

    def __init__(self, nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia):
        super().__init__(nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia)
        self.desplazamiento = 0
        self.salida = True
        self.evento_disponible = True

        # Se ejecutan las habilidades de los tripulantes, es decir, los alimentos
        # tienen el doble de tiempo y aumenta la carga máxima
        self.ejecutar_habilidades()

    def desplazarse(self):
        self.desplazamiento += self.distancia

    def probabilidad(self, canal):
        comparador = (self.velocidad_base + self.peso - self.experiencia) / 120
        return max(0, min(1, comparador) * TENDENCIA_ENCALLAR_CARGUERO * canal.ponderador)

    def encallar(self, canal):
        return random() < self.probabilidad(canal)

    def ejecutar_evento_especial(self, canal):
        if self.evento_disponible:
            if random() < PROBABILIDAD_EVENTO_ESPECIAL and self.salida:

                # Se le quita la mercancía por el robo de los piratas y
                # el atributo salida se vuelve False para indicar que no puede 
                # pagar la tarifa de salida del canal
                self.mercancia = []
                self.salida = False
                print(f'El barco carguero {self.nombre} ha sido atacado por piratas y no ' \
                    'podrá pagar la tarifa de salida del canal :(')
                self.evento_disponible = False
                return True


class Buque(Barco):
    
    def __init__(self, nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia):
        super().__init__(nombre, costo_de_mantencion, velocidad_base, pasajeros, \
            carga_maxima, moneda_de_origen, tripulacion, mercancia)
        self.desplazamiento = 0
        self.horas_detencion = 0
        self.salida = True
        self.evento_disponible = True

        # Se ejecutan las habilidades de los tripulantes, es decir, los alimentos
        # tienen el doble de tiempo y aumenta la carga máxima
        self.ejecutar_habilidades()


    # Solo aumenta el desplazamiento si el barco no está detenido
    def desplazarse(self):
        if self.horas_detencion == 0:
            self.desplazamiento += self.distancia

    def probabilidad(self, canal):
        comparador = (self.velocidad_base + self.peso - self.experiencia) / 120
        return max(0, min(1, comparador) * TENDENCIA_ENCALLAR_BUQUE * canal.ponderador)

    def encallar(self, canal):
        return random() < self.probabilidad(canal)

    def ejecutar_evento_especial(self, canal):
        if self.evento_disponible:
            if self.horas_detencion == 0:
                if random() < PROBABILIDAD_EVENTO_ESPECIAL:
                    self.horas_detencion = TIEMPO_AVERIA_BUQUE
                    print(f'El buque {self.nombre} ha quedado detenido y estará en ' \
                        f'condiciones de continuar en {self.horas_detencion} horas.')
                    self.evento_disponible = False
                    return True

        else:
            if self.horas_detencion > 0:
                self.horas_detencion -= 1
                print(f'Al buque {self.nombre} le quedan {self.horas_detencion} horas detenido.')
            return False

if __name__ == '__main__':
    pass