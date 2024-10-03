from ..bases.minion import *


class BeadyLongLegs(Minion):
    pass


def load_me():
    this_minion = BeadyLongLegs(
        set="1",  # str
        number=32,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Beady Long Legs",  # str
        image="32_Beady_Long_Legs.png",  # str
        cardclass=4,  # int
        base_energy=5,  # int
        base_time=4,  # int
        elements=["Crush"],  # list[str]
        immunities=["Crush"],  # list[str]
        traits=["Multi-Attack", "Up High"],  # list[str]
        base_attack=3,  # int
        base_health=4,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
