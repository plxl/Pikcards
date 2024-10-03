from ..bases.minion import *


class PuckeringBlinnow(Minion):
    pass


def load_me():
    this_minion = PuckeringBlinnow(
        set="0",  # str
        number=0,  # int
        fifth=False,  # bool
        rarity=-1,  # int
        name="Puckering Blinnow",  # str
        image="Puckering_Blinnow.png",  # str
        cardclass=0,  # int
        base_energy=1,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Area"],  # list[str](optional)
        base_abilities=["School Call", "Group Up", "Jump Out"],  # list[str](optional)
    )

    return this_minion
