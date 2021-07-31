# <span style="font-family:Bebas Neue; font-size:2em;">Tarea 2: DCCimpsons :doughnut::policeman: </span>

## Indice :octocat:
- [Introducción :speech_balloon:](#Introducción-speech_balloon)
- [Consideraciones generales :nerd_face:](#Consideraciones-generales-nerd_face)
- [Ejecución :computer:](#Ejecución-computer)
- [Librerías :books:](#Librerías-books)
- [Supuestos y consideraciones adicionales :thinking:](#Supuestos-y-consideraciones-adicionales-thinking)
- [Algunas consideraciones acerca del código :grimacing:](#Algunas-consideraciones-acerca-del-código-grimacing)
- [Referencias de código externo :octocat:](#Referencias-de-código-externo-octocat)

---

## Introducción :speech_balloon:

El presente  ```README.md``` contiene una visión general del programa *DCCimpsons* correspondiente a la Tarea 2, además, profundiza en su ejecución, las librerías utilizadas, los supuestos considerados y las referencias de código externo incorporadas durante la elaboración del código. 

---

## Consideraciones generales :nerd_face:

*DCCimpsons* es un juego que consiste en recolectar la mayor cantidad de objetos en un tiempo determinado, lo que se debe hacer esquivando obstáculos y al enemigo. Al finalizar cada ronda, se muestra un puntuje y estadísticas según la cantidad y naturaleza de los objetos atrapados durante esta, siendo el objetivo del juego obtener la mayor puntuación posible, que quedará registrada en un archivo ```.txt``` para poder visualizar los mejores puntajes posteriormente. La interacción del usuario se da en distintas ventanas mediante _clicks_ en los botones correspondientes y combinaciones de teclas al interior del juego, el programa se separa en quince archivos ```.py``` redactados en español y separados en carpetas de _frontend_ y _backend_, rescatando los fundamentos de interfaces gráficas y threading. Por último, respecto a su ejecución, el programa cumple con casi todas las funciones solicitadas y solo se encontraron dos pequeños errores al correr el código.

### Cosas implementadas y no implementadas :white_check_mark::x:

* Mecánicas del juego <sub>3</sub>: **Completado** :white_check_mark:
    * Personajes <sub>3.1</sub>: **Completado** :white_check_mark:
        * Homero: **Completado** :white_check_mark:
        * Lisa: **Completado** :white_check_mark:
    * Lugares del juego <sub>3.2</sub>: **Completado** :white_check_mark:
        * Planta Nuclear: **Completado** :white_check_mark:
        * Primaria: **Completado** :white_check_mark:
    * Objetos <sub>3.3</sub>: **Completado** :white_check_mark:
        * Objetos normales <sub>3.3.1</sub>: **Completado** :white_check_mark:
        * Objetos buenos <sub>3.3.2</sub>: **Completado** :white_check_mark:
        * Objetos peligrosos <sub>3.3.3</sub>: **Completado** :white_check_mark:
    * Obstáculos <sub>3.4</sub>: **Completado** :white_check_mark:
    * Personaje enemigo <sub>3.5</sub>: **Completado** :white_check_mark:
    * Dificultad <sub>3.6</sub>: **Completado** :white_check_mark:
    * Puntaje y vida <sub>3.7</sub>: **Completado** :white_check_mark:
    * Fin de ronda <sub>3.8</sub>: **Completado** :white_check_mark:
    * Fin del juego <sub>3.9</sub>: **Completado** :white_check_mark:

* Interfaz gráfica <sub>4</sub>: **Completado** :white_check_mark:
    * Modelación del programa <sub>4.1</sub>: **Completado** :white_check_mark:
    * Ventanas <sub>4.2</sub>: **Completado** :white_check_mark:
        * Ventana de inicio <sub>4.2.1</sub>: **Completado** :white_check_mark:
        * Ventana de ranking <sub>4.2.2</sub>: **Completado** :white_check_mark:
        * Ventana de preparación <sub>4.2.3</sub>: **Completado** :white_check_mark:
        * Ventana de juego <sub>4.2.4</sub>: **Completado** :white_check_mark:
        * Ventana de post-ronda <sub>4.2.5</sub>: **Completado** :white_check_mark:

* Interacción con el usuario <sub>5</sub>: **Completado** :white_check_mark:
    * Movimiento <sub>5.1</sub>: **Completado** :white_check_mark:
    * Click <sub>5.2</sub>: **Completado** :white_check_mark:
    * Cheatcodes <sub>5.3</sub>: **Completado** :white_check_mark:
    * Pausa <sub>5.4</sub>: **Parcialmente completado** :eight_pointed_black_star:


* Archivos <sub>6</sub>: **Completado** :white_check_mark:
    * Sprites <sub>6.1</sub>: **Completado** :white_check_mark:
    * Canciones <sub>6.2</sub>: **Completado** :white_check_mark:
    * ```ranking.txt``` <sub>6.3</sub>: **Completado** :white_check_mark:
    * ```parametros.py``` <sub>6.4</sub>: **Completado** :white_check_mark:

* Bonus <sub>7</sub>: **Parcialmente completado** :eight_pointed_black_star:
    * Drag and drop <sub>7.1</sub>: **No completado** :x:
    * Música <sub>7.2</sub>: **Completado** :white_check_mark:
    * Otros personajes <sub>7.3</sub>: **Completado** :white_check_mark:

---

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos en el mismo directorio del código principal:
1. ```funciones.py``` en ```T2```
2. ```clases.py``` en ```T2```
3. ```parametros.py``` en ```T2```
4. ```jefe_gorgory.py``` en ```T2/backend```
5. ```logica_inicio.py``` en ```T2/backend```
6. ```logica_juego.py``` en ```T2/backend```
7. ```logica_postronda.py``` en ```T2/backend```
8. ```logica_preparacion.py``` en ```T2/backend```
9. ```logica_ranking.py``` en ```T2/frontend```

10. ```ventana_inicio.py``` en ```T2/frontend```
11. ```ventana_juego.py``` en ```T2/frontend```
12. ```ventana_postronda.py``` en ```T2/frontend```
13. ```ventana_preparacion.py``` en ```T2/frontend```
14. ```ventana_ranking.py``` en ```T2/frontend```
15. Imágenes (```.png```, ```.jpg```) en ```T2/sprites``` y ```T2/imagenes```
16. ```musica.wav``` en ```T2/canciones```

---

## Librerías :books:
### Librerías externas utilizadas :rocket:
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```__excepthook__```, ```argv```, ```exit```, ```exec_```
2. ```time```: ```sleep```, ```time```
3. ```os.path```: ```join```
4. ```random```: ```random```, ```randint```, ```choice```
5. ```collections```: ```namedtuple```, ```deque```
6. ```PyQt5```: ```QtMultimedia``` (debe instalarse)

    * ```QtWidgets```: ```QLabel```, ```QWidget```, ```QLineEdit```, ```QHBoxLayout```, ```QVBoxLayout```, ```QPushButton```, ```QProgressBar```, ```QButtonGroup```, ```QRadioButton```, ```QComboBox```

    * ```QtCore```: ```pyqtSignal```, ```Qt```, ```QThread```, ```QObject```, ```QTimer```

    * ```QtGui```: ```QPixmap```, ```QFont```, ```QIcon```
    

### Librerías propias :art:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones.py```: Contiene funciones utilizadas para comprobar colisiones entre el personaje y obstáculos, objetos y el jefe Gorgory.

2. ```clases.py```: Contiene clases de estilo como *FotoEstandar* y *BotonPersonalizado*, además de la clase de *Objeto* que posee un atributo de *QTimer* permitiendo que maneje su propia desaparición de la ventana.

3. ```jefe_gorgory.py```: Contiene las clases *JefeGorgory* y *ThreadGorgory* que se encargan de manejar aspectos visuales del label del jefe Gorgory (posición y sprite) y de manejar el delay con el que ocurren las acciones, respectivamente.

4. ```logica_inicio.py```: Contiene las clases *LogicaInicio* y *Musica*, la primera realiza la comprobación de la condición alfanumérica del nombre, mientras que la segunda se encarga del manejo de la canción de fondo (pausa, reproducción y reinicio).

5. ```logica_juego.py```: Contiene a la clase *LogicaJuego*, que constituye el *backend* de la ventana de juego.

6. ```logica_postronda.py```: Contiene a la clase *LogicaPostronda*, que constituye el *backend* de la ventana post-ronda.

7. ```logica_preparacion.py```: Contiene a la clase *LogicaPreparacion*, que constituye el *backend* de la ventana de preparación.

8. ```logica_ranking.py```: Contiene a la clase *LogicaRanking*, que constituye el *backend* de la ventana de ranking.

9. ```ventana_inicio.py```: Contiene a la clase *VentanaInicio* que es responsable de todos los elementos visuales de la ventana de incio.

10. ```ventana_juego.py```: Contiene a la clase *VentanaJuego* que es responsable de todos los elementos visuales de la ventana de juego.

11. ```ventana_postronda.py```: Contiene a la clase *VentanaPostronda* que es responsable de todos los elementos visuales de la ventana post-ronda.

12. ```ventana_preparacion.py```: Contiene a la clase *VentanaPreparacion* que es responsable de todos los elementos visuales de la ventana de preparación.

13. ```ventana_ranking.py```: Contiene a la clase *VentanaRanking* que es responsable de todos los elementos visuales de la ventana de ranking.

14. ```parametros.py```: Contiene a todos los parámetros utilizados en el programa, desde los *paths* hacia los *sprites* de cada personaje hasta las probabilidades de aparición de cada tipo de objeto.


---

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la realización de la tarea son los siguientes:

1. Las habilidades de los personajes se reinician después de cada ronda.

    * > Si las habilidades de los personajes no se reiniciaran en cada ronda, podrían darse casos en los que los saxofones de lisa aparecieran 32 o incluso más veces más rápido que el parámetro inicial, o incluso, podrían darse casos en los que el delay del jefe Gorgory fuera tan alto que ni siquiera llegara a aparecer en la ronda.

2. Los parámetros siempre serán del tipo correspondiente, por lo que no se realizó manejo de errores de ese aspecto.

    * > Se deposita la confianza en el usuario para que escoja los parámetros del tipo correspondiente. Si bien en el archivo ```parametros.py``` se explicita el tipo de dato que debe ser con un comentario al lado, se recomienda guiarse por el tipo de dato que ya esta definido para cada parámetro, exceptuando el caso de *PONDERADOR_VIDA_HOMERO* que está definido como *None* pero debe ser de tipo *float*.

3. La música no se reinicia en la ventana de ranking.

    * > Si bien, según el enunciado, la música debe reiniciarse cada vez que se cambia de ventana, este también señala que desde la ventana de ranking se debe poder volver a la ventana de inicio mediante el botón volver o cerrando la ventana, por lo que la ventana de ranking se ha interpretado como un *pop-up* que surge sobre la ventana de inicio, lo que en consecuencia, hace que el cambio de la ventana de inicio a la ventana de ranking y viceversa no constituya un cambio de ventana y, por ende, no sea necesario reiniciar la música al hacerlo.

---

## Algunas consideraciones acerca del código :grimacing:

1. Existe un error que ocurre con la vida del personaje al interactuar con un objeto o acción que aumente o disminuya su vida. Esto solo ocurre cuando se utilizan parámetros cuyo ponderador de vida sean menores a 0.1, debido a un round presente al hacer la adición de dicho ponderador en la *property* de vida. Sin embargo, esto puede arreglarse mediante el siguiente cambio de línea en la línea 125 de ```ventana_juego.py```:


    ```python
    '''Actualmente dice'''
    @vida.setter
    def vida(self, valor):
        if valor > 1:
            self.__vida = 1
        elif valor < 0:
            self.__vida = 0
        else:
            self.__vida = round(valor, 1)
    
    '''Debería decir'''
    @vida.setter
    def vida(self, valor):
        if valor > 1:
            self.__vida = 1
        elif valor < 0:
            self.__vida = 0
        else:
            self.__vida = round(valor, 2)
    ```

    Lo anterior siempre asumiendo que los parámetros utilizados en los ponderadores de vida (corazones, *cheatcode* y *PONDERADOR_VIDA_HOMERO*) constituyan floats de largo no mayor a 4, es decir, que sean *floats* de la forma 0.01, 0.25, 0.1, etc.

2. Los bonus incorporados fueron el de música y el de personajes adicionales. Mientras que la decisión para los *cheatcodes* fue realizar la secuencia de teclas por sobre la combinación.

3. Habilidad de Moe un tanto distinta.

    * > Al momento de activarse la habilidad de Moe, no genera un delay en la aparición del jefe Gorgory, sino que aumenta el delay de los movimientos posteriores al último realizado antes de que se activara la habilidad. 

4. Pausa y jefe Gorgory.

    * > Otro error que se detectó al probar el juego es que la pausa no afecta al movimiento del jefe Gorgory, esto se debe a como se modeló la actividad del enemigo. Sin embargo, todas las demás funcionalidades del botón pausa fueron correctamente implementadas.

5. Hitbox de los personajes.

| Explicación |  Imagen   |
|------------|-------------|
|Si bien el enunciado decía que en caso de colisionar cualquier parte del personaje con un obstáculo, este debía quedarse pegado. Sin embargo, para darle más perspectiva al juego, se modeló el *hitbox* de los personajes un poco más bajo que su altura, permitiendo que se vea parte de la cabeza sobre los obstáculos, como se ve en la imagen. Si esto dificulta la corrección, puede ser facilmente revertido para atenerse completamente al enunciado, redefiniendo el parámetro *ALTO_PERSONAJE* = *ALTO_BALDOSA*, al hacerlo, se logrará que el *hitbox* del personaje sea igual a su altura.| <img src="imagenes\screenshot_lisa.png" width="2560">|

---

## Referencias de código externo :octocat:

Para realizar mi tarea saqué código de:

1. Gran parte del código fue basado en los realizados para la [AF4](https://github.com/IIC2233/ivanvlam-iic2233-2021-1/tree/main/Actividades/AF4) y [AS2](https://github.com/IIC2233/ivanvlam-iic2233-2021-1/tree/main/Actividades/AS2).

2. [Limpiar un QVBoxLayout](https://forum.qt.io/topic/89218/how-to-clear-qvboxlayout-by-a-signal/6): Utilizado en la ventana de ranking para limpiar los labels de los *layouts* verticales cada vez que se carga el ranking, evitando la superposición del texto.

3. [QAStack](https://qastack.mx/programming/2749798/qlabel-set-color-of-text-and-background) y [Documentación de Qt](https://doc.qt.io/qt-5/stylesheet-examples.html): Agregar estilo y colores a los QLabels mediante *stylesheets*.

4. [Barra de progreso](https://riptutorial.com/pyqt5/example/29500/basic-pyqt-progress-bar) y [Estilo de la barra de progreso](https://www.geeksforgeeks.org/pyqt5-how-to-change-style-and-size-of-text-progress-bar/): Utilizada en las ventana de preparación y de juego para actualizar periodicamente los valores de las barras de vida y de tiempo.

5. [Combobox](https://www.techwithtim.net/tutorials/pyqt5-tutorial/comboboxes/), [Estilo de combobox](https://www.geeksforgeeks.org/pyqt5-how-to-make-text-center-align-for-non-editable-combobox/) y [Setear un valor default en un Combobox](https://www.geeksforgeeks.org/pyqt5-setting-current-text-in-combobox/): Utilizado en la ventana de preparación para seleccionar la dificultad, sin embargo, el último aspecto fue finalmente retirado del código.

6. [Drag and drop](https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5): Se investigó acerca de la implementación pero finalmente se optó por no incluirlo por temas de tiempo.

7. [Radiobutton](https://www.delftstack.com/es/tutorial/pyqt5/pyqt5-radiobutton/) y [Deseleccionar un Radiobutton](https://python-forum.io/thread-21955.html): Utilizado para la selección de personaje en la ventana de preparación.

8. [Texto a imagen png](https://www.coolgenerator.com/png-text-generator): Utilizado en las ventanas de ranking y post-ronda para una visualización más agradable a la vista.

9. [Implementación de un singleshot QTimer](https://stackoverflow.com/questions/23860665/using-qtimer-singleshot-correctly): Utilizado para lograr que, al poner pausa, los objetos sigan en pantalla por el tiempo que les restaba, y no por el tiempo total de duración. Además, se había implementado en la modelación del jefe Gorgory, pero finalmente se optó por utilizar un *QThread*.

10. [Detener un QThread mediante el método terminate()](https://stackoverflow.com/questions/42679791/how-to-stop-a-qthread-in-qt): Se utilizó para eliminar los *threads* de movimiento del jefe Gorgory una vez finalizada la ronda.

