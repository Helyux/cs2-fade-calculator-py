__author__ = "Lukas Mahler"
__version__ = "1.1.5"
__date__ = "04.10.2024"
__email__ = "m@hler.eu"
__status__ = "Production"

from src.RandomNumberGenerator import RandomNumberGenerator


class FadePercentage:

    def __init__(self, seed, percentage, ranking):
        self.seed = seed
        self.percentage = percentage
        self.ranking = ranking


class WeaponFadePercentage:

    def __init__(self, weapon, percentages):
        self.weapon = weapon
        self.percentages = percentages


class BaseCalculator:

    def __init__(self):
        self.weapons = []
        self.reversed_weapons = []
        self.trade_up_weapons = []
        self.configs = {}
        self.min_percentage = 80

    def get_supported_weapons(self):
        return self.weapons

    def get_fade_percentage(self, weapon, seed):
        percentages = self.get_fade_percentages(weapon)
        return percentages[seed]

    def get_all_fade_percentages(self):
        return [
            WeaponFadePercentage(weapon, self.get_fade_percentages(weapon))
            for weapon in self.weapons
        ]

    def get_fade_percentages(self, weapon):
        if weapon not in self.weapons:
            raise ValueError(f'The weapon "{weapon}" is currently not supported.')

        config = self.configs.get(weapon, self.configs['default'])

        raw_results = []

        max_seed = 1000 if weapon in self.trade_up_weapons else 999

        for i in range(max_seed + 1):
            random_number_generator = RandomNumberGenerator()
            random_number_generator.set_seed(i)

            x_offset = random_number_generator.random_float(
                config['pattern_offset_x_start'], config['pattern_offset_x_end']
            )

            random_number_generator.random_float(
                config['pattern_offset_y_start'], config['pattern_offset_y_end']
            )

            rotation = random_number_generator.random_float(
                config['pattern_rotate_start'], config['pattern_rotate_end']
            )

            uses_rotation = config['pattern_rotate_start'] != config['pattern_rotate_end']
            uses_x_offset = config['pattern_offset_x_start'] != config['pattern_offset_x_end']

            if uses_rotation and uses_x_offset:
                raw_result = rotation * x_offset
            elif uses_rotation:
                raw_result = rotation
            else:
                raw_result = x_offset

            raw_results.append(abs(raw_result))

        is_reversed = weapon in self.reversed_weapons

        if is_reversed:
            best_result = max(raw_results)
            worst_result = min(raw_results)
        else:
            best_result = min(raw_results)
            worst_result = max(raw_results)

        result_range = worst_result - best_result

        percentage_results = [
            (worst_result - raw_result) / result_range
            for raw_result in raw_results
        ]

        sorted_percentage_results = sorted(percentage_results)

        return [
            FadePercentage(
                i,
                self.min_percentage + (percentage_result * (100 - self.min_percentage)),
                min(
                    sorted_percentage_results.index(percentage_result) + 1,
                    len(sorted_percentage_results) - sorted_percentage_results.index(percentage_result)
                )
            )
            for i, percentage_result in enumerate(percentage_results)
        ]


if __name__ == '__main__':
    exit(1)
