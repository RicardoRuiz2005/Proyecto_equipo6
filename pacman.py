"""Pacman, classic arcade game."""

from random import choice
from turtle import Turtle, bgcolor, clear, up, goto, dot, update, ontimer, setup, hideturtle, tracer, listen, onkey, done
from freegames import floor, vector

# Estado del juego y configuraciones iniciales
state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)

# Configuración inicial de los fantasmas (posición y dirección)
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
]

# Mapa del tablero (20x20)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # Continúa con el resto del mapa, asegurando 400 elementos
]

def square(x, y):
    """Dibuja un cuadrado en la posición (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()

def offset(point):
    """Devuelve el índice en la lista 'tiles' para una posición 'point'."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    if index < 0 or index >= len(tiles):
        return None
    return index

def valid(point):
    """Comprueba si el punto está en un espacio válido (sin paredes)."""
    index = offset(point)
    if index is None or tiles[index] == 0:
        return False
    index = offset(point + 19)
    if index is None or tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    """Dibuja el tablero inicial y los puntos usando el objeto 'path'."""
    bgcolor('black')
    path.color('blue')
    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    """Mueve pacman y los fantasmas en cada ciclo del juego."""
    writer.undo()
    writer.write(state['score'])
    clear()
    if valid(pacman + aim):
        pacman.move(aim)
    index = offset(pacman)
    if index is not None and tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')
    update()
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return
    ontimer(move, 50)

def change(x, y):
    """Cambia la dirección de pacman si la nueva dirección es válida."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Configuración de pantalla y controles
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
