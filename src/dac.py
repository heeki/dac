import csv
import json


class DotaAutoChess:
    def __init__(self, comp):
        self.comp = comp
        with open("etc/pieces.csv", "r") as csv_data:
            self.pieces = {}
            header = []
            reader = csv.reader(csv_data, delimiter=",")
            for row in reader:
                if not header:
                    header = row
                else:
                    data = {
                        "cost": row[0],
                        "species1": row[2],
                        "species2": row[3],
                        "class": row[4],
                        "ability": row[5]
                    }
                    self.pieces[row[1]] = data
        with open("etc/synergy_class.csv", "r") as csv_data:
            self.synergy_class = {}
            header = []
            reader = csv.reader(csv_data, delimiter=",")
            for row in reader:
                if not header:
                    header = row
                else:
                    if row[0] not in self.synergy_class:
                        self.synergy_class[row[0]] = {}
                    self.synergy_class[row[0]][row[1]] = row[2]
        with open("etc/synergy_species.csv", "r") as csv_data:
            self.synergy_species = {}
            header = []
            reader = csv.reader(csv_data, delimiter=",")
            for row in reader:
                if not header:
                    header = row
                else:
                    if row[0] not in self.synergy_species:
                        self.synergy_species[row[0]] = {}
                    self.synergy_species[row[0]][row[1]] = row[2]

    def __str__(self):
        output = {
            "pieces": self.pieces,
            "synergy_class": self.synergy_class,
            "synergy_species": self.synergy_species
        }
        return json.dumps(output)

    def get_comp_detail(self):
        output = {}
        for piece in self.comp:
            if self.pieces[piece]["species2"] == "":
                output[piece] = "{} {}".format(self.pieces[piece]["species1"], self.pieces[piece]["class"])
            else:
                output[piece] = "{}/{} {}".format(self.pieces[piece]["species1"], self.pieces[piece]["species2"], self.pieces[piece]["class"])
        return output

    def get_synergy_class(self):
        counts = {}
        synergies = {}
        for piece in self.comp:
            pclass = self.pieces[piece]["class"]
            if pclass not in counts:
                counts[pclass] = 1
            else:
                counts[pclass] += 1
        for pclass in counts.keys():
            # print("synergy={}, count={}".format(pclass, counts[pclass]))
            for tier in self.synergy_class[pclass]:
                if counts[pclass] >= int(tier):
                    # print("synergy_tiers={}, {}".format(tier, self.synergy_class[pclass][tier]))
                    if pclass not in synergies:
                        synergies[pclass] = {}
                    synergies[pclass][tier] = self.synergy_class[pclass][tier]
        return counts, synergies

    def get_synergy_species(self):
        counts = {}
        synergies = {}
        for piece in self.comp:
            all_species = [
                self.pieces[piece]["species1"]
            ]
            if self.pieces[piece]["species2"] != "":
                all_species.append(self.pieces[piece]["species2"])
            for species in all_species:
                if species not in counts:
                    counts[species] = 1
                else:
                    counts[species] += 1
        for species in counts.keys():
            # print("synergy={}, count={}".format(species, counts[species]))
            if species == "Demon" and counts[species] > 1:
                continue
            for tier in self.synergy_species[species]:
                if counts[species] >= int(tier):
                    # print("synergy_tiers={}, {}".format(tier, self.synergy_species[species][tier]))
                    if species not in synergies:
                        synergies[species] = {}
                    synergies[species][tier] = self.synergy_species[species][tier]
        return counts, synergies

