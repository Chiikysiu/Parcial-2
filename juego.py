import pygame
import random
import sys


pygame.init()


ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(" Esquiva los bloques ")

NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)


reloj = pygame.time.Clock()


jugador_tam = 40
jugador_x = ANCHO // 2
jugador_y = ALTO - jugador_tam - 10
velocidad_jugador = 10


enemigo_tam = 40
enemigo_velocidad = 7
enemigos = []


def crear_enemigo():
    x = random.randint(0, ANCHO - enemigo_tam)
    y = 0
    enemigos.append([x, y])

def dibujar_enemigos():
    for enemigo in enemigos:
        pygame.draw.rect(ventana, ROJO, (enemigo[0], enemigo[1], enemigo_tam, enemigo_tam))


def mover_enemigos():
    global enemigos
    for enemigo in enemigos:
        enemigo[1] += enemigo_velocidad
    enemigos = [e for e in enemigos if e[1] < ALTO]


def colision(jugador_x, jugador_y, enemigo_x, enemigo_y):
    return (
        jugador_x < enemigo_x + enemigo_tam
        and jugador_x + jugador_tam > enemigo_x
        and jugador_y < enemigo_y + enemigo_tam
        and jugador_y + jugador_tam > enemigo_y
    )

score = 0
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_tam:
        jugador_x += velocidad_jugador

    if random.randint(1, 20) == 1:
        crear_enemigo()

    mover_enemigos()

    ventana.fill(NEGRO)

   
    pygame.draw.rect(ventana, VERDE, (jugador_x, jugador_y, jugador_tam, jugador_tam))
    dibujar_enemigos()

    
    for enemigo in enemigos:
        if colision(jugador_x, jugador_y, enemigo[0], enemigo[1]):
            print(f"💀 Fin del juego — Puntuación: {score}")
            pygame.quit()
            sys.exit()

    score += 1
    fuente = pygame.font.SysFont(None, 35)
    texto = fuente.render(f"Puntuación: {score}", True, (255, 255, 255))
    ventana.blit(texto, (10, 10))

    pygame.display.update()
    reloj.tick(30)
