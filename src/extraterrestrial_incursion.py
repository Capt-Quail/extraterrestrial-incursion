import sys

import pygame

from settings import Settings
from ship import Ship

class ExtraterrestrialIncursion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # Called
        # a surface in pygame! The surface returned by display.set_mode()
        # represents the entire game window.
        pygame.display.set_caption("Extraterrestrial Incursion")

        # Initialize ship after setting up the screen
        self.ship = Ship(self)
    
    def run_game(self):
        """Start the main loop for a game."""
        while True:
            self._check_events()
            self._update_screen()
          
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ei = ExtraterrestrialIncursion()
    ei.run_game()

def _check_events(self):
    """Respond to krypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    pygame.display.flip()