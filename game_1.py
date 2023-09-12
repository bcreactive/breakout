import pygame
import sys
from random import randint, choice
from pygame.sprite import Sprite


class Settings:
    
    def __init__(self):
        
        self.points = 0
        self.player_speed = 6
        # self.ball_speed_x = 5
        self.ball_speed_y = 5

        self.value_blue = 1
        

class Player(Sprite):
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = 100
        self.height = 30
        self.x = 400 - self.width/2
        self.x = float(self.x)
        self.y = self.screen_rect.height - self.height
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect_image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (123, 123, 123)

        self.moving_left = False
        self.moving_right = False
        self.speed = game.settings.player_speed
        
    def update(self):
        if self.moving_left == True and self.x > 0:
            self.x -= self.speed
        if self.moving_right == True and self.x < self.game.screen_width - self.width:
            self.x += self.speed
        self.rect.x = self.x
        self.rect_image.x = self.x
        self.rect_image.y = self.y - 10

    def drawme(self):
        pygame.draw.rect(self.screen, self.color, (self.rect_image))


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
               
                if self.ball_x + 2*self.ball.radius >= self.rect.left:
                    self.ball.direction_x *= -1
                
                if self.ball_y + 2*self.ball.radius >= self.rect.top:
                    self.ball.direction_y *= -1
            
                if self.ball_y <= self.rect.bottom:
                    self.ball.direction_y *= -1
                    print()


    def update(self):
        self.check_hp()
        self.check_collision(self.ball.x, self.ball.y)

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.screen, self.color, self.rect)


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
        self.y = 550
        self.x = float(self.x)
        self.y = float(self.y)
        self.color = (200, 250, 200)
        # self.speed_x = self.settings.ball_speed_x
        self.speed_y = self.settings.ball_speed_y
        values = [randint(-5, -1), randint(1, 5)]
        self.speed_x = choice(values)
        # self.speed_y = randint(-4, 8)
        self.direction_x = 1
        self.direction_y = -1
        # self.image = pygame.image.load("ballx.png")
        # self.rect = self.image.get_rect()
        self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.check_walls()
        self.check_platform()
        self.check_bottom()
        self.x += (self.speed_x * self.direction_x)
        self.y += (self.speed_y * self.direction_y)
        self.rect.x = self.x
        self.rect.y = self.y

    def check_walls(self):
        if self.x + self.radius >= self.screen_rect.right:
           self.direction_x *= -1
            
        if self.x - self.radius <= self.screen_rect.left:
            self.direction_x *= -1
           
        if self.y - self.radius <= self.screen_rect.top:
            self.direction_y *= -1
          
    def check_platform(self):
        if self.rect.colliderect(self.platform.rect):
            if not self.y + self.radius >= self.screen_rect.bottom - 29:
                self.direction_y *= -1

    def check_bottom(self):
        if self.y + self.radius >= self.screen_rect.bottom:
            print("game over!")
            exit(0)

    def change_dir(self, i):
        if self.rect.x + self.radius <= i.rect.right:
            self.direction_x *= -1
            # print(self.direction_x, self.direction_y)
        if self.rect.x - self.radius >= i.rect.left:
            self.direction_x *= -1
            # print(self.direction_x, self.direction_y)
        if self.rect.y + self.radius >= i.rect.top:
            self.direction_y *= -1
            # print(self.direction_x, self.direction_y)
        if self.rect.y <= i.rect.bottom:
            self.direction_y *= -1
            # print(self.direction_x, self.direction_y)
            # print(self.rect.y - self.radius)
            print(i.rect.bottom)
 
    def drawme(self):
        # self.screen.blit(self.image, (self.x, self.y))
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    
    
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
                self.ball.change_dir(i)
            
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

