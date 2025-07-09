
# TresEnRaya (Tic-Tac-Toe)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/5a4ef735f2ff46e6a4c6b4227d0c4816)](https://app.codacy.com/gh/draexx/TresEnRaya/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

Este es un sencillo juego de Tres en Raya (también conocido como Tic-Tac-Toe, Ta-Te-Ti, o Ceros y Cruces) implementado en Python. El juego se ejecuta en la consola y permite a dos jugadores competir entre sí.

## Descripción del Juego

El Tres en Raya es un juego de lápiz y papel entre dos jugadores, O y X, que marcan los espacios de un tablero de 3×3 alternadamente. Un jugador gana si consigue tener una línea de tres de sus símbolos: la línea puede ser horizontal, vertical o diagonal. Si todas las casillas se llenan y ningún jugador ha conseguido hacer una línea, el juego termina en empate.

## Características

*   Juego por turnos para dos jugadores (humano vs. humano).
*   Interfaz de consola clara y sencilla.
*   Tablero de 3x3.
*   Permite ingresar nombres personalizados para los jugadores.
*   Permite seleccionar el número de partidas a jugar en una sesión.
*   Muestra la puntuación actualizada después de cada partida.
*   Anuncia un ganador general al final de la sesión de juego.

## Cómo Jugar

Para jugar, sigue estos pasos:

1. **Asegúrate de tener Python instalado** en tu sistema.
2. **Descarga o clona este repositorio.**
3. **Abre una terminal** y navega hasta el directorio donde se encuentra el archivo `main.py`.
4. **Ejecuta el juego** con el siguiente comando:

```bash
python main.py
```

5. Al iniciar, el juego te dará la bienvenida y te pedirá:
    *   Ingresar el nombre para el Jugador X (puedes presionar Enter para usar "Jugador X").
    *   Ingresar el nombre para el Jugador O (puedes presionar Enter para usar "Jugador O").
    *   Especificar cuántas partidas desean jugar.
6. Una vez configurada la sesión, comenzará la primera partida. El juego te mostrará el tablero y solicitará el movimiento al jugador en turno.
7. Los movimientos se ingresan utilizando abreviaturas para las casillas del tablero:

```text
* `SI`: Superior Izquierda
* `SC`: Superior Centro
* `SD`: Superior Derecha
* `CI`: Centro Izquierda
* `CC`: Centro Centro
* `CD`: Centro Derecha
* `II`: Inferior Izquierda
* `IC`: Inferior Centro
* `ID`: Inferior Derecha

Por ejemplo, si quieres marcar la casilla del centro, escribirías `CC` y presionarías Enter.
```

8. Los jugadores (con sus nombres personalizados, si los ingresaron) se turnarán hasta que uno gane la partida o termine en empate.
9. Después de cada partida, se mostrará la puntuación actual (victorias por jugador y empates).
10. Al finalizar todas las partidas solicitadas, se mostrará un resumen final y se anunciará al ganador general de la sesión, si lo hay.

## Estructura del Código

El juego está contenido en `main.py` y se estructura de la siguiente manera:

*   **`Tablero`**: Clase que gestiona el estado del tablero de 3x3, incluyendo la impresión del tablero, la validación de movimientos, el registro de movimientos y la comprobación de si hay un ganador en la partida actual.
*   **`Ficha`**: Clase que representa a un jugador (X o O) y almacena su símbolo y nombre personalizado.
*   **`Juego`**: Clase que orquesta la lógica general de una partida. Inicializa a los dos jugadores (con sus nombres) y un tablero. Gestiona el cambio de turnos y la comprobación del ganador de la partida.
*   **`solicitar_nombres_jugadores()`**: Función que pide al usuario los nombres para los jugadores X y O.
*   **`solicitar_numero_partidas()`**: Función que pide al usuario el número de partidas a jugar y valida la entrada.
*   **`jugar_una_partida(juego)`**: Función que maneja el bucle de una única partida, incluyendo la solicitud de movimientos, la actualización del tablero y la determinación del ganador o empate de esa partida. Reinicia el tablero para la partida.
*   **Bloque `if __name__ == '__main__':`**: Es el punto de entrada principal del programa. Se encarga de:
    *   Mostrar el mensaje de bienvenida.
    *   Llamar a las funciones para solicitar los nombres de los jugadores y el número de partidas.
    *   Inicializar un objeto `Juego` con los nombres de los jugadores.
    *   Gestionar un bucle para el número total de partidas a jugar.
    *   Llamar a `jugar_una_partida()` para cada partida.
    *   Mantener y mostrar la puntuación acumulada.
    *   Anunciar los resultados finales de la sesión de juego.


## Futuras Mejoras (Posibles)

* Implementar una interfaz gráfica de usuario (GUI) en lugar de la consola.
* Añadir un modo de juego contra la computadora (IA).
* Permitir personalizar los símbolos de los jugadores.

¡Diviértete jugando!
