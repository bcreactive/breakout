import pygame


class Timer:
    def __init__(self, game):

        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.x = 120
        self.y = 10
        self.value = 180
        self.label_rect = pygame.Rect(self.x, self.y, 180, 20)
        self.reset()

    def reset(self):
        self.collected = False
        self.value = 180
        self.value_rect = pygame.Rect(self.x, self.y, self.value, 20)
    
    def update(self):
        if self.collected:
            if self.value == 0:
                self.collected = False
                self.value = 180
                self.value_rect = pygame.Rect(self.x, self.y, self.value, 20)
                self.game.drops_collected.append(self.game.active_drop)
                self.game.active_drop = ""
            elif self.value > 0: 
                self.value -= 1
                self.value_rect = pygame.Rect(self.x, self.y, self.value, 20)

    def drawme(self):  
        if self.collected and self.value > 0:     
            pygame.draw.rect(self.screen, (234, 234, 234), (self.label_rect))
            pygame.draw.rect(self.screen, (24, 24, 34), (self.value_rect))