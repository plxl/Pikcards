from ..bases.minion import *

class Bulborb(Minion):
    pass


def load_me():
    this_minion = Bulborb(
        set = "1", # str
        number = 12, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Bulborb", # str
        image = "12_Bulborb.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        base_attack = 4, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Iconic'] # list[str](optional)
    )
    
    return this_minion