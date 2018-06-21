import pygame, sys

from pygame.locals import *

# inicia o pygame
pygame.init()

# inicia a janela
janela = pygame.display.set_mode((500, 400))

# inicia as cores utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fundo branco
janela.fill(WHITE)

pygame.draw.line(janela, BLUE, (60, 40), (120, 60), 4)

# roda o loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()