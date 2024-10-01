from ..bases.minion import *

class GatlingGroink(Minion):
    pass


def load_me():
    this_minion = GatlingGroink(
        set = "2", # str
        number = 41, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Gatling Groink", # str
        image = "041_Gatling_Groink.png", # str
        cardclass = 1, # int
        base_energy = 6, # int
        base_time = 7, # int
        elements = ['"Explosive"'], # list[str]
        immunities = ['"First Strike"', '"Up High"'], # list[str]
        traits = ['"2 Defense"'], # list[str]
        base_attack = 2, # int
        base_health = 2, # int
        defense = 2, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Spread Shot', 'Wind Shield'] # list[str](optional)
    )
    
    return this_minion