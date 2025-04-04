import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
class AlienInvasion:
    
    def __init__(self) -> None:
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

        self.ship = Ship(self, ShipArsenal(self))

        pygame.mixer.init()
        self.bullet_sound = pygame.mixer.Sound(self.settings.bullet_sound)
        self.bullet_sound.set_volume(self.settings.bullet_volume)



    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()


    def _check_events(self):
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
        if event.key ==pygame.K_d:
            self.ship.moving_right=False
        elif event.key ==pygame.K_a:
            self.ship.moving_left=False
 

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

