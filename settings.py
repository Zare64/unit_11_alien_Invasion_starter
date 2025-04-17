##Rover Rampage Game, Solomon Harkins, 4/4/2025
from pathlib import Path
from random import randint

class Settings:
    """Stores a lot of components for outside reference
    """
    def __init__(self) -> None:
        """Sets stored components for outside reference
        """

        """Credits:
        All mp3 files were created by me utilizing beepbox for music or jsfxr for sfx

        All png files were created by me (at various points of time) utilizing piskel

        All ttf files were aquired via google fonts
        """
        self.name: str = 'Rover Rampage'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        print(f"My Path is: {Path.cwd()}")
        self.image_import_file = Path.cwd() / 'Assets' / 'images'
        self.sound_import_file = Path.cwd() / 'Assets' / 'sound'
        self.font_import_file = Path.cwd() / 'Assets' / 'Fonts'
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'
        
        self.player_rover_folder = self.image_import_file / 'player_rover'
        self.bg_file = self.image_import_file / 'mud_background.png'
        self.ship_file = self.player_rover_folder / 'idle' / 'player_rover000.png'
        self.ship_w = 96
        self.ship_h = 120
        

        self.bullet_file = self.image_import_file / 'rover_bullet.png'
        self.bullet_sound = self.sound_import_file / 'laser.mp3'
        self.impact_sound = self.sound_import_file / 'impactSound.mp3'
        self.main_music = self.sound_import_file / 'music' / 'Rover Battlefield Main Theme.mp3'
        self.pause_music = self.sound_import_file / 'music' / 'Rover Battlefield Pause Theme.mp3'

        self.bullet_volume = 0.7
        self.bullet_fadeout = 250
        self.impact_volume = 0.9
        self.impact_fadeout = 125
        
        
        self.alien_folder = self.image_import_file / 'enemy_trooper'
        self.alien_file = self.alien_folder / 'idle' / 'tile000.png'

        self.alien_w = 48
        self.alien_h = 60
        self.fleet_direction = 1 




        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20

        self.font_file = self.font_import_file / 'Comfortaa-Medium.ttf'

        self.difficulty_scale = 1.1
        self.bulk_configurations = [
            [
                '  a  a  a a a  a  a',
                'a  a  a  aaa  a  a  a',
                '  a  a  a   a  a  a',
            ],
            [
                'aaaaaaaaaaaa',
                '',
                'aaaaaaaaaaaa'
            ],
            [
                'aaaaaa aaa aaaaaa',
                '    a   a   a ',
                '   aa aa aa aa'
            ],
            [
                '   aaaa aa aaaa   ',
                'aaaaaaa    aaaaaaa',
                '   aaaa aa aaaa   ',
                '   aaaa    aaaa   '
            ],
            [
                'aaaaaaaaaaaaaaaaaa',
                '     a       a    ',
                'aaaaaaaaaaaaaaaaaa',
                'a     aa aa      a',
                'aaaaaaaaaaaaaaaaaa'
            ],
            [
                '    aa      aa    ',
                '     a      a     ',
                '         a        ',
                'aaa            aaa',
                '  aaaaaaaaaaaaaa  '
            ],
            [
                'aaaaaaaaaaaaaa',
                'a            a',
                'a            a',
                'aaaaaaaaaaaaaa'
            ],
            [
                'aa          aa',
                ' aa        aa ',
                '  aa      aa  ',
                '   aa    aa   ',
                '    aa  aa    ',
                '     aaaa     '
            ],
            [
                'aaa  aaa  aaa  aaa',
                ' aaa  aaa  aaa  aa',
                '  aaa  aaa  aaa  a',
                'a  aaa  aaa  aaa  ',
                'aa  aaa  aaa  aaa '
            ],
            [
                'aaaaaaaaaaaaaaaa',
                'aaaaaaaaaaa',
                'aaaaaa'
            ],
            [
                '    aaa     ',
                ' aaa   aaa  ',
                'aa       aa ',
                ' aa     aa  ',
                '   aaaaa    '
            ],
            [
                'aaaaaaaaaaaaaaa',
                'aaaaaa   aaaaaa',
                'aaa         aaa',
                'a             a'
            ]


        ]

    def initialize_dynamic_settings(self) -> None:
        """Initialises settings that are designed to potentially change over time
        """
        self.current_music = self.pause_music
        self.alien_points = 50
        self.bullet_w = 24
        self.bullet_h = 48
        self.bullet_amount = 5
        self.bullet_speed = 5
        self.starting_ship_amount = 3
        self.ship_speed = 1
        self.fleet_drop_speed = 60
        self.fleet_speed = 2
        self.configuration_list = [
            [
                '  a  a  a a a  a  a',
                'a  a  a  aaa  a  a  a',
                '  a  a  a   a  a  a',
            ],
            [
                'aaaaaaaaaaaa',
                '',
                'aaaaaaaaaaaa'
            ],
            [
                'aaaaaa aaa aaaaaa',
                '    a   a   a ',
                '   aa aa aa aa'
            ],
            [
                '   aaaa aa aaaa   ',
                'aaaaaaa    aaaaaaa',
                '   aaaa aa aaaa   ',
                '   aaaa    aaaa   '
            ]


        ]

    def increase_difficulty(self) -> None:
        """Modifies dynamic settings to increase the difficulty
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
        bulk_index = randint(0,len(self.bulk_configurations)-1)
        config_index = randint(0,len(self.configuration_list)-1)
        self.configuration_list[config_index] = self.bulk_configurations[bulk_index]