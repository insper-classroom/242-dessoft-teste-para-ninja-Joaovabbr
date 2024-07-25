import pygame
import config
from pygame import Rect
from gerador import gera_numeros, gera_quadrados


pygame.init()
tela = pygame.display.set_mode((config.LARGURA_TELA, config.COMPRIMENTO_TELA))
pygame.display.set_caption("Calcula Game")
clock = pygame.time.Clock()
runing = True
nums = gera_numeros()
blocos = pygame.sprite.Group()


while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for quadrado in blocos.sprites():
                if quadrado.rect.collidepoint(event.pos):
                    print(quadrado.numero)
                    break
        

    
    tela.fill("white")
    pygame.draw.rect(tela, "gray", Rect(-10, 550, 850,250))
    gera_quadrados(config.CORES, nums, blocos, tela)
    for quadrado in blocos:
        fonte = pygame.font.Font(None, 56)
        texto = fonte.render(str(quadrado.numero),True, 'black')
        texto_rect = texto.get_rect()
        texto_rect.x = quadrado.rect.x + config.QUADRADO_LADO/2 -10
        texto_rect.y = quadrado.rect.y + config.QUADRADO_LADO/2 - 10
        tela.blit(texto, texto_rect)
    
    texto = fonte.render(str(nums[3]), True, 'black')
    texto_rect = texto.get_rect()
    texto_rect.x = 10
    texto_rect.y = 10
    tela.blit(texto, texto_rect)

    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()