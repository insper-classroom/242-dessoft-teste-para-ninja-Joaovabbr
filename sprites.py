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
        self.soma = True
        if nums.index(n) == 0 or nums.index(n) == 1:
            self.soma = True
        else:
            self.soma = False
        

