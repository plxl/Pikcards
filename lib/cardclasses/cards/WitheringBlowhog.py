from ..bases.minion import *

class WitheringBlowhog(Minion):
    pass


def load_me():
    this_minion = WitheringBlowhog(
        set = "2", # str
        number = 19, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Withering Blowhog", # str
        image = "019_Withering_Blowhog.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Up High', 'Indirect'], # list[str]
        base_attack = 0, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Weaken', 'Return'] # list[str](optional)
    )
    
    return this_minion