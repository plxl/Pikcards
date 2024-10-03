from ..bases.minion import *


class BrambleWall(Minion):
    pass


def load_me():
    this_minion = BrambleWall(
        set="1",  # str
        number=72,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Bramble Wall",  # str
        image="72_Bramble_Wall.png",  # str
        card_class=4,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=0,  # int
        base_health=7,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
