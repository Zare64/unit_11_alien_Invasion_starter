##Rover Rampage Game, Solomon Harkins, 4/4/2025
from typing import TYPE_CHECKING
import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Player Bullet

    Args:
        Sprite (Sprite): Visual component
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """Initialises all needed bullet values

        Args:
            game (AlienInvasion): Game reference for pulling stuff from the settings
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self) -> None:
        """Used to update elements periodically
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self) -> None:
        """Handles necessary screen manipulation
        """
        self.screen.blit(self.image, self.rect)