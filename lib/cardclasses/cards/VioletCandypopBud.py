from ..bases.minion import *

class VioletCandypopBud(Minion):
    pass


def load_me():
    this_minion = VioletCandypopBud(
        set = "2", # str
        number = 4, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Violet Candypop Bud", # str
        image = "004_Violet_Candypop_Bud.png", # str
        cardclass = 1, # int
        base_energy = 3, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Passive'], # list[str]
        base_attack = 0, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Candypop'] # list[str](optional)
    )
    
    return this_minion