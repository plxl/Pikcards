from ..bases.minion import *

class PuffyBlowhog(Minion):
    pass


def load_me():
    this_minion = PuffyBlowhog(
        set = "1", # str
        number = 33, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Puffy Blowhog", # str
        image = "33_Puffy_Blowhog.png", # str
        cardclass = 2, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Up High', 'Indirect'], # list[str]
        base_attack = 0, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Return'] # list[str](optional)
    )
    
    return this_minion