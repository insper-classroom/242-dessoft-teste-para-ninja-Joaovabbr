import pygame
import config
from jogo import jogo
from inicio import inicio
from fim import fim
pygame.init()
tela = pygame.display.set_mode((config.LARGURA_TELA, config.COMPRIMENTO_TELA))
pygame.display.set_caption('Calcula Game')


estado = config.INICIO

while estado != config.SAIR:
    if estado == config.INICIO:
        estado = inicio(tela)
    elif estado == config.JOGO:
        estado = jogo(tela)
    elif estado == config.FIM:
        estado = fim(tela)