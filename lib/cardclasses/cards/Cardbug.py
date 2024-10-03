from ..bases.minion import *


class Cardbug(Minion):
    pass


def load_me():
    this_minion = Cardbug(
        set="C",  # str
        number=24,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Cardbug",  # str
        image="24_Cardbug.png",  # str
        cardclass=5,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Defense", "Digging", "Passive"],  # list[str]
        base_attack=1,  # int
        base_health=3,  # int
        defense=1,  # int
        maxcarry=1,  # int
        base_weaknesses=["Crush"],  # list[str](optional)
        base_abilities=["Item Gifter"],  # list[str](optional)
    )

    return this_minion
