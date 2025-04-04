##Rover Rampage Game, Solomon Harkins, 4/4/2025
#I took some creative liberties on the movement I hope that is alright, I wasn't entirely sure if these labs were meant to
#differ from the source material at all so I kept it pretty tame, if it is alright to do that I was thinking about having a different
#enemy behavior and spawning and have a cycling background to simulate player forward movement if not i'll revert the movement to what was
#shown in the tutorial for future submissions and might go back later and redo the project in Godot with intended changes
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from unit_11_alien_Invasion_starter.arsenal import ShipArsenal

class Rover:
    """Player Controlled Object
    """

    def __init__(self, game: 'AlienInvasion', arsenal: 'ShipArsenal') -> None:
        """Sets all variables

        Args:
            game (AlienInvasion): The game for later reference
            arsenal (ShipArsenal): Bullet manager
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
            )

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.velocity=0
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self) -> None:
        """Handles all periodic changes needed
        """
        self._update_rover_movement()
        self.arsenal.update_arsenal()

    def _update_rover_movement(self) -> None:
        """Handles all movement calculations of the player
        """
        #Utilises velocity based movement for smoother directional transitions 
        # and moving to stop transitions
        if self.moving_right:
            self.velocity+=1
        if self.moving_left:
            self.velocity-=1
        if self.velocity<.1 and self.velocity>-.1:
            self.velocity=0
        self.velocity/=1.2

        #Produces boundary 'bounce' effect
        self.x+=self.velocity
        if self.rect.left < self.boundaries.left:
            self.velocity+=5
        if self.rect.right > self.boundaries.right:
            self.velocity-=5
        self.rect.x=self.x

    def draw(self) -> None:
        """Draws all components onto the screen
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Passes down a fire command to the arsenal

        Returns:
            bool: Returns if firing was successful
        """
        return self.arsenal.fire_bullet()
    
