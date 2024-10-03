from ..bases.minion import *


class Ujadani(Minion):
    pass


def load_me():
    this_minion = Ujadani(
        set="C",  # str
        number=6,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Ujadani",  # str
        image="06_Ujadani.png",  # str
        cardclass=5,  # int
        base_energy=0,  # int
        base_time=10,  # int
        elements=["Poison"],  # list[str]
        immunities=[],  # list[str]
        traits=["Digging", "Swarm"],  # list[str]
        base_attack=1,  # int
        base_health=4,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Counter Only", "Panic", "Conjure"],  # list[str](optional)
    )

    return this_minion
