from ..bases.minion import *


class WaterDumple(Minion):
    pass


def load_me():
    this_minion = WaterDumple(
        set="1",  # str
        number=16,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Water Dumple",  # str
        image="16_Water_Dumple.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=["Water"],  # list[str]
        traits=["Explorer"],  # list[str]
        base_attack=3,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
