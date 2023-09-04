import pygame
import sys

class Game:
    """Main gameclass."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()   
        self.fps = 60
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Game")      
    
    def run_game(self):      
        while True:
            self.check_events()
            # if self.game_active:
                
            self.update_screen()  
            self.clock.tick(self.fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
             
            # if self.game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not self.player.direction == "s":
                        self.player.direction = "n"
                     
                            
    def update_screen(self):
        self.screen.fill((0, 0, 0))
       

        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

