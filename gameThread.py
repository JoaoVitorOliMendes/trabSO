import pygame
import time
import random
from consts import *

go_away = False
available_doors = []
in_use_doors = []
semaphore_global = None

def pessoaThread(threadN, pessoa, screen, semaphore):
    global go_away, available_doors, in_use_doors, semaphore_global
    semaphore_global = semaphore
    acquired = False
    kill = False
    door = ()
    while not kill:
        if go_away and not acquired:
            print(f'{threadN} Acquiring')
            semaphore.acquire()
            print(f'{threadN} Acquired')
            acquired = True
            if available_doors[0]:
                door = available_doors.pop(0)
                in_use_doors.append(door)
                print(f'{threadN} GETTING')
                print(threadN, available_doors, in_use_doors, door)
        #print(threadN, available_doors, in_use_doors, door)
        pessoa.update(door, threadN)
        time.sleep(0.1)
    print(f'{threadN} Finished')
    kill = False
    semaphore_global.release()

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

    def update(self, door, threadN):
        global go_away
        if go_away:
            self.moveToDoor(door, threadN)
        else:
            self.moveRandom()
    
    def moveRandom(self):
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

    def moveToDoor(self, door, threadN):
        global semaphore_global, available_doors, in_use_doors, kill
        if self.rect.center[0] != door[0]:
            if self.rect.center[0] > door[0]:
                self.rect.center = (self.rect.center[0] - PIXEL_SIZE, self.rect.center[1])
            else:
                self.rect.center = (self.rect.center[0] + PIXEL_SIZE, self.rect.center[1])
        elif self.rect.center[1] != door[1]:
            if self.rect.center[1] > door[1]:
                self.rect.center = (self.rect.center[0], self.rect.center[1] - PIXEL_SIZE)
            else:
                self.rect.center = (self.rect.center[0], self.rect.center[1] + PIXEL_SIZE)
        elif self.rect.center[0] == door[0] and self.rect.center[1] == door[1]:
            in_use_doors.remove(door)
            available_doors.append(door)
            kill = True
            print(f'{threadN} REMOVING')
            print(threadN, self.rect.center, available_doors, in_use_doors)