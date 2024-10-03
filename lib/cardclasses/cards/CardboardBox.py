from ..bases.minion import *


class CardboardBox(Minion):
    pass


def load_me():
    this_minion = CardboardBox(
        set="1",  # str
        number=75,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Cardboard Box",  # str
        image="75_Cardboard_Box.png",  # str
        cardclass=2,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=0,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Pikmin"],  # list[str](optional)
        base_abilities=["Heal", "Conjure"],  # list[str](optional)
    )

    return this_minion
