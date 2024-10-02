from ..bases.minion import *

class CloakingBurrownit(Minion):
    pass


def load_me():
    this_minion = CloakingBurrownit(
        set = "2", # str
        number = 25, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Cloaking Burrow-nit", # str
        image = "025_Cloaking_Burrow-nit.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = ['Piercing'], # list[str]
        immunities = [], # list[str]
        traits = ['Burrowing', '2 Defense', 'Swarm'], # list[str]
        base_attack = 1, # int
        base_health = 3, # int
        defense = 2, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion