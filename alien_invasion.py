import sys 

import pygame 

from settings import Settings

from ship import Ship 

class AlienInvasion:
    """Manage Game Assets and Behavior"""

    def __init__(self):
        """Initialize the game, create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
            #Create window with tuple 1200 pixels wide by 800 pixels high
            #.display is a surface that represents entire game window
        self.ship = Ship(self) #game is being created, pass it as parameter for Ship constructor
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        """Start loop for game"""
        while True:
            #Watch for Keyboard and Mouse Events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if the user clicks the window's close button
                    sys.exit() #exit program
            
            #Update screen 
            self.screen.fill(self.settings.bg_color)
            #Draw Ship on screen 
            self.ship.blitme()
            #Make most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance, run game
    ai = AlienInvasion()
    ai.run_game()
