import random

def getRandomPessoas(set_pessoas_pos, quant_pessoas):
    array_pessoas_pos = []
    for x in range(quant_pessoas-len(set_pessoas_pos)):
        n1 = random.randrange(11, 40)
        n2 = random.randrange(11, 40)
        array_pessoas_pos.append((n1*10, n2*10))
    set_pessoas_pos.update(array_pessoas_pos)
    if len(set_pessoas_pos) != quant_pessoas:
        set_pessoas_pos = getRandomPessoas(set_pessoas_pos, quant_pessoas)
    return set_pessoas_pos