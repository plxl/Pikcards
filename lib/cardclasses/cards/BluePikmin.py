from ..bases.minion import *


class BluePikmin(Minion):
    pass


def load_me():
    this_minion = BluePikmin(
        set="1",  # str
        number=8,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Blue Pikmin",  # str
        image="08_Blue_Pikmin.png",  # str
        cardclass=3,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=["Water"],  # list[str]
        traits=["Explorer", "Pikmin"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
