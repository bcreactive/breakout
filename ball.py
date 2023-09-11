import pygame
import math
from random import randint
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
        self.speed = self.settings.ball_speed
        # self.ticker = 0
        # self.direction_x = 1
        # self.direction_y = -1

        # self.start_point = (100, 100)
        # self.angle = self.get_angle()
        self.angle = 245
        self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.check_edges()
        self.check_platform()
        self.check_bottom()
        new_x = self.get_new_x(self.angle)
        nex_y = self.get_new_y(self.angle)
        self.x += new_x
        self.y += nex_y
        self.rect.x = self.x
        self.rect.y = self.y
        # self.ticker += 1

    def check_edges(self):
        
        if self.x + self.radius >= self.screen_rect.right:
            if self.angle == 0:
                self.angle += 1
            if self.angle > 270:
                a = 360 - self.angle
                b = 90 - a
                c = 180 - 90 - b
                self.angle -= (180 - 2 * c)
                # print(self.angle)

            if self.angle < 90:
                a = 90 - self.angle
                b = 180 - 90 - a
                self.angle += (180 - 2 * b)
                # print(self.angle)
            
        if self.x - self.radius <= self.screen_rect.left:
            if self.angle == 180:
                self.angle += 1
            if self.angle > 180:
                a = self.angle - 180
                b = 90 - a
                c = 180 - 90 - b
                d = 90 - c
                self.angle = 270 + d
                # print(self.angle)

            if self.angle < 180:
                a = self.angle - 90
                # b = 180 - (a + 90)
                self.angle = 180 - 90 -a
                # print(self.angle)

        if self.y - self.radius <= self.screen_rect.top:
            if self.angle == 270:
                self.angle += 1
            a = 360 - self.angle
            b = 180 - (a + 90)
            self.angle = (180 - 2 * b) / 2
            # print(self.angle)

    def check_platform(self):
        if self.rect.colliderect(self.platform.rect):
            a = 360 - self.angle
            b = 180 - (a + 90)
            self.angle = (180 - 2 * b) / 2
            print(self.angle)
            if self.platform.moving_left:
                self.angle -= 3
            if self.platform.moving_right:
                self.angle += 3
            print(self.angle)

    def check_bottom(self):
        if self.y + self.radius >= self.screen_rect.bottom:
            print("game over!")
            exit(0)

    # def change_dir(self, i):
    #     # if self.ticker % 5 == 0:
    #     #     print(self.angle)
    #     if self.x + self.radius >= i.rect.right:
    #         a = 360 - self.angle
    #         b = 180 - (a + 90)
    #         self.angle = self.angle + 90 - 2 * b

    #     if self.x - self.radius <= i.rect.left:
    #         a = 360 - self.angle
    #         b = 180 - (a + 90)
    #         self.angle = self.angle + 90 - 2 * b

    #     if self.y - self.radius <= i.rect.top:
    #         a = 360 - self.angle
    #         b = 180 - (a + 90)
    #         self.angle = (180 - 2 * b) / 2

    #     if self.y + self.radius >= i.rect.bottom:
    #         a = 360 - self.angle
    #         b = 180 - (a + 90)
    #         self.angle = (180 - 2 * b) / 2

    def get_new_x(self, angle):
        rad_angle = angle * math.pi/180
        x = (self.speed * math.cos(rad_angle))
        return x
        
    def get_new_y(self, angle):
        rad_angle = angle * math.pi/180
        y = (self.speed * math.sin(rad_angle))
        return y
        
    def drawme(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        