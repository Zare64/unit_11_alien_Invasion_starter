##Rover Rampage Game, Solomon Harkins, 4/4/2025
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class RoverArsenal:
    """Class that manages all player bullets
    """

    def __init__(self, game:'AlienInvasion') -> None:
        """Sets up all attributes for the arsenal

        Args:
            game (AlienInvasion): The game for later reference of typically used for getting setting info
        """
        self.game = game
        self.settings = game.settings.screen = game.screen
        self.arsenal = pygame.sprite.Group()
    
    def update_arsenal(self) -> None:
        """Handles any part of the arsenal that requires periodic change
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Checks if bullets belonging to it are offscreen and removes them if they are
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom < 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws all components
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self) -> bool:
        """Checks if bullet can be fired and if it can it generates it in the game

        Returns:
            bool: Returns if firing was successful
        """
        if len(self.arsenal) < self.game.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
