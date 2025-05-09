from ..bases.minion import *

class SSDolphin(Minion):
    pass


def load_me():
    this_minion = SSDolphin(
        set = "1", # str
        number = 39, # int
        fifth = False, # bool
        rarity = 2, # int
        name = "S.S. Dolphin", # str
        image = "39_S.S._Dolphin.png", # str
        cardclass = 3, # int
        base_energy = 6, # int
        base_time = 8, # int
        elements = [], # list[str]
        immunities = ['Poison', 'Mushroom', 'Piercing'], # list[str]
        traits = ['Indirect'], # list[str]
        base_attack = 0, # int
        base_health = 7, # int
        defense = 0, # int
        maxcarry = 3, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Carry', 'Dolphin Powers', 'Big Heal'] # list[str](optional)
    )
    
    return this_minion