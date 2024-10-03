from ..bases.minion import *


class HydroDweevil(Minion):
    pass


def load_me():
    this_minion = HydroDweevil(
        set="2",  # str
        number=31,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Hydro Dweevil",  # str
        image="031_Hydro_Dweevil.png",  # str
        cardclass=4,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=["Water"],  # list[str]
        immunities=["Water"],  # list[str]
        traits=[],  # list[str]
        base_attack=2,  # int
        base_health=3,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Crush", "Piercing"],  # list[str](optional)
        base_abilities=["Terrified", "Carry Camo"],  # list[str](optional)
    )

    return this_minion
