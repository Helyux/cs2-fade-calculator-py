__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "12.07.2023"
__email__ = "m@hler.eu"
__status__ = "Production"

from src.BaseCalculator import BaseCalculator


class FadeCalculator(BaseCalculator):

    def __init__(self):

        super().__init__()

        self.weapons = [
            'AWP',
            'Bayonet',
            'Bowie Knife',
            'Butterfly Knife',
            'Classic Knife',
            'Falchion Knife',
            'Flip Knife',
            'Glock-18',
            'Gut Knife',
            'Huntsman Knife',
            'Karambit',
            'M9 Bayonet',
            'MAC-10',
            'MP7',
            'Navaja Knife',
            'Nomad Knife',
            'Paracord Knife',
            'R8 Revolver',
            'Shadow Daggers',
            'Skeleton Knife',
            'Stiletto Knife',
            'Survival Knife',
            'Talon Knife',
            'UMP-45',
            'Ursus Knife'
        ]

        self.reversed_weapons = [
            'AWP',
            'Karambit',
            'Talon Knife'
        ]

        self.trade_up_weapons = [
            'AWP',
            'Glock-18',
            'MAC-10',
            'MP7',
            'R8 Revolver',
            'UMP-45'
        ]

        self.configs = {
            'default': {
                'pattern_offset_x_start': -0.7,
                'pattern_offset_x_end': -0.7,
                'pattern_offset_y_start': -0.7,
                'pattern_offset_y_end': -0.7,
                'pattern_rotate_start': -55,
                'pattern_rotate_end': -65
            },
            'MP7': {
                'pattern_offset_x_start': -0.9,
                'pattern_offset_x_end': -0.3,
                'pattern_offset_y_start': -0.7,
                'pattern_offset_y_end': -0.5,
                'pattern_rotate_start': -55,
                'pattern_rotate_end': -65
            }
        }


if __name__ == '__main__':
    exit(1)
