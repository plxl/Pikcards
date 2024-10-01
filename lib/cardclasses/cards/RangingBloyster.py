from ..bases.minion import *

class RangingBloyster(Minion):
    pass


def load_me():
    this_minion = RangingBloyster(
        set = "2", # str
        number = 50, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Ranging Bloyster", # str
        image = "050_Ranging_Bloyster.png", # str
        cardclass = 3, # int
        base_energy = 4, # int
        base_time = 8, # int
        elements = ['"Water"', '"Poison"'], # list[str]
        immunities = ['"Water"', '"Crush"'], # list[str]
        traits = ['"Explorer"'], # list[str]
        base_attack = 3, # int
        base_health = 6, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Chase', 'Ink Spread'] # list[str](optional)
    )
    
    return this_minion