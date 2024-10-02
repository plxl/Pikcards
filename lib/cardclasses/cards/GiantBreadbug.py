from ..bases.minion import *

class GiantBreadbug(Minion):
    pass


def load_me():
    this_minion = GiantBreadbug(
        set = "2", # str
        number = 46, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Giant Breadbug", # str
        image = "046_Giant_Breadbug.png", # str
        cardclass = 2, # int
        base_energy = 4, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = ['First Strike'], # list[str]
        traits = ['Defense', 'Digging'], # list[str]
        base_attack = 1, # int
        base_health = 5, # int
        defense = 1, # int
        maxcarry = 3, # int
        weakness_descriptions = ['Crush'], # list[str](optional)
        ability_descriptions = ['Carry', 'Item Thief'] # list[str](optional)
    )
    
    return this_minion