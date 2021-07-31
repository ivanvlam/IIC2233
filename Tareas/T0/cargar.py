from collections import defaultdict, namedtuple


# Función para cargar usuarios
def cargar_usuarios():
    with open('usuarios.csv', 'r') as archivo:
        lineas = archivo.readlines()[1:]
    for i in range(len(lineas)):
        lineas[i] = lineas[i].strip()
    return lineas


# Función para cargar contactos de un usuario en forma de lista
def cargar_contactos(usuario):
    contactos = []
    with open('contactos.csv', 'r') as archivo:
        lineas = archivo.readlines()[1:]
    for linea in lineas:
        datos_linea = linea.strip().split(',')
        if datos_linea[0] == usuario:
            contactos.append(datos_linea[1])
    return contactos


# Función para cargar todos los grupos
# Retorna un defaultdict de la forma {Nombre grupo: [integrantes]}
def cargar_grupos():
    diccionario_grupos = defaultdict(list)
    with open('grupos.csv', 'r') as archivo:
        lineas = archivo.readlines()[1:]
    for linea in lineas:
        datos_linea = linea.strip().split(',')
        if len(datos_linea) == 2:
            diccionario_grupos[datos_linea[0]].append(datos_linea[1])
    return diccionario_grupos

# Función para cargar todos los grupos
# Retorna un lista que contiene a todoas los mensajes
# Los mensajes son retornados en nametuples
def cargar_mensajes():
    mensajes = []
    Mensaje = namedtuple('Mensaje', ['tipo_chat', 'emisor', \
            'receptor', 'fecha_emision', 'contenido'])
    with open('mensajes.csv', 'r') as archivo:
        lineas = archivo.readlines()[1:]
    for linea in lineas:
        datos_linea = tuple(linea.strip().split(',', maxsplit = 4))
        if len(datos_linea) > 2:
            mensaje = Mensaje(*datos_linea)
            mensajes.append(mensaje)
    return mensajes


# Carga el chat
# Utilizado cada vez que se abre una conversación o se envía un mensaje
def cargar_chat(emisor, receptor, tipo_chat):
    print('~' * 5 + ' Historial con ' + str(receptor) + ' ' + '~' * 5 + '\n')
    mensajes = cargar_mensajes()
    if tipo_chat == 'grupo':
        for mensaje in mensajes:
            if receptor == mensaje.receptor:
                print(f'{mensaje.fecha_emision}, {mensaje.emisor}: {mensaje.contenido}')
    else:
        integrantes = (emisor, receptor)
        for mensaje in mensajes:
            if mensaje.emisor in integrantes and mensaje.receptor in integrantes:
                print(f'{mensaje.fecha_emision}, {mensaje.emisor}: {mensaje.contenido}')
    return True


# Pruebas de funciones
if __name__ == '__main__':
    usuarios = cargar_usuarios()
    contactos = cargar_contactos('lily416')
    print(usuarios)
    print(f'Contactos: {contactos}\n')
    print(f'Grupos: {cargar_grupos()}\n')
    print(f'Mensajes: {cargar_mensajes()}')
    cargar_chat('lily416', 'Los Teletubbies', 'grupo')
    cargar_chat('lily416', 'DCCollao', 'regular')
