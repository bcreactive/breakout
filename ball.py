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
        self.x = 389
        self.y = 540
        self.x = float(self.x)
        self.y = float(self.y)
        self.color = (200, 250, 200)
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.start_pos()
        self.speed_y = self.settings.ball_speed_y
        values = [uniform(-2.99, -1.99), uniform(1.99, 2.99)]
        self.speed_x = choice(values)
        # self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def start_pos(self):
        self.x = 389
        self.y = 540
        self.speed_x = 0
        self.speed_y = 0
        self.direction_x = 1
        self.direction_y = -1
        self.platform.x = 350

    def check_launch(self):
        if self.platform.moving_left or self.platform.moving_right:
            # print(self.speed_x, self.speed_y, self.temp_speed_x, self.temp_speed_y)
            # self.speed_x = self.temp_speed_x
            # self.speed_y = self.temp_speed_y
            # print(self.speed_x, self.speed_y, self.temp_speed_x, self.temp_speed_y)
            self.speed_y = self.settings.ball_speed_y
            values = [uniform(-2.99, -1.99), uniform(1.99, 2.99)]
            self.speed_x = choice(values)
            self.game.level_running = True

    def update(self):
        if not self.game.level_running:
            self.check_launch()
            # print("checking")
        if self.game.level_running:
            # print("running")
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

            if self.platform.moving_right and self.direction_x == 1:
                self.speed_x += 0.149
                print("inc")
            elif self.platform.moving_right and self.direction_x == -1:
                self.speed_x -= 0.148
                print("dec")
            elif self.platform.moving_left and self.direction_x == -1:
                self.speed_x += 0.149
                print("inc")
            elif self.platform.moving_left and self.direction_x == 1:
                self.speed_x -= 0.148
                print("dec")

    def check_bottom(self):
        if self.y + self.radius > self.screen_rect.bottom:    
            self.game.dead()  
              

    def drawme(self):
        self.screen.blit(self.image, (self.x, self.y))