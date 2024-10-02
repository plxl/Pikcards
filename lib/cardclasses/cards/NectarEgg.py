from ..bases.minion import *

class NectarEgg(Minion):
    pass


def load_me():
    this_minion = NectarEgg(
        set = "2", # str
        number = 101, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Nectar Egg", # str
        image = "101_Nectar_Egg.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Passive'], # list[str]
        base_attack = 0, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Egg Crack'] # list[str](optional)
    )
    
    return this_minion