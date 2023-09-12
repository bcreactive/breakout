import pygame
import sys
from random import choice
from time import sleep

from player import Player
from settings import Settings
from ball import Ball
from block import Block
from button import Button
from scorelabel import Scorelabel


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

        self.play_button = Button(self, "Play!")
        self.settings = Settings()
        self.platform = Player(self)
        self.ball = Ball(self)
        self.scorelabel = Scorelabel(self)
        
        self.blocks = []
        self.level_pos = []
        # self.title_screen = 
        # self.level_screen = 
        # self.music = 
        
        self.points = 0
        self.level = 1
        self.load_next_level(self.level)       
        self.get_blocks()

        self.game_active = False
        
    def run_game(self):      
        while True:
            self.check_events()
            if self.game_active:
                self.platform.update()
                self.ball.update(self.blocks)                    
                self.check_level_end()
                self.check_blocks()
                self.update_blocks()
                self.scorelabel.prep_score(self.points)
            self.update_screen()  
            self.clock.tick(self.fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()          
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
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

    def check_play_button(self, mouse_pos):
        """Start a new game if the player clicks Play."""
        if not self.game_active:
            if self.play_button.rect.collidepoint(mouse_pos):
                # pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound\\button.mp3'))
                sleep(1)
                # pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound\playing.mp3'))
                # self.player.reset_stats()
                self.points = 0
                self.game_active = True
                pygame.mouse.set_visible(False)
                # self.new_high_score = False
                # self.bonus_fruit_visible = False

    def get_color(self):
        colors = ["blue", "red", "green", "violet", "yellow"]
        return choice(colors)
    
    def get_blocks(self):
        for i in self.level_pos:
            color = self.get_color()
            new_block = Block(self, i[0], i[1], color)
            self.blocks.append(new_block)

    def update_blocks(self):
        for i in self.blocks:
            i.update()           
            if self.ball.rect.colliderect(i.rect):         
                i.hp -= 1
                if i.hp == 0:
                    self.points += i.points
                    self.blocks.remove(i)
                    print(self.points)

    def check_blocks(self):
        for i in self.blocks:
            if self.ball.rect.colliderect(i.rect):
                if self.ball.rect.bottom >= i.rect.top and self.ball.rect.top <= i.rect.top:
                    if self.ball.rect.left <= i.rect.right  and self.ball.rect.right >= i.rect.left :
                            if self.ball.direction_y == 1:
                                self.ball.direction_y *= -1
                                print("top")
                if self.ball.rect.right >= i.rect.left and self.ball.rect.left <= i.rect.left: 
                    if self.ball.rect.bottom >= i.rect.top  and self.ball.rect.top <= i.rect.bottom :  
                            if self.ball.direction_x == 1:      
                                self.ball.direction_x *= -1
                                print("left")
                if self.ball.rect.left <= i.rect.right and self.ball.rect.right >= i.rect.right: 
                    if self.ball.rect.bottom >= i.rect.top  and self.ball.rect.top <= i.rect.bottom:  
                            if self.ball.direction_x == -1:      
                                self.ball.direction_x *= -1
                                print("right")
                if self.ball.rect.top <= i.rect.bottom and self.ball.rect.bottom >= i.rect.bottom: 
                    if self.ball.rect.left <= i.rect.right and self.ball.rect.right >= i.rect.left :  
                            if self.ball.direction_y == -1:      
                                self.ball.direction_y *= -1
                                print("bottom")

    def check_level_end(self):
        if len(self.blocks) == 0:
            # self.level += 1
            self.load_next_level(self.level)
            # print(self.level)
            return
            # exit()

    def load_next_level(self, level):
        if level == 1:
            self.level_pos = [(30, 50), (90, 50), (150, 50), (210, 50),
                            (270, 50), (330, 50), (390, 50), (450, 50),
                            (510, 50), (570, 50),(630, 50), (690, 50),
                            (30, 90), (90, 90), (150, 90), (210, 90),
                            (270, 90), (330, 90), (390, 90), (450, 90),
                            (510, 90), (570, 90),(630, 90), (690, 90), 
                            (30, 130), (90, 130), (150, 130), (210, 130),
                            (270, 130), (330, 130), (390, 130), (450, 130),
                            (510, 130), (570, 130),(630, 130), (690, 130),
                            (30, 170), (90, 170), (150, 170), (210, 170),
                            (270, 170), (330, 170), (390, 170), (450, 170),
                            (510, 170), (570, 170),(630, 170), (690, 170)] 
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
        if not self.game_active:
            self.play_button.draw_button()
        if self.game_active:
            self.scorelabel.draw_score()
            self.platform.drawme()
            self.ball.drawme()
            for i in self.blocks:
                i.draw()
            
            
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

