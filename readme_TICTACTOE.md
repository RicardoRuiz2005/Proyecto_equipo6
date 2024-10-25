# Tic Tac Toe

Este proyecto es un juego de Tic Tac Toe básico creado en Python, utilizando Turtle Graphics y el módulo `freegames`. Se han realizado varias modificaciones para mejorar la experiencia visual del juego y añadir validaciones. Este archivo describe los cambios realizados y proporciona instrucciones para ejecutar el juego.

## Descripción del Proyecto

El juego de Tic Tac Toe permite a dos jugadores colocar los símbolos "X" y "O" en una cuadrícula 3x3, alternando turnos. El objetivo es conseguir tres símbolos en línea, ya sea en horizontal, vertical o diagonal. En este proyecto se ha hecho un esfuerzo por seguir los estándares de codificación PEP8 y mejorar la claridad del código.

## Modificaciones Realizadas

Se realizaron las siguientes mejoras en el código original:

1. **Cambio de Tamaño, Color y Centrado de los Símbolos**:
   - La "X" ahora se dibuja en color azul y la "O" en color rojo.
   - Se ajustó el tamaño y el grosor de ambos símbolos para mejorar la visibilidad en la cuadrícula.
   - Los símbolos se centraron en sus respectivas casillas de la cuadrícula para una apariencia más estética.

2. **Validación de Casillas Ocupadas**:
   - Se implementó una validación que evita que un jugador coloque su símbolo en una casilla ya ocupada. Si una casilla ya está tomada, se imprime un mensaje en consola y el jugador debe seleccionar otra casilla.

3. **Comentarios y Documentación en PEP8**:
   - Se añadieron docstrings y comentarios en español para cada función, explicando su propósito, los parámetros y el valor de retorno (cuando aplica).
   - Se organizaron las funciones y variables siguiendo las convenciones de nombres en PEP8.
   - Las constantes y variables globales se declararon con nombres descriptivos en español.

## Estructura del Código

### Funciones Principales

- **dibujar_cuadricula**: Dibuja las líneas de la cuadrícula del juego.
- **dibujar_x**: Dibuja el símbolo "X" en la posición indicada, con tamaño y color personalizados.
- **dibujar_o**: Dibuja el símbolo "O" en la posición indicada, con tamaño y color personalizados.
- **alinear_a_cuadricula**: Alinea las coordenadas proporcionadas al centro de una casilla de la cuadrícula.
- **manejar_toque**: Maneja el toque en la pantalla, colocando un símbolo en una casilla si está libre, y alterna el turno entre los jugadores.

## Ejecución

Para ejecutar el juego en tu entorno local, sigue estos pasos:

1. **Instala las dependencias**:
   Asegúrate de que el módulo `freegames` esté instalado. Puedes instalarlo con:
   ```bash
   pip install freegames
