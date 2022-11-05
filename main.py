import pygame
from pygame.locals import *
import random
import gameUtils
from consts import *

array_pessoas_pos = utils.getRandomPessoas(set(), PESSOAS_TOTAIS)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(TITLE)

pessoa_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))

arena_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
arena_surface.fill((165, 42, 42))

def thread(initial_pos):
    pessoa_surface.fill((0, 0, 200))
    pass

while True:
    screen.fill((50, 200, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    for pessoa in array_pessoas_pos:
        screen.blit(pessoa_surface, pessoa)

    for x in range(300):
        screen.blit(arena_surface, (x+100, 100))
        screen.blit(arena_surface, (100, x+100))
        screen.blit(arena_surface, (400-x, 400))
        screen.blit(arena_surface, (400, 400-x))

    pygame.display.update()
    clock.tick(TICK)