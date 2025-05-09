from ..bases.minion import *

class Doodlebug(Minion):
    pass


def load_me():
    this_minion = Doodlebug(
        set = "2", # str
        number = 24, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Doodlebug", # str
        image = "024_Doodlebug.png", # str
        cardclass = 1, # int
        base_energy = 4, # int
        base_time = 7, # int
        elements = ['Poison'], # list[str]
        immunities = [], # list[str]
        traits = ['Wall'], # list[str]
        base_attack = 1, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Stinky Scuttle', 'Belly Stash'] # list[str](optional)
    )
    
    return this_minion