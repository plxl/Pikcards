from ..bases.minion import *


class CinderBlock(Minion):
    pass


def load_me():
    this_minion = CinderBlock(
        set="C",  # str
        number=30,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Cinder Block",  # str
        image="30_Cinder_Block.png",  # str
        card_class=5,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["2 Defense", "Wall"],  # list[str]
        base_attack=0,  # int
        base_health=9,  # int
        base_defense=2,  # int
        max_carry=1,  # int
        base_weaknesses=["Explosive", "Louie"],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
