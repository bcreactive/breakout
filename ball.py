import pygame
from random import choice


class Ball:
    """This class builds the ball and update the position."""

    def __init__(self, game):
        """Initialize ball attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.platform = game.platform
        self.settings = game.settings

        self.radius = 10
        self.x = 388.337
        self.y = 540
        self.x = float(self.x)
        self.y = float(self.y)
        self.color = (200, 250, 200)
        self.image = pygame.image.load("images/ball.png")
        self.rect = pygame.Rect(self.x, self.y, 19.999, 19.999)
        self.start_pos()
        self.ball_speed = self.settings.ball_speed
        self.speed_y = self.ball_speed + 0.07
        values = [self.ball_speed, -self.ball_speed]
        self.speed_x = choice(values)
        self.dmg = 1

    def start_pos(self):
        # Reset start position of ball and platform.
        self.x = 388.73
        self.y = 540.03
        self.speed_x = 0
        self.speed_y = 0
        self.direction_x = 1
        self.direction_y = -1
        self.platform.x = 350
        self.dmg = 1

    def check_launch(self):
        # Waiting for a keyboard action, to launch the ball.
        if self.platform.moving_left or self.platform.moving_right:
            self.speed_y = self.ball_speed
            values = [self.ball_speed, -self.ball_speed]
            self.speed_x = choice(values)
            self.game.level_running = True

    def update(self):
        # Update the position and call methods for collisiontests.
        if not self.game.level_running:
            self.check_launch()
        if self.game.level_running:
            self.check_walls()
            self.check_platform()
            self.check_bottom()
            self.x += (self.speed_x * self.direction_x)
            self.y += (self.speed_y * self.direction_y)
            self.rect.x = self.x
            self.rect.y = self.y

    def check_walls(self):
        # Changes direction of ball, if a wall is touched.
        if self.x + 2*self.radius >= self.screen_rect.right:
            # if self.direction_x == 1:
            #     self.speed_x -= 0.022
            # elif self.direction_x == -1:
            #     self.speed_x += 0.033             
            self.direction_x *= -1
            
        if self.x <= self.screen_rect.left:
            # if self.direction_x == 1:
            #     self.speed_x -= 0.024
            # elif self.direction_x == -1:
            #     self.speed_x += 0.031
            self.direction_x *= -1
           
        if self.y <= self.screen_rect.top:           
            # self.speed_x += 0.017
            self.direction_y *= -1
          
    def check_platform(self):
        # Changes direction of ball, if the platform is touched.
        if self.rect.colliderect(self.platform.rect):

            if not self.rect.bottom >= self.screen_rect.bottom - 29.99:
                self.direction_y *= -1
            elif self.rect.bottom >= self.screen_rect.bottom - 29.99:
                self.direction_x *= -1

            if self.platform.moving_right and self.direction_x == 1:
                self.speed_x += 0.00195
            elif self.platform.moving_right and self.direction_x == -1:
                self.speed_x -= 0.00206
            elif self.platform.moving_left and self.direction_x == -1:
                self.speed_x += 0.00193
            elif self.platform.moving_left and self.direction_x == 1:
                self.speed_x -= 0.00202

    def check_bottom(self):
        # Check if ball is lost.
        if self.y + self.radius > self.screen_rect.bottom:    
            self.game.dead()  
              
    def drawme(self):
        # Draw the ball on the screen.
        self.screen.blit(self.image, (self.x, self.y))