import pygame 

class Ship:
    """A class to manage the ship."""

    def __init__(self, ei_game):
        """Initialize the ship and set its starting position."""
        self.screen = ei_game.screen
        self.screen_rect = ei_game.screen.get_rect()

        # Load the ship and get its rect.
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement flags; start with a ship tha's not moving
        self.moving_right = False
        self.moving_left = False 
    
    def update(self):
          """Update the ship's position based on movement flags."""
          if self.moving_right:
               self.rect += 1 
          if self.moving_left:
               self.rect += 1           
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)