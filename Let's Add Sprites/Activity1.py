import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('Lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('Yellow')
MAGENTA = pygame.Color('Magenta')
ORANGE = pygame.Color('Orange')
WHITE= pygame.Color('White')

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, weight):
        super(). __init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    
    def update(self):

        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or  self.rect.right



