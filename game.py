import pygame
import sys
from random import randint, choice
from time import *

from player import Player
from settings import Settings
from ball import Ball
from block import Block
from button import Button
from scorelabel import Scorelabel
from pickup import Pickup
from timer import Timer
from highscore import Highscore


class Game:
    """Main gameclass."""

    def __init__(self):
        pygame.init()
        
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Game")   
        self.bg_color = (23, 23, 187) #(0, 100, 150) (0, 0, 85)
        self.clock = pygame.time.Clock()   
        self.fps = 60

        self.title_screen = pygame.image.load("images/title_screen.png")
        self.end_screen = pygame.image.load("images/end_screen.png")
        self.ball_lost_screen = pygame.image.load("images/ball_lost.png")
        self.levelup_screen = pygame.image.load("images/levelup.png")
        self.dmgup_image = pygame.image.load("images/dmg_up.png")
        self.lifeup_image = pygame.image.load("images/life_up.png")
        self.widthup_image = pygame.image.load("images/width_up.png")
        self.intro_sound = pygame.mixer.Channel(0).play(
                            pygame.mixer.Sound('sound/intro.mp3')) 
        
        self.play_button = Button(self, "Play!")
        self.settings = Settings()
        self.lives = self.settings.lives
        self.platform = Player(self)
        self.ball = Ball(self)
        self.scorelabel = Scorelabel(self)
        self.pickup = Pickup(self, self.lifeup_image)
        self.timer = Timer(self)
        self.highscore = Highscore(self)
        
        self.blocks = []
        self.level_pos = []
        self.active_drop = ""
        self.drops_collected = []
        self.points = 0
        self.current_level = 1
        self.bonus = ""

        self.game_active = False
        self.level_running = False
        self.pickup_visible = False
        self.pickup_collected = False
        self.endscreen_visible = False
        self.ball_lost = False
        self.level_up = False

        self.load_next_level(self.current_level) 
        
    # Main game loop.
    def run_game(self):      
        while True:
            self.check_events()
            if self.game_active:
                if self.ball_lost:
                    pygame.time.delay(1000)
                    self.ball_lost = False
                if self.level_up:
                    pygame.time.delay(1800)
                    self.level_up = False
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/level.mp3'))
                self.platform.update()
                self.ball.update()                    
                self.scorelabel.prep_score(self.points)
                if self.level_running:
                    self.check_blocks()
                    self.update_blocks()
                    self.check_level_end()
                    self.bonus_action(self.active_drop)
                    if self.pickup_visible:
                        self.pickup.update()
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
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\\blib.wav'))
                sleep(1)
                self.points = 0
                self.current_level = 1
                self.ball.start_pos()
                self.level_pos = []
                self.blocks = []
                self.bonus = ""
                self.active_drop = ""
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
                self.endscreen_visible = False
                self.platform.moving_left = False
                self.platform.moving_right = False
                self.ball.ball_speed = self.settings.ball_speed
                self.highscore.grats = False
                self.scorelabel.prep_level(self.current_level)
                pygame.mouse.set_visible(False)
                self.intro_sound = pygame.mixer.Channel(0).play(
                                    pygame.mixer.Sound('sound/level.mp3')) 

    def bonus_action(self, drop):
        if self.pickup_collected:
            if drop == "widthup":
                self.platform.width = 180
            elif drop == "dmgup":
                self.ball.dmg = 3
        if not self.pickup_collected:
            self.ball.dmg = 1
            self.platform.width = 100

    def check_spawn(self):
        value = randint(1, 1000)
        if value <= 150 and not self.active_drop:
            if len(self.drops_collected) <= 4:
                # pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/spawn.wav'))
                return True

    def create_pickup(self, rect, image):
        self.pickup = Pickup(self, image)
        self.pickup.x = rect.x
        self.pickup.y = rect.y
        self.pickup_visible = True

    def check_pickup(self):     
        self.pickup_rect = pygame.Rect(self.pickup.x, self.pickup.y, 40, 40)

        if self.pickup_rect.colliderect(self.platform.rect):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/pickupget.wav'))
            if self.pickup_visible and not self.pickup_collected:
                if self.bonus == "lifeup" and not self.lives >= 4:
                    self.lives += 1

                self.pickup_collected = True
                self.pickup_visible = False   
                self.active_drop = self.bonus                              
                self.bonus = ""

                self.timer.collected = True
            
        if self.pickup_rect.top > self.screen_rect.bottom and self.pickup_visible:           
            self.pickup_visible = False
            self.active_drop = ""
            self.bonus = ""

    def get_pickup(self):
        value = randint(1, 1000)
        if value > 550:
            self.bonus = "widthup"
            return self.widthup_image
        elif value <= 550 and value >= 100:
            self.bonus = "dmgup"
            return self.dmgup_image
        elif value < 100:
            self.bonus = "lifeup"
            return self.lifeup_image
        
    def get_color(self):
        if self.current_level == 1:
            colors = ["blue", "red", "blue"]
        elif self.current_level == 2:
            colors = ["blue", "orange", "red", "blue", "red"]
        elif self.current_level == 3:
            colors = ["blue", "red", "orange", "blue", "orange", "red", 
                      "violet"]
        elif self.current_level >= 4:
            colors = ["blue", "red", "yellow", "orange", "violet", "orange",
                      "blue"]

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
                i.hp -= self.ball.dmg
                if i.hp <= 0:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound/blib2.wav'))
                    self.points += i.points
                    self.blocks.remove(i)
                    self.check_bonus(i)
                    
    def check_bonus(self, block):
        bonus = self.check_spawn()
        if bonus and not self.pickup_visible and not self.active_drop:
            image = self.get_pickup()
            if not self.bonus in self.drops_collected:
                self.create_pickup(block.rect, image)
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/spawn.wav'))

    def check_blocks(self):
        for i in self.blocks:
            if self.ball.rect.colliderect(i.rect):
                if self.ball.rect.bottom >= i.rect.top and self.ball.rect.top < i.rect.top:
                    if self.ball.rect.left <= i.rect.right  and self.ball.rect.right >= i.rect.left :
                            if self.ball.direction_y == 1:
                                self.ball.speed_y += 0.0117
                                self.ball.direction_y *= -1
                if self.ball.rect.right >= i.rect.left and self.ball.rect.left < i.rect.left: 
                    if self.ball.rect.bottom >= i.rect.top  and self.ball.rect.top <= i.rect.bottom :  
                            if self.ball.direction_x == 1:
                                self.ball.speed_x += 0.0132 
                                self.ball.direction_x *= -1
                if self.ball.rect.left <= i.rect.right and self.ball.rect.right > i.rect.right: 
                    if self.ball.rect.bottom >= i.rect.top  and self.ball.rect.top <= i.rect.bottom:  
                            if self.ball.direction_x == -1:    
                                self.ball.speed_x += 0.0121  
                                self.ball.direction_x *= -1
                if self.ball.rect.top <= i.rect.bottom and self.ball.rect.bottom > i.rect.bottom: 
                    if self.ball.rect.left <= i.rect.right and self.ball.rect.right >= i.rect.left :  
                            if self.ball.direction_y == -1: 
                                self.ball.speed_y -= 0.0123     
                                self.ball.direction_y *= -1

    def dead(self):
        self.lives -= 1
        if self.lives > 0:
            self.level_running = False  
            self.platform.moving_left = False
            self.platform.moving_right = False       
            self.pickup_visible = False
            self.pickup_collected = False
            self.timer.reset()
            self.ball.start_pos()
            self.active_drop = ""
            self.ball_lost = True
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound/balllost.wav'))
        else:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/fail.wav'))
            self.play_button = Button(self, "Replay?")
            self.highscore.prep_high_score()
            self.game_active = False
            self.level_running = False
            self.current_level = 1
            pygame.mouse.set_visible(True)
            self.endscreen_visible = True
            pygame.time.delay(3000)
            if self.highscore.grats:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/highscore.wav'))
            
    def check_level_end(self):
        if len(self.blocks) == 0:           
            self.level_running = False
            self.pickup_visible = False
            self.pickup_collected = False
            self.level_up = True
            self.active_drop = ""
            self.drops_collected = []
            self.ball.start_pos()
            self.current_level += 1
            self.ball.ball_speed += 0.33
            self.platform.speed += 0.7
            self.load_next_level(self.current_level)
            self.get_blocks()
            self.scorelabel.prep_level(self.current_level)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/complete.wav'))
            # pygame.time.delay(1820)
            # pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/level.mp3'))
                    
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
            self.level_pos = [
                            (70, 50), (370, 50), (670, 50), (130, 90),
                            (190, 90), (370, 90), (550, 90), (610, 90),
                            (250, 130), (310, 130), (370, 130),
                            (430, 130), (490, 130), (190, 170), (370, 170),
                            (550, 170), (130, 210), (190, 210), (250, 210),
                            (310, 210), (370, 210), (430, 210), (490, 210),
                            (550, 210), (610, 210), (250, 250), (490, 250),
                            (190, 290), (310, 290), (370, 290), (430, 290),
                            (550, 290), (70, 330), (130, 330), (370, 330),
                            (610, 330), (670, 330)
                            ]
            
        if level == 4:
            self.level_pos = [
                            (250, 50), (370, 50), (490, 50), (70, 90),
                            (190, 90), (250, 90), (310, 90), (370, 90),
                            (430, 90), (490, 90), (550, 90), (670, 90),                           
                            (70, 130), (190, 130), (310, 130), (370, 130),
                            (430, 130), (550, 130), (670, 130), (130, 170),
                            (190, 170), (370, 170), (550, 170), (610, 170),
                            (190, 210), (250, 210), (310, 210), (370, 210),
                            (430, 210), (490, 210), (550, 210), (130, 250),
                            (250, 250), (490, 250), (610, 250), (70, 290), 
                            (250, 290), (310, 290), (370, 290), (430, 290),
                            (490, 290), (670, 290), (70, 330), (190, 330),
                            (310, 330), (370, 330), (430, 330), (550, 330),
                            (670, 330)
                            ] 
            
        # if level == 5:
        #     self.level_pos = [
        #                     (30, 50), (90, 50), (150, 50), (210, 50),
        #                     (270, 50), (330, 50), (390, 50), (450, 50),
        #                     (510, 50), (570, 50),(630, 50), (690, 50),
        #                     (30, 90), (90, 90), (150, 90), (210, 90),
        #                     (270, 90), (330, 90), (390, 90), (450, 90),
        #                     (510, 90), (570, 90),(630, 90), (690, 90), 
        #                     (30, 130), (90, 130), (150, 130), (210, 130),
        #                     (270, 130), (330, 130), (390, 130), (450, 130),
        #                     (510, 130), (570, 130),(630, 130), (690, 130),
        #                     (30, 170), (90, 170), (150, 170), (210, 170),
        #                     (270, 170), (330, 170), (390, 170), (450, 170),
        #                     (510, 170), (570, 170),(630, 170), (690, 170)
        #                     ] 
            
    def update_screen(self):
        self.screen.fill(self.bg_color)

        if not self.game_active and self.endscreen_visible:
            self.screen.blit(self.end_screen, (0, 0))
            self.play_button.draw_button()
            self.highscore.draw_highscore()
        elif not self.game_active and not self.endscreen_visible:
            self.screen.blit(self.title_screen, (0, 0))
            self.play_button.draw_button()

        if self.game_active and self.ball_lost:
            self.screen.blit(self.ball_lost_screen, (0, 0))

        if self.game_active and not self.ball_lost:
            self.scorelabel.draw_score()
            if not self.active_drop == "lifeup":
                self.timer.drawme()           
            if self.pickup_visible:
                self.pickup.drawme()
            self.platform.drawme()
            for i in self.blocks:
                i.drawme()                 
            self.ball.drawme()

        if self.game_active and self.level_up:
            self.screen.blit(self.levelup_screen, (0, 0))

        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

