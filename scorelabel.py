import pygame.font


class Scorelabel:
    """This class gets the score and prepares the image to blit."""

    def __init__(self, game):
        """Initialize score attributes."""
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        # self.score_rect = pygame.rect.Rect(0, 0, 0, 0)
        
        # Font settings
        self.label_color = (0, 100, 150)   
        self.text_color = (30, 230, 230)
        self.font = pygame.font.SysFont(None, 48)
        self.lives = self.settings.lives
        self.level = 1
        self.prep_score(0)
        self.prep_level(self.level)
       
    def prep_score(self, score):
        # Get a rendered image with the score.
        self.score = score
        score_str = f"Score: {self.score}"
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.label_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 5
        self.score_rect.top = 5
    
    def prep_level(self, level):
        # Get a rendered image with the level.
        level_str = f"Level: {level}"
        self.level_img = self.font.render(level_str, True, self.text_color,
                                            self.label_color)
        
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 280
        self.level_rect.top = 5

    def show_lives(self):
        self.lives = self.game.lives
        if self.lives == 1:
            self.screen.blit(self.game.ball.image, (10, 10))
        elif self.lives == 2:
            self.screen.blit(self.game.ball.image, (10, 10))
            self.screen.blit(self.game.ball.image, (40, 10))
        elif self.lives == 3:
            self.screen.blit(self.game.ball.image, (10, 10))
            self.screen.blit(self.game.ball.image, (40, 10))
            self.screen.blit(self.game.ball.image, (70, 10))
        elif self.lives == 4:
            self.screen.blit(self.game.ball.image, (10, 10))
            self.screen.blit(self.game.ball.image, (40, 10))
            self.screen.blit(self.game.ball.image, (70, 10))
            self.screen.blit(self.game.ball.image, (100, 10))

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.show_lives()
        

