from ..bases.minion import *


class BeanPikmin(Minion):
    pass


def load_me():
    this_minion = BeanPikmin(
        set="C",  # str
        number=1,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Bean Pikmin",  # str
        image="01_Bean_Pikmin.png",  # str
        cardclass=5,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Pikmin"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Bean"],  # list[str](optional)
    )

    return this_minion
