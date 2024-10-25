from random import *
from turtle import *

from freegames import path

car_image = path('car.gif')  # carga la imagen de referencia para mostrar en el centro
tile_values = list(range(32)) * 2  # crea una lista de números pares hasta 32 y duplica
game_state = {'marked_tile': None}  # inicializa el estado para el seguimiento del tap
hidden_tiles = [True] * 64  # establece el estado de visibilidad de cada tile (ocultos)

def draw_square(tile_x, tile_y):
    """Dibuja un cuadrado blanco con borde negro en (tile_x, tile_y)."""
    up()
    goto(tile_x, tile_y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

def get_tile_index(click_x, click_y):
    """Convierte las coordenadas (click_x, click_y) en el índice de tiles."""
    # convierte coordenadas x, y a índice en la lista de tiles
    return int((click_x + 200) // 50 + ((click_y + 200) // 50) * 8)

def get_tile_coordinates(tile_index):
    """Convierte el índice del tile en coordenadas (tile_x, tile_y)."""
    # convierte índice del tile a coordenadas x, y
    return (tile_index % 8) * 50 - 200, (tile_index // 8) * 50 - 200  

def tap_tile(click_x, click_y):
    """Actualiza la marca y oculta los tiles según el tap."""
    clicked_tile = get_tile_index(click_x, click_y)
    marked_tile = game_state['marked_tile']

    # Si no hay marca previa o es el mismo tile, establece la nueva marca
    if marked_tile is None or marked_tile == clicked_tile or \
       tile_values[marked_tile] != tile_values[clicked_tile]:
        game_state['marked_tile'] = clicked_tile
    else:
        # Si coincide con el anterior, revela ambos tiles
        hidden_tiles[clicked_tile] = False
        hidden_tiles[marked_tile] = False
        game_state['marked_tile'] = None

def draw_game():
    """Dibuja la imagen y los tiles."""
    clear()
    goto(0, 0)
    shape(car_image)
    stamp()

    # Dibuja todos los tiles ocultos en sus posiciones correspondientes
    for tile_index in range(64):
        if hidden_tiles[tile_index]:
            tile_x, tile_y = get_tile_coordinates(tile_index)
            draw_square(tile_x, tile_y)

    marked_tile = game_state['marked_tile']

    # Si hay una marca y el tile está oculto, muestra el número del tile
    if marked_tile is not None and hidden_tiles[marked_tile]:
        tile_x, tile_y = get_tile_coordinates(marked_tile)
        up()
        goto(tile_x + 2, tile_y)
        color('black')
        write(tile_values[marked_tile], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw_game, 100)

shuffle(tile_values)
setup(420, 420, 370, 0)
addshape(car_image)
hideturtle()
tracer(False)
onscreenclick(tap_tile)
draw_game()
done()
