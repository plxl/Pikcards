from ..bases.minion import *


class VictoryMacaroon(Minion):
    pass


def load_me():
    this_minion = VictoryMacaroon(
        set="C",  # str
        number=16,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Victory Macaroon",  # str
        image="16_Victory_Macaroon.png",  # str
        cardclass=5,  # int
        base_energy=5,  # int
        base_time=30,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Victory"],  # list[str](optional)
    )

    return this_minion
