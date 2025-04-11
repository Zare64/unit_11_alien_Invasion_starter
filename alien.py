##Rover Rampage Game, Solomon Harkins, 4/4/2025
from typing import TYPE_CHECKING
import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """Enemy Alien

    Args:
        Sprite (Sprite): Visual component
    """
    def __init__(self, game : "AlienInvasion", x : float, y : float) -> None:
        """Initialises all needed alien values

        Args:
            game (AlienInvasion): Game reference for pulling stuff from the settings
        """
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.y = float(self.rect.y)
    
    def update(self) -> None:
        """Used to update elements periodically
        """
        pass
    
    def draw_alien(self) -> None:
        """Handles necessary screen manipulation
        """
        self.screen.blit(self.image, self.rect)