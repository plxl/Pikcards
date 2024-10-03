from ..bases.minion import *

class MungeDweevil(Minion):
    pass


def load_me():
    this_minion = MungeDweevil(
        set = "2", # str
        number = 32, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Munge Dweevil", # str
        image = "032_Munge_Dweevil.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = ['Poison'], # list[str]
        immunities = ['Poison'], # list[str]
        traits = [], # list[str]
        base_attack = 3, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush', 'Piercing'], # list[str](optional)
        ability_descriptions = ['Terrified', 'Carry Camo'] # list[str](optional)
    )
    
    return this_minion