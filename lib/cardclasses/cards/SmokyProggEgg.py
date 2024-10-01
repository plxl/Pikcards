from ..bases.minion import *

class SmokyProggEgg(Minion):
    pass


def load_me():
    this_minion = SmokyProggEgg(
        set = "C", # str
        number = 22, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Smoky Progg Egg", # str
        image = "22_Smoky_Progg_Egg.png", # str
        cardclass = 5, # int
        base_energy = 4, # int
        base_time = 9, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Passive"'], # list[str]
        base_attack = 0, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Hatch'] # list[str](optional)
    )
    
    return this_minion