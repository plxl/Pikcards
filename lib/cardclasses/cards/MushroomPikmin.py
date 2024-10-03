from ..bases.minion import *


class MushroomPikmin(Minion):
    pass


def load_me():
    this_minion = MushroomPikmin(
        set="1",  # str
        number=31,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Mushroom Pikmin",  # str
        image="31_Mushroom_Pikmin.png",  # str
        cardclass=4,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=["Mushroom"],  # list[str]
        immunities=["Mushroom"],  # list[str]
        traits=["Pikmin"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Mush Rush"],  # list[str](optional)
    )

    return this_minion
