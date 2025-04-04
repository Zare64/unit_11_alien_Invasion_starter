from pathlib import Path

class Settings:

    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        print(f"My Path is: {Path.cwd()}")
        self.image_import_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images'
        self.sound_import_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'sound'
        
        self.bg_file = self.image_import_file / 'Starbasesnow.png'
        self.ship_file = self.image_import_file / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60

        self.bullet_file = self.image_import_file / 'laserBlast.png'
        self.bullet_sound = self.sound_import_file / 'laser.mp3'
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5
        self.bullet_speed = 5
        self.bullet_volume = 0.7
        self.bullet_fadeout = 250