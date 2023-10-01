import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tablero de luces")

# Configuración del tablero
num_rows, num_cols = 20, 20
cell_size = width // num_cols

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Función para dibujar el tablero
def draw_board(board):
    for row in range(num_rows):
        for col in range(num_cols):
            color = white if board[row][col] else black
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Inicializar el tablero con todas las casillas apagadas
board = [[False] * num_cols for _ in range(num_rows)]

# Bucle principal
running = True
clock = pygame.time.Clock()

# Duración del encendido de cada casilla (en milisegundos)
encendido_duration = 400  # 0.4 segundos

# Tiempo de espera entre casillas (en milisegundos)
delay_between_cells = 200  # 0.2 segundos

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Apagar todas las casillas
    for row in range(num_rows):
        for col in range(num_cols):
            board[row][col] = False

    # Seleccionar una casilla al azar y encenderla
    row = random.randint(0, num_rows - 1)
    col = random.randint(0, num_cols - 1)
    board[row][col] = True

    # Dibujar el tablero
    screen.fill(black)
    draw_board(board)
    pygame.display.flip()

    # Controlar la duración del encendido
    pygame.time.delay(encendido_duration)

    # Apagar la casilla
    board[row][col] = False

    # Dibujar el tablero (casilla apagada)
    screen.fill(black)
    draw_board(board)
    pygame.display.flip()

    # Controlar el tiempo entre casillas
    pygame.time.delay(delay_between_cells)

# Salir del juego
pygame.quit()
sys.exit()
