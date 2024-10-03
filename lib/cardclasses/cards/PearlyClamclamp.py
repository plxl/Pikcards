from ..bases.minion import *


class PearlyClamclamp(Minion):
    pass


def load_me():
    this_minion = PearlyClamclamp(
        set="1",  # str
        number=34,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Pearly Clamclamp",  # str
        image="34_Pearly_Clamclamp.png",  # str
        cardclass=1,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=["Water"],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=11,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Indirect"],  # list[str](optional)
        base_abilities=["Counter Only"],  # list[str](optional)
    )

    return this_minion
