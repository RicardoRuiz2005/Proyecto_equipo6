"""Pacman, classic arcade game."""

from random import choice  # Importa choice para seleccionar movimientos al azar para los fantasmas
from turtle import *       # Importa todas las funciones gráficas de Turtle
from freegames import floor, vector  # Importa funciones adicionales para el juego

# Estado del juego y configuraciones iniciales
state = {'score': 0}          # Puntuación inicial del juego, comienza en 0
path = Turtle(visible=False)   # Turtle para dibujar el tablero sin ser visible
writer = Turtle(visible=False) # Turtle para escribir la puntuación sin ser visible
aim = vector(5, 0)             # Dirección inicial de movimiento de Pacman
pacman = vector(-40, -80)      # Posición inicial de Pacman en el tablero

# Configuración inicial de los fantasmas (posición y dirección)
# Cada fantasma tiene una posición inicial y un vector de movimiento que controla su dirección y velocidad
ghosts = [
    [vector(-180, 160), vector(10, 0)],   # Fantasma 1
    [vector(-180, -160), vector(0, 10)],  # Fantasma 2
    [vector(100, 160), vector(0, -10)],   # Fantasma 3
    [vector(100, -160), vector(-10, 0)],  # Fantasma 4
]

# Mapa del tablero (20x20) donde:
# 0 representa una pared y 1 representa un espacio con puntos comestibles
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    """Dibuja un cuadrado en la posición (x, y)"""
    path.up()           # Levanta el lápiz antes de mover
    path.goto(x, y)      # Posiciona el lápiz en las coordenadas (x, y)
    path.down()          # Baja el lápiz para comenzar a dibujar
    path.begin_fill()    # Comienza a rellenar el cuadrado
    for count in range(4):
        path.forward(20) # Dibuja el lado del cuadrado de 20 píxeles
        path.left(90)    # Gira 90 grados a la izquierda
    path.end_fill()      # Termina el relleno

def offset(point):
    """Devuelve el índice en la lista 'tiles' para una posición 'point'"""
    x = (floor(point.x, 20) + 200) / 20  # Calcula el índice x en tiles
    y = (180 - floor(point.y, 20)) / 20  # Calcula el índice y en tiles
    index = int(x + y * 20)              # Convierte x, y a un índice único en tiles
    if index < 0 or index >= len(tiles): # Comprueba si el índice está en el rango
        return None
    return index

def valid(point):
    """Comprueba si el punto está en un espacio válido (sin paredes)"""
    index = offset(point)
    if index is None or tiles[index] == 0:
        return False
    index = offset(point + 19)
    if index is None or tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    """Dibuja el tablero inicial y los puntos usando el objeto 'path'"""
    bgcolor('black')      # Fondo del tablero en negro
    path.color('blue')    # Color de las paredes en azul
    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            x = (index % 20) * 20 - 200  # Calcula posición x del tile
            y = 180 - (index // 20) * 20 # Calcula posición y del tile
            square(x, y)                 # Dibuja el cuadrado de la pared o espacio
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')     # Dibuja punto blanco para los puntos comestibles

def move():
    """Mueve pacman y los fantasmas en cada ciclo del juego"""
    writer.undo()                    # Elimina el texto de puntuación anterior
    writer.write(state['score'])     # Muestra la puntuación actualizada
    clear()                          # Limpia la pantalla antes de cada actualización
    if valid(pacman + aim):          # Si la nueva posición de pacman es válida
        pacman.move(aim)             # Mueve a pacman en la dirección actual
    index = offset(pacman)
    if index is not None and tiles[index] == 1:  # Verifica si pacman come un punto
        tiles[index] = 2            # Cambia el tile a 2 (punto comido)
        state['score'] += 1         # Incrementa la puntuación
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)                # Limpia el punto comido
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')               # Dibuja a pacman como un círculo amarillo
    for point, course in ghosts:    # Mueve a cada fantasma
        if valid(point + course):   # Si el siguiente paso es válido
            point.move(course)      # Mueve al fantasma en su dirección
        else:                       # Si hay una pared, cambia la dirección
            options = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')              # Dibuja a los fantasmas como círculos rojos
    update()                        # Actualiza la pantalla
    for point, course in ghosts:    # Verifica si algún fantasma alcanza a pacman
        if abs(pacman - point) < 20:  # Distancia menor a 20 indica colisión
            return                  # Termina el juego
    ontimer(move, 50)               # Repite el movimiento en 50 ms para mayor velocidad

def change(x, y):
    """Cambia la dirección de pacman si la nueva dirección es válida"""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Configuración de pantalla y controles
setup(420, 420, 370, 0)            # Configura el tamaño de la ventana
hideturtle()                       # Oculta el cursor de turtle
tracer(False)                      # Evita el trazado de animación para mejorar la velocidad
writer.goto(160, 160)              # Posición de la puntuación
writer.color('white')              # Color de la puntuación
writer.write(state['score'])       # Muestra la puntuación inicial
listen()                           # Escucha los eventos de teclado
# Define los controles de movimiento para pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()                            # Dibuja el tablero
move()                             # Inicia el movimiento del juego
done()                             # Finaliza el código
