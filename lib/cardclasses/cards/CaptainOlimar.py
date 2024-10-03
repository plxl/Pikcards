from ..bases.minion import *


class CaptainOlimar(Minion):
    pass


def load_me():
    this_minion = CaptainOlimar(
        set="1",  # str
        number=1,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Captain Olimar",  # str
        image="01_Captain_Olimar.png",  # str
        card_class=4,  # int
        base_energy=6,  # int
        base_time=14,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Explorer"],  # list[str]
        base_attack=0,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Leadership", "Conjure"],  # list[str](optional)
    )

    return this_minion
