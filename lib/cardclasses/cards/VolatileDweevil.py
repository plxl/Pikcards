from ..bases.minion import *

class VolatileDweevil(Minion):
    pass


def load_me():
    this_minion = VolatileDweevil(
        set = "2", # str
        number = 33, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Volatile Dweevil", # str
        image = "033_Volatile_Dweevil.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 6, # int
        elements = ['Explosive'], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        base_attack = 6, # int
        base_health = 1, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush', 'First Strike', 'Explosive'], # list[str](optional)
        ability_descriptions = ['Chase', 'Self-Destruct'] # list[str](optional)
    )
    
    return this_minion