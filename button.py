import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, game, msg):
        """Initialize button attributes."""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = 160
        self.height = 80
        self.button_color = (170, 0, 170)

        # Set the dimensions and properties of the button.
        if msg == "Play!":
            self.width, self.height = 180, 70
            self.button_color = (170, 0, 170)
            self.text_color = (255, 255, 85)
        elif msg == "Replay?":
            self.width, self.height = 200, 80
            self.button_color = (55, 23, 100)
            self.text_color = (255, 55, 255)

        self.font = pygame.font.SysFont(None, 60)

        # Build the button's rect object and set position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if msg == "Play!":
            self.width, self.height = 180, 70      
            self.rect.x = 500
            self.rect.y = 405
        elif msg == "Replay?":
            self.rect.x = 20
            self.rect.y = 450
        
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # Get a rendered image of the buttontext.
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        # self.border = pygame.draw.rect(self.screen, (255, 55, 255), (self.rect), 2)
        self.screen.blit(self.msg_image, self.msg_image_rect)