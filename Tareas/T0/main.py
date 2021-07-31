from parametros import ABANDONAR_FRASE, VOLVER_FRASE
from cargar import cargar_chat, cargar_contactos, \
    cargar_grupos, cargar_chat, cargar_usuarios
from modificar import iniciar_sesion, crear_usuario, \
    agregar_contacto, dejar_grupo, crear_grupo, enviar_mensaje


# Control del menu de inicio
def menu_inicio():
    print('\n' + '|' * 7 + ' Menu de Inicio ' + '|' * 7)
    print('\nSelecciona una opción:')
    print('\n[1] Registrarse\n[2] Iniciar Sesión\n[0] Salir\n')
    opcion = input('Introduzca su opción: ')
    if opcion == '0':
        print(f'\nGracias por preferir DCConecta2!\n'\
            'Esperamos verte pronto!\n')
        return False
    elif opcion == '1':
        nombre = input('\nIngrese nombre de usuario: ')
        registro_correcto, motivo = crear_usuario(nombre)
        if registro_correcto:
            print('\nUsuario ingresado exitosamente')
            return menu_chats(nombre)
        else:
            if motivo == 1:
                print(f'\nEl nombre de usuario {nombre} ya está en uso')
            else:
                print('\nEl nombre de usuario ingresado no es válido.\n' \
                'Debe contener entre 3 y 15 caracteres (ambos ' \
                'extremos) y no debe incluir comas (",")')
            print('Volviendo al menu de inicio...')
            return menu_inicio()
    elif opcion == '2':
        nombre = input('\nIngrese nombre de usuario: ')
        inicio_correcto = iniciar_sesion(nombre)
        if inicio_correcto:
            print('\nSesión iniciada exitosamente...')
            return menu_chats(nombre)
        else:
            print('\nUsuario no encontrado')
            print('Volviendo al menu de inicio...')
            return menu_inicio()
    else:
        print('\nPor favor ingresa una opción válida')
        print('Recargando menu de inicio...')
        return menu_inicio()

# Control del menu de chats
def menu_chats(usuario):
    print('\n' + '|' * 7 + ' Menu de Chats ' + '|' * 7)
    print('\nSelecciona una opción:')
    print('\n[1] Menu de Contactos\n[2] Menu de Grupos\n[0] Volver al menu de inicio\n')
    opcion = input('Introduzca su opción: ')
    if opcion == '0':
        return menu_inicio()
    elif opcion == '1':
        return menu_contactos(usuario)
    elif opcion == '2':
        return menu_grupos(usuario)
    else:
        print('\nPor favor ingresa una opción válida')
        print('Recargando menu de chats...')
        return menu_chats(usuario)


# Control del menu de contactos
def menu_contactos(usuario):
    print('\n' + '|' * 7 + ' Menu de Contactos ' + '|' * 7)
    print('\nSelecciona una opción:')
    print('\n[1] Ver Contactos\n[2] Añadir Contacto\n[0] Volver al menu de chats\n')
    opcion = input('Introduzca su opción: ')
    if opcion == '1':
        return ver_contactos(usuario)
    elif opcion == '2':
        return menu_agregar_contacto(usuario)
    elif opcion == '0':
        return menu_chats(usuario)
    else:
        print('\nPor favor ingresa una opción válida')
        print('Recargando menu de contactos...')
        return menu_contactos(usuario)


# Control del menu de añadir contactos
def menu_agregar_contacto(usuario):
    print('\n' + '|' * 7 + ' Agregar Contacto ' + '|' * 7)
    print('\nIngresa el nombre del usuario que deseas agregar: ')
    nuevo_contacto = input()
    agregar_correcto, motivo = agregar_contacto(usuario, nuevo_contacto)
    if agregar_correcto:
        print('\nContacto agregado exitosamente')
    else:
        if motivo == 1:
            print('\nNo te puedes agregar a ti mismo')
        elif motivo == 2:
            print(f'\n{nuevo_contacto} no existe dentro de la lista de usuarios')
        else:
            print(f'\n{nuevo_contacto} ya está en tu lista de contactos')
    print('Volviendo al menu de contactos...')
    return menu_contactos(usuario)


# Control del menu de ver contactos
def ver_contactos(usuario):
    contactos = cargar_contactos(usuario)
    print('\n' + '|' * 7 + f' Contactos de {usuario} ' + '|' * 7)
    print('\nSelecciona una opción:\n')
    opciones = '0'
    for i in range(len(contactos)):
        opciones += str(i + 1)
        contacto = contactos[i]
        print(f'[{i + 1}] {contacto}')
    print('[0] Volver al menu de contactos\n')
    opcion = input('Introduzca su opción: ')
    if opcion == '0':
        return menu_contactos(usuario)
    elif opcion in opciones and opcion != '':
        chat_seleccionado = contactos[int(opcion) - 1]
        conversacion(usuario, chat_seleccionado, 'regular')
    else:
        print('\nPor favor ingresa una opción válida')
        print('Recargando tus contactos...')
        return ver_contactos(usuario)


