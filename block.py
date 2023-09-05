import pygame
from pygame.sprite import Sprite
from random import randint

class Block(Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.x = 200
        self.y = 150
        self.width = 60
        self.height = 25
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self):
        pass


    def drawme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)