from ..bases.minion import *

class AnodeBeetle(Minion):
    pass


def load_me():
    this_minion = AnodeBeetle(
        set = "2", # str
        number = 34, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Anode Beetle", # str
        image = "034_Anode_Beetle.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 2, # int
        elements = ['Electricity'], # list[str]
        immunities = ['Explosive'], # list[str]
        traits = ['Defense', 'Swarm'], # list[str]
        base_attack = 0, # int
        base_health = 2, # int
        defense = 1, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush'], # list[str](optional)
        ability_descriptions = ['Swarm'] # list[str](optional)
    )
    
    return this_minion