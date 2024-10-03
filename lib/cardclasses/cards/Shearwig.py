from ..bases.minion import *


class Shearwig(Minion):
    pass


def load_me():
    this_minion = Shearwig(
        set="1",  # str
        number=19,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Shearwig",  # str
        image="19_Shearwig.png",  # str
        cardclass=4,  # int
        base_energy=2,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=["Burrowing", "Up High"],  # list[str]
        traits=["Swarm"],  # list[str]
        base_attack=2,  # int
        base_health=1,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Crush"],  # list[str](optional)
        base_abilities=["Swarm"],  # list[str](optional)
    )

    return this_minion
