from ..bases.minion import *

class IridescentFlintBeetle(Minion):
    pass


def load_me():
    this_minion = IridescentFlintBeetle(
        set = "1", # str
        number = 26, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Iridescent Flint Beetle", # str
        image = "26_Iridescent_Flint_Beetle.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = ['Explosive'], # list[str]
        traits = ['Wall'], # list[str]
        base_attack = 0, # int
        base_health = 5, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Scuttle', 'Belly Stash'] # list[str](optional)
    )
    
    return this_minion