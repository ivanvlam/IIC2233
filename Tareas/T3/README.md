# <span style="font-family:Bebas Neue; font-size:2em;">Tarea 3: DCCópteros :helicopter: </span>

## Indice :octocat:
- [Introducción :speech_balloon:](#Introducción-speech_balloon)
- [Consideraciones generales :nerd_face:](#Consideraciones-generales-nerd_face)
- [Ejecución :computer:](#Ejecución-computer)
- [Librerías :books:](#Librerías-books)
- [Supuestos y consideraciones adicionales :thinking:](#Supuestos-y-consideraciones-adicionales-thinking)
- [Referencias de código externo :octocat:](#Referencias-de-código-externo-octocat)

---

## Introducción :speech_balloon:

El presente  ```README.md``` contiene una visión general del programa *DCCópteros* correspondiente a la Tarea 3, además, profundiza en su ejecución, las librerías utilizadas, los supuestos considerados y las referencias de código externo incorporadas durante la elaboración del código. 

---

## Consideraciones generales :nerd_face:

*DCCópteros* es un juego de simulación multijugador por turnos, en el que se competirá por ser el jugador que logre acumular más puntos al final de la partida. Un jugador ganará puntos ya sea por adquirir un camino que conecta 2 lugares o bien, por completar un objetivo secreto que se le asigna al inicio del juego. El programa cuenta con un servidor, que debe ser ejecutado antes que cualquier otro archivo, mientras que la interacción del usuario está mediada por la interacción con distintas ventanas mediante _clicks_ en los botones correspondientes, el programa se separa en quince archivos ```.py``` redactados en español y separados en carpetas de _cliente_ y _servidor_, rescatando los fundamentos de interfaces gráficas, networking, threading y manejo de bytes. Por último, respecto a su ejecución, el programa cumple con la mayoría de las funciones solicitadas pero no se pudo lograr el desarrollo del juego.

### Cosas implementadas y no implementadas :white_check_mark::x:

* Reglas de DCCópteros <sub>3</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Mapa <sub>3.1</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Objetivos <sub>3.2</sub>: **No completado** :x:
    * Desarrollo del juego <sub>3.3</sub>: **No completado** :x:
    * Fin del juego <sub>3.4</sub>: **No completado** :x:

* Networking <sub>4</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Arquitectura cliente-servidor <sub>4.1</sub>: **Completado** :white_check_mark:
    * Módulos a completar <sub>4.2</sub>: **Parcialmente completado** :eight_pointed_black_star:
        * Logs del servidor <sub>4.2.1</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Roles <sub>4.3</sub>: **Parcialmente completado** :eight_pointed_black_star:
        * Servidor <sub>4.3.1</sub>: **Parcialmente completado** :eight_pointed_black_star:
        * Cliente <sub>4.3.2</sub>: **Parcialmente completado** :eight_pointed_black_star:

* Interfaz gráfica <sub>5</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Ventana de inicio <sub>5.1</sub>: **Completado** :white_check_mark:
    * Sala de espera <sub>5.2</sub>: **Completado** :white_check_mark:
    * Sala de juegos <sub>5.3</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Fin de partida <sub>5.4</sub>: **No completado** :x:


* Archivos <sub>6</sub>: **Completado** :white_check_mark:
    * Archivos entregados <sub>6.1</sub>: **Completado** :white_check_mark:
    * Archivos a crear <sub>6.2</sub>: **Completado** :white_check_mark:

* Bonus <sub>7</sub>: **No completado** :x:
    * GIF de celebración <sub>7.1</sub>: **No completado** :x:
    * Turnos cronometrados <sub>7.2</sub>: **No completado** :x:

---

## Ejecución :computer:
### Servidor :earth_americas:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos en el mismo directorio del código principal:

1. ```funciones.py``` en ```T3/servidor```
2. ```clases.py``` en ```T3/servidor```
3. ```codificacion.py``` en ```T3/servidor```
4. ```servidor.py``` en ```T3/servidor```
5. ```logica.py``` en ```T3/servidor```
6. ```parametros.json``` en ```T3/servidor```
7. Avatares (```.png```, ```.jpg```) en ```T3/servidor```

### Cliente :man_technologist:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos en el mismo directorio del código principal:

1. ```ventana_inicio.py``` en ```T3/cliente/ventanas```
2. ```ventana_espera.py``` en ```T3/cliente/ventanas```
3. ```ventana_juego.py``` en ```T3/cliente/ventanas```
4. ```funciones.py``` en ```T3/cliente```
5. ```clases.py``` en ```T3/cliente```
6. ```codificacion.py``` en ```T3/cliente```
7. ```cliente.py``` en ```T3/cliente```
8. ```logica.py``` en ```T3/cliente```
9. ```parametros.json``` en ```T3/cliente```
10. ```mapa.json``` en ```T3/cliente```
11. imagenes (```.png```, ```.jpg```) en ```T3/cliente```
12. sprites (```.png```, ```.jpg```) en ```T3/cliente```

---

## Librerías :books:
### Librerías externas utilizadas :rocket:
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```__excepthook__```, ```argv```, ```exit```, ```exec_```
2. ```os.path```: ```join```, ```listdir```
3. ```random```: ```shuffle```, ```choice```
4. ```collections```: ```namedtuple```
5. ```json```: ```loads```, ```dumps```
6. ```socket```: ```socket```
7. ```threading```: ```Thread```
8. ```PyQt5```: ```QtMultimedia``` (debe instalarse)

    * ```QtWidgets```: ```QLabel```, ```QWidget```, ```QLineEdit```, ```QHBoxLayout```, ```QVBoxLayout```, ```QPushButton```, ```QProgressBar```, ```QButtonGroup```, ```QRadioButton```, ```QComboBox```

    * ```QtCore```: ```pyqtSignal```, ```Qt```, ```QThread```, ```QObject```, ```QTimer```

    * ```QtGui```: ```QPixmap```, ```QFont```, ```QIcon```
    

### Librerías propias :art:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones.py```: Contiene funciones utilizadas para cargar parámetros, grafo y seleccionar la opción de codificación adecuada.

2. ```clases.py```: Contiene clases como *Nodo*, *Grafo* y *MegaThread*.

3. ```logica.py```: Contiene la clase *Lógica* que realiza el manejo e interpretación de mensajes. 

4. ```servidor.py```: Contiene a la clase *Servidor*, que constituye el *backend* del servidor.

5. ```cliente.py```: Contiene a la clase *Cliente*, que constituye el *backend* del cliente.

6. ```ventanas```: Contiene a las clases *Ventanas* que corresponden a la interfaz gráfica.

---

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la realización de la tarea son los siguientes:

1. Ningún jugador se saldrá de la espera después de votar.

    * > Se modeló así por simplicidad al momento de contar votos y permitir el ingreso a la ventana de juego.

2. Los parámetros siempre serán del tipo correspondiente, por lo que no se realizó manejo de errores de ese aspecto.

    * > Se deposita la confianza en el usuario para que escoja los parámetros del tipo correspondiente.

---

## Referencias de código externo :octocat:

Para realizar mi tarea saqué código de:

1. Gran parte del código fue basado en los realizados para la [AF7](https://github.com/IIC2233/syllabus/tree/main/Actividades/AF7).

2. [Convertir bytes a JSON](https://stackoverflow.com/questions/40059654/python-convert-a-bytes-array-into-json-format): Utilizado en la sección de ```codificacion.py```.