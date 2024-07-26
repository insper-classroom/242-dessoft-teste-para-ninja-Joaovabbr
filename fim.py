import pygame
import config


def fim(tela):
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = config.SAIR
                running = False

        tela.fill("white")
        fonte = pygame.font.Font(None, 56)
        texto = fonte.render(f'PONTOS DO JOGADOR: {config.PONTOS}',True, 'black')
        texto_rect = texto.get_rect()
        texto_rect.x = config.COMPRIMENTO_TELA/2 - 100
        texto_rect.y = config.LARGURA_TELA/2 - 150
        tela.blit(texto, texto_rect)  

        pygame.display.flip()

    return estado