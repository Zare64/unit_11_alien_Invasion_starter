from pathlib import Path

class Settings:

    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        print(f"My Path is: {Path.cwd()}")
        self.image_import_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images'

        self.bg_file = self.image_import_file / 'Starbasesnow.png'
        self.ship_file = self.image_import_file / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60