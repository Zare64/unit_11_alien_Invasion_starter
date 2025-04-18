##Rover Rampage fleet.game, Solomon Harkins, 4/13/2025
from typing import TYPE_CHECKING
import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Enemy Alien

    Args:
        Sprite (Sprite): Visual component
    """
    def __init__(self, fleet : "AlienFleet", x : float, y : float) -> None:
        """Initialises all needed alien values

        Args:
            fleet (AlienInvasion): fleet.game reference for pulling stuff from the settings
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        #self.y = float(self.rect.y)
    
    def update(self) -> None:
        """Handles all needed periodic updates for the alien
        """
        temp_speed = self.settings.fleet_speed

        #if self.check_edges():
            #self.settings.fleet_direction *= -1
            #self.y+=self.settings.fleet_drop_speed

        self.x+=temp_speed*self.fleet.fleet_direction
        self.rect.x=self.x
        self.rect.y=self.y
    
    def check_edges(self) -> bool:
        """Checks if the alien is touching an edge

        Returns:
            bool: Returns true if it is touching an edge, false if it isn't
        """
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self) -> None:
        """Handles necessary screen manipulation
        """
        self.screen.blit(self.image, self.rect)