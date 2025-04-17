##Rover Rampage Game, Solomon Harkins, 4/17/2025
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class Button:
    """Button object, displays color and text and can respond to clicks
    """
    def __init__(self, game: "AlienInvasion", msg:str) -> None:
        """Initialises all needed variables

        Args:
            game (AlienInvasion): reference to game to pull outside information
            msg (str): displayed message on button
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)

        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prop_msg(msg)

    def _prop_msg(self, msg:str) -> None:
        """Centers the text on the button

        Args:
            msg (str): Displayed message
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw(self) -> None:
        """Draws button
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos:tuple) -> bool:
        """Checks if the button is being hovered by mouse

        Args:
            mouse_pos (tuple): Position of mouse

        Returns:
            bool: true if mouse is over button, false otherwise
        """
        return self.rect.collidepoint(mouse_pos)