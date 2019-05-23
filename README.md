# DotA Auto Chess Composition Analyzer
This is a simple utility for checking the species and class bonus synergies for various team compositions.

Step 1: Define the team composition in a var/[filename].json file as an array:
```
[
  "Bat Rider",
  "Luna",
  "Chaos Knight",
  "Abaddon",
  "Dragon Knight",
  "Omni Knight",
  "Shadow Shaman",
  "Disruptor",
  "Dazzle"
]
```

Step 2: Execute the python script:
```
# syntax
python src/analyze.py [file]

# example
python src/analyze.py var/example.json | jq

{
  "comp": {
    "Bat Rider": "Troll Knight",
    "Luna": "Elf Knight",
    "Chaos Knight": "Demon Knight",
    "Abaddon": "Undead Knight",
    "Dragon Knight": "Human/Dragon Knight",
    "Omni Knight": "Human Knight",
    "Shadow Shaman": "Troll Shaman",
    "Disruptor": "Orc Shaman",
    "Dazzle": "Troll Priest"
  },
  "class_counts": {
    "Knight": 6,
    "Shaman": 2,
    "Priest": 1
  },
  "class_synergies": {
    "Knight": {
      "3": "All friendly knights have a 40% chance to trigger a damage-reduction shield when attacked.",
      "6": "All allies knights have a 40% chance to trigger a damage-reduction shield when attacked."
    },
    "Shaman": {
      "2": "Hex affects a random enemy when the battle starts."
    },
    "Priest": {
      "1": "20% less damage to the courier."
    }
  },
  "species_counts": {
    "Troll": 3,
    "Elf": 1,
    "Demon": 1,
    "Undead": 1,
    "Human": 2,
    "Dragon": 1,
    "Orc": 1
  },
  "species_synergies": {
    "Troll": {
      "2": "Attack speed increased by 35% for all friendly trolls."
    },
    "Demon": {
      "1": "Deals 50% extra pure damage to their target. (inactive if more than one king of demon)"
    },
    "Human": {
      "2": "All friendly humans have a 20% chance to silence the target for 4s when attacking."
    }
  }
}
```