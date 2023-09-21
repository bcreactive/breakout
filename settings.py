class Settings:
    """This class contains the settings for the game."""
    
    def __init__(self):
        """Initialize setting attributes."""
        
        self.lives = 3
        self.points = 0

        #screen settings
        self.screen_width = 800
        self.screen_height = 600

        #speed settings
        self.player_speed = 6
        self.ball_speed = 3.07119
        self.pickup_speed = 2
       
