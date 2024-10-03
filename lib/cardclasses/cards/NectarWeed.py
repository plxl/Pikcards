from ..bases.minion import *


class NectarWeed(Minion):
    pass


def load_me():
    this_minion = NectarWeed(
        set="C",  # str
        number=5,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Nectar Weed",  # str
        image="05_Nectar_Weed.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=["Crush"],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=3,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Swarm"],  # list[str](optional)
        base_abilities=["Conjure"],  # list[str](optional)
    )

    return this_minion
