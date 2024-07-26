import pygame
import config
from sprites import Botao

def inicio(tela):
    clock = pygame.time.Clock()
    botao = Botao(config.LARGURA_BOTAO, config.COMPRIMENTO_BOTAO, [config.COMPRIMENTO_TELA/2 - 25, config.LARGURA_TELA/2-125])
    group = pygame.sprite.Group()
    group.add(botao)
    running = True

    while running:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = config.SAIR
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao.rect.collidepoint(event.pos):
                    estado = config.JOGO
                    running = False


             
        tela.fill("white")
        group.draw(tela)
        fonte = pygame.font.Font(None, 56)
        texto = fonte.render('JOGAR',True, 'black')
        texto_rect = texto.get_rect()
        texto_rect.x = botao.rect.x + 25
        texto_rect.y = botao.rect.y + 7
        tela.blit(texto, texto_rect)  

        pygame.display.flip()

    return estado