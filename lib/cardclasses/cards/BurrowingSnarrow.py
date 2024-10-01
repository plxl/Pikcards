from ..bases.minion import *

class BurrowingSnarrow(Minion):
    pass


def load_me():
    this_minion = BurrowingSnarrow(
        set = "C", # str
        number = 20, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Burrowing Snarrow", # str
        image = "20_Burrowing_Snarrow.png", # str
        cardclass = 5, # int
        base_energy = 4, # int
        base_time = 5, # int
        elements = ['"Piercing"'], # list[str]
        immunities = [], # list[str]
        traits = ['"Burrowing"', '"Up High"'], # list[str]
        base_attack = 3, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['First Strike'], # list[str](optional)
        ability_descriptions = ['Blind', 'Mystery Creature'] # list[str](optional)
    )
    
    return this_minion