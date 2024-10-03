from ..bases.minion import *


class FireGeyser(Minion):
    pass


def load_me():
    this_minion = FireGeyser(
        set="1",  # str
        number=74,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Fire Geyser",  # str
        image="74_Fire_Geyser.png",  # str
        card_class=1,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=["Fire"],  # list[str]
        immunities=[],  # list[str]
        traits=["Indirect", "Wall"],  # list[str]
        base_attack=2,  # int
        base_health=4,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
