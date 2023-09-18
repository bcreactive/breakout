import pygame
from pygame.sprite import Sprite


class Pickup(Sprite):
    def __init__(self, game, drop):
        super().__init__()

        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.x = 400
        self.y = 100
        self.image = drop
        self.rect = self.image.get_rect()

    def update(self):
        self.y += self.settings.pickup_speed

    def drawme(self):
        if not self.rect.top >= self.screen_rect.bottom: 
            self.screen.blit(self.image, (self.x, self.y))