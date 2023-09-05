import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.radius = 10
        self.x = 400 
        self.y = 570 - self.radius
        
        self.color = (200, 250, 200)

        self.start_point = (100, 100)
        self.start_angle = 120


    def update(self):
        pass
        # if self.x - self.radius > 0:
        #     self.x -= self.settings.ball_speed
        # if self.x + self.radius < self.screen_rect.width:
        #     self.x += self.settings.ball_speed
        


    def drawme(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        