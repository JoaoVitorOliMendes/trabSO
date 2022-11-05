import pygame
import random
from consts import *

class Pessoa(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
        n1 = random.randrange(30, 150)
        n2 = random.randrange(30, 150)
        self.image.fill((n1, n2, 200))
        self.rect = self.image.get_rect(center = position)
        self.mask = pygame.mask.from_surface(self.image)
        self.last_direction = 4
    
    def update(self):
        direction = random.randrange(0, 6)

        if direction == 0 and self.rect.center[0] < (WALL_END[0]-(PIXEL_SIZE*1.5)):
            self.rect.center = (self.rect.center[0] + PIXEL_SIZE, self.rect.center[1])
            self.last_direction = direction
        elif direction == 1 and self.rect.center[0] > (WALL_START[0]+(PIXEL_SIZE*2)):
            self.rect.center = (self.rect.center[0] - PIXEL_SIZE, self.rect.center[1])
            self.last_direction = direction
        elif direction == 2 and self.rect.center[1] < (WALL_END[1]-(PIXEL_SIZE*1.5)):
            self.rect.center = (self.rect.center[0], self.rect.center[1] + PIXEL_SIZE)
            self.last_direction = direction
        elif direction == 3 and self.rect.center[1] > (WALL_START[1]+(PIXEL_SIZE*2)):
            self.rect.center = (self.rect.center[0], self.rect.center[1] - PIXEL_SIZE)
            self.last_direction = direction
        elif direction == 4:
            pass
        else:
            if self.last_direction == 0 and self.rect.center[0] < (WALL_END[0]-(PIXEL_SIZE*1.5)):
                self.rect.center = (self.rect.center[0] + PIXEL_SIZE, self.rect.center[1])
                self.last_direction = direction
            elif self.last_direction == 1 and self.rect.center[0] > (WALL_START[0]+(PIXEL_SIZE*2)):
                self.rect.center = (self.rect.center[0] - PIXEL_SIZE, self.rect.center[1])
                self.last_direction = direction
            elif self.last_direction == 2 and self.rect.center[1] < (WALL_END[1]-(PIXEL_SIZE*1.5)):
                self.rect.center = (self.rect.center[0], self.rect.center[1] + PIXEL_SIZE)
                self.last_direction = direction
            elif self.last_direction == 3 and self.rect.center[1] > (WALL_START[1]+(PIXEL_SIZE*2)):
                self.rect.center = (self.rect.center[0], self.rect.center[1] - PIXEL_SIZE)
                self.last_direction = direction