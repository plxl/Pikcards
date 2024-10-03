from ..bases.minion import *

class RavenousWhiskerpillar(Minion):
    pass


def load_me():
    this_minion = RavenousWhiskerpillar(
        set = "2", # str
        number = 43, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Ravenous Whiskerpillar", # str
        image = "043_Ravenous_Whiskerpillar.png", # str
        cardclass = 2, # int
        base_energy = 1, # int
        base_time = 6, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Burrowing', 'Passive'], # list[str]
        base_attack = 0, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Passive Agressive'] # list[str](optional)
    )
    
    return this_minion