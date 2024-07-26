import pygame
import config
from pygame import Rect, time
from gerador import gera_numeros, gera_quadrados


def jogo(tela):
    clock = pygame.time.Clock()
    running = True
    nums = gera_numeros()
    blocos = pygame.sprite.Group()
    textos = pygame.sprite.Group()
    jogou = False
    gera_quadrados(config.CORES, nums.copy(), blocos)
    tempo_inicial = time.get_ticks()
    tempo_clique = 1000


    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return config.SAIR
            if event.type == pygame.MOUSEBUTTONDOWN:
                for quadrado in blocos.sprites():
                    if quadrado.rect.collidepoint(event.pos):
                        if not jogou:
                            fonte = pygame.font.Font(None, 56)
                            if not quadrado.soma:
                                texto = fonte.render('Certo!', True, 'black')
                                config.PONTOS += 1
                            else:
                                texto = fonte.render('Errado!', True, 'black')
                                config.VIDAS -= 1
                            texto_rect = texto.get_rect()
                            texto_rect.center = quadrado.rect.center
                            texto_sprite = pygame.sprite.Sprite()
                            texto_sprite.image = texto
                            texto_sprite.rect = texto_rect
                            textos.add(texto_sprite)
                            
                            
                            quadrado.kill()
                            jogou = True   
                            tempo_clique = time.get_ticks()
                            
                        break
            
        if jogou:
            if time.get_ticks() - tempo_clique >= config.TEMPO_RENOVACAO:
                for texto in textos:
                    texto.kill()
                for quadrado in blocos:
                    quadrado.kill()
                nums = gera_numeros()
                gera_quadrados(config.CORES, nums.copy(), blocos)
                jogou = False


                
        
        tela.fill("white")
        pygame.draw.rect(tela, "gray", Rect(-10, 550, 850,250))
        textos.draw(tela)
        blocos.draw(tela)

        for quadrado in blocos:
            fonte = pygame.font.Font(None, 56)
            texto = fonte.render(str(quadrado.numero),True, 'black')
            texto_rect = texto.get_rect()
            texto_rect = quadrado.rect.center
            tela.blit(texto, texto_rect)
        texto = fonte.render(str(nums[3]), True, 'black')
        texto_rect = texto.get_rect()
        texto_rect.x = 10
        texto_rect.y = 10
        texto_sprite = pygame.sprite.Sprite()
        texto_sprite.image = texto
        texto_sprite.rect = texto_rect
        textos.add(texto_sprite)

        
        if time.get_ticks() - tempo_inicial >= config.TEMPO or config.VIDAS == 0:
           running= False
           return config.FIM
        pygame.display.flip()
        clock.tick(config.FPS)

    return config.FIM