from ..bases.minion import *

class WaluigiDumple(Minion):
    pass


def load_me():
    this_minion = WaluigiDumple(
        set = "C", # str
        number = 23, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Waluigi Dumple", # str
        image = "23_Waluigi_Dumple.png", # str
        cardclass = 5, # int
        base_energy = 5, # int
        base_time = 0, # int
        elements = [], # list[str]
        immunities = ['"Water"'], # list[str]
        traits = ['"Explorer"'], # list[str]
        base_attack = 1, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure', 'Wa Boost'] # list[str](optional)
    )
    
    return this_minion