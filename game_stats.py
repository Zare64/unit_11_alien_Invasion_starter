##Rover Rampage Game, Solomon Harkins, 4/17/2025
from typing import TYPE_CHECKING
import json

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

        self.init_save_scores()

    def init_save_scores(self) -> None:
        """Takes the saved highscore from the file or defaults to 0
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get('high_score', 0)
        else:
            self.high_score = 0
            self.save_scores()
            #save the file

    def save_scores(self) -> None:
        """Saves the highscore to the file
        """
        scores = {
            'high_score': self.high_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        
    def reset_stats(self) -> None:
        """Resets all stats that would change between games
        """
        self.ships_left = self.settings.starting_ship_amount
        self.score = 0
        self.level = 1
    
    def update(self, collisions) -> None:
        """Collection of all update score functions for ease of use

        Args:
            collisions (Any): All collisions that were passed 
        """
        #update score
        self._update_score(collisions)
        #update max_score
        self._update_max_score()
        #update high score
        self._update_high_score()


    def _update_max_score(self) -> None:
        """Updates the max score
        """
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')
        

    def _update_score(self, collisions) -> None:
        """Updates the score based on passed collisions

        Args:
            collisions (Any): All collisions passed, used to determine number of points to give
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Score: {self.score}')

    def update_level(self) -> None:
        """Updates the level
        """
        self.level += 1
        #print (self.level)

    def _update_high_score(self) -> None:
        """Updates the high score
        """
        if self.score > self.high_score:
            self.high_score = self.score