import pygame
import random
from consts import *

class ArenaWall(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        super().__init__()
        self.image = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
        self.image.fill((165, 42, 42))
        self.rect = self.image.get_rect(center = position)
        self.mask = pygame.mask.from_surface(self.image)