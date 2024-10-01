from ..bases.item import *

class MonsterPump(Item):
    pass


def load_me():
    this_item = MonsterPump(
        set = "2", # str
        number = 94, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Monster Pump", # str
        image = "094_Monster_Pump.png", # str
        cardclass = 4, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = ['"Water"'], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Bubble'] # list[str](optional)
    )
    
    return this_item