from ..bases.minion import *


class GoldenPikpikCarrot(Minion):
    pass


def load_me():
    this_minion = GoldenPikpikCarrot(
        set="C",  # str
        number=26,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Golden Pikpik Carrot",  # str
        image="26_Golden_Pikpik_Carrot.png",  # str
        card_class=5,  # int
        base_energy=3,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Digging", "Passive", "Pikmin"],  # list[str]
        base_attack=12,  # int
        base_health=3,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Fire"],  # list[str](optional)
        base_abilities=["Carrot Power", "Lure", "Profit"],  # list[str](optional)
    )

    return this_minion
