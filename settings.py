class Settings:
    """This class contains the settings for the game."""
    
    def __init__(self):
        """Initialize setting attributes."""
        
        self.lives = 3
        self.points = 0

        #screen settings
        self.screen_width = 799
        self.screen_height = 599
        self.bg_color = (89, 111, 175)

        #speed settings
        self.player_speed = 6.5
        self.ball_speed = 3.571
        self.pickup_speed = 2
       
