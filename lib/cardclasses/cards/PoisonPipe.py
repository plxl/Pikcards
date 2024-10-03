from ..bases.minion import *

class PoisonPipe(Minion):
    pass


def load_me():
    this_minion = PoisonPipe(
        set = "2", # str
        number = 99, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Poison Pipe", # str
        image = "099_Poison_Pipe.png", # str
        cardclass = 2, # int
        base_energy = 2, # int
        base_time = 6, # int
        elements = ['Poison'], # list[str]
        immunities = [], # list[str]
        traits = ['Indirect', 'Wall'], # list[str]
        base_attack = 4, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Indirect'], # list[str](optional)
        ability_descriptions = ['Counter Only'] # list[str](optional)
    )
    
    return this_minion