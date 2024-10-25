"""
Tic Tac Toe

Modificaciones:
1. Cambia el tamaño y color de los símbolos "X" y "O" y los centra.
2. Valida si una casilla ya está ocupada antes de colocar un símbolo.
"""

from turtle import *
from freegames import line

def dibujar_cuadricula():
    """Dibuja la cuadrícula de tic-tac-toe."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def dibujar_x(x, y):
    """Dibuja una 'X' en la posición de cuadrícula (x, y) con color y tamaño personalizados."""
    color("blue")             # Color de la 'X'
    width(4)                  # Grosor de la 'X'
    up()
    goto(x + 10, y + 10)      # Posición centrada en el cuadrado
    down()
    line(x + 10, y + 10, x + 123, y + 123)
    line(x + 10, y + 123, x + 123, y + 10)

def dibujar_o(x, y):
    """Dibuja una 'O' en la posición de cuadrícula (x, y) con color y tamaño personalizados."""
    color("red")              # Color de la 'O'
    width(4)                  # Grosor de la 'O'
    up()
    goto(x + 67, y + 15)      # Posición centrada en el cuadrado
    down()
    circle(52)                # Tamaño del círculo para la 'O'

def alinear_a_cuadricula(valor):
    """Alinea el valor dado al centro de la cuadrícula."""
    return ((valor + 200) // 133) * 133 - 200

# Diccionario de estado del juego
state = {'player': 0, 'board': {}}  # 'board' almacena las posiciones ocupadas
players = [dibujar_x, dibujar_o]

def manejar_toque(x, y):
    """Maneja un toque en pantalla en (x, y), colocando X u O si el cuadro está libre."""
    x = alinear_a_cuadricula(x)
    y = alinear_a_cuadricula(y)

    # Verifica si la casilla está ocupada
    if (x, y) not in state['board']:
        player = state['player']
        draw = players[player]
        draw(x, y)
        state['board'][(x, y)] = player  # Marca la casilla como ocupada
        update()
        state['player'] = not player     # Cambia al siguiente jugador
    else:
        print("Casilla ocupada, elige otra.")

# Configuración inicial del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
dibujar_cuadricula()
update()
onscreenclick(manejar_toque)
done()
