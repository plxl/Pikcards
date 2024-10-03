from ..bases.minion import *

class ManatLegs(Minion):
    pass


def load_me():
    this_minion = ManatLegs(
        set = "2", # str
        number = 48, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Man-at-Legs", # str
        image = "048_Man-at-Legs.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 13, # int
        elements = ['Explosive'], # list[str]
        immunities = ['Crush', 'Explosive'], # list[str]
        traits = ['Multi-Attack', 'Up High', 'Indirect'], # list[str]
        base_attack = 1, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Turret', 'Concentrated Fire'] # list[str](optional)
    )
    
    return this_minion