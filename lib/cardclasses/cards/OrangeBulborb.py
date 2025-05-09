from ..bases.minion import *

class OrangeBulborb(Minion):
    pass


def load_me():
    this_minion = OrangeBulborb(
        set = "2", # str
        number = 10, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Orange Bulborb", # str
        image = "010_Orange_Bulborb.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 9, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['First Strike'], # list[str]
        base_attack = 4, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion