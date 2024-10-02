from ..bases.minion import *

class DwarfOrangeBulborb(Minion):
    pass


def load_me():
    this_minion = DwarfOrangeBulborb(
        set = "2", # str
        number = 11, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Dwarf Orange Bulborb", # str
        image = "011_Dwarf_Orange_Bulborb.png", # str
        cardclass = 4, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['First Strike'], # list[str]
        base_attack = 2, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush', 'First Strike'], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion