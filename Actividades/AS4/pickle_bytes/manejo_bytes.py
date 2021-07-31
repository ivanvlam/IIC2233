from os.path import join
from typing import Text

"""
Este módulo contiene funciones para el manejo general de los bytes de las
imágenes

Corresponde a la parte de Bytes
"""


def tuplas_desde_bytes(bytes_):
    """
    Recibe un bytearray proveniente de una imagen, que representa la información
    condensada de cada pixel. Se deben separar los pixeles (un pixel son 4 bytes
    en el bytearray) en una lista de tuplas.

    Argumentos:
        bytes_ (bytearray): La información a separar en tuplas.

    Retorna:
        list[tuple[int]]: lista de tuplas separadas
    """
    TAMANO_CHUNK = 4
    
    lista = []
    
    for i in range(0, len(bytes_) - 3, TAMANO_CHUNK):
        chunk = bytearray(bytes_[i: i + TAMANO_CHUNK])
        
        tupla = (chunk[0], chunk[1], chunk[2], chunk[3])
        
        lista.append(tupla)
    
    return lista


def bytes_desde_tuplas(tuplas):
    """
    Recibe una lista de tuplas, y las transforma en un bytearray. Realiza la
    función inversa de tuples_from_bytes.

    Argumentos:
        tuplas (list[tuple[int]]): Lista de tuplas a juntar

    Retorna:
        bytearray: bytes resultantes de juntar las información de las tuplas
    """
    bytes_ = bytearray()
    
    for tupla in tuplas:

        caracteres = bytes(tupla)
        bytes_.extend(caracteres)  
        
    return bytes_


def recuperar_contenido(bytearray_):
    """
    Recibe una ruta referente al archivo corrompido, tu tienes que sobreescrivir ese mismo archivo
    despues de corrigirlo con el algoritimo mencionado en el Enunciado.
    """
    byte_array = bytearray()
    
    for i in range(0, len(bytearray_), 2):
        chunk = bytearray(bytearray_[i: i + 2])
        
        if (i // 2) % 2 == 0:
            valor = 2 * chunk[0] + chunk[1]
        
        else:
            valor = chunk[0] + 2 * chunk[1]
        
        caracteres = bytes((valor, ))
        
        byte_array.extend(caracteres)
    
    return byte_array


def organizar_bmp(info_bytes):
    """
    Separa la información de la imagen en formato bmp en sus componentes
    principales

    Argumentos:
        info_bytes (bytearray): bytes representando la info de la imagen bmp

    Retorna:
        tuple[bytearray]: contiene el header, DIB Header, los pixeles, y el EOF
    """
    # No debes modificar esta función
    header = info_bytes[:15]
    dib_header = info_bytes[15:125]
    pixel_data = info_bytes[125:-1]
    eof = [info_bytes[-1]]
    return header, dib_header, pixel_data, eof


def int_desde_bytes(bytes_):
    """
    Decodifica el valor de un bytearray a un int con codificación little endian

    Argumentos:
        bytes_ (bytearray): Los bytes a decodificar

    Retorna:
        int: valor numérico correspondiente a los bytes
    """
    # No debes modificar esta función
    return int.from_bytes(bytes_, byteorder="little")


if __name__ == "__main__":
    """
    PUEDES PROBAR TU CÓDIGO AQUÍ
    """
    test = bytearray(b"\x00\x00\x01\x02\x01\x00\x01\x07\x04\x00")
    print(recuperar_contenido(test))
