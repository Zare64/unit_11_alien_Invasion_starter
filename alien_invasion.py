##Rover Rampage Game, Solomon Harkins, 4/4/2025
#FYI the reason there are so many image files is I wanted to add animations
#(Mostly because these sprites have sat unused in my file system for like a solid 2 years)
#when I was trying to figure out how to do it it looked really weird to do but
#I have found out even more recently its probably not too bad to do with the blit()
#function so I might try that which would lead to a much cleaner looking import later on
#if that doesn't work I'll at a bare minimum reimport cuz I'm like 99.9% sure I messed up scaling
#and then just iterate over the individual folders for state based animation or if that has problems just
#leave it unanimated

#I also hope its alright I'm submitting this with a zip folder I have the github set up but am not sure
#how to submit it
import sys
import pygame
from settings import Settings
from rover import Rover
from arsenal import ShipArsenal
class AlienInvasion:
    """The overall game object that displays all objects below it and contains the settings
    """
    def __init__(self) -> None:
        """References the background and settings aswell as sfx
        """
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock= pygame.time.Clock()

        self.ship = Rover(self, ShipArsenal(self))

        pygame.mixer.init()
        self.bullet_sound = pygame.mixer.Sound(self.settings.bullet_sound)
        self.bullet_sound.set_volume(self.settings.bullet_volume)



    def run_game(self) -> None:
        """Handles the game loop
        """
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _update_screen(self) -> None:
        """Updates all screen elements (the ones updated tell descendents to update)
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()


    def _check_events(self) -> None:
        """Checks for all events and responds to them
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


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

