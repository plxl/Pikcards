from ..bases.item import *

class AncientSecretsSeries(Item):
    pass


def load_me():
    this_item = AncientSecretsSeries(
        set = "2", # str
        number = 61, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Ancient Secrets Series", # str
        image = "061_Ancient_Secrets_Series.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Status'] # list[str](optional)
    )
    
    return this_item