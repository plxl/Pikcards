from ..bases.minion import *

class MaleSheargrub(Minion):
    pass


def load_me():
    this_minion = MaleSheargrub(
        set = "1", # str
        number = 18, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Male Sheargrub", # str
        image = "18_Male_Sheargrub.png", # str
        cardclass = 4, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = ['Burrowing'], # list[str]
        traits = ['Swarm'], # list[str]
        base_attack = 1, # int
        base_health = 1, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush'], # list[str](optional)
        ability_descriptions = ['Swarm'] # list[str](optional)
    )
    
    return this_minion