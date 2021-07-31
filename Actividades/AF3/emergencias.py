from time import sleep
from threading import Thread
from random import randint
from companias import CompaniaServicio
from parametros import RECURSOS_MAX


# Completar
class Emergencia(Thread):

    companias = {"agua": CompaniaServicio("agua", RECURSOS_MAX),
                 "banditas": CompaniaServicio("banditas", RECURSOS_MAX),
                 "donas": CompaniaServicio("donas", RECURSOS_MAX)}

    def __init__(self, aviso, numero_catastrofe) -> None:
        super().__init__()
        self.aviso = aviso
        self.numero_catastrofe = numero_catastrofe
        self.gravedad = randint(1, 10)


# Completar
class Incendio(Emergencia):

    def __init__(self, aviso, numero_catastrofe) -> None:
        super().__init__(aviso, numero_catastrofe)
    

    def run(self) -> None:

        # Inicia el incendio
        print(f"Inicio de catastrofe N°{self.numero_catastrofe}:")
        print(f"{self.aviso}\n")

        # NO MODIFICAR
        agua_necesaria, banditas_necesarias = 100 * self.gravedad, 2 * self.gravedad
        agua, banditas = Emergencia.companias["agua"], Emergencia.companias["banditas"]

        with agua.disponibilidad:
            agua.solicitar(agua_necesaria)
        
        with banditas.disponibilidad:
            banditas.solicitar(banditas_necesarias)


        self.llamar_bomberos()
        print(f"Fin de catastrofe N°{self.numero_catastrofe}\n")

    def llamar_bomberos(self) -> None:
        sleep(self.gravedad)



# Completar
class Choque(Emergencia):

    def __init__(self, aviso, numero_catastrofe) -> None:
        super().__init__(aviso, numero_catastrofe)

    def run(self) -> None:

        # Inicia el choque
        print(f"Inicio de catastrofe N°{self.numero_catastrofe}:")
        print(f"{self.aviso}\n")

        # NO MODIFICAR
        donas_necesarias, banditas_necesarias = 3 * self.gravedad, 2 * self.gravedad
        donas, banditas = Emergencia.companias["donas"], Emergencia.companias["banditas"]
        
        with banditas.disponibilidad:
            banditas.solicitar(banditas_necesarias)

        with donas.disponibilidad:
            donas.solicitar(donas_necesarias)

        self.atender_heridos()

        print(f"Fin de catastrofe N°{self.numero_catastrofe}\n")

    def atender_heridos(self) -> None:
        sleep(self.gravedad)


if __name__ == "__main__":


    """
    Al correr el test a veces se presenta el inicio de las catástrofes en desorden,
    se preguntó a un ayudante y dijo que podía suceder debido al shuffle.
    """


    incendio_1 = Incendio(aviso="Incendio intencial de prueba, que podria salir mal...\n", 
                         numero_catastrofe=1)
    incendio_2 = Incendio(aviso="Incendio de prueba a la facultad de matematicas \n", 
                         numero_catastrofe=2)

    choque_1 = Choque(aviso="Choque de prueba, abrochence los cinturones !!! \n",
                     numero_catastrofe=3)
    choque_2 = Choque(aviso="Chocare el primer poste que vea >:( \n", 
                     numero_catastrofe=4)

    incendio_1.start()
    incendio_2.start()
    choque_1.start()
    choque_2.start()
