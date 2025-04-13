##Rover Rampage Game, Solomon Harkins, 4/13/2025
import pygame
from typing import TYPE_CHECKING
from alien import Alien
from random import randint

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class AlienFleet: 
    """Manages all aliens in the alien waves
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """Establishes all important variables and sets up the fleet

        Args:
            game (AlienInvasion): The game used typically to reference settings
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()
    
    def create_fleet(self) -> None:
        """Creates the ships in the fleet
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calc_fleet_size(alien_w, screen_w, alien_h, screen_h)

        x_offset, y_offset = self.calculate_offset(alien_w, alien_h, screen_w, fleet_w, fleet_h)
        
        configuration = self.settings.configuration_list[randint(0, 3)]
        self.create_preconfigured_fleet(configuration, alien_w, alien_h, x_offset, y_offset)
        #self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w:int, alien_h:int, fleet_w:int, fleet_h:int, x_offset:int, y_offset:int) -> None:
        """Creates a fleet in a rectangle formation

        Args:
            alien_w (int): Width in pixels of the alien unit
            alien_h (int): Height in pixels of the alien unit
            fleet_w (int): Number of aliens across the fleet is comprised of
            fleet_h (int): Number of aliens up a fleet is comprised of
            x_offset (int): Horizontal offset of fleet origin
            y_offset (int): Vertical offset of fleet origin
        """
        for row in range(fleet_h):
            for collumn in range(fleet_w):
                current_y = alien_h * row +y_offset
                current_x = alien_w*collumn + x_offset
                if collumn%2 ==0:
                    continue
                self._create_alien(current_x,current_y)

    def create_preconfigured_fleet(self, configuration:list, blank_size:int, row_height:int, x_offset:int, y_offset:int) -> None:
        """Creates a fleet based on a list of strings

        Args:
            configuration (list): List of strings determining fleet composition
            blank_size (int): X Size of a "blank" space
            row_height (int): Amount of space between the rows
            x_offset (int): X offset of the fleet
            y_offset (int): Y offset of the fleet
        """
        current_x=x_offset
        current_y=y_offset
        for row in configuration:
            
            for char in row:
                if char.isspace():
                    current_x+=blank_size
                    continue
                elif char=='a':
                    current_x+=self.settings.alien_w
                    self._create_alien(current_x,current_y)
            current_x=x_offset
            current_y+=row_height

    def calculate_offset(self, alien_w:int, alien_h:int, screen_w:int, fleet_w:int, fleet_h:int) -> tuple:
        """Calculates offset for fleet generation

        Args:
            alien_w (int): Width in pixels of alien unit
            alien_h (int): Height in pixels of alien unit
            screen_w (int): Width of screen
            fleet_w (int): Width of fleet
            fleet_h (int): Height of fleet

        Returns:
            tuple: x and y offset
        """
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w-fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset, y_offset


    def calc_fleet_size(self, alien_w: int, screen_w: int, alien_h: int, screen_h: int) -> tuple:
        """Calculates the size the fleet should be

        Args:
            alien_w (int): Width of alien
            screen_w (int): Width of screen
            alien_h (int): Height of alien
            screen_h (int): Height of screen

        Returns:
            tuple: Size of fleet relative to alien unit
        """
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h/2)//alien_h)

        if fleet_w % 2 ==0:
            fleet_w -=1
        else:
            fleet_w -= 2
        
        if fleet_h%2==0:
            fleet_h-=1
        else:
            fleet_h-=2
        
        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        """Creates an Alien and adds it to the fleet

        Args:
            current_x (int): X that alien is created at 
            current_y (int): Y that alien is created at
        """
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)
    
    def _check_fleet_edges(self):
        """Checks whether any alien is touching the edge of the screen, if they are it moves the alien fleet down
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction*=-1
                break
                
    
    def _drop_alien_fleet(self) -> None:
        """Moves the alien fleet down
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
    
    def update_fleet(self) -> None:
        """Handles all periodic updates needed for the fleet
        """
        self._check_fleet_edges()
        self.fleet.update()
        

    def draw(self) -> None:
        """Draws all the aliens in the fleet
        """
        alien:'Alien'
        for alien in self.fleet:
            alien.draw_alien()
    
    def check_collisions(self, other_group) -> None:
        """Checks if the fleet is colliding with specified party

        Args:
            other_group (Any): Whatever you are checking against for collision

        Returns:
            Bool: Returns if its colliding or not
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self) -> None:
        """Checks if the fleet has reached the bottom of the screen

        Returns:
            Bool: True if the fleet is at bottom, false if not
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self) -> None:
        """Checks if the fleet is destroyed

        Returns:
            Bool: True if there aren't ships, false if there are
        """
        return not self.fleet