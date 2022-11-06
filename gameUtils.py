import random
from consts import *

def getRandomPessoas(set_pessoas_pos, quant_pessoas):
    array_pessoas_pos = []
    for x in range(quant_pessoas-len(set_pessoas_pos)):
        n1 = random.randrange(WALL_START[0]/PIXEL_SIZE, WALL_END[0]/PIXEL_SIZE)
        n2 = random.randrange(WALL_START[1]/PIXEL_SIZE, WALL_END[1]/PIXEL_SIZE)
        array_pessoas_pos.append(((n1*PIXEL_SIZE) + PIXEL_SIZE, n2*PIXEL_SIZE))
    set_pessoas_pos.update(array_pessoas_pos)
    if len(set_pessoas_pos) != quant_pessoas:
        set_pessoas_pos = getRandomPessoas(set_pessoas_pos, quant_pessoas)
    return set_pessoas_pos


def getRandomDoors(set_portas_pos, quant_portas):
    array_portas_pos = []
    for x in range(quant_portas-len(set_portas_pos)):
        n1 = random.choice([0, 1])
        n2 = random.randrange((WALL_START[n1]/PIXEL_SIZE) + PIXEL_SIZE, (WALL_END[n1]/PIXEL_SIZE) - PIXEL_SIZE)
        n3 = random.choice([WALL_START, WALL_END])
        n2 = n2*PIXEL_SIZE
        if n1:
            if n3 == WALL_START:
                array_portas_pos.append((n2, n3[n1]))
            else:
                array_portas_pos.append((n2, n3[n1]))
        else:
            if n3 == WALL_START:
                array_portas_pos.append((n3[n1], n2))
            else:
                array_portas_pos.append((n3[n1], n2))
    set_portas_pos.update(array_portas_pos)
    if len(set_portas_pos) != quant_portas:
        set_portas_pos = getRandomDoors(set_portas_pos, quant_portas)
    return set_portas_pos