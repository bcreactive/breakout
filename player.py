import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.width = 100
        self.height = 30
        self.x = 400 - self.width/2
        self.x = float(self.x)
        self.y = self.screen_rect.height - self.height - 10
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect_image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (123, 123, 123)

        self.moving_left = False
        self.moving_right = False
        
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect_image = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.moving_left == True and self.x > 0:
            self.x -= self.settings.player_speed
        if self.moving_right == True and self.x < self.game.screen_width - self.width:
            self.x += self.settings.player_speed
        self.rect.x = self.x
        self.rect_image.x = self.x
        self.rect_image.y = self.y + 5
    
    def drawme(self):
        pygame.draw.rect(self.screen, self.color, (self.rect_image))
        pygame.draw.rect(self.screen, (60, 60, 60), (self.rect_image), 2)

