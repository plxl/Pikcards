from ..bases.minion import *


class AnodeDweevil(Minion):
    pass


def load_me():
    this_minion = AnodeDweevil(
        set="2",  # str
        number=30,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Anode Dweevil",  # str
        image="030_Anode_Dweevil.png",  # str
        card_class=3,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=["Electricity"],  # list[str]
        immunities=["Electricity"],  # list[str]
        traits=[],  # list[str]
        base_attack=2,  # int
        base_health=3,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Crush", "Piercing"],  # list[str](optional)
        base_abilities=["Terrified", "Carry Camo"],  # list[str](optional)
    )

    return this_minion
