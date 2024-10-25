from random import *
from turtle import *

from freegames import path

car = path('car.gif')  # carga la imagen de referencia para mostrar en el centro
tiles = list(range(32)) * 2  # crea una lista de números pares hasta 32 y duplica los elementos para hacer pares
state = {'mark': None}  # inicializa el estado para el seguimiento del tap (marca)
hide = [True] * 64  # establece el estado de visibilidad para cada tile (inicialmente ocultos)


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x, y) en el índice de tiles."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)  # convierte coordenadas x, y a índice en la lista de tiles


def xy(count):
    """Convierte el índice del tile en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200  # convierte índice del tile a coordenadas x, y


def tap(x, y):
    """Actualiza la marca y oculta los tiles según el tap."""
    spot = index(x, y)
    mark = state['mark']

    # Si no hay marca previa o es el mismo tile, establece la nueva marca
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Si coincide con el anterior, revela ambos tiles
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Dibuja la imagen y los tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibuja todos los tiles ocultos en sus posiciones correspondientes
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # Si hay una marca y el tile está oculto, muestra el número del tile
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
