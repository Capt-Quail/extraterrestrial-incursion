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
            # Watch for the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each passthrough the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ei = ExtraterrestrialIncursion()
    ei.run_game()