from ..bases.minion import *

class FieryBlowhog(Minion):
    pass


def load_me():
    this_minion = FieryBlowhog(
        set = "1", # str
        number = 20, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Fiery Blowhog", # str
        image = "20_Fiery_Blowhog.png", # str
        cardclass = 3, # int
        base_energy = 3, # int
        base_time = 4, # int
        elements = ['Fire'], # list[str]
        immunities = ['Fire'], # list[str]
        traits = ['Indirect', 'Explorer'], # list[str]
        base_attack = 1, # int
        base_health = 6, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Draw'] # list[str](optional)
    )
    
    return this_minion