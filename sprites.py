from pygame import sprite
import pygame
import config

class Quadrado(sprite.Sprite):
    def __init__(self, cor, x, y, n,nums):
        sprite.Sprite.__init__(self)
        self.image = pygame.Surface([config.QUADRADO_LADO,config.QUADRADO_LADO])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.numero = n
        self.soma = False
        self.resultado = nums[-1]
        del nums[-1]
        del nums[nums.index(n)]
        for n in nums:
            if not self.soma and n + self.numero == self.resultado:
                self.soma = True

class Botao(sprite.Sprite):
    def __init__(self, comprimento, largura, posicao):
        sprite.Sprite.__init__(self)
        self.image = pygame.Surface([largura,comprimento])
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        