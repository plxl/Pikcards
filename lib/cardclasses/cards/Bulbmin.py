from ..bases.minion import *

class Bulbmin(Minion):
    pass


def load_me():
    this_minion = Bulbmin(
        set = "2", # str
        number = 16, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Bulbmin", # str
        image = "016_Bulbmin.png", # str
        cardclass = 3, # int
        base_energy = 4, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = ['"Fire"', '"Water"', '"Electricity"', '"Poison"', '"Ice"'], # list[str]
        traits = [], # list[str]
        base_attack = 2, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Abandon', 'Pikmin-like'] # list[str](optional)
    )
    
    return this_minion