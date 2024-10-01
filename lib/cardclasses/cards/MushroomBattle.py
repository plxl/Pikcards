from ..bases.area import *

class MushroomBattle(Area):
    pass


def load_me():
    this_area = MushroomBattle(
        set = "C", # str
        number = 33, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Mushroom Battle", # str
        image = "33_Mushroom_Battle.png", # str
        cardclass = 5, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = ['"Mushroom"'], # list[str]
        immunities = ['"Mushroom"'], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Mushroom Battle'] # list[str](optional)
    )
    
    return this_area