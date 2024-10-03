from ..bases.minion import *


class Puffstool(Minion):
    pass


def load_me():
    this_minion = Puffstool(
        set="1",  # str
        number=30,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Puffstool",  # str
        image="30_Puffstool.png",  # str
        cardclass=4,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=["Mushroom"],  # list[str]
        immunities=["Mushroom"],  # list[str]
        traits=[],  # list[str]
        base_attack=1,  # int
        base_health=5,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Summon", "Shroomify"],  # list[str](optional)
    )

    return this_minion
