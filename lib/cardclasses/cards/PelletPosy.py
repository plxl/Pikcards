from ..bases.minion import *


class PelletPosy(Minion):
    pass


def load_me():
    this_minion = PelletPosy(
        set="1",  # str
        number=11,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Pellet Posy",  # str
        image="11_Pellet_Posy.png",  # str
        cardclass=4,  # int
        base_energy=2,  # int
        base_time=7,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=2,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Pellet Boost"],  # list[str](optional)
    )

    return this_minion
