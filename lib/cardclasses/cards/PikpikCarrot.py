from ..bases.minion import *


class PikpikCarrot(Minion):
    pass


def load_me():
    this_minion = PikpikCarrot(
        set="2",  # str
        number=102,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Pikpik Carrot",  # str
        image="102_Pikpik_Carrot.png",  # str
        card_class=4,  # int
        base_energy=3,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Digging", "Passive", "Pikmin"],  # list[str]
        base_attack=7,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Fire"],  # list[str](optional)
        base_abilities=["Carrot Power", "Lure"],  # list[str](optional)
    )

    return this_minion
