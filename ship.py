"""Contains Ship Module for Alien Invasion Game"""

import pygame

class Ship: 
    """Manages the Ship"""

    def __init__(self, ai_game): #ship is created after the game instance is created
        """Initialize the ship and set start coordinates"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect() #treat all game elements like rectangles

        #Start each new ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom
            #the ship's rectangle coordinates are the middle bottom of the screen's middle bottom
        #rect can access: x, y, top, bottom, left, right edge, and the center

        #Flags for movement
        self.moving_right = False

    def update(self):
        """Update ship's position based on movement flags"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)
    
