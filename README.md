# Juego de Memoria

Este es un sencillo juego de memoria desarrollado en Python, donde el objetivo es encontrar los pares de tiles (o cartas) idénticos. El juego utiliza la biblioteca `turtle` para gráficos y `random` para la generación aleatoria de tiles. Es ideal para practicar habilidades de concentración y retención de memoria.

## Características del Juego

- Muestra una cuadrícula de 64 tiles (8x8), cada uno representando un número oculto.
- El jugador debe hacer clic en los tiles para revelar el número oculto y buscar su par.
- Si se encuentra el par, ambos tiles permanecen visibles.
- La cuadrícula se vuelve a dibujar cada 100 milisegundos para actualizar el estado visual del juego.
- Se ha ajustado el código siguiendo las convenciones PEP8 para mejorar la claridad y mantener un estilo profesional y estandarizado.

## Ejercicios Pendientes

Estos son algunos ejercicios sugeridos para extender o personalizar el juego:
1. Contar y mostrar la cantidad de clics realizados.
2. Reducir el número de tiles a una cuadrícula de 4x4.
3. Detectar cuándo todos los tiles han sido revelados y mostrar un mensaje de victoria.
4. Centrar los tiles de un solo dígito.
5. Usar letras en lugar de números en los tiles.

## Estructura del Código

### Variables Principales

- `CAR_IMAGE`: imagen que aparece en el centro de la pantalla al inicio del juego.
- `TILE_VALUES`: lista de valores que se asignan aleatoriamente a los tiles.
- `GAME_STATE`: diccionario que mantiene el estado actual del juego, como el tile seleccionado.
- `HIDDEN_TILES`: lista que indica la visibilidad de cada tile (ocultos o revelados).
- `TILE_SIZE`: tamaño en píxeles de cada tile.
- `GRID_OFFSET`: desplazamiento que centra la cuadrícula en la pantalla.
- `GRID_DIMENSION`: tamaño de la cuadrícula (actualmente 8x8).

### Funciones

- `draw_square(tile_x, tile_y)`: Dibuja un cuadrado blanco en las coordenadas dadas.
- `get_tile_index(click_x, click_y)`: Convierte las coordenadas del clic a un índice de tile.
- `get_tile_coordinates(tile_index)`: Convierte el índice de tile a coordenadas en la cuadrícula.
- `tap_tile(click_x, click_y)`: Maneja la lógica cuando el jugador hace clic en un tile.
- `draw_game()`: Dibuja el estado actual del juego, incluyendo los tiles y la imagen de fondo.

## Instalación y Ejecución

1. Clona el repositorio y asegúrate de tener Python instalado en tu sistema.
2. Instala el módulo `freegames` si no está disponible:
   ```bash
   pip install freegames
