import pygame
from pygame.sprite import Sprite
from random import randint

class Block(Sprite):
    
    def __init__(self, game, x, y, color):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.ball = game.ball
        self.x = x
        self.y = y
        self.width = 60
        self.height = 25
        # self.width = 200
        # self.height = 100
        self.color = self.get_color(color)
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  
        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)  
        
        self.points = self.get_points(color)
        self.hp = self.get_hp(color)
           
        self.visible = True
        self.tick = 0
        # self.collision = False

    def get_color(self, col):
        if col == "blue":
            return (0, 0, 255, 0)
        elif col == "red":
            return (255, 0, 0)
        elif col == "green":
            return (0, 255, 0)
        elif col == "violet":
            return (200, 0, 200)
        elif col == "yellow":
            return (0, 200, 200)
        
    def get_points(self, col):
        if col == "blue":
            return 100
        elif col == "red":
            return 200
        elif col == "green":
            return 300
        elif col == "violet":
            return 400
        elif col == "yellow":
            return 500
        
    def get_hp(self, col):
        if col == "blue":
            return 1
        elif col == "red":
            return 2
        elif col == "green":
            return 3
        elif col == "violet":
            return 4
        elif col == "yellow":
            return 5

    def check_hp(self):     
        if self.hp == 0:
            self.visible = False

    def check_collision(self, ball_x, ball_y):
        self.ball_x = ball_x
        self.ball_y = ball_y

        if self.ball.rect.colliderect(self.rect):
        # if self.collision:
            # print("got hit!")
            if self.ball_x <= self.rect.right:
                self.ball.direction_x *= -1
                # self.collision = False
                # print(self.direction_x, self.direction_y)
            if self.ball_x + 2*self.ball.radius >= self.rect.left:
                self.ball.direction_x *= -1
                # self.collision = False
                # print(self.direction_x, self.direction_y)
            if self.ball_y + 2*self.ball.radius >= self.rect.top:
                self.ball.direction_y *= -1
                # self.collision = False
                # print(self.direction_x, self.direction_y)
            if self.ball_y <= self.ball.rect.bottom:
                self.ball.direction_y *= -1
                # self.collision = False

    def update(self):
        self.check_hp()
        self.check_collision(self.ball.x, self.ball.y)

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.screen, self.color, self.rect)