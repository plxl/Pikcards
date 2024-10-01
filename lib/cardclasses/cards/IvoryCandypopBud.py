from ..bases.minion import *

class IvoryCandypopBud(Minion):
    pass


def load_me():
    this_minion = IvoryCandypopBud(
        set = "2", # str
        number = 6, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Ivory Candypop Bud", # str
        image = "006_Ivory_Candypop_Bud.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Passive"'], # list[str]
        base_attack = 0, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Candypop'] # list[str](optional)
    )
    
    return this_minion