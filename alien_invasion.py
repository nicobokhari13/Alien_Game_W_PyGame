import sys 

import pygame 

class AlienInvasion:
    """Manage Game Assets and Behavior"""

    def __init__(self):
        """Initialize the game, create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800)) 
            #Create window with tuple 1200 pixels wide by 800 pixels high
            #.display is a surface that represents entire game window
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start loop for game"""
        while True:
            #Watch for Keyboard and Mouse Events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Make most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance, run game
    ai = AlienInvasion()
    ai.run_game()
