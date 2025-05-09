from ..bases.minion import *

class YellowPikmin(Minion):
    pass


def load_me():
    this_minion = YellowPikmin(
        set = "1", # str
        number = 5, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Yellow Pikmin", # str
        image = "05_Yellow_Pikmin.png", # str
        cardclass = 2, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = ['Electricity'], # list[str]
        traits = ['First Strike', 'Digging', 'Pikmin'], # list[str]
        base_attack = 1, # int
        base_health = 1, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion