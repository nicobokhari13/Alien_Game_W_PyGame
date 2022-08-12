"""Module will hold settings"""
#easier to modify game's appearance and behavior as project grows

class Settings:
    """Store all settings for Alien Invasion"""

    def __init__(self):
        """Initalize Game Settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5