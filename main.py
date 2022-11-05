import pygame
import random
import gameUtils
from pygame.locals import *
from threading import Thread
from pessoa import Pessoa
from consts import *
from gameThread import pessoaThread

array_pessoas_pos = gameUtils.getRandomPessoas(set(), PESSOAS_TOTAIS)
array_pessoas = []
array_threads = []

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(TITLE)

arena_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
arena_surface.fill(WALL_COLORS)

for x in array_pessoas_pos:
    pessoa = pygame.sprite.GroupSingle(Pessoa(x))
    thread = Thread(target=pessoaThread, args=(pessoa, screen))
    array_pessoas.append(pessoa)
    array_threads.append(thread)
    thread.start()

while True:
    screen.fill(SCREEN_COLORS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
            for x in array_threads:
                x.join()
    
    for x in array_pessoas:
        x.draw(screen)

    for x in range(WALL_SIZE[0]):
        screen.blit(arena_surface, (x+WALL_START[0], WALL_START[1]))
        screen.blit(arena_surface, (WALL_END[0]-x, WALL_END[1]))

    for x in range(WALL_SIZE[1]):
        screen.blit(arena_surface, (WALL_START[0], x+WALL_START[1]))
        screen.blit(arena_surface, (WALL_END[0], WALL_END[1]-x))

    pygame.display.update()
    clock.tick(TICK)

for x in array_threads:
    x.join()