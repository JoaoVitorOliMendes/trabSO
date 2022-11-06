import pygame
import random
import gameUtils
import time
import gameThread
from pygame.locals import *
from threading import Thread, Semaphore
from consts import *

array_pessoas_pos = gameUtils.getRandomPessoas(set(), PESSOAS_TOTAIS)
array_portas_pos = gameUtils.getRandomDoors(set(), QTD_PORTAS)
gameThread.available_doors = list(array_portas_pos)
array_pessoas = []
array_threads = []
semaphore = Semaphore(QTD_PORTAS)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(TITLE)

arena_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
arena_surface.fill(WALL_COLORS)
porta_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
porta_surface.fill(PORTA_COLORS)

y = 0
for x in array_pessoas_pos:
    pessoa = pygame.sprite.GroupSingle(gameThread.Pessoa(x))
    thread = Thread(target=gameThread.pessoaThread, args=(y, pessoa, screen, semaphore))
    array_pessoas.append(pessoa)
    array_threads.append(thread)
    thread.start()
    y += 1

startlog = time.time()

while True:
    screen.fill(SCREEN_COLORS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
            for x in array_threads:
                x.join()

    for x in range(WALL_SIZE[0]):
        screen.blit(arena_surface, (x+WALL_START[0], WALL_START[1]))
        screen.blit(arena_surface, (WALL_END[0]-x, WALL_END[1]))

    for x in range(WALL_SIZE[1]):
        screen.blit(arena_surface, (WALL_START[0], x+WALL_START[1]))
        screen.blit(arena_surface, (WALL_END[0], WALL_END[1]-x))
    
    for x in array_portas_pos:
        screen.blit(porta_surface, x)
    
    for x in array_pessoas:
        x.draw(screen)
    
    if (time.time() - startlog) > TIME_LIMIT and not gameThread.go_away:
        gameThread.go_away = True

    pygame.display.update()
    clock.tick(TICK)

for x in array_threads:
    x.join()