from ..bases.minion import *

class WaterClog(Minion):
    pass


def load_me():
    this_minion = WaterClog(
        set = "C", # str
        number = 29, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Water Clog", # str
        image = "29_Water_Clog.png", # str
        cardclass = 5, # int
        base_energy = 1, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = ['Fire'], # list[str]
        traits = ['Explorer', 'Wall'], # list[str]
        base_attack = 0, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Water'], # list[str](optional)
        ability_descriptions = ['Drain'] # list[str](optional)
    )
    
    return this_minion