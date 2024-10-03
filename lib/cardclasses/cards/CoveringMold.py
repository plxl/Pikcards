from ..bases.minion import *


class CoveringMold(Minion):
    pass


def load_me():
    this_minion = CoveringMold(
        set="2",  # str
        number=9,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Covering Mold",  # str
        image="009_Covering_Mold.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=5,  # int
        elements=["Mushroom"],  # list[str]
        immunities=["Mushroom"],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=0,  # int
        base_health=9,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[
            "Fire",
            "Water",
            "Electricity",
            "Poison",
            "Ice",
            "Gloom",
            "Piercing",
        ],  # list[str](optional)
        base_abilities=["Mold Cover"],  # list[str](optional)
    )

    return this_minion
