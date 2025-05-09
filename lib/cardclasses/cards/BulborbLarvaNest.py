from ..bases.minion import *

class BulborbLarvaNest(Minion):
    pass


def load_me():
    this_minion = BulborbLarvaNest(
        set = "C", # str
        number = 11, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Bulborb Larva Nest", # str
        image = "11_Bulborb_Larva_Nest.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Burrowing', 'Passive'], # list[str]
        base_attack = 0, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Digging', 'Burrowing'], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_minion