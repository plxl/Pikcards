from ..bases.minion import *


class HairyBulborb(Minion):
    pass


def load_me():
    this_minion = HairyBulborb(
        set="2",  # str
        number=12,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Hairy Bulborb",  # str
        image="012_Hairy_Bulborb.png",  # str
        cardclass=3,  # int
        base_energy=4,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=["Ice"],  # list[str]
        traits=["Explorer"],  # list[str]
        base_attack=4,  # int
        base_health=6,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
