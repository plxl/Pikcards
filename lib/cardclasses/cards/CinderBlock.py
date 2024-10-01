from ..bases.minion import *

class CinderBlock(Minion):
    pass


def load_me():
    this_minion = CinderBlock(
        set = "C", # str
        number = 30, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Cinder Block", # str
        image = "30_Cinder_Block.png", # str
        cardclass = 5, # int
        base_energy = 4, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"2 Defense"', '"Wall"'], # list[str]
        base_attack = 0, # int
        base_health = 9, # int
        defense = 2, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Explosive', 'Louie'], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion