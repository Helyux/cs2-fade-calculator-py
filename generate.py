__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "12.07.2023"
__email__ = "m@hler.eu"
__status__ = "Production"

import json

from src.FadeCalculator import FadeCalculator
from src.AmberFadeCalculator import AmberFadeCalculator
from src.AcidFadeCalculator import AcidFadeCalculator


def main():
    """
    Generate static .json files, this is different from the original typescript repository.
    I like this .json format more for accessing the seeds later.
    e.g. static_data['AWP][42]['percentage'] where 42 is the seed.
    """

    # Create instances of the calculators
    fade_calc = FadeCalculator()
    amber_calc = AmberFadeCalculator()
    acid_calc = AcidFadeCalculator()

    # Build a new dict using format [WEAPON][SEED] = seed, percentage, ranking
    for calc, name in [(fade_calc, 'fade'), (amber_calc, 'amber'), (acid_calc, 'acid')]:
        rebuild = {}
        for obj in calc.get_all_fade_percentages():
            rebuild[obj.weapon] = {}
            for subobj in obj.percentages:
                rebuild[obj.weapon][subobj.seed] = {
                    'seed': subobj.seed,
                    'percentage': subobj.percentage,
                    'ranking': subobj.ranking
                }

        # dump the new dicts to a json file using 4 indents under ./generated
        with open(f"./generated/{name}-percentages.json", 'w') as jf:
            json.dump(rebuild, jf, indent=4)


if __name__ == '__main__':
    main()
