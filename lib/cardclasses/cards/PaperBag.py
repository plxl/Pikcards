from ..bases.minion import *

class PaperBag(Minion):
    pass


def load_me():
    this_minion = PaperBag(
        set = "2", # str
        number = 100, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Paper Bag", # str
        image = "100_Paper_Bag.png", # str
        cardclass = 1, # int
        base_energy = 4, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Wall"'], # list[str]
        base_attack = 0, # int
        base_health = 10, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Press Down'] # list[str](optional)
    )
    
    return this_minion