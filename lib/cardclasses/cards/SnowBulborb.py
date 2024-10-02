from ..bases.minion import *

class SnowBulborb(Minion):
    pass


def load_me():
    this_minion = SnowBulborb(
        set = "2", # str
        number = 13, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Snow Bulborb", # str
        image = "013_Snow_Bulborb.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = ['Ice'], # list[str]
        traits = ['Explorer'], # list[str]
        base_attack = 2, # int
        base_health = 5, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush', 'First Strike'], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion