import json
from enum import Enum
from os import listdir
from os import path, getcwd


# Classes that a card can have
class CardClass:
    NONE = 0
    FIGHTING = 1
    TRAPPERS = 2
    SURVIVAL = 3
    BOOSTER = 4
    HANDY = 5

# Types that a card can have
class CardType:
    Minion = 0
    Item = 1
    Area = 2
    Exploration = 3

# Rarity which cards can have
Rarity = Enum(
    value="Rarity",
    names=[
        ("Plain",     0),
        ("Common",    1),
        ("Rare",      2),
        ("Very Rare", 3)])

# Base card abilities and stats
class Card:
    def __init__(self, 
            set,
            number,
            fifth,
            rarity,
            name,
            image,
            cardclass,
            cardtype,
            base_energy,
            base_time,
            base_attack,
            base_health,
            defense,
            maxcarry,
            elements,
            immunities,
            weaknesses,
            traits,
            abilities,
            additions,
            notes):
        self.set = set
        self.number = number
        self.fifth = fifth
        self.rarity = rarity
        self.name = name
        self.image = image
        self.cardclass = cardclass
        self.cardtype = cardtype
        self.base_energy = base_energy  # Standard energy cost of the card
        self.energy = base_energy  # current energy cost of the card
        self.base_time = base_time  # Standard time cost of the card
        self.time = base_time  # Current time cost of the card
        self.base_attack = base_attack  # Standard attack power of the card
        self.attack = base_attack  # Current attack power of the card
        self.base_health = base_health  # Standard Max Health of the card, used to prevent a card from healing over this number
        self.health = base_health  # Current Health of the card, used to calculate how much damage was taken
        self.defense = defense  # Defense of the card
        self.maxcarry = maxcarry  # Maximum number of Items this card can hold
        self.elements = elements
        self.immunities = immunities
        self.weaknesses = weaknesses
        self.traits = traits
        self.abilities = abilities
        self.additions = additions
        self.notes = notes
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def load_cards():
        folder = path.join(getcwd(), "cards", "json")
        jsons = [
            path.join(folder, j) for j in listdir(folder) if j.lower().endswith(".json")
        ]

        print("Loading Cards...")
        for j in jsons:
            # print(f'Loading {j}...')
            f = open(j, "r")
            Cards.append(json.loads(f.read(), object_hook=lambda d: Card(**d)))
            f.close()

# All cards
Cards: list[Card] = []