# Control del menu de grupos
def menu_grupos(usuario):
    print('\n' + '|' * 7 + ' Menu de Grupos ' + '|' * 7)
    print('\nSelecciona una opción:')
    print('\n[1] Ver Grupos\n[2] Crear Grupo\n[0] Volver al menu de chats\n')
    opcion = input('Introduzca su opción: ')
    if opcion == '1':
        return ver_grupos(usuario)
    elif opcion == '2':
        return menu_crear_grupo(usuario)
    elif opcion == '0':
        return menu_chats(usuario)
    else:
        print('\nPor favor ingresa una opción válida')
        print('Recargando menu de grupos...')
        return menu_grupos(usuario)


# Control del menu de crear grupos
def menu_crear_grupo(usuario):
    print('\n' + '|' * 7 + ' Crear Grupo ' + '|' * 7)
    print(('\nIngrese el nombre del grupo:'))
    nombre_grupo = input()
    grupos_total = cargar_grupos()
    if nombre_grupo in grupos_total.keys():
        print('\nNombre de grupo ya está en uso.')
        print('Volviendo al menu de grupos...')
        return menu_grupos(usuario)
    elif len(nombre_grupo) < 1 or ',' in nombre_grupo:
        print('\nEl nombre de grupo ingresado no es válido.\n' \
            'Debe contener al menos 1 caracter y no debe incluir comas (",")')
        print('Volviendo al menu de grupos...')
        return menu_grupos(usuario)
    print('\nIngrese el nombre de los participantes separados por ";":')
    participantes = set(input().split(';'))
    participantes.add(usuario)
    if len(participantes) < 2:
        print('\nEl grupo debe contener al menos dos participantes.')
        print('Volviendo al menu de grupos...')
        return menu_grupos(usuario)
    usuarios = cargar_usuarios()
    for miembro in participantes:
        if miembro not in usuarios:
            print('\nNo todos los integrantes del grupo están registrados.')
            print('Volviendo al menu de grupos...')
            return menu_grupos(usuario)

    crear_grupo(usuario, nombre_grupo, participantes)
    print('\nGrupo agregado exitosamente')
    print('Volviendo al menu de grupos...')
    return menu_grupos(usuario)


# Control del menu de ver grupos
def ver_grupos(usuario):
    grupos_usuario = []
    grupos_total = cargar_grupos()
    for nombre, integrantes in grupos_total.items():
        if usuario in integrantes:
            grupos_usuario.append(nombre)
    print('\n' + '|' * 7 + f' Grupos de {usuario} ' + '|' * 7)
    print('\nSelecciona una opción:\n')
    opciones = '0'
    for i in range(len(grupos_usuario)):
        opciones += str(i + 1)
        grupo = grupos_usuario[i]
        print(f'[{i + 1}] {grupo}')
    print('[0] Volver al menu de grupos\n')
    opcion = input('Introduzca su opción: ')
    if opcion not in opciones or opcion == '':
        print('\nPor favor ingresa una opción válida')
        print('Recargando tus grupos...')
        return ver_grupos(usuario)
    elif opcion != '0':
        chat_seleccionado = grupos_usuario[int(opcion) - 1]
        conversacion(usuario, chat_seleccionado, 'grupo')
    else:
        return menu_grupos(usuario)


# Control de conversación
def conversacion(usuario, chat_seleccionado, tipo_chat):
    cargar_chat(usuario, chat_seleccionado, tipo_chat)
    contenido = input('\nMensaje: ').strip(' ')
    if len(contenido) > 0:
        if contenido == ABANDONAR_FRASE and tipo_chat == 'grupo':
            enviar_mensaje(usuario, chat_seleccionado, \
                f'{usuario} ha abandonado el grupo', tipo_chat)
            dejar_grupo(chat_seleccionado, usuario)
            return menu_grupos(usuario)
        elif contenido == VOLVER_FRASE:
            cargar_chat(usuario, chat_seleccionado, tipo_chat)
            print('\n' + '~' * 5 + ' Fin de historial con ' + str(chat_seleccionado) + ' ' + '~' * 5)
            if tipo_chat == 'grupo':
                return ver_grupos(usuario)
            else:
                return ver_contactos(usuario)
        else:
            enviar_mensaje(usuario, chat_seleccionado, contenido, tipo_chat)
            print('')
            conversacion(usuario, chat_seleccionado, tipo_chat)
    else:
        print('\nEl contenido del mensaje no puede ser vacío.\n' \
            'Recargando conversación...\n')
        conversacion(usuario, chat_seleccionado, tipo_chat)


# Correr el código
ingreso_correcto = menu_inicio()
