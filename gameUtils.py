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