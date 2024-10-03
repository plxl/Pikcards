from ..bases.minion import *


class Woollyhop(Minion):
    pass


def load_me():
    this_minion = Woollyhop(
        set="C",  # str
        number=15,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Woollyhop",  # str
        image="15_Woollyhop.png",  # str
        card_class=5,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=["Water"],  # list[str]
        immunities=["Ice"],  # list[str]
        traits=["First Strike"],  # list[str]
        base_attack=1,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Draw"],  # list[str](optional)
    )

    return this_minion
