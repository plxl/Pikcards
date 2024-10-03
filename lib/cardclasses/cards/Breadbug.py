from ..bases.minion import *


class Breadbug(Minion):
    pass


def load_me():
    this_minion = Breadbug(
        set="1",  # str
        number=25,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Breadbug",  # str
        image="25_Breadbug.png",  # str
        cardclass=2,  # int
        base_energy=3,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Defense", "Digging"],  # list[str]
        base_attack=1,  # int
        base_health=3,  # int
        base_defense=1,  # int
        maxcarry=1,  # int
        base_weaknesses=["Crush"],  # list[str](optional)
        base_abilities=["Item Thief"],  # list[str](optional)
    )

    return this_minion
