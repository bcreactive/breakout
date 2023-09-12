import pygame
from pygame.sprite import Sprite
from random import randint

class Block(Sprite):
    
    def __init__(self, game, x, y, color="blue"):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.x = x
        self.y = y
        self.width = 160
        self.height = 140
        self.color = self.get_color(color)
        self.points = self.get_points(color)
        self.hp = self.get_hp(color)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  
        self.image_rect = pygame.Rect(self.x, self.y, self.width, self.height)  
           
        self.visible = True

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

    def update(self):
        self.check_hp()

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.screen, self.color, self.rect)
            pygame.draw.rect(self.screen, (20, 20, 20), self.rect, 1)