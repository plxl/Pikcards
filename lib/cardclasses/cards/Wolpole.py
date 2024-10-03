from ..bases.minion import *


class Wolpole(Minion):
    pass


def load_me():
    this_minion = Wolpole(
        set="1",  # str
        number=22,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Wolpole",  # str
        image="22_Wolpole.png",  # str
        cardclass=4,  # int
        base_energy=1,  # int
        base_time=2,  # int
        elements=["Water"],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=0,  # int
        base_health=1,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Transform"],  # list[str](optional)
    )

    return this_minion
