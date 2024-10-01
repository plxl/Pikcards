from ..bases.minion import *

class SovereignBulblax(Minion):
    pass


def load_me():
    this_minion = SovereignBulblax(
        set = "1", # str
        number = 38, # int
        fifth = False, # bool
        rarity = 2, # int
        name = "Sovereign Bulblax", # str
        image = "38_Sovereign_Bulblax.png", # str
        cardclass = 1, # int
        base_energy = 7, # int
        base_time = 7, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        base_attack = 7, # int
        base_health = 6, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Explosive'], # list[str](optional)
        ability_descriptions = ['Pull Buff', 'Jump Attack'] # list[str](optional)
    )
    
    return this_minion