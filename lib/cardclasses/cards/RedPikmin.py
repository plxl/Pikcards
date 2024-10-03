from ..bases.minion import *


class RedPikmin(Minion):
    pass


def load_me():
    this_minion = RedPikmin(
        set="1",  # str
        number=2,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Red Pikmin",  # str
        image="02_Red_Pikmin.png",  # str
        cardclass=1,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=["Fire"],  # list[str]
        traits=["Pikmin"],  # list[str]
        base_attack=2,  # int
        base_health=1,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
