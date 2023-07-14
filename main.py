import math
import random

import pygame
from pygame import mixer

# Iniciando Pygame
pygame.init()

# Criando tela do jogo
tela = pygame.display.set_mode((800, 600))

# Descrição e Ícone
pygame.display.set_caption("Space Invaders python version")
icone = pygame.image.load('ufo.png')
pygame.display.set_icon(icone)

# Som
mixer.music.load("background.wav")
mixer.music.play(-1)

# Fundo
fundotela = pygame.image.load('background.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_alt = 0

# Inimigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_alt = []
enemyY_alt = []
num_de_inimigos = 10

for i in range(num_de_inimigos):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_alt.append(4)
    enemyY_alt.append(40)

# Balas
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_alt = 0
bulletY_alt = 10
bullet_estado = "pronto"

# Pontuação
pontuvalor = 0
fonte = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
gameoverfonte = pygame.font.Font('freesansbold.ttf', 64)