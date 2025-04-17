from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Handles all game stats that are designed to change over time and are not tied to an individual class (similar to settings)
    """
    def __init__(self, game:'AlienInvasion') -> None:
        """Sets up all variables

        Args:
            ship_limit (int): Lives left
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

        self.current_score = 0 

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_amount
        self.score = 0
        self.level = 1
    
    def update(self, collisions):
        #update score
        self._update_score(collisions)
        #update max_score
        self._update_max_score()
        #update high score


    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')
        

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Score: {self.score}')

    def update_level(self) -> None:
        self.level += 1
        print (self.level)
