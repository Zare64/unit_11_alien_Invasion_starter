import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from unit_11_alien_Invasion_starter.arsenal import ShipArsenal

class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'ShipArsenal'):
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

    def update(self):
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        if self.moving_right:
            self.velocity+=1
        if self.moving_left:
            self.velocity-=1
        if self.velocity<.1 and self.velocity>-.1:
            self.velocity=0
        self.velocity/=1.2

        
        self.x+=self.velocity
        if self.rect.left < self.boundaries.left:
            self.velocity+=5
        if self.rect.right > self.boundaries.right:
            self.velocity-=5
        self.rect.x=self.x

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
    
