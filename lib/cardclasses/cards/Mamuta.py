from ..bases.minion import *

class Mamuta(Minion):
    pass


def load_me():
    this_minion = Mamuta(
        set = "1", # str
        number = 36, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Mamuta", # str
        image = "36_Mamuta.png", # str
        cardclass = 1, # int
        base_energy = 3, # int
        base_time = 5, # int
        elements = ['Crush'], # list[str]
        immunities = [], # list[str]
        traits = ['Passive'], # list[str]
        base_attack = 8, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure', 'Return'] # list[str](optional)
    )
    
    return this_minion