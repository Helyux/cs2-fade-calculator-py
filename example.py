__author__ = "Lukas Mahler"
__version__ = "1.1.6"
__date__ = "06.10.2024"
__email__ = "m@hler.eu"
__status__ = "Production"

from src.FadeCalculator import FadeCalculator
from src.AmberFadeCalculator import AmberFadeCalculator
from src.AcidFadeCalculator import AcidFadeCalculator


def main():
    """
    Showcase some example usage
    """

    # Create instances of the calculators
    fade_calc = FadeCalculator()
    amber_calc = AmberFadeCalculator()
    acid_calc = AcidFadeCalculator()

    # Get list of supported weapons
    print("Supported weapons in fade calculator:      ", fade_calc.get_supported_weapons())
    print("Supported weapons in amber fade calculator:", amber_calc.get_supported_weapons())
    print("Supported weapons in acid fade calculator: ", acid_calc.get_supported_weapons())

    # Get the fade percentages for a specific weapon and seed
    fade = fade_calc.get_fade_percentage(weapon := "M4A1-S", 374)
    print(f"Base fade percentage for  [{weapon:>10s}] "
          f"with seed: {fade.seed:4d} is {fade.percentage:6.2f}% / ranked: {fade.ranking:4d}")

    # Get the amber fade percentages for a specific weapon and seed
    fade = amber_calc.get_fade_percentage(weapon := "AUG", 763)
    print(f"Amber fade percentage for [{weapon:>10s}] "
          f"with seed: {fade.seed:4d} is {fade.percentage:6.2f}% / ranked: {fade.ranking:4d}")

    # Get the acid fade percentages for a specific weapon and seed
    fade = acid_calc.get_fade_percentage(weapon := "SSG 08", 576)
    print(f"Acid fade percentage for  [{weapon:>10s}] "
          f"with seed: {fade.seed:4d} is {fade.percentage:6.2f}% / ranked: {fade.ranking:4d}")


if __name__ == '__main__':
    main()
