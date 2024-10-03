from ..bases.minion import *


class Moguraimo(Minion):
    pass


def load_me():
    this_minion = Moguraimo(
        set="C",  # str
        number=7,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Moguraimo",  # str
        image="07_Moguraimo.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=["Poison"],  # list[str]
        immunities=[],  # list[str]
        traits=["Explorer", "Passive", "Swarm"],  # list[str]
        base_attack=0,  # int
        base_health=2,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Transform", "Stun"],  # list[str](optional)
    )

    return this_minion
