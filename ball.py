import pygame
import math
from random import randint
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.radius = 10
        # self.x = 400 
        # self.y = 570 - self.radiu
        self.x = 400 
        self.y = 300
        
        self.color = (200, 250, 200)
        self.speed = self.settings.ball_speed
        self.direction = 1

        self.start_point = (100, 100)
        # self.angle = self.get_angle()
        self.angle = 271
        self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.check_edges()
        self.x += self.speed * self.direction
        # self.x = self.get_new_x(self.angle)
        # self.y = self.get_new_y(self.angle)
        # print(self.x, self.y)
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        if self.x + self.radius >= self.screen_rect.right:
            self.direction *= -1
        if self.x - self.radius <= self.screen_rect.left:
            self.direction *= -1
        print(self.direction)


    def get_angle(self):
        deg_angle = randint(210, 330)
        rad_angle = deg_angle * math.pi/180
        # print(deg_angle, rad_angle)
        return rad_angle

    def get_new_x(self, angle):
        new_x = (self.speed * math.cos(angle))
        return new_x

    def get_new_y(self, angle):
         new_y = (self.speed * math.sin(angle))
         return new_y
    
    def drawme(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        