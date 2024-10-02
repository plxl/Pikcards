from ..bases.minion import *

class Kakureimo(Minion):
    pass


def load_me():
    this_minion = Kakureimo(
        set = "C", # str
        number = 8, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Kakureimo", # str
        image = "08_Kakureimo.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 9, # int
        elements = ['Poison'], # list[str]
        immunities = [], # list[str]
        traits = ['Digging', 'Explorer', 'Swarm'], # list[str]
        base_attack = 1, # int
        base_health = 5, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_minion