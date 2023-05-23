# robot
Este código es un juego de robots en el que dos jugadores controlan robots y se enfrentan en una batalla. Aquí hay un resumen del código:

    Se importa el módulo random, que se utiliza más adelante para barajar las cartas mágicas.
    Se define la clase Card, que representa una carta mágica. Cada carta tiene un nombre, nivel de ataque, nivel de defensa, estado, y beneficio. La función use permite usar una carta mágica en una parte específica del robot enemigo, modificando sus niveles de ataque o defensa según el estado de la carta.
    Se define la clase Part, que representa una parte del robot. Cada parte tiene un nombre, nivel de ataque, nivel de defensa y consumo de energía. La función get_status_dict devuelve un diccionario con la información de la parte.
    Se define una representación artística de un robot en forma de cadena de texto llamada robot_art.
    Se define un diccionario de colores para imprimir el texto en colores.
    Se define la clase Robot, que representa un robot en el juego. Cada robot tiene un nombre, un código de color, una cantidad de energía, una lista de partes, una lista de cartas mágicas y un contador de cartas mágicas usadas. El método greet muestra un saludo, print_energy muestra la cantidad de energía restante, attack permite que el robot ataque a otro robot en una parte específica, is_on verifica si el robot aún tiene energía, is_there_available_parts verifica si el robot tiene partes disponibles para usar, print_status muestra la información del robot y sus partes, y use_magic_card permite usar una carta mágica en una parte específica del robot.
    La función play es el bucle principal del juego. Se crean dos instancias de la clase Robot (robot_one y robot_two) con sus respectivos nombres y códigos de color. También se crean y se barajan las cartas mágicas.
    Dentro del bucle, se alterna el turno entre los robots. Se muestra el estado actual de cada robot y se solicita al jugador que elija una parte para atacar y una parte del enemigo para atacar. Luego se realiza el ataque y se actualiza el contador de rondas.
    Después de cada turno, se verifica si el robot enemigo ha perdido o si ya no tiene partes disponibles. Si alguna de estas condiciones se cumple, el juego termina y se muestra un mensaje de victoria.
    Si el jugador tiene menos de dos cartas mágicas usadas, se le da la opción de usar una carta mágica. Se muestra una lista de cartas mágicas disponibles y se solicita al jugador que elija una. Dependiendo del beneficio de la carta, se usará en el propio robot o en el enemigo.
    La función play se llama al final para comenzar el juego.
