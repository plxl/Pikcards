from ..bases.minion import *

class GoldenPikpikCarrot(Minion):
    pass


def load_me():
    this_minion = GoldenPikpikCarrot(
        set = "C", # str
        number = 26, # int
        fifth = False, # bool
        rarity = 2, # int
        name = "Golden Pikpik Carrot", # str
        image = "26_Golden_Pikpik_Carrot.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 6, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Digging', 'Passive', 'Pikmin'], # list[str]
        base_attack = 12, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Fire'], # list[str](optional)
        ability_descriptions = ['Carrot Power', 'Lure', 'Profit'] # list[str](optional)
    )
    
    return this_minion