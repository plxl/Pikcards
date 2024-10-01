from ..bases.minion import *

class Woollyhop(Minion):
    pass


def load_me():
    this_minion = Woollyhop(
        set = "C", # str
        number = 15, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Woollyhop", # str
        image = "15_Woollyhop.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = ['"Water"'], # list[str]
        immunities = ['"Ice"'], # list[str]
        traits = ['"First Strike"'], # list[str]
        base_attack = 1, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Draw'] # list[str](optional)
    )
    
    return this_minion