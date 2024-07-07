class GameStats:
    """Track statistics fpr Alien Invasion."""

    def __init__ (self, ei_game):
        """Initialize game statistics."""
        self.settings = ei_game.settings
        self.reset_stats()
        
        # High score should never be reset.
        self.high_score = 0
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0