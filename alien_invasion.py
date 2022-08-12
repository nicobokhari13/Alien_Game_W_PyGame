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
        #Run Game in Full Screen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        #Run Game in a Window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
            #Create window with tuple 1200 pixels wide by 800 pixels high
            #.display is a surface that represents entire game window
        self.ship = Ship(self) #game is being created, pass it as parameter for Ship constructor
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        """Start loop for game"""
        while True:
            #Refactoring into _check_events() and _update_screen()
            self._check_events()
            #Update Ship 
            self.ship.update()
            #Update screen 
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the user clicks the window's close button
                sys.exit() #exit program
            elif event.type == pygame.KEYDOWN: #if a key is pressed
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #if a key is released
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT: #if the key is the right key
            #move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self, event):
        """Response to key releases"""
        if event.key == pygame.K_RIGHT: #if the key is the right key
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Update images on screen, flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        #Draw Ship on screen 
        self.ship.blitme()
        #Make most recently drawn screen visible
        pygame.display.flip()
        


if __name__ == '__main__':
    # Make game instance, run game
    ai = AlienInvasion()
    ai.run_game()
