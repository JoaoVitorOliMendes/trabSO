import pygame
import time
from pessoa import Pessoa

def pessoaThread(pessoa, screen):

    while True:
        pessoa.update()
        time.sleep(0.1)