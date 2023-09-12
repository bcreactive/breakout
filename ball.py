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
        self.y = 540
        self.x = float(self.x)
        self.y = float(self.y)
        self.color = (200, 250, 200)
        self.speed_x = self.settings.ball_speed_x
        self.speed_y = self.settings.ball_speed_y
        values = [randint(-5, -1), randint(1, 5)]
        # self.speed_x = choice(values)
        # self.speed_y = randint(-4, 8)
        self.direction_x = 1
        self.direction_y = -1
        self.image = pygame.image.load("ballx.png")
        self.rect = self.image.get_rect()
        # self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        print(self.rect)

    def update(self, blocks):
        pass
        self.check_walls()
        self.check_platform()
        self.check_bottom()
        self.check_blocks(blocks)
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
            # if self.y + 2*self.radius >= self.screen_rect.bottom - 29:
                self.direction_y *= -1

    def check_bottom(self):
        if self.y + self.radius >= self.screen_rect.bottom:
            print("game over!")
            exit(0)

    def check_blocks(self, blocks):
        self.blocks = blocks
        for i in self.blocks:
            # print(i.rect)
            # print(self.rect.bottom)
            # print(self.rect)
            if self.rect.colliderect(i.rect):
                if self.rect.y + 20 > i.rect.x and self.rect.y + 20 < i.rect.x + i.height:
                    if self.rect.x < i.rect.x + i.width and self.rect.x + 20 > i.rect.x:
                        if self.direction_y == 1:
                            self.direction_y *= -1
                            print("top")
                if self.rect.right > i.rect.left and self.rect.left < i.rect.right: 
                    if self.rect.bottom > i.rect.top and self.rect.top < i.rect.bottom:  
                        if self.direction_x == 1:      
                            self.direction_x *= -1
                            print("left")
           
    def drawme(self):
        self.screen.blit(self.image, (self.x, self.y))
        # pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
# def check_blocks(self):
#         self.blocks = self.game.blocks
#         # print(self.blocks)
#         for i in self.blocks:
#             # print(i.rect)
#             # if self.rect.colliderect(i.rect):
#                 if self.rect.bottom >= i.rect.top and self.rect.top <= i.rect.bottom:
#                     if self.rect.colliderect(i.rect):
#                 # if self.rect.bottom >= i.rect.top and self.direction_y == 1 and (self.direction_x == 1 or self.direction_x == -1):
#                     # if len(self.buffer) <= 2 and not "top" in self.buffer:
#                     #     self.buffer.append("top")
#                         self.direction_y *= -1
#                         print("top")
#             # if self.rect.colliderect(i.rect):
#                 if self.rect.right >= i.rect.left and self.rect.left <= i.rect.right: 
#                     if self.rect.colliderect(i.rect):
#                 # elif self.rect.right >= i.rect.left and self.direction_x == 1 and self.direction_y == 1 or self.direction_y == -1: 
#                     # if len(self.buffer) <= 2 and not "left" in self.buffer:   
#                     #     self.buffer.append("left")  
#                         self.direction_x *= -1
#                         print("left")
            # if self.rect.colliderect(i.rect):
            #     if self.rect.left <= i.rect.right and self.direction_x == -1: 
            #         if not len(self.buffer) >= 2 and not "right" in self.buffer:   
            #             self.buffer.append("right")  
            #             self.direction_x *= -1
            #             print("right")
            # if self.rect.colliderect(i.rect):
            #     if self.rect.top <= i.rect.bottom and self.direction_y == -1:
            #         if not len(self.buffer) >= 2 and not "bottom" in self.buffer:
            #             self.buffer.append("bottom")
            #             self.direction_y *= -1
            #             print("bottom")
        # print(self.buffer)                   
                 
                
    
    # def get_site(self, block_rect):
    #     b_rect = block_rect
    #     if self.rect.bottom >= b_rect.top and self.collision:
    #         self.direction_y *= -1
    #         print("top")
    #         self.collision = False
    #     if self.rect.right >= b_rect.left and self.collision:
    #         self.direction_x *= -1
    #         print("left")
    #         self.collision = False
    #         return "right"print("top")
    #     elif self.ball_x + 20 >= self.rect.left and self.ball_y + 20 >= self.rect.top and self.ball_y <= self.rect.bottom:
    #         # self.ball.direction_x *= -1
    #         return "left"    
    #     # elif self.ball_y + 20 >= self.rect.top and self.ball_y + 20 >= self.rect.left and self.ball_y <= self.rect.right:
    #     #     # self.ball.direction_y *= -1
    #     #     return "top"
    #     elif self.ball_y <= self.rect.bottom and self.ball_y + 20 >= self.rect.left and self.ball_y <= self.rect.right:
    #         # self.ball.direction_y *= -1

    


      # def change_dir(self, i):
    #     if self.rect.x <= i.rect.right:
    #         self.direction_x *= -1
    #         # print(self.direction_x, self.direction_y)
    #     if self.rect.x + 20 >= i.rect.left:
    #         self.direction_x *= -1
    #         # print(self.direction_x, self.direction_y)
    #     if self.rect.y + 20 >= i.rect.top:
    #         self.direction_y *= -1
    #         # print(self.direction_x, self.direction_y)
    #     if self.rect.y <= i.rect.bottom:
    #         self.direction_y *= -1
    #         # print(self.direction_x, self.direction_y)
    #         # print(self.rect.y - self.radius)
    #     print(i.rect.bottom)
    #     print(self.direction_x, self.direction_y)
   
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
