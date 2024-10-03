from ..bases.minion import *


class ToadyBloyster(Minion):
    pass


def load_me():
    this_minion = ToadyBloyster(
        set="2",  # str
        number=37,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Toady Bloyster",  # str
        image="037_Toady_Bloyster.png",  # str
        card_class=3,  # int
        base_energy=4,  # int
        base_time=3,  # int
        elements=["Water", "Poison"],  # list[str]
        immunities=["Water", "Crush"],  # list[str]
        traits=["Explorer"],  # list[str]
        base_attack=1,  # int
        base_health=6,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Ink Spread"],  # list[str](optional)
    )

    return this_minion
