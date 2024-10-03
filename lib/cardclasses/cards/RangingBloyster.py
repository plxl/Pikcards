from ..bases.minion import *


class RangingBloyster(Minion):
    pass


def load_me():
    this_minion = RangingBloyster(
        set="2",  # str
        number=50,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Ranging Bloyster",  # str
        image="050_Ranging_Bloyster.png",  # str
        card_class=3,  # int
        base_energy=4,  # int
        base_time=8,  # int
        elements=["Water", "Poison"],  # list[str]
        immunities=["Water", "Crush"],  # list[str]
        traits=["Explorer"],  # list[str]
        base_attack=3,  # int
        base_health=6,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Chase", "Ink Spread"],  # list[str](optional)
    )

    return this_minion
