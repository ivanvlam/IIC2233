from cargar import cargar_usuarios, cargar_contactos, \
    cargar_grupos, cargar_mensajes
from datetime import datetime


# Maneja el inicio de sesión
def iniciar_sesion(nombre = ''):
    usuarios = cargar_usuarios()
    if nombre in usuarios:
        return True
    else:
        return False


# Maneja la creación de usuario
def crear_usuario(nombre = ''):
    usuarios = cargar_usuarios()
    condicion_1 = nombre in usuarios
    condicion_2 = len(nombre) > 2 and len(nombre) < 16
    if condicion_1:
        return False, 1
    elif not condicion_2 or ',' in nombre:
        return False, 2
    else:
        usuarios.append(nombre)
        with open('usuarios.csv', 'w') as archivo:
            print('usuario', file = archivo)
            for usuario in usuarios:
                if len(usuario) > 2:
                    print(usuario, file = archivo)
        return True, 0


# Permite agregar contactos
def agregar_contacto(usuario, nuevo_contacto):
    usuarios = cargar_usuarios()
    contactos = cargar_contactos(usuario)
    if usuario == nuevo_contacto:
        return False, 1
    elif nuevo_contacto not in usuarios:
        return False, 2
    else:
        if nuevo_contacto in contactos:
            return False, 3
        else:
            with open('contactos.csv', 'r') as archivo:
                lineas = archivo.readlines()
            with open('contactos.csv', 'w') as archivo:
                for linea in lineas:
                    if len(linea) > 2:
                        print(linea.strip(), file = archivo)
                print(f'{usuario},{nuevo_contacto}', file = archivo)
                print(f'{nuevo_contacto},{usuario}', file = archivo)
            return True, 1


# Permite crear un grupo
# El control de flujo de las condiciones esta en el archivo main
def crear_grupo(usuario, nombre_grupo, miembros):
    with open('grupos.csv', 'r') as archivo:
        lineas = archivo.readlines()
    with open('grupos.csv', 'w') as archivo:
        for linea in lineas:
            if len(linea) > 2:
                print(linea.strip(), file = archivo)
        for miembro in miembros:
            print(f'{nombre_grupo},{miembro}', file = archivo)
    return True, 1
    

# Permite abandonar un grupo
def dejar_grupo(grupo_a_dejar, usuario):
    grupos = cargar_grupos()
    grupos[grupo_a_dejar].pop(grupos[grupo_a_dejar].index(usuario))
    with open('grupos.csv', 'w') as archivo:
        print('grupo,integrante', file = archivo)
        for grupo, integrantes in grupos.items():
            if len(integrantes) > 0:
                for integrante in integrantes:
                    print(f'{grupo},{integrante}', file = archivo)


# Permite enviar mensajes
# Las funciones datetime y pytz entregan la horas en tiempo real de Chile continental
def enviar_mensaje(emisor, receptor, contenido, tipo_chat):
    now = datetime.now()
    fecha_emision = now.strftime("%Y/%m/%d %H:%M:%S")
    with open('mensajes.csv', 'r') as archivo:
        lineas = archivo.readlines()
    with open('mensajes.csv', 'w') as archivo:
        for linea in lineas:
            if len(linea) > 2:
                print(linea.strip(), file = archivo)
        print(f'{tipo_chat},{emisor},{receptor},{fecha_emision},{contenido}', file = archivo)


# Pruebas de funciones
if __name__ == '__main__':
    print(agregar_contacto('lily416', 'pedroparamo'))
    print(agregar_contacto('lily416', 'lily416'))
    print(agregar_contacto('lily416', 'matiasmasjuan'))
    print(agregar_contacto('lily416', 'Pablok98'))


