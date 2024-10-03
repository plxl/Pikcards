from ..bases.minion import *


class Blonghong(Minion):
    pass


def load_me():
    this_minion = Blonghong(
        set="C",  # str
        number=13,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Blonghong",  # str
        image="13_Blonghong.png",  # str
        card_class=5,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Up High", "Indirect"],  # list[str]
        base_attack=0,  # int
        base_health=3,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return"],  # list[str](optional)
    )

    return this_minion
