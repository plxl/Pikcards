from ..bases.minion import *

class CareeningDirigibug(Minion):
    pass


def load_me():
    this_minion = CareeningDirigibug(
        set = "2", # str
        number = 40, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Careening Dirigibug", # str
        image = "040_Careening_Dirigibug.png", # str
        cardclass = 1, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = ['"Explosive"'], # list[str]
        traits = ['"Up High"', '"Indirect"'], # list[str]
        base_attack = 0, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Bomb Saliva', 'Support Hold'] # list[str](optional)
    )
    
    return this_minion