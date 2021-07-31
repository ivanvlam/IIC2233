# <span style="font-family:Bebas Neue; font-size:2em;">Tarea 0: DCConecta2 :iphone:</span>

## Indice :octocat:
- [Introducción :speech_balloon:](#Introducción-speech_balloon)
- [Consideraciones generales :nerd_face:](#Consideraciones-generales-nerd_face)
- [Ejecución :computer:](#Ejecución-computer)
- [Librerías :books:](#Librerías-books)
- [Supuestos y consideraciones adicionales :thinking:](#Supuestos-y-consideraciones-adicionales-thinking)
- [Referencias de código externo :trollface:](#Referencias-de-código-externo-trollface)

---

## Introducción :speech_balloon:

El presente  ```README.md``` contiene una visión general del programa *DCConecta2* correspondiente a la Tarea 0, además, profundiza en su ejecución, las librerías utilizadas, los supuestos considerados y las referencias de código externo incorporadas durante la elaboración del código. 

---

## Consideraciones generales :nerd_face:

*DCConecta2* consiste en un sistema de mensajería guíado por la interacción del usuario con distinos menús del programa, como el menú de inicio, de chats, de contactos y de grupos. La información se organiza en una serie de archivos .csv, que permiten el correcto flujo del programa mediante el chequeo de los usuarios, contactos, grupos y mensajes contenidos en ellos. Los archivos mencionados son editados cada vez que se modifica algún paramétro, por ejemplo: con el registro de un usuario, la creación de un grupo o el simple envío de un mensaje. En cuanto al código, el programa se separa en cuatro archivos .py redactados en español, y respecto a su ejecución, el programa cumple con todas las funciones solicitadas y no se encontraron errores al correr el código.

### Cosas implementadas y no implementadas :white_check_mark::x:

* Menús <sub>4</sub>: **Completado** :white_check_mark:
    * Menú de inicio <sub>4.1</sub>: **Completado** :white_check_mark:
        1. Registrarse: **Completado** :white_check_mark:
        2. Iniciar sesión: **Completado** :white_check_mark:
        3. Salir: **Completado** :white_check_mark:
    * Menú de chats <sub>4.2</sub>: **Completado** :white_check_mark:
        * Menú de Contactos <sub>4.2.1</sub>: **Completado** :white_check_mark:
            1. Ver contactos: **Completado** :white_check_mark:
            2. Añadir contacto: **Completado** :white_check_mark:
            3. Volver al menú de chats: **Completado** :white_check_mark:
        * Menú de Grupos <sub>4.2.2</sub>: **Completado** :white_check_mark:
            1. Ver grupos: **Completado** :white_check_mark:
            2. Crear grupo: **Completado** :white_check_mark:
            3. Volver al menú de chats: **Completado** :white_check_mark:
* Manejo de archivos <sub>5</sub>: **Completado** :white_check_mark:
    * ```usuarios.csv``` <sub>5.1</sub>: **Completado** :white_check_mark:
    * ```contactos.csv``` <sub>5.2</sub>: **Completado** :white_check_mark:
    * ```grupos.csv``` <sub>5.3</sub>: **Completado** :white_check_mark:
    * ```mensajes.csv``` <sub>5.4</sub>: **Completado** :white_check_mark:

---

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos en el mismo diirectorio del código principal:
1. ```cargar.py``` en ```T0```
2. ```modificar.py``` en ```T0```
3. ```parametros.py``` en ```T0```
4. ```usuarios.csv``` en ```T0```
5. ```contactos.csv``` en ```T0```
6. ```grupos.csv``` en ```T0```
7. ```mensajes.csv``` en ```T0```

---

## Librerías :books:
### Librerías externas utilizadas :rocket:
La lista de librerías externas que utilicé fue la siguiente:

1. ```collections```: ```namedtuple```, ```defaultdict```
2. ```datetime```: ```datetime``` (debe instalarse)

### Librerías propias :art:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cargar```: Contiene a las funciones que permiten cargar todos los datos del programa, ya sea mensajes, grupos, usuarios, contactos, etc.
2. ```modificar```: Funciones utilizadas para modificar los archvos .csv, por ejemplo: registrar usuario, abandonar grupo, enviar mensaje, etc.

---

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la realización de la tarea son los siguientes:

1. Todos los contactos que se tenían agregados, se encontraban agregados mutuamente.

    * > Al agregar un contacto en la lista de contactos de un usuario, también se debía agregar al usuario a la lista de contactos del nuevo contacto.

2. El contenido de un mensaje no puede ser vacío.

    * > *DCConecta2* replica un servicio de mensajería instantánea, por lo que su funcionamiento debe ser similar al de los más conocidos (*WhatsApp*, *Instagram*, *Messenger*, etc.). En ellos, no se puede enviar un mensaje sin contenido o lleno con espacios (" ").

---

## Referencias de código externo :trollface:

Para decorar mi tarea saqué código de:
1. [Guía de estilo Markdown](https://support.squarespace.com/hc/en-us/articles/206543587-Markdown-cheat-sheet): Referenciado para cambiar la fuente y tamaño del título del presente ```README.md```.
2. [Introducción a Markdown](https://www.youtube.com/watch?v=pTCROLZLhDM): Referenciado para elaborar un índice con hipervínculos del presente ```README.md```.
3. [Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#github-custom-emoji): Referenciado para obtener fácilmente los *shortcodes* para insertar emojis en el presente ```README.md```.



