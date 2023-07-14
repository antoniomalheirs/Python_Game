import math
import random

import pygame
from pygame import mixer

# Iniciando Pygame
pygame.init()

# Criando tela do jogo
screen = pygame.display.set_mode((600, 250))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Descrição e Ícone
pygame.display.set_caption("Space Invaders python version")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)