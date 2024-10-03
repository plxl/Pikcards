from ..bases.minion import *


class Iwagen(Minion):
    pass


def load_me():
    this_minion = Iwagen(
        set="C",  # str
        number=21,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Iwagen",  # str
        image="21_Iwagen.png",  # str
        cardclass=5,  # int
        base_energy=6,  # int
        base_time=2,  # int
        elements=["Crush"],  # list[str]
        immunities=[],  # list[str]
        traits=["Multi-Attack", "Indirect", "Digging", "Wall"],  # list[str]
        base_attack=4,  # int
        base_health=3,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
