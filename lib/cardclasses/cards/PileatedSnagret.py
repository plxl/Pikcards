from ..bases.minion import *

class PileatedSnagret(Minion):
    pass


def load_me():
    this_minion = PileatedSnagret(
        set = "2", # str
        number = 47, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Pileated Snagret", # str
        image = "047_Pileated_Snagret.png", # str
        cardclass = 2, # int
        base_energy = 6, # int
        base_time = 6, # int
        elements = ['Piercing'], # list[str]
        immunities = [], # list[str]
        traits = ['Burrowing', 'Up High', 'Defense', 'First Strike'], # list[str]
        base_attack = 4, # int
        base_health = 4, # int
        defense = 1, # int
        maxcarry = 1, # int
        weakness_descriptions = ['First Strike'], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion