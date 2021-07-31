# <span style="font-family:Bebas Neue; font-size:2em;">Tarea 1: DCCanal :ship:</span>

## Indice :octocat:
- [Introducción :speech_balloon:](#Introducción-speech_balloon)
- [Consideraciones generales :nerd_face:](#Consideraciones-generales-nerd_face)
- [Ejecución :computer:](#Ejecución-computer)
- [Librerías :books:](#Librerías-books)
- [Supuestos y consideraciones adicionales :thinking:](#Supuestos-y-consideraciones-adicionales-thinking)
- [Algunas consideraciones acerca del código y modelación :grimacing:](#Algunas-consideraciones-acerca-del-código-y-modelación-grimacing)
- [Diagrama de clases :chart_with_upwards_trend:](#Diagrama-de-clases-chart_with_upwards_trend)
- [Referencias de código externo :octocat:](#Referencias-de-código-externo-octocat)

---

## Introducción :speech_balloon:

El presente  ```README.md``` contiene una visión general del programa *DCCanal* correspondiente a la Tarea 1, además, profundiza en su ejecución, las librerías utilizadas, los supuestos considerados y las referencias de código externo incorporadas durante la elaboración del código. 

---

## Consideraciones generales :nerd_face:

*DCCanal* consiste en un sistema simulación del estado de un canal de navegación guíado por la interacción del usuario con distinos menús del programa, como el menú de inicio y de acciones. La información se organiza en una serie de archivos ```.csv```, que permiten el correcto flujo del programa mediante la creación de instancias de barcos, tripulantes, mercancías y canales, cuya información se encuentra contenida en los ya mencionados archivos, los cuales **no son modificados durante la ejecución del programa**, además, existe un archivo especial para que el usuario defina parámetros como dinero y probabilidades que influirán al ejecutar el programa. En cuanto al código, el programa se separa en ocho archivos ```.py``` redactados en español, rescatando los fundamentos de POO, herencia y properties. Por último, respecto a su ejecución, el programa cumple con todas las funciones solicitadas y no se encontraron errores al correr el código.

### Cosas implementadas y no implementadas :white_check_mark::x:

* Entidades <sub>3</sub>: **Completado** :white_check_mark:
    * Barco <sub>3.1</sub>: **Completado** :white_check_mark:
        * Barco de pasajeros: **Completado** :white_check_mark:
        * Barco Carguero: **Completado** :white_check_mark:
        * Buque: **Completado** :white_check_mark:
    * Caja de Mercancía <sub>3.2</sub>: **Completado** :white_check_mark:
    * Tripulación <sub>3.3</sub>: **Completado** :white_check_mark:
        * DCCapitán: **Completado** :white_check_mark:
        * DCCocinero: **Completado** :white_check_mark:
        * DCCarguero: **Completado** :white_check_mark:
    * Canales <sub>3.4</sub>: **Completado** :white_check_mark:
* Menús <sub>4</sub>: **Completado** :white_check_mark:
    * Menú de Inicio <sub>4.1</sub>: **Completado** :white_check_mark:
    * Menú Acciones <sub>4.2</sub>: **Completado** :white_check_mark:
        * Mostrar riesgo de encallamiento <sub>4.2.1</sub>: **Completado** :white_check_mark:
        * Desencallar barco <sub>4.2.2</sub>: **Completado** :white_check_mark:
        * Simular nueva hora <sub>4.2.3</sub>: **Completado** :white_check_mark:
        * Mostrar Estado <sub>4.2.4</sub>: **Completado** :white_check_mark:
* Archivos <sub>5</sub>: **Completado** :white_check_mark:
    * ```barcos.csv``` <sub>5.1</sub>: **Completado** :white_check_mark:
    * ```canales.csv``` <sub>5.2</sub>: **Completado** :white_check_mark:
    * ```tripulantes.csv``` <sub>5.3</sub>: **Completado** :white_check_mark:
    * ```mercancia.csv``` <sub>5.4</sub>: **Completado** :white_check_mark:
    * ```parametros.py``` <sub>5.5</sub>: **Completado** :white_check_mark:

---

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos en el mismo diirectorio del código principal:
1. ```cargar_archivos.py``` en ```T1```
2. ```barcos.py``` en ```T1```
3. ```canales.py``` en ```T1```
4. ```tripulantes.py``` en ```T1```
5. ```mercancia.py``` en ```T1```
6. ```dccanal.py``` en ```T1```
7. ```parametros.py``` en ```T1```
8. ```barcos.csv``` en ```T1```
9. ```canales.csv``` en ```T1```
10. ```tripulantes.csv``` en ```T1```
11. ```mercancia.csv``` en ```T1```

---

## Librerías :books:
### Librerías externas utilizadas :rocket:
La lista de librerías externas que utilicé fue la siguiente:

1. ```collections```: ```defaultdict```, ```deque```
2. ```abc```: ```ABC```, ```abstractmethod```
3. ```random```: ```random```
4. ```currency_converter```: ```CurrencyConverter``` (debe instalarse)



### Librerías propias :art:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cargar_archivos```: Contiene a las funciones que permiten cargar todos los datos del programa, ya sea barcos, tripulantes, mercancías y canales. Además de una función que permite reiniciar los atributos de un barco.
2. ```canales```: Contiene a la modelación de la clase *Canal*, incluyendo todos sus atributos y métodos, corresponde a gran parte del *back-end* del programa.
3. ```tripulantes```: Contiene toda la modelación de barcos, desde la clase abstracta *Tripulante* hasta las que heredan de ella, *DCCapitan*, *DCCocinero* y *DCCocinero*.
4. ```mercancia```: Contiene a la modelación de la clase *Mercancia*, sus atributos de instancia y un atributo de clase muy útil para ejecutar el método expirar.
5. ```barcos```: Contiene toda la modelación de barcos, desde la clase abstracta *Barco* hasta las que heredan de ella, *BarcoDePasajeros*, *BarcoCarguero* y *Buque*.
6. ```dccanal```: Contiene la clase *DCCanal*, la entidad principal del programa, desde donde se ejecutan los menus.
7. ```parametros```: Contiene a todos los parámetros utilizados en el programa, desde los comandos para volver y salir de cada menu hasta las probabilidades de encallar.

---

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la realización de la tarea son los siguientes:


1. El Buque no puede encallar mientras está detenido.

    * > Mientras duré un evento especial de un barco, este no puede encallar, y como el único evento especial que tiene duración de una o más horas es el del Buque, este se encuentra en un estado de libertad frente a la posibilidad de encallar.

2. El capitán vuelve a tener su habilidad cada vez que reingresa al canal.

    * > Como se reinician los atributos de cada barco luego de salir del canal, es claro que las habilidades de los tripulantes también deben reiniciarse.

3. Los parámetros siempre serán del tipo correspondiente, por lo que no se realizó manejo de errores de ese aspecto.

    * > El manejo de errores solo se realizó en el input, por lo que se deposita confianza en el usuario para que escoja los parámetros en los intervalos y tipos de datos adecuados.

4. Las multas por expiración están en dólares.

    * > Como son comunes a las mercancías de todos los barcos y el cobro se realiza al canal, se asume que los valores para las multas ingresados en el archivo ```parametros.py``` están en USD.

5. El producto entre tendencia_encallar y dificultad_canal siempre sera un número entre 0 y 1.

    * > Al constituir una probabilidad, se debe encontrar entre 0 y 1, por lo que se asume que el usuario definirá los parámetros correspondientes tomando esto en consideración.

---

## Algunas consideraciones acerca del código y modelación :grimacing:

1. Las habilidades de los tripulantes son aplicadas automáticamente mediante métodos y properties del barco, y no mediante métodos del tripulante.

    * > Fue definido de esta forma por simplicidad al momento de instanciar los barcos, si se analiza el flujo del programa se verá que se encuentran todas las instancias de los integrantes de la tripulación antes de instanciar el barco, por lo que la función ejecutar_habilidades() ,que se ejecuta dentro del *\_\_init\_\_* de cada barco, comprueba la presencia de *DCCarguero* y *DCCocinero* para aplicar sus bonus a la carga máxima y mercancía de tipo alimento.

2. Se intentó modelar el tiempo_expiracion como property mediante el código:

    ```python
    @property
    def tiempo_expiracion(self):
        return self.__tiempo_expiracion
    
    @tiempo_expiracion.setter
    def tiempo_expiracion(self, valor):
        if valor < 0:
            self.__tiempo_expiracion = 0
        else:
            self.__tiempo_expiracion = valor
    ```

    Sin embargo, no funcionó como debía, por lo que se optó por dejarlo como atributo de instancia, asumiendo que un valor menor o igual a 0 significa que la mercancía expiró.

3. En el diagrama de clases no sabía como diferenciar a un atributo de instancia de atributo de clase, por lo que este último se representó de la forma ```NombreClase.nombre_atributo```.

4. En el diagrama de clases se representan todos los tipos de dinero como *float* debido a que, en muchos casos, dependen de la conversión a otra moneda, es decir, dependen de la función *convert* de la clase *CurrencyConverter*, cuyo output en la mayoría de los casos corresponde a un *float*.

5. En la clase DCCanal del diagrama de clases se indica como ```method/bool``` a lo que retorna cada función, debido a que se modeló de forma qwue el usuario fuera avanzando entre menús, permitiendo la interacción entre ellos. En cuanto al bool, siempre es ```False``` e indica la salida del programa.

6. La implementación del método *\_\_repr\_\_* en varias clases fue con la intención de comprobar si se estaba realizando bien la carga de archivos ```.csv```.

7. Al entregarse el estado de los barcos actuales en el canal, se mostrará algo de la forma:

    ```
    ----------------- Barcos en el canal ------------------

               ________________
    ~~~~~~~~~~/ Nombre Barco 1 \~ (KM Barco 1/KM canal) ~~~
              ------------------
        __________________
    ~~~~\ Nombre Barco 2 /~ (KM Barco 2/KM canal) ~~~~~~~~~
         ----------------
    ```
    En este caso, el Barco 1 se encuentra **encallado** en la posición KM Barco 1, mientras que el Barco 2 se encuentra **desencallado** en la posición KM Barco 2. Los barcos siempre se mostrarán en orden decreciente, es decir, los barcos que van más adelante en el canal primero.

---

## Diagrama de clases :chart_with_upwards_trend:

<img title="Diagrama de clases" alt="" src="Diagrama DCCanal.jpg">

---

## Referencias de código externo :octocat:

Para realizar mi tarea saqué código de:
1. [Obtener el nombre de la clase a partir de una instancia](https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance)
2. [Cómo usar CurrencyConverter](https://pypi.org/project/CurrencyConverter/)
3. [Cómo se representa una clase abstracta en un diagrama de clases](https://stackoverflow.com/questions/46049761/how-to-present-an-abstract-class-in-uml-class-diagram#46049899): En el avance de la tarea se señaló que no explicitaba las clases abstractas en el diagrama de clases, sin embargo, utilicé esta guía para indicarlos. De igual manera, en el diagrama final lo escribí como ```NombreClase (ABC)```.
4. [Cómo agregar imágenes al README](https://www.digitalocean.com/community/tutorials/markdown-markdown-images)


