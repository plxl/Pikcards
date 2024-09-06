import json
from enum import Enum
from os import listdir
from os import path, getcwd

"""
    TO DO:
    - Remove requirement of parser and json files (def ToJSON and part of def load_cards)
    - Turn CardElement and CardTrait into actual used elements
    - Simplify rarity Enum

    - attack
        - remove stun on attempted attack
    - take damage
    - die/discarded
    - make player draw
    - make player conjure
    - setStatus (blind, burrow, stun, petrified, panic, bubble)

    - onPlayed
    - onEnterLane
    - start round
        - If wall, increase. If 3, die
    - start of night
    - end of night
    - end of round

    - change Items held (both for gaining and losing one)
    - for Items, check Pikmin on field
"""



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

# Elements a card can have
class CardElement:
    Fire = 0
    Water = 1
    Electricity = 2
    Crush = 3
    Explosive = 4
    Poison = 5
    Ice = 6
    Gloom = 7
    Mushroom = 8

# Traits a card can have
class CardTrait:
    Pikmin = 0
    Passive = 1
    Wall = 2
    Swarm = 3
    DolphinPart = 4
    DebtTreasure = 5
    FirstStrike = 6
    Burrowing = 7
    Digging = 8
    UpHigh = 9
    Explorer = 10
    MultiAttack = 11
    Indirect = 12

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
        self.additions = additions  # Should be removed once no longer needed
        self.notes = notes  # Should be removed once no longer needed

        self.blind = False  # Whether the card is displayed as a Blind Card
        self.burrowed = False  # Whether the card is burrowed
        self.just_unburrowed = False  # Whether the card has unburrowed during the round
        self.wallcounter = 0  # Counter for wall cards being on the field
        self.stun = False  # Whether the card is stunned
        self.petrified = False  # Whether the card is petrified
        self.petrified_nightstarted = False  # So petrified cards know Night has begun
        self.panic = False  # Whether the card is panicked
        self.bubble_time = 0  # Whether the card is bubbled. If the card has bubble, this is set to 12. If zero, it is not bubbled.
    

    # Loads all existing cards from individual json files
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


    # Turns card data into a json file, used by the parser
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


# List containing all cards
Cards: list[Card] = []