from random import *
from turtle import *

from freegames import path

CAR_IMAGE = path('car.gif')  # carga la imagen de referencia para mostrar en el centro
TILE_VALUES = list(range(32)) * 2  # crea una lista de números pares hasta 32 y duplica
GAME_STATE = {'marked_tile': None}  # inicializa el estado para el seguimiento del tap
HIDDEN_TILES = [True] * 64  # establece el estado de visibilidad de cada tile (ocultos)
TILE_SIZE = 50  # tamaño del lado de cada tile
GRID_OFFSET = 200  # desplazamiento para centrar la cuadrícula
GRID_DIMENSION = 8  # dimensión de la cuadrícula en tiles

def draw_square(tile_x, tile_y):
    """Dibuja un cuadrado blanco con borde negro en (tile_x, tile_y)."""
    up()
    goto(tile_x, tile_y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(TILE_SIZE)
        left(90)
    end_fill()

def get_tile_index(click_x, click_y):
    """Convierte las coordenadas (click_x, click_y) en el índice de tiles."""
    # convierte coordenadas x, y a índice en la lista de tiles
    return int((click_x + GRID_OFFSET) // TILE_SIZE +
               ((click_y + GRID_OFFSET) // TILE_SIZE) * GRID_DIMENSION)

def get_tile_coordinates(tile_index):
    """Convierte el índice del tile en coordenadas (tile_x, tile_y)."""
    # convierte índice del tile a coordenadas x, y
    return (tile_index % GRID_DIMENSION) * TILE_SIZE - GRID_OFFSET, \
           (tile_index // GRID_DIMENSION) * TILE_SIZE - GRID_OFFSET

def tap_tile(click_x, click_y):
    """Actualiza la marca y oculta los tiles según el tap."""
    clicked_tile = get_tile_index(click_x, click_y)
    marked_tile = GAME_STATE['marked_tile']

    # Si no hay marca previa o es el mismo tile, establece la nueva marca
    if marked_tile is None or marked_tile == clicked_tile or \
       TILE_VALUES[marked_tile] != TILE_VALUES[clicked_tile]:
        GAME_STATE['marked_tile'] = clicked_tile
    else:
        # Si coincide con el anterior, revela ambos tiles
        HIDDEN_TILES[clicked_tile] = False
        HIDDEN_TILES[marked_tile] = False
        GAME_STATE['marked_tile'] = None

def draw_game():
    """Dibuja la imagen y los tiles."""
    clear()
    goto(0, 0)
    shape(CAR_IMAGE)
    stamp()

    # Dibuja todos los tiles ocultos en sus posiciones correspondientes
    for tile_index in range(len(HIDDEN_TILES)):
        if HIDDEN_TILES[tile_index]:
            tile_x, tile_y = get_tile_coordinates(tile_index)
            draw_square(tile_x, tile_y)

    marked_tile = GAME_STATE['marked_tile']

    # Si hay una marca y el tile está oculto, muestra el número del tile
    if marked_tile is not None and HIDDEN_TILES[marked_tile]:
        tile_x, tile_y = get_tile_coordinates(marked_tile)
        up()
        goto(tile_x + 2, tile_y)
        color('black')
        write(TILE_VALUES[marked_tile], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw_game, 100)

shuffle(TILE_VALUES)
setup(420, 420, 370, 0)
addshape(CAR_IMAGE)
hideturtle()
tracer(False)
onscreenclick(tap_tile)
draw_game()
done()
