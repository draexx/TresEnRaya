# TresEnRaya (Tic-Tac-Toe)

Este es un sencillo juego de Tres en Raya (también conocido como Tic-Tac-Toe, Ta-Te-Ti, o Ceros y Cruces) implementado en Python. El juego se ejecuta en la consola y permite a dos jugadores competir entre sí.

## Descripción del Juego

El Tres en Raya es un juego de lápiz y papel entre dos jugadores, O y X, que marcan los espacios de un tablero de 3×3 alternadamente. Un jugador gana si consigue tener una línea de tres de sus símbolos: la línea puede ser horizontal, vertical o diagonal. Si todas las casillas se llenan y ningún jugador ha conseguido hacer una línea, el juego termina en empate.

## Cómo Jugar

Para jugar, sigue estos pasos:

1. **Asegúrate de tener Python instalado** en tu sistema.
2. **Descarga o clona este repositorio.**
3. **Abre una terminal o consola** y navega hasta el directorio donde se encuentra el archivo `main.py`.
4. **Ejecuta el juego** con el siguiente comando:
    ```bash
    python main.py
    ```
5. El juego te mostrará el tablero y te pedirá que ingreses tu movimiento.
6. Los movimientos se ingresan utilizando abreviaturas para las casillas del tablero:

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

7. Los jugadores X y O se turnarán hasta que uno gane o el juego termine en empate.

## Estructura del Código

El juego está estructurado en las siguientes clases principales dentro de `main.py`:

* **`Ficha`**: Representa a un jugador (X o O).
* **`Tablero`**: Gestiona el estado del tablero de 3x3, incluyendo la validación de movimientos, el registro de movimientos y la comprobación de si hay un ganador.
* **`Juego`**: Orquesta la lógica general del juego, incluyendo el cambio de turnos, la interacción con el usuario para los movimientos y la determinación del estado final del juego (victoria o empate).
* **`jugar()`**: La función principal que inicializa y ejecuta el bucle del juego.

## Futuras Mejoras (Posibles)

* Implementar una interfaz gráfica de usuario (GUI) en lugar de la consola.
* Añadir un modo de juego contra la computadora (IA).
* Permitir personalizar los símbolos de los jugadores.

¡Diviértete jugando!
