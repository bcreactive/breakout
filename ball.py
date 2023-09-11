import pygame
import math
from random import randint, choice
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
        self.y = 550
        self.x = float(self.x)
        self.y = float(self.y)
        self.color = (200, 250, 200)
        # self.speed_x = self.settings.ball_speed_x
        self.speed_y = self.settings.ball_speed_y
        values = [randint(-5, -1), randint(1, 5)]
        self.speed_x = choice(values)
        # self.speed_y = randint(-4, 8)
        self.direction_x = 1
        self.direction_y = -1

        self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.check_walls()
        self.check_platform()
        self.check_bottom()
        self.x += (self.speed_x * self.direction_x)
        self.y += (self.speed_y * self.direction_y)
        self.rect.x = self.x
        self.rect.y = self.y

    def check_walls(self):
        if self.x + self.radius >= self.screen_rect.right:
           self.direction_x *= -1
            
        if self.x - self.radius <= self.screen_rect.left:
            self.direction_x *= -1
           
        if self.y - self.radius <= self.screen_rect.top:
            self.direction_y *= -1
          
    def check_platform(self):
        if self.rect.colliderect(self.platform.rect):
            if not self.y + self.radius >= self.screen_rect.bottom - 29:
                self.direction_y *= -1

    def check_bottom(self):
        if self.y + self.radius >= self.screen_rect.bottom:
            print("game over!")
            exit(0)

    def change_dir(self, i):
        if self.rect.x + self.radius <= i.rect.right:
            self.direction_x *= -1
            # print(self.direction_x, self.direction_y)
        if self.rect.x - self.radius >= i.rect.left:
            self.direction_x *= -1
            # print(self.direction_x, self.direction_y)
        if self.rect.y + self.radius >= i.rect.top:
            self.direction_y *= -1
            # print(self.direction_x, self.direction_y)
        if self.rect.y <= i.rect.bottom:
            self.direction_y *= -1
            # print(self.direction_x, self.direction_y)
            # print(self.rect.y - self.radius)
            print(i.rect.bottom)
 
    def drawme(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    
    #  if self.x + self.radius <= i.rect.right:
    #         if self.angle > 270:
    #             a = 360 - self.angle
    #             b = 90 - a
    #             c = 180 - 90 - b
    #             self.angle -= (180 - 2 * c)

    #         if self.angle < 90:
    #             a = 90 - self.angle
    #             b = 180 - 90 - a
    #             self.angle += (180 - 2 * b)

    #     if self.x - self.radius >= i.rect.left:
    #         if self.angle > 180:
    #             a = self.angle - 180
    #             b = 90 - a
    #             c = 180 - 90 - b
    #             d = 90 - c
    #             self.angle = 270 + d

    #         if self.angle < 180:
    #             a = self.angle - 90
    #             self.angle = 180 - 90 -a

    #     if self.y + self.radius >= i.rect.top:
    #         if self.angle < 90:
    #             b = 180 - 90 - self.angle
    #             self.angle = 270 - b
    #         if self.angle > 90:
    #             a = 180 - self.angle
    #             b = 180 - 90 - a
    #             self.angle = 270 + b

    #     if self.y - self.radius <= i.rect.bottom:
    #         a = 360 - self.angle
    #         b = 180 - (a + 90)
    #         self.angle = ((180 - 2 * b) / 2)

    #     print(self.angle)

        # if self.x + self.radius >= self.screen_rect.right:
        #     if self.angle == 0:
        #         self.angle += 1
        #     if self.angle > 270:
        #         a = 360 - self.angle
        #         b = 90 - a
        #         c = 180 - 90 - b
        #         self.angle -= (180 - 2 * c)

        #     if self.angle < 90:
        #         a = 90 - self.angle
        #         b = 180 - 90 - a
        #         self.angle += (180 - 2 * b)
            
        # if self.x - self.radius <= self.screen_rect.left:
        #     if self.angle == 180:
        #         self.angle += 1
        #     if self.angle > 180:
        #         a = self.angle - 180
        #         b = 90 - a
        #         c = 180 - 90 - b
        #         d = 90 - c
        #         self.angle = 270 + d

        #     if self.angle < 180:
        #         a = self.angle - 90
        #         self.angle = 180 - 90 -a

        # if self.y - self.radius <= self.screen_rect.top:
        #     if self.angle == 270:
        #         self.angle += 1
        #     a = 360 - self.angle
        #     b = 180 - (a + 90)
        #     self.angle = (180 - 2 * b) / 2
