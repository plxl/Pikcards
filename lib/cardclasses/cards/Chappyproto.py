from ..bases.minion import *

class Chappyproto(Minion):
    pass


def load_me():
    this_minion = Chappyproto(
        set = "C", # str
        number = 12, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Chappyproto", # str
        image = "12_Chappyproto.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Digging'], # list[str]
        base_attack = 1, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Base Concept'] # list[str](optional)
    )
    
    return this_minion