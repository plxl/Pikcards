from ..bases.minion import *

class Coguchi(Minion):
    pass


def load_me():
    this_minion = Coguchi(
        set = "C", # str
        number = 9, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Coguchi", # str
        image = "09_Coguchi.png", # str
        cardclass = 5, # int
        base_energy = 1, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['First Strike'], # list[str]
        base_attack = 1, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Area'], # list[str](optional)
        ability_descriptions = ['School Call', 'Group Up', 'Jump Out'] # list[str](optional)
    )
    
    return this_minion