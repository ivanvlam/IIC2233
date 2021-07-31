from copy import copy


class IterableDescuentos:
    # NO MODIFICAR
    def __init__(self, mascotas):
        self.mascotas = mascotas

    def __iter__(self):
        return IteradorDescuentos(self)


class IteradorDescuentos:
    def __init__(self, iterable):
        # NO MODIFICAR
        self.iterable = copy(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable is None or self.iterable.mascotas == []:
            raise StopIteration('Se acabaron las mascotas')
        
        else:
            mascotas_ordenadas = sorted(self.iterable.mascotas, key = lambda x: x.edad, reverse = True)
            descuento = min(mascotas_ordenadas[0].edad * 0.1, 0.35) * 100
            mascotas_ordenadas[0].descuento_por_edad = descuento
            mascotas_ordenadas[0].precio *= (1 - descuento / 100)
            
            self.iterable.mascotas.remove(mascotas_ordenadas[0])
            return mascotas_ordenadas[0]
