from ..bases.minion import *

class YellowWollyhop(Minion):
    pass


def load_me():
    this_minion = YellowWollyhop(
        set = "1", # str
        number = 23, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Yellow Wollyhop", # str
        image = "23_Yellow_Wollyhop.png", # str
        cardclass = 3, # int
        base_energy = 3, # int
        base_time = 4, # int
        elements = ['Crush'], # list[str]
        immunities = [], # list[str]
        traits = ['First Strike'], # list[str]
        base_attack = 2, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion