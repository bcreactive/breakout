import pygame
import sys
from random import choice

from player import Player
from settings import Settings
from ball import Ball
from block import Block


class Game:
    """Main gameclass."""

    def __init__(self):
        pygame.init()
        
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Game")   
        self.clock = pygame.time.Clock()   
        self.fps = 30

        # self.button = 
        self.settings = Settings()
        self.platform = Player(self)
        self.ball = Ball(self)
        
        self.blocks = []
        self.level_pos = []
        # self.title_screen = 
        # self.level_screen = 
        # self.music = 
        
        self.points = 0
        self.level = 2
        self.load_next_level(self.level)       
        self.get_blocks()

        self.game_active = True
        
    
    def run_game(self):      
        while True:
            self.check_events()
            if self.game_active:
                self.platform.update()
                self.ball.update()
                for i in self.blocks:
                    i.update()
                self.update_blocks()
            self.update_screen()  
            self.clock.tick(self.fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
             
            if self.game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.platform.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.platform.moving_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.platform.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.platform.moving_right = False

    def get_color(self):
        colors = ["blue", "red", "green", "violet", "yellow"]
        return choice(colors)
    
    def get_blocks(self):
        for i in self.level_pos:
            color = self.get_color()
            new_block = Block(self, i[0], i[1], color)
            self.blocks.append(new_block)

    def update_blocks(self):
        self.check_level_end()
        for i in self.blocks:
            if self.ball.rect.colliderect(i.rect):
                # i.collision = True               
                i.hp -= 1
                if i.hp == 0:
                    self.points += i.points
                    self.blocks.remove(i)
                # self.ball.change_dir(i)
            
    def check_level_end(self):
        if len(self.blocks) == 0:
            # self.level += 1
            self.load_next_level(self.level)
            # print(self.level)
            return
            # exit()

    def load_next_level(self, level):
        if level == 1:
            self.level_pos = [(50, 50), (170, 50), (290, 50), (410, 50),
                            (530, 50), (650, 50)]
        if level == 2:
            self.level_pos = [(50, 150), (150, 150), (250, 150), (350, 150),
                            (450, 150), (550, 150), (650, 150)]
            
        if level == 3:
            self.level_pos = [(300, 300)]
        if level == 4:
            self.level_pos = [(100, 300),(300, 300),(500, 300) ]
        else:
            return
            
        # ball despawn, reset positions of platform and ball, level screen, 
        # get_blocks() ev timer 3,2,1..

    def update_screen(self):
        self.screen.fill((0, 100, 150))
        self.platform.drawme()
        self.ball.drawme()
        for i in self.blocks:
            i.draw()

        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

