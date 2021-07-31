from abc import ABC, abstractmethod

class Tripulante(ABC):

    def __init__(self, nombre, agnos_de_experiencia):
        self.nombre = nombre # str
        self.agnos_de_experiencia = int(agnos_de_experiencia) # int


    def __repr__(self):

        return f'[Tipo({type(self).__name__}), Nombre({self.nombre}),' \
            + f' Años({self.agnos_de_experiencia})]'


class DCCapitan(Tripulante):

    def __init__(self, nombre, agnos_de_experiencia):
        super().__init__(nombre, agnos_de_experiencia)


class DCCocinero(Tripulante):

    def __init__(self, nombre, agnos_de_experiencia):
        super().__init__(nombre, agnos_de_experiencia)


class DCCarguero(Tripulante):

    def __init__(self, nombre, agnos_de_experiencia):
        super().__init__(nombre, agnos_de_experiencia)


if __name__ == '__main__':
    ivan = DCCarguero('ivan', 19)
    print(ivan)