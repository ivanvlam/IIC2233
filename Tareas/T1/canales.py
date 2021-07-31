from parametros import COBRO_USO_PRINCIPIANTE, COBRO_USO_AVANZADO, DINERO_INICIAL, \
    PONDERADOR_PRINCIPIANTE, PONDERADOR_AVANZADO, PROB_BASE_DESENCALLAR, COSTO_DESENCALLAR
from random import random
from collections import defaultdict, deque
from currency_converter import CurrencyConverter

c = CurrencyConverter()


# Se define la clase Canal
class Canal:

    # Diccionario de propiedades como atributo de clase
    dicc_properties = {'principiante': (PONDERADOR_PRINCIPIANTE, COBRO_USO_PRINCIPIANTE), \
                        'avanzado': (PONDERADOR_AVANZADO, COBRO_USO_AVANZADO)}

    def __init__(self, nombre, largo, dificultad):
        
        self.nombre = nombre # str
        self.largo = int(largo) # int
        self.dificultad = dificultad # str
        self.__dinero_actual = DINERO_INICIAL
        self.dinero_recibido = 0
        self.dinero_gastado = 0
        self.dinero_recibido_hora = 0
        self.dinero_gastado_hora = 0
        self.eventos_especiales_ocurridos = 0
        self.dicc_barcos_encallaron = defaultdict(int)
        self.total_encallamientos = 0
        self.barcos_que_pasaron = 0
        self.barcos = deque() # list
        self.encallados = [] # list
        self.kilometro_encallados = []
        self.desencallados = defaultdict(int)

    # Se define dinero_actual como una property que no puede ser menor que 0
    @property
    def dinero_actual(self):
        return self.__dinero_actual
    
    @dinero_actual.setter
    def dinero_actual(self, valor):
        if valor < 0:
            self.__dinero_actual = 0
        else:
            self.__dinero_actual = valor

    # Se define ponderador_dificultad y cobro_de_uso como properties
    @property
    def ponderador(self):
        return Canal.dicc_properties[self.dificultad][0]

    @property
    def cobro_de_uso(self):
        return Canal.dicc_properties[self.dificultad][1]
    
    # Ingresa un barco a la lista de barcos del canal
    def ingresar_barco(self, barco):
        if barco not in self.barcos:
            self.barcos.appendleft(barco)


    # Simula todo el avance de los barcos, incluyendo encallamiento
    # y eventos especiales, además considera expiración de la mercancía
    def avanzar_barcos(self):
        barcos_remover = []
        self.dinero_recibido_hora = 0
        self.dinero_gastado_hora = 0
        for barco in self.barcos:
            if barco not in self.encallados:
                
                # Comprueba si el barco es un Buque y está detenido,
                # si es así, no puede encallar, por lo que no se comprueba
                if type(barco).__name__ == 'Buque' and barco.horas_detencion > 0:
                    barco.ejecutar_evento_especial(self)
                    
                else:
                    if barco.encallar(self):
                        # La lista de kilometro_encallados permite detener el avance
                        # de los barcos que se encuentren detrás en el canal
                        self.kilometro_encallados.append(barco.desplazamiento)
                        self.encallados.append(barco)
                        self.dicc_barcos_encallaron[barco.nombre] = 1
                        self.total_encallamientos += 1

                        # Aquí se comprueba la property de habilidad_capitan que permite un
                        # desencallamiento gratis e inmediato, el diccionario desencallados
                        # permite que esto ocurra solo la primera vez que se encalla
                        if self.desencallados[barco.nombre] == 0 and barco.habilidad_capitan:
                            self.encallados.pop(self.encallados.index(barco))
                            self.kilometro_encallados.remove(barco.desplazamiento)
                            self.desencallados[barco.nombre] += 1
                            print(f'{barco.nombre} ha quedado encallado pero se ha desencallado' \
                                ' instantáneamente gracias a las habilidades de su DCCapitán!')
                        
                        else:
                            print(f'{barco.nombre} ha quedado encallado!')

                    else:
                        evento = barco.ejecutar_evento_especial(self)
                        # Si lo que retorna el método ejecutar_evento_especial es un float
                        # entonces obligatoriamente se trata de la intoxicación de pasajeros,
                        # por lo que se realiza el pago al canal
                        if isinstance(evento, float):
                            self.dinero_recibido_hora += evento
                            self.dinero_actual += evento
                            self.eventos_especiales_ocurridos += 1
                        
                        # Si lo anterior no se cumple, ocurren  los eventos especiales del
                        # BarcoDePasajeros o de Buque, los cuales se ejecutan dentro de ellos
                        elif evento:
                            self.eventos_especiales_ocurridos += 1

        for barco in self.barcos:
            avanzar = True
            if barco not in self.encallados:
                if barco.desplazamiento < self.largo:
                    posicion_actual = barco.desplazamiento
                    for kilometro in self.kilometro_encallados:
                        
                        # Se comprueba si hay un barco encallado más adelante
                        if posicion_actual < kilometro:
                            avanzar = False
                    
                if avanzar:
                    # El Buque debe cumplir dos condiciones para avanzar, no debe estar
                    # encallado ni con una avería, por lo que se realiza esta comprobación
                    if type(barco).__name__ != 'Buque':
                        continuar = True
                    elif barco.horas_detencion == 0:
                        continuar = True
                    else:
                        continuar =  False
                    
                    if continuar:
                        
                        # El desplazamiento del barco ocurre por parte de la propia instancia
                        barco.desplazarse()

                        print(f'{barco.nombre} se ha desplazado ' \
                            f'{round(barco.distancia, 2)} km')
                        
                        if barco.desplazamiento > self.largo:
                            
                            barco.desplazamiento = 0

                            self.desencallados[barco.nombre] = 0

                            if barco.salida:
                                self.barcos_que_pasaron += 1

                                # Si el barco sale del canala, debe ser removido de la
                                # lista de barcos para que pueda ser reintegrado en el futuro
                                barcos_remover.append(barco)

                                self.dinero_actual += self.cobro_de_uso
                                self.dinero_recibido_hora += self.cobro_de_uso
                                print(f'{barco.nombre} ha salido del canal y ha pagado ' \
                                    f'la tarifa de salida de ${self.cobro_de_uso}.')

                            else:
                                # Solo se ejecuta si el barco sufrió un ataque de piratas
                                print(f'{barco.nombre} ha salido del canal sin pagar ' \
                                    'la tarifa de salida debido al ataque de piratas recibido!')
                                self.barcos_que_pasaron += 1
                                barcos_remover.append(barco)

                else:
                    print(f'{barco.nombre} no puede avanzar porque hay un barco ' \
                        'encallado más adelante.')

            else:
                 print(f'{barco.nombre} no puede avanzar porque sigue encallado')

        for barco in barcos_remover:
            self.barcos.remove(barco)

        # Resta 1 a cada mercancía de cada barco y avisa si expira
        # Además, se realiza el camnio de moneda para cobrarle al canal
        # el costo de mantención de cada barco
        for barco in self.barcos:
            for caja in barco.mercancia:
                caja.tiempo_expiracion = caja.tiempo_expiracion - 1
                if caja.tiempo_expiracion == 0:
                    dinero = caja.expirar()
                    self.dinero_gastado_hora += dinero
                    self.dinero_actual -= dinero
                    print(f'La mercancía número {caja.numero_de_lote} de tipo {caja.tipo} ' \
                        f'del barco {barco.nombre} ha expirado. ' \
                        f'El canal ha pagado ${round(dinero, 2)} por eso.')

            dinero = c.convert(barco.costo_de_mantencion, barco.moneda_de_origen, 'USD')
            self.dinero_actual -= dinero
            self.dinero_gastado_hora += dinero
            print(f'{barco.nombre} ha recibido ${round(dinero, 2)} ' \
                'en costos de mantención.')

        self.dinero_recibido += self.dinero_recibido_hora
        self.dinero_gastado += self.dinero_gastado_hora

        # Imprime el resumen de cada hora
        print(f'\n{str(" Resumen de la hora "):-^51s}\n')
        print(f'{self.nombre} | {self.largo} KM | Dificultad {self.dificultad}.' \
            f'\nDinero gastado: ${round(self.dinero_gastado_hora, 2)}' \
            f'\nDinero recibido: ${round(self.dinero_recibido_hora, 2)}' \
            f'\nDinero total: ${round(self.dinero_actual, 2)}')
        
        print(f'\n\n {str("-" * 32 + " Barcos en el canal " + 32 * "-"): ^60s}\n')

        # Se ordenan los barcos para mostrarlos en pantalla según el lugar
        # en el que se encuentran en el canal
        barcos_ordenados = sorted(self.barcos, key = por_posicion, reverse = True)

        for barco in barcos_ordenados:
            espacios_anteriores = int(barco.desplazamiento * 75 / self.largo)
            espacios_posteriores = 70 - espacios_anteriores - len(barco.nombre)
            espacios_posteriores -= len(str(round(barco.desplazamiento, 2)))
            if barco in self.encallados:
                print(f'{str(" ") * espacios_anteriores} {(len(barco.nombre) + 2) * "_"}\n' \
                    f'{str("~") * espacios_anteriores}/ {barco.nombre} \\~ ' \
                    f'({round(barco.desplazamiento, 2)}/{round(self.largo, 2)} KM) '
                    f'{str("~") * espacios_posteriores}\n' \
                    f'{str(" ") * espacios_anteriores}{(len(barco.nombre) + 4) * "-"}')
            else:
                print(f'{str(" ") * espacios_anteriores}{(len(barco.nombre) + 4) * "_"}\n' \
                    f'{str("~") * espacios_anteriores}\\ {barco.nombre} /~ ' \
                    f'({round(barco.desplazamiento, 2)}/{round(self.largo, 2)} KM) '
                    f'{str("~") * espacios_posteriores}\n' \
                    f'{str(" ") * espacios_anteriores} {(len(barco.nombre) + 2) * "-"}')
        
        return barcos_remover


    # Retorna un booleano y un número, siendo este último el motivo por el
    # cual el barco no pudo ser desencallado (dinero o probabilidades)
    def desencallar_barco(self, barco):

        if self.dinero_actual < COSTO_DESENCALLAR:
            return False, 0

        elif random() < (PROB_BASE_DESENCALLAR * self.ponderador):
            self.dinero_actual -= COSTO_DESENCALLAR
            self.dinero_gastado += COSTO_DESENCALLAR
            self.encallados.pop(self.encallados.index(barco))
            self.kilometro_encallados.remove(barco.desplazamiento)
            self.desencallados[barco.nombre] += 1
            return True, 1
        
        self.dinero_actual -= COSTO_DESENCALLAR
        self.dinero_gastado += COSTO_DESENCALLAR
        return False, 1

    def __repr__(self):
        return f'[Nombre({self.nombre}), Largo({self.largo}), Dificultad({self.dificultad})' \
            + f' Barcos({self.barcos}), Cobro({self.cobro_de_uso})]'


def por_posicion(barco):
    return barco.desplazamiento