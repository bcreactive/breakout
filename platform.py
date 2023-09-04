import pygame


class Platform:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = 100
        self.height = 30
        self.x = 400 - self.width/2
        self.y = self.screen_rect.height - self.height
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (123, 123, 123)

        # self.rect.midbottom = self.screen_rect.midbottom
        self.moving_left = False
        self.moving_right = False
        self.speed = game.settings.speed
        
    def update(self):
        if self.moving_left == True and self.x > 0:
            self.x -= self.speed
        if self.moving_right == True and self.x < self.game.screen_width - self.width:
            self.x += self.speed
        self.rect.x = self.x

    def drawme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

