from ..bases.minion import *

class SkitterLeaf(Minion):
    pass


def load_me():
    this_minion = SkitterLeaf(
        set = "2", # str
        number = 28, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Skitter Leaf", # str
        image = "028_Skitter_Leaf.png", # str
        cardclass = 3, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Passive"', '"Swarm"'], # list[str]
        base_attack = 0, # int
        base_health = 1, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Crush', 'First Strike'], # list[str](optional)
        ability_descriptions = ['Swarm', 'Friendly Presence'] # list[str](optional)
    )
    
    return this_minion