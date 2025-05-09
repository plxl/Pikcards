from ..bases.minion import *

class Mitite(Minion):
    pass


def load_me():
    this_minion = Mitite(
        set = "2", # str
        number = 27, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Mitite", # str
        image = "027_Mitite.png", # str
        cardclass = 2, # int
        base_energy = 0, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Passive', 'Swarm'], # list[str]
        base_attack = 0, # int
        base_health = 1, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Smelly Entrance', 'Overswarm'] # list[str](optional)
    )
    
    return this_minion