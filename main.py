import math
import random

import pygame
from pygame import mixer

# Iniciando Pygame
pygame.init()

# Criando tela do jogo
screen = pygame.display.set_mode((800, 600))

# Descrição e Ícone
pygame.display.set_caption("Space Invaders python version")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Som
mixer.music.load("background.wav")
mixer.music.play(-1)

# Fundo
background = pygame.image.load('background.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6