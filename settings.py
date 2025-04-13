##Rover Rampage Game, Solomon Harkins, 4/4/2025
from pathlib import Path

class Settings:
    """Stores a lot of components for outside reference
    """
    def __init__(self) -> None:
        """Sets stored components for outside reference
        """
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        print(f"My Path is: {Path.cwd()}")
        self.image_import_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images'
        self.sound_import_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'sound'
        
        self.player_rover_folder = self.image_import_file / 'player_rover'
        self.bg_file = self.image_import_file / 'mud_background.png'
        self.ship_file = self.player_rover_folder / 'idle' / 'player_rover000.png'
        self.ship_w = 96
        self.ship_h = 120
        self.starting_ship_amount = 3

        self.bullet_file = self.image_import_file / 'rover_bullet.png'
        self.bullet_sound = self.sound_import_file / 'laser.mp3'
        self.impact_sound = self.sound_import_file / 'impactSound.mp3'
        self.bullet_w = 24
        self.bullet_h = 48
        self.bullet_amount = 5
        self.bullet_speed = 5
        self.bullet_volume = 0.7
        self.bullet_fadeout = 250
        self.impact_volume = 0.9
        self.impact_fadeout = 125

        self.alien_folder = self.image_import_file / 'enemy_trooper'
        self.alien_file = self.alien_folder / 'idle' / 'tile000.png'
        self.fleet_speed = 2
        self.alien_w = 48
        self.alien_h = 60
        self.fleet_direction = 1 
        self.fleet_drop_speed = 60