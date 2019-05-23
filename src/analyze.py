import json
import sys
from dac import DotaAutoChess


def main():
    file = sys.argv[1]
    output = {}
    with open(file, "r") as input_file:
        comp = json.load(input_file)
        dac = DotaAutoChess(comp)
        output["comp"] = dac.get_comp_detail()
        class_counts, class_synergies = dac.get_synergy_class()
        output["class_counts"] = class_counts
        output["class_synergies"] = class_synergies
        species_counts, species_synergies = dac.get_synergy_species()
        output["species_counts"] = species_counts
        output["species_synergies"] = species_synergies
    print(json.dumps(output))


if __name__ == "__main__":
    main()
