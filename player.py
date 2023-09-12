import pygame
from pygame.sprite import Sprite
from random import uniform, choice

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
        # self.speed = game.settings.player_speed
        # self.ball_start = False
        
    def update(self):
        # if not self.game.level_running:
        #     self.check_launch()
        # if not self.ball_start:
        #     self.check_launch() 
        # else:
            if self.moving_left == True and self.x > 0:
                self.x -= self.settings.player_speed
            if self.moving_right == True and self.x < self.game.screen_width - self.width:
                self.x += self.settings.player_speed
            self.rect.x = self.x
            self.rect_image.x = self.x
            self.rect_image.y = self.y + 5
    
    # def check_launch(self):
    #     if self.moving_left or self.moving_right:
    #         self.game.level_running = True
    #         self.game.ball.speed_y = self.settings.ball_speed_y
    #         values = [uniform(-4.99, -0.99), uniform(0.99, 4.99)]
    #         self.game.ball.speed_x = choice(values)


    def drawme(self):
        pygame.draw.rect(self.screen, self.color, (self.rect_image))

