"""
Tic Tac Toe

Ejercicios:

1. Da a las X y O un color y grosor diferente.
2. ¿Qué sucede cuando alguien toca un espacio ya tomado?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador automático?
"""

from turtle import *
from freegames import line

def dibujar_cuadricula():
    """Dibuja una cuadrícula de tic-tac-toe con dos líneas verticales y dos horizontales."""
    line(-67, 200, -67, -200)  # Línea vertical izquierda
    line(67, 200, 67, -200)    # Línea vertical derecha
    line(-200, -67, 200, -67)  # Línea horizontal inferior
    line(-200, 67, 200, 67)    # Línea horizontal superior

def dibujar_x(x, y):
    """Dibuja una 'X' en la posición de cuadrícula dada (x, y)."""
    line(x, y, x + 133, y + 133)    # Dibuja una línea diagonal para la X
    line(x, y + 133, x + 133, y)    # Dibuja la línea diagonal opuesta para la X

def dibujar_o(x, y):
    """Dibuja una 'O' en la posición de cuadrícula dada (x, y)."""
    up()                            # Levanta el lápiz para evitar dibujar al moverlo
    goto(x + 67, y + 5)             # Coloca el lápiz en el centro del cuadrado
    down()                          # Baja el lápiz para comenzar a dibujar
    circle(62)                      # Dibuja un círculo con un radio de 62

def alinear_a_cuadricula(valor):
    """Alinea el valor dado a la posición más cercana en la cuadrícula de tamaño de 133."""
    # Redondea la posición para ajustarse a los límites de la cuadrícula
    return ((valor + 200) // 133) * 133 - 200

# Diccionario de estado del juego para rastrear el jugador actual y el estado de la cuadrícula
state = {'player': 0}  # 'player' alternará entre 0 (X) y 1 (O)
players = [dibujar_x, dibujar_o]  # Lista de funciones de dibujo para cada jugador

def manejar_toque(x, y):
    """Maneja un evento de toque en pantalla en (x, y), dibujando una X o O si el cuadro está libre."""
    x = alinear_a_cuadricula(x)         # Alinea la posición del toque a la cuadrícula
    y = alinear_a_cuadricula(y)
    player = state['player']            # Obtiene el jugador actual (0 para X, 1 para O)
    draw = players[player]              # Selecciona la función de dibujo para el jugador
    draw(x, y)                          # Dibuja X o O en la posición alineada (x, y)
    update()                            # Actualiza la pantalla
    state['player'] = not player        # Cambia al siguiente jugador

# Configuración y dibujo de la ventana de juego inicial
setup(420, 420, 370, 0)                 # Configura el tamaño y posición de la ventana
hideturtle()                            # Oculta el cursor de la tortuga
tracer(False)                           # Desactiva la animación para dibujar más rápido
dibujar_cuadricula()                    # Dibuja la cuadrícula inicial de tic-tac-toe
update()                                # Actualiza la pantalla para mostrar la cuadrícula
onscreenclick(manejar_toque)            # Asigna manejar_toque para responder a clics en pantalla
done()                                  # Mantiene la ventana abierta
