##Rover Rampage Game, Solomon Harkins, 4/4/2025
#I couldn't get around to utilizing the image files for animation, a lot of classes are hitting me with work atm
#I don't know if it's realistic that I will get around to it however just in case that is a thing I'll be able to do 
#I plan to leave the assets in

import sys
import pygame
from settings import Settings
from rover import Rover
from arsenal import RoverArsenal
#from alien import Alien
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:
    """The overall game object that displays all objects below it and contains the settings
    """
    def __init__(self) -> None:
        """References the background and settings aswell as sfx
        """
        pygame.init()
        self.settings=Settings()
        self.settings.initialize_dynamic_settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )
        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock= pygame.time.Clock()

        self.ship = Rover(self, RoverArsenal(self))

        pygame.mixer.init()
        self.bullet_sound = pygame.mixer.Sound(self.settings.bullet_sound)
        self.bullet_sound.set_volume(self.settings.bullet_volume)
        self.impact_sound= pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(self.settings.impact_volume)
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, 'Play')
        self.game_active= False
        self.pause_music = self.settings.pause_music
        self.main_music = self.settings.main_music
        self.play_track(self.pause_music)
        



    def run_game(self) -> None:
        """Handles the game loop
        """
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Checks if the alien fleet has triggered victory or defeat conditions and responds
        also handles bullet collision with alien events
        """
        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            #subtract a life if possible

        #check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        if self.alien_fleet.check_destroyed_status():
            self.settings.increase_difficulty()
            #update game stats level
            #update HUD view
            self.game_stats.update_level()
            self._reset_level()
        #check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.game_stats.update(collisions)
            self.HUD.update_scores()
            self.impact_sound.play()
            self.impact_sound.fadeout(self.settings.impact_fadeout)

    def _check_game_status(self):
        """Checks for lives, if there are none left it stops the game loop
        """
        if self.game_stats.ships_left>0:
            self.game_stats.ships_left-=1
            self._reset_level()
            sleep(0.5)
        else:
            self.play_track(self.pause_music)
            self.game_active = False
        print(self.game_stats.ships_left)
        
    def play_track(self, track):
        pygame.mixer.music.load(track)
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)
            

    def _reset_level(self) -> None:
        """Resets the player bullets and the aliens
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        #setting up settings
        #reset game_stats
        #update hud scores
        #reset level
        #recenter the ship
        self.play_track(self.main_music)
        self.settings.initialize_dynamic_settings()
        self.game_active = True
        self.HUD.update_scores()
        pygame.mouse.set_visible(False)
        self.ship._center_ship()
        self._reset_level()
        self.game_stats.reset_stats()
        #draw HUD
        
    def _update_screen(self) -> None:
        """Updates all screen elements (the ones updated tell descendents to update)
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        #self.alien.draw_alien()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()


    def _check_events(self) -> None:
        """Checks for all events and responds to them
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_stats.save_scores()
                self.running=False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


    def _check_keydown_events(self, event) -> None:
        """Checks for key presses and responds to them

        Args:
            event (event): Any pygame event but should only be keydown
        """
        if event.key ==pygame.K_d:
            self.ship.moving_right=True
        if event.key ==pygame.K_a:
            self.ship.moving_left=True
        if event.key == pygame.K_q:
            self.game_stats.save_scores()
            self.running=False
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.bullet_sound.play()
                self.bullet_sound.fadeout(self.settings.bullet_fadeout)


    def _check_keyup_events(self, event) -> None:
        """Checks for key releases and responds to them

        Args:
            event (event): Any pygame event but should only be keyup
        """
        if event.key ==pygame.K_d:
            self.ship.moving_right=False
        elif event.key ==pygame.K_a:
            self.ship.moving_left=False
 

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

