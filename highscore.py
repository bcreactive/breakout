import pygame.font
import csv

class Highscore:
    """This class builds an image with the highscore."""

    def __init__(self, game):
        """Initialize attributes."""

        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.high_score = self.get_saved_highscore()
        self.high_score = int(self.high_score)

        # Font settings
        self.text_color = (130, 230, 230)
        self.font = pygame.font.SysFont(None, 60)
        self.label_color = (118, 66, 138)
        self.grats_image = None
        self.grats = False
        self.prep_grats()


    def get_saved_highscore(self):
        file_name = "save_file.csv"
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                return row[0]
           
    def save_highscore(self):
        csv_file = "save_file.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.high_score])

    def check_high_score(self):
        if self.game.points > self.high_score:
            self.high_score = self.game.points
            self.grats = True
            
    def prep_high_score(self):
        # Get a rendered high-score image.
        self.check_high_score()
        # print(self.game.points)
        high_score = self.high_score
        high_score_str = f"Highscore: {high_score}"
        self.high_score_image = self.font.render(high_score_str, True,
                                    self.text_color, self.label_color)
        
        self.high_score_rect = self.high_score_image.get_rect()  
        self.high_score_rect.x = 60
        self.high_score_rect.y = 380
        self.save_highscore()  
        self.draw_highscore()
        self.prep_grats()
    
    def prep_grats(self):
        # Shows a message, when a new high-score is achieved.
        text_color = (130, 230, 250)
        grats_str = f"!!!New Highscore!!!"
        self.grats_image = self.font.render(grats_str, True,
                                    text_color, self.label_color)
        
        self.grats_rect = self.grats_image.get_rect()  
        self.grats_rect.x = 60
        self.grats_rect.y = 320
        # self.draw_grats()

    def draw_highscore(self):
        self.screen.blit(self.high_score_image, self.high_score_rect)
        if self.grats:
            self.screen.blit(self.grats_image, self.grats_rect)
    
    # def draw_grats(self):
    #     self.screen.blit(self.grats_image, self.grats_rect)



        
        

    
