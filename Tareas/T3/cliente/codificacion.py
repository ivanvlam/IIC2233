import json

"""
Modulo para funciones de codificacion y decodificacion para envio de mensajes.
Recuerda, no debes modificar los argumentos que recibe cada funcion,
y debes entregar exactamente lo que esta pide en el enunciado.
"""


# Codificar un mensaje a un bytearray segun el protocolo especificado.
def codificar_mensaje(mensaje):
    mensaje_final = b''
    try:
        json_mensaje = json.dumps(mensaje)
        mensaje_enviar = json_mensaje.encode('utf-8')
        largo = len(mensaje_enviar).to_bytes(4, byteorder = 'big')
        
        mensaje_final += largo
        mensaje_final += (2).to_bytes(4, byteorder = 'little')
        
        while len(mensaje_enviar) % 60 != 0:
            mensaje_enviar += bytes(1)
        
        for i in range(0, len(mensaje_enviar), 60):
            mensaje_final += (int(i // 60)).to_bytes(4, byteorder = 'little')
            mensaje_final += mensaje_enviar[i: i + 60]
        
        return mensaje_final

    except json.JSONDecodeError:
        print('No se pudo codificar el mensaje')
        return mensaje_enviar


# Decodificar un bytearray para obtener el mensaje original.
def decodificar_mensaje(mensaje):
    mensaje_decodificado = bytearray()
    try:
        largo = int.from_bytes(mensaje[:4], 'big')
        mensaje = mensaje[12:]
        
        for i in range(0, len(mensaje), 64):
            mensaje_decodificado.extend(mensaje[i: i + 60])
            
        mensaje_decodificado = mensaje_decodificado[:largo - len(mensaje_decodificado)]
        mensaje = mensaje_decodificado.decode('utf-8')
        mensaje = json.loads(mensaje)
        
        return mensaje
    
    except json.JSONDecodeError:
        print('No se pudo decodificar el mensaje')
        return [bytearray(), 0]


# Codificar una imagen a un bytearray segun el protocolo especificado.
def codificar_imagen(ruta):
    mensaje_enviar = b''
    mensaje_archivo = b''
    try:
        with open(ruta, 'rb') as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            mensaje_archivo += linea
    
        try:
            largo = len(mensaje_archivo).to_bytes(4, byteorder = 'big')

            mensaje_enviar += largo
            mensaje_enviar += (1).to_bytes(4, byteorder = 'little')
            
            for caracter in ruta:
                if caracter.isnumeric():
                    color = caracter
            
            mensaje_enviar += (int(color)).to_bytes(4, byteorder = 'big')

            while len(mensaje_archivo) % 100 != 0:
                mensaje_archivo += bytes(1)
            
            for i in range(0, len(mensaje_archivo), 100):
                mensaje_enviar += (int(i // 100)).to_bytes(4, byteorder = 'little')
                mensaje_enviar += mensaje_archivo[i: i + 100]
            
            return bytearray(mensaje_enviar)

        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje')
            return mensaje_enviar
    
    except FileNotFoundError:
        print('No se pudo abrir el archivo')
        return mensaje_enviar


# Decodificar un bytearray a una lista segun el protocolo especificado.
def decodificar_imagen(mensaje):
    mensaje_decodificado = bytearray()
    try:
        #mensaje = json.dumps(mensaje)
        largo = int.from_bytes(mensaje[:4], 'big')
        color = int.from_bytes(mensaje[8:12], 'big')
        
        mensaje = mensaje[16:]
        
        for i in range(0, len(mensaje), 104):
            mensaje_decodificado.extend(mensaje[i: i + 100])

        mensaje_decodificado = mensaje_decodificado[:largo - len(mensaje_decodificado)]
        
        return [mensaje_decodificado, color]
    
    except json.JSONDecodeError:
        print('No se pudo decodificar el mensaje')
        return [bytearray(), 0]


if __name__ == '__main__':
    
    codificado = codificar_imagen('servidor/Avatares/avatar-1.png')
    bytes_ = decodificar_imagen(codificado)[0]

    with open('test.png', 'wb') as archivo:
        archivo.write(bytes_)
    
    mensaje = {i: f'hola_{i + 1}' for i in range(100)}
    codificado = codificar_mensaje(mensaje)
    print(decodificar_mensaje(codificado))