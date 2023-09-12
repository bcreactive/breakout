import pygame
import math
from random import randint, choice, uniform
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.platform = game.platform
        self.settings = game.settings

        self.radius = 10
        self.x = 400
        self.y = 540 
        self.x = float(self.x)
        self.y = float(self.y)
        self.color = (200, 250, 200)
        # self.speed_x = self.settings.ball_speed_x
        self.speed_y = self.settings.ball_speed_y
        values = [uniform(-4.99, -0.99), uniform(0.99, 4.99)]
        self.speed_x = choice(values)
        self.direction_x = 1
        self.direction_y = -1
        self.image = pygame.image.load("ballx.png")
        self.rect = self.image.get_rect()
        # self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        # print(self.rect)

    def update(self, blocks):
        self.check_walls()
        self.check_platform()
        self.check_bottom()
        self.x += (self.speed_x * self.direction_x)
        self.y += (self.speed_y * self.direction_y)
        self.rect.x = self.x
        self.rect.y = self.y
        # if len(self.buffer) == 2:
        # self.buffer = []

    def check_walls(self):
        if self.x + 2*self.radius >= self.screen_rect.right:
           self.direction_x *= -1
            
        if self.x <= self.screen_rect.left:
            self.direction_x *= -1
           
        if self.y <= self.screen_rect.top:
            self.direction_y *= -1
          
    def check_platform(self):
        if self.rect.colliderect(self.platform.rect):

            if not self.rect.bottom >= self.screen_rect.bottom - 29:
                self.direction_y *= -1

            if self.platform.moving_right:
                self.speed_x += 0.15
                print(self.speed_x)

            if self.platform.moving_left:
                self.speed_x -= 0.149
                print(self.speed_x)

    def check_bottom(self):
        if self.y + self.radius > self.screen_rect.bottom:
            print("game over!")
            exit(0)
       
    def drawme(self):
        self.screen.blit(self.image, (self.x, self.y))