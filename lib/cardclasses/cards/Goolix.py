from ..bases.minion import *

class Goolix(Minion):
    pass


def load_me():
    this_minion = Goolix(
        set = "1", # str
        number = 35, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Goolix", # str
        image = "35_Goolix.png", # str
        cardclass = 3, # int
        base_energy = 4, # int
        base_time = 9, # int
        elements = ['Water'], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        base_attack = 0, # int
        base_health = 12, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Electricity', 'Ice'], # list[str](optional)
        ability_descriptions = ['Wide', 'Goo Bounce'] # list[str](optional)
    )
    
    return this_minion