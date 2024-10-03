from ..bases.minion import *


class UnmarkedSpectralids(Minion):
    pass


def load_me():
    this_minion = UnmarkedSpectralids(
        set="2",  # str
        number=42,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Unmarked Spectralids",  # str
        image="042_Unmarked_Spectralids.png",  # str
        card_class=4,  # int
        base_energy=4,  # int
        base_time=0,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive", "6 Swarm"],  # list[str]
        base_attack=0,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
