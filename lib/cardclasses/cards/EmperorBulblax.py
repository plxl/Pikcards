from ..bases.minion import *


class EmperorBulblax(Minion):
    pass


def load_me():
    this_minion = EmperorBulblax(
        set="2",  # str
        number=45,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Emperor Bulblax",  # str
        image="045_Emperor_Bulblax.png",  # str
        cardclass=1,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=4,  # int
        base_health=3,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Explosive"],  # list[str](optional)
        base_abilities=["Pull Buff", "Panic"],  # list[str](optional)
    )

    return this_minion
