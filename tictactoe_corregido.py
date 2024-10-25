"""
Tic Tac Toe

Juego de Tic Tac Toe en Python usando Turtle Graphics.

Modificaciones:
1. Cambia el tamaño, color, y centra los símbolos "X" y "O".
2. Valida si una casilla ya está ocupada antes de colocar un símbolo.
"""

from turtle import *
from freegames import line


def dibujar_cuadricula():
    """Dibuja la cuadrícula de tic-tac-toe con líneas verticales y horizontales."""
    line(-67, 200, -67, -200)  # Línea vertical izquierda
    line(67, 200, 67, -200)    # Línea vertical derecha
    line(-200, -67, 200, -67)  # Línea horizontal inferior
    line(-200, 67, 200, 67)    # Línea horizontal superior


def dibujar_x(x, y):
    """Dibuja una 'X' en la posición de cuadrícula (x, y).

    La 'X' se dibuja en color azul, centrada en el cuadrado.
    """
    color("blue")               # Color de la 'X'
    width(4)                    # Grosor de las líneas
    up()
    goto(x + 10, y + 10)        # Posiciona la 'X' centrada en el cuadrado
    down()
    line(x + 10, y + 10, x + 123, y + 123)
    line(x + 10, y + 123, x + 123, y + 10)


def dibujar_o(x, y):
    """Dibuja una 'O' en la posición de cuadrícula (x, y).

    La 'O' se dibuja en color rojo y está centrada en el cuadrado.
    """
    color("red")                # Color de la 'O'
    width(4)                    # Grosor de la línea
    up()
    goto(x + 67, y + 15)        # Posiciona la 'O' centrada en el cuadrado
    down()
    circle(52)                  # Dibuja el círculo con un radio de 52


def alinear_a_cuadricula(valor):
    """Alinea el valor dado al centro de la cuadrícula de 133x133.

    Args:
        valor (int): Coordenada en el eje x o y.

    Returns:
        int: Coordenada alineada al centro de la cuadrícula.
    """
    return ((valor + 200) // 133) * 133 - 200


# Estado inicial del juego que incluye el jugador actual y un tablero vacío
state = {'player': 0, 'board': {}}  # 'board' almacena las posiciones ocupadas
players = [dibujar_x, dibujar_o]    # Lista de funciones de dibujo para cada jugador


def manejar_toque(x, y):
    """Maneja un toque en pantalla en (x, y).

    Coloca una X u O en la cuadrícula si la casilla está libre y alterna
    el turno entre jugadores.

    Args:
        x (int): Coordenada en el eje x donde se realizó el toque.
        y (int): Coordenada en el eje y donde se realizó el toque.
    """
    x = alinear_a_cuadricula(x)
    y = alinear_a_cuadricula(y)

    # Verifica si la casilla está ocupada
    if (x, y) not in state['board']:
        player = state['player']    # Obtiene el jugador actual
        draw = players[player]      # Selecciona la función de dibujo para el jugador
        draw(x, y)                  # Dibuja X o O en la posición alineada
        state['board'][(x, y)] = player  # Marca la casilla como ocupada
        update()
        state['player'] = not player  # Cambia al siguiente jugador
    else:
        print("Casilla ocupada, elige otra.")  # Mensaje si la casilla ya está ocupada


# Configuración inicial del juego
setup(420, 420, 370, 0)           # Configura el tamaño y posición de la ventana
hideturtle()                      # Oculta el cursor de la tortuga
tracer(False)                     # Desactiva la animación para dibujar más rápido
dibujar_cuadricula()              # Dibuja la cuadrícula de tic-tac-toe
update()                          # Actualiza la pantalla para mostrar la cuadrícula
onscreenclick(manejar_toque)      # Asigna manejar_toque para responder a clics en pantalla
done()                            # Mantiene la ventana abierta hasta que se cierre
