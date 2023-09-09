import pygame
import sys

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
        self.fps = 60

        self.settings = Settings()
        self.platform = Player(self)
        self.ball = Ball(self)
        self.block = Block(self, 200, 200, "yellow")
        self.level = 1
        self.load_level(self.level)
        self.game_active = True
    
    def run_game(self):      
        while True:
            self.check_events()
            if self.game_active:
                self.platform.update()
                self.ball.update()
                self.block.update()
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

    def load_level(self, level):
        pass

    def update_screen(self):
        self.screen.fill((0, 100, 150))
        # self.platform.drawme()
        self.ball.drawme()
        # self.block.drawme()

        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

