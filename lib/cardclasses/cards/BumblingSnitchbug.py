from ..bases.minion import *

class BumblingSnitchbug(Minion):
    pass


def load_me():
    this_minion = BumblingSnitchbug(
        set = "2", # str
        number = 22, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Bumbling Snitchbug", # str
        image = "022_Bumbling_Snitchbug.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Up High', 'First Strike', 'Swarm'], # list[str]
        base_attack = 2, # int
        base_health = 2, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Fling'] # list[str](optional)
    )
    
    return this_minion