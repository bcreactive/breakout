import pygame
import sys
from random import randint, choice
from time import sleep

from player import Player
from settings import Settings
from ball import Ball
from block import Block
from button import Button
from scorelabel import Scorelabel
from pickup import Pickup
from timer import Timer


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

        self.dmgup_image = pygame.image.load("images/dmg_up.png")
        self.lifeup_image = pygame.image.load("images/life_up.png")
        self.widthup_image = pygame.image.load("images/width_up.png")
        # self.title_screen = 
        # self.level_screen = 
        # self.music = 

        self.play_button = Button(self, "Play!")
        self.settings = Settings()
        self.lives = self.settings.lives
        self.platform = Player(self)
        self.ball = Ball(self)
        self.scorelabel = Scorelabel(self)
        self.pickup = Pickup(self, self.lifeup_image)
        self.timer = Timer(self)
        
        self.blocks = []
        self.level_pos = []
        self.active_drop = []
        self.drops_collected = []
        self.points = 0
        self.current_level = 1

        self.game_active = False
        self.level_running = False
        self.pickup_visible = False
        self.pickup_collected = False

        self.load_next_level(self.current_level) 
        
    # Main game loop.
    def run_game(self):      
        while True:
            self.check_events()
            if self.game_active:
                self.platform.update()
                self.ball.update()                    
                self.scorelabel.prep_score(self.points)
                if self.level_running:
                    self.check_blocks()
                    self.update_blocks()
                    self.check_level_end()
                    self.pickup.update()
                    
                    if self.pickup_visible:
                        self.check_pickup()
                    self.timer.update()
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
                self.points = 0
                self.current_level = 1
                self.ball.start_pos()
                self.level_pos = []
                self.blocks = []
                self.active_drop = []
                self.drops_collected = []
                self.load_next_level(self.current_level)
                self.get_blocks()
                self.lives = self.settings.lives               
                self.level_running = False
                self.game_active = True
                self.pickup_visible = False
                self.pickup_collected = False
                self.timer.value = 180
                self.timer.collected = False
                pygame.mouse.set_visible(False)
                # self.new_high_score = False
                # self.bonus_fruit_visible = False

    def check_spawn(self):
        value = randint(1, 1000)
        if value <= 333 and len(self.active_drop) <= 1:
            if len(self.drops_collected) <= 4:
                return True

    def create_pickup(self, rect):
        # block_rect = rect
        self.pickup = Pickup(self, self.dmgup_image)
        self.pickup.x = rect.x
        self.pickup.y = rect.y
        self.pickup_visible = True

    def check_pickup(self):     
        self.pickup_rect = pygame.Rect(self.pickup.x, self.pickup.y, 40, 40)
        if self.pickup_rect.colliderect(self.platform.rect):
            if self.pickup_visible and not self.pickup_collected:
                self.pickup_collected = True
                self.pickup_visible = False
               
                self.active_drop = []  
                self.drops_collected.append("")
                self.timer.collected = True
                self.pickup_collected = False
            return

    def get_color(self):
        if self.current_level == 1:
            colors = ["blue"]
        elif self.current_level == 2:
            colors = ["blue", "red"]
        elif self.current_level == 3:
            colors = ["blue", "red", "green", "violet"]
        elif self.current_level == 4:
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
                    
                    bonus = self.check_spawn()
                    if bonus and not self.pickup_visible:
                        self.create_pickup(i.rect)
                
    def check_blocks(self):
        for i in self.blocks:
            if self.ball.rect.colliderect(i.rect):
                if self.ball.rect.bottom >= i.rect.top and self.ball.rect.top < i.rect.top:
                    if self.ball.rect.left <= i.rect.right  and self.ball.rect.right >= i.rect.left :
                            if self.ball.direction_y == 1:
                                self.ball.direction_y *= -1
                                print("top")
                if self.ball.rect.right >= i.rect.left and self.ball.rect.left < i.rect.left: 
                    if self.ball.rect.bottom >= i.rect.top  and self.ball.rect.top <= i.rect.bottom :  
                            if self.ball.direction_x == 1:      
                                self.ball.direction_x *= -1
                                print("left")
                if self.ball.rect.left <= i.rect.right and self.ball.rect.right > i.rect.right: 
                    if self.ball.rect.bottom >= i.rect.top  and self.ball.rect.top <= i.rect.bottom:  
                            if self.ball.direction_x == -1:      
                                self.ball.direction_x *= -1
                                print("right")
                if self.ball.rect.top <= i.rect.bottom and self.ball.rect.bottom > i.rect.bottom: 
                    if self.ball.rect.left <= i.rect.right and self.ball.rect.right >= i.rect.left :  
                            if self.ball.direction_y == -1:      
                                self.ball.direction_y *= -1
                                print("bottom")
        # if self.level_running:
        #     self.check_level_end()

    def dead(self):
        self.lives -= 1
        # print fail screen
        print(self.lives)
        if self.lives > 0:
            self.level_running = False         
            self.pickup_visible = False
            self.pickup_collected = False
            self.timer.reset()
            self.ball.start_pos()
        else:
            self.play_button = Button(self, "Replay?")
            self.game_active = False
            self.level_running = False
            self.current_level = 1
            print("game over")
            pygame.mouse.set_visible(True)
            
    def check_level_end(self):
        if len(self.blocks) == 0:           
            self.level_running = False
            self.pickup_visible = False
            self.pickup_collected = False
            self.active_drop = []
            self.drops_collected = []
            self.ball.start_pos()
            self.current_level += 1
            self.load_next_level(self.current_level)
            self.get_blocks()
            self.scorelabel.prep_level(self.current_level)

    def load_next_level(self, level):
       
        if level == 1:
            self.level_pos = [
                            (250, 50), (490, 50), (310, 90), (430, 90),
                            (310, 130), (370, 130), (430, 130), (250, 170),
                            (370, 170), (490, 170), (310, 210), (430, 210),
                            (250, 250), (370, 250), (490, 250),
                            (190, 290), (550, 290)
                            ]
            
        if level == 2:
            self.level_pos = [
                            (190, 50), (370, 50), (550, 50),
                            (250, 90), (370, 90), (490, 90),
                            (130, 130), (310, 130), (370, 130), (430, 130), 
                            (610, 130), (190, 170), (250, 170), (370, 170), 
                            (490, 170), (550, 170), (310, 210), (370, 210), 
                            (430, 210), (250, 250), (490, 250), (190, 290), 
                            (250, 290), (310, 290), (370, 290), (430, 290), 
                            (490, 290), (130, 330), (190, 330), (370, 330),
                            (550, 330), (610, 330)
                            ]
            
        if level == 3:
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
        
            # if level == 1:
        #     self.level_pos = [(100, 100)]
        # if level == 1:
        #     self.level_pos = [
        #                     (250, 50), (490, 50), (310, 90), (430, 90),
        #                     ]
        # if level == 2:
        #     self.level_pos = [
        #                     (310, 130), (370, 130), (430, 130), (250, 170),

    def update_screen(self):
        self.screen.fill((0, 100, 150))

        if not self.game_active:
            self.play_button.draw_button()

        if self.game_active:
            self.timer.drawme()
            self.scorelabel.draw_score()
            if self.pickup_visible:
                self.pickup.drawme()
            self.platform.drawme()
            for i in self.blocks:
                i.drawme()                 
            self.ball.drawme()
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

