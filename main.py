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
mixer.music.set_volume(0.050)
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

# Variáveis de controle de tempo
clock = pygame.time.Clock()
FPS = 60  # Limite de quadros por segundo


def mostrapontuacao(x, y):
    pontu = fonte.render("Pontuação : " + str(pontuvalor), True, (255, 255, 255))
    tela.blit(pontu, (x, y))


def gameovertexto():
    gameovertext = gameoverfonte.render("Você falhou", True, (255, 255, 255))
    tela.blit(gameovertext, (200, 250))


def player(x, y):
    tela.blit(playerImg, (x, y))


def inimigo(x, y, i):
    tela.blit(enemyImg[i], (x, y))


def balas(x, y):
    global bullet_estado
    bullet_estado = "fogo"
    tela.blit(bulletImg, (x + 16, y + 10))


def colissao(enemyX, enemyY, bulletX, bulletY):
    distancia = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distancia < 27:
        return True
    else:
        return False


# Execução do Game
executando = True
while executando:
    clock.tick(FPS)
    # RGB = Red, Green, Blue
    tela.fill((0, 0, 0))
    # Imagem de Fundo
    tela.blit(fundotela, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            executando = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_alt = -5
            if event.key == pygame.K_RIGHT:
                playerX_alt = 5
            if event.key == pygame.K_SPACE:
                if bullet_estado is "pronto":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.set_volume(0.070)
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    balas(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_alt = 0

    playerX += playerX_alt
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_de_inimigos):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_de_inimigos):
                enemyY[j] = 2000
            gameovertexto()
            break

        enemyX[i] += enemyX_alt[i]
        if enemyX[i] <= 0:
            enemyX_alt[i] = 4
            enemyY[i] += enemyY_alt[i]
        elif enemyX[i] >= 736:
            enemyX_alt[i] = -4
            enemyY[i] += enemyY_alt[i]
        # Collision
        collision = colissao(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.set_volume(0.060)
            explosionSound.play()
            bulletY = 480
            bullet_estado = "pronto"
            pontuvalor += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        inimigo(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_estado = "pronto"

    if bullet_estado is "fogo":
        balas(bulletX, bulletY)
        bulletY -= bulletY_alt

    player(playerX, playerY)
    mostrapontuacao(textX, testY)
    pygame.display.update()