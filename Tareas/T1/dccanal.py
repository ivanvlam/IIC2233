from cargar_archivos import cargar_barcos, cargar_canales, reiniciar_barco
from parametros import COSTO_DESENCALLAR, COMANDO_VOLVER, COMANDO_SALIR

class DCCanal:

    def __init__(self):
        self.barcos_disponibles = []
        self.horas_simuladas = 0


    def menu_inicio(self):
        print(f'\n{str(" Menú de inicio "):-^51s}\n')
        print('Bienvenido a DCCanal! :)\nPara comenzar, por favor seleccione una opción:\n')
        print(f'[1] Comenzar nueva simulación\n[{COMANDO_SALIR}] Salir del programa\n')

        opcion = input('Ingrese su opción: ')
        opciones = [COMANDO_SALIR, '1']

        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            return self.menu_inicio()
        else:
            if opcion == '1':
                return self.menu_seleccionar_canal()
            else:
                return False


    def menu_seleccionar_canal(self):
        print(f'\n{str(" Seleccionar canal "):-^51s}\n')
        canales_totales = cargar_canales()
        opciones = [COMANDO_VOLVER, COMANDO_SALIR]
        for i in range(len(canales_totales)):
            canal = canales_totales[i]
            print(f'[{i + 1}]', canal.nombre)
            opciones.append(str(i + 1))
        
        print(f'\n[{COMANDO_VOLVER}] Volver\n[{COMANDO_SALIR}] Salir\n')

        opcion = input('Ingrese su opción: ')
        
        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            return self.menu_seleccionar_canal()
        else:
            if opcion == COMANDO_VOLVER:
                return self.menu_inicio()
            
            elif opcion == COMANDO_SALIR:
                return False

            else:
                # Cada vez que se vuelve al menú de seleccionar canal
                # se reinicia la simulación
                self.barcos_disponibles = cargar_barcos()
                self.horas_simuladas = 0
                self.canal = canales_totales[int(opcion) - 1]
                return self.menu_acciones()

        
    def menu_acciones(self):
        print(f'\n{str(" Menú de acciones "):-^51s}\n')
        opciones = [COMANDO_VOLVER, COMANDO_SALIR, '1', '2', '3', '4']

        print('[1] Mostrar riesgo de encallamiento\n[2] Desencallar barco\n' \
            '[3] Simular nueva hora\n[4] Mostrar estado simulación')
        
        print(F'\n[{COMANDO_VOLVER}] Volver\n[{COMANDO_SALIR}] Salir\n')

        opcion = input('Ingrese su opción: ')
        
        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            return self.menu_acciones()
        else:
            if opcion == COMANDO_VOLVER:
                return self.menu_seleccionar_canal()
            elif opcion == COMANDO_SALIR:
                return False

            elif opcion == '1':
                return self.mostrar_riesgo_encallamiento()
            elif opcion == '2':
                self.menu_desencallar_barco()
            elif opcion == '3':
                return self.iniciar_simulacion()
            else:
                return self.mostrar_estado_simulacion()


    def mostrar_riesgo_encallamiento(self):
        opciones = [COMANDO_VOLVER, COMANDO_SALIR]
        print(f'\n{str(" Riesgo de encallamiento "):-^55s}\n')

        print(f'{str("BARCO"): ^27s}|{str("PROBABILIDAD"): ^27s}' \
            + '\n' + '-' * 27 + '|' + 27 * '-')
        for barco in self.canal.barcos:
                print(f'{barco.nombre: ^27s}|{barco.probabilidad(self.canal): ^27.2f}')
        print(F'\n[{COMANDO_VOLVER}] Volver\n[{COMANDO_SALIR}] Salir\n')
        opcion = input('Ingrese su opción: ')
        
        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            return self.mostrar_riesgo_encallamiento()
        else:
            if opcion == COMANDO_VOLVER:
                return self.menu_acciones()
            else:
                return False
        
    def menu_desencallar_barco(self):
        opciones = [COMANDO_VOLVER, COMANDO_SALIR]
        if len(self.canal.encallados) == 0:
            print('\nActualmente no hay barcos encallados :)')
        else:
            print(f'\n{str(" Desencallar barco "):-^51s}\n')
            opciones = [COMANDO_VOLVER]
            for i in range(len(self.canal.encallados)):
                barco = self.canal.encallados[i]
                print(f'[{i + 1}]', barco.nombre)
                opciones.append(str(i + 1))

        print(F'\n[{COMANDO_VOLVER}] Volver\n[{COMANDO_SALIR}] Salir\n')

        opcion = input('Selecciona una opción: ')
        print('')

        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            self.menu_desencallar_barco()
        else:
            if opcion == COMANDO_VOLVER:
                return self.menu_acciones()
            elif opcion == COMANDO_SALIR:
                return False
            else:
                barco = self.canal.encallados[int(opcion) - 1]
                desencallado, motivo = self.canal.desencallar_barco(barco)

                if desencallado:
                    print(f'{barco.nombre} ha sido desencallado ' \
                        f'con éxito. El canal ha pagado ${COSTO_DESENCALLAR}.')
                else:
                    if motivo == 0:
                        print(f'{barco.nombre} no ha podido ser desencallado ' \
                            f'debido a que el canal no cuenta con ${COSTO_DESENCALLAR}.')
                    else:
                        print(f'El canal pagó ${COSTO_DESENCALLAR} pero {barco.nombre} ' \
                            'no ha podido ser desencallado.')
                    
                print('\nRegresando al menú de acciones...')
                return self.menu_acciones()


    def iniciar_simulacion(self):
        opciones = [COMANDO_VOLVER, COMANDO_SALIR, '00']

        # Solo permite ingresar barcos si no hay ninguno encallado
        if len(self.canal.encallados) == 0:
            print(f'\n{str(" Ingresar barco "):-^64s}\n')
            contador = 0
            for i in range(len(self.barcos_disponibles)):
                barco = self.barcos_disponibles[i]
                if barco not in self.canal.barcos:
                    contador += 1
                    texto = f'[{i + 1}]{barco.nombre: ^27s}|'
                    if i < 9:
                        texto = ' ' + texto
                    if contador % 2 == 1:
                        print(texto, end = '')
                    else:
                        print(texto[:-1])
        
                    opciones.append(str(i + 1))

            print(f'[00]{str("Ninguno"): ^27s}')
        
        else:
            print('\nEl canal se encuentra bloqueado, por lo que no pueden entrar nuevos ' \
                'barcos.\n\n[00] Continuar con la simulación')
        
        print(F'\n[{COMANDO_VOLVER}] Volver\n[{COMANDO_SALIR}] Salir\n')

        opcion = input('Ingrese su opción: ')
        
        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            return self.iniciar_simulacion()
        else:
            if opcion == COMANDO_VOLVER:
                return self.menu_acciones()
            
            elif opcion == COMANDO_SALIR:
                return False

            elif opcion != '00':
                barco = self.barcos_disponibles[int(opcion) - 1]
                self.canal.ingresar_barco(barco)

        
        print('\nIniciando simulación...\n')
        barcos_removidos = self.canal.avanzar_barcos()

        # Reinicio de atributos de barcos luego de salir del canal
        for barco_removido in barcos_removidos:
            reiniciar_barco(barco_removido, self.barcos_disponibles)

        self.horas_simuladas += 1

        # Cierre espontáneo del programa al quedarse sin dinero
        if self.canal.dinero_actual == 0:
            print('\nEl canal se ha quedado sin fondos, por lo que ha quebrado :(\n')
            return False
        else:
            return self.menu_acciones()


    def mostrar_estado_simulacion(self):
        opciones = [COMANDO_VOLVER, COMANDO_SALIR]

        # Impresión del gran resumen
        print(f'\n{str( "Estado del canal "):-^70s}\n')
        print(f'{self.canal.nombre} de {self.canal.largo} km de largo, con dificultad ' \
            f'{self.canal.dificultad}.' \
            f'\nHoras simuladas: {self.horas_simuladas}' \
            f'\nDinero gastado: ${round(self.canal.dinero_gastado, 2)}' \
            f'\nDinero recibido: ${round(self.canal.dinero_recibido, 2)}' \
            f'\nDinero total: ${round(self.canal.dinero_actual, 2)}' \
            f'\nNúmero de barcos en el canal: {len(self.canal.barcos)}' \
            '\nNúmero de barcos que han encallado: ' \
                f'{sum(self.canal.dicc_barcos_encallaron.values())}' \
            f'\nNúmero total de encallamientos: {self.canal.total_encallamientos}' \
            f'\nNúmero de barcos que han cruzado: {self.canal.barcos_que_pasaron}' \
            '\nNúmero de eventos especiales ocurridos: ' \
                f'{self.canal.eventos_especiales_ocurridos}')
        
        
        print(F'\n[{COMANDO_VOLVER}] Volver\n[{COMANDO_SALIR}] Salir\n')

        opcion = input('Ingrese su opción: ')
        
        try:
            verificar_input(opcion, opciones)
        except ValueError as error:
            print(error)
            return self.mostrar_estado_simulacion()
        else:
            if opcion == COMANDO_VOLVER:
                return self.menu_acciones()
            else:
                return False

        
        print('\nIniciando simulación...\n')
        self.canal.avanzar_barcos()
        self.horas_simuladas += 1

        # Cierre espontáneo del programa al quedarse sin dinero
        if self.canal.dinero_actual == 0:
            print('\nEl canal se ha quedado sin fondos, por lo que ha quebrado :(\n')
            return False
        else:
            return self.menu_acciones()


# Todo el manejo de errores de input se realiza mediante esta función
def verificar_input(texto, opciones):
    if texto not in opciones:
        raise ValueError('\nLa opción seleccionada no se encuentra en las disponibles.\n'\
            'Por favor intentarlo nuevamente. Recargando página...')


if __name__ == '__main__':
    dccanal = DCCanal()
    dccanal.menu_inicio()