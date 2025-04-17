##Rover Rampage Game, Solomon Harkins, 4/17/2025
import pygame.font




class HUD:
    """Handles all non-button text elements on the screen
    """
    def __init__(self, game) -> None:
        """Initialises variables and sets up the class

        Args:
            game (AlienInvasion): Reference to the game for the purposes of gathering outside variables
        """
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, 
                                     self.settings.HUD_font_size,
                                     )
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self) -> None:
        """Stores information regarding the life sprite
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_w/2, self.settings.ship_h/2
        ))
        self.life_rect = self.life_image.get_rect()
    


    def update_scores(self) -> None:
        """Collection of the 3 score update functions for ease of calling/organisation
        """
        self._update_score()
        self._update_high_score()
        self._update_max_score()

    def _update_score(self) -> None:
        """Updates the score in the HUD
        """
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.score_rect.bottom + self.padding
    
    def _update_max_score(self) -> None:
        """Updates the max score in the HUD
        """
        max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding
    
    def _update_high_score(self) -> None:
        """Updates the high score in the HUD
        """
        high_score_str = f'High-Score: {self.game_stats.high_score: ,.0f}'
        self.high_score_image = self.font.render(high_score_str, True, self.settings.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        
        self.high_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def update_level(self) -> None:
        """Updates the Level in the HUD
        """
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self) -> None:
        """For each life it draws a predefined life image
        """
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x,current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self) -> None:
        """Draws all HUD elements
        """
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
    

