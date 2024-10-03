from ..bases.minion import *


class VolatileDweevil(Minion):
    pass


def load_me():
    this_minion = VolatileDweevil(
        set="2",  # str
        number=33,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Volatile Dweevil",  # str
        image="033_Volatile_Dweevil.png",  # str
        card_class=1,  # int
        base_energy=2,  # int
        base_time=6,  # int
        elements=["Explosive"],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=6,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Crush", "First Strike", "Explosive"],  # list[str](optional)
        base_abilities=["Chase", "Self-Destruct"],  # list[str](optional)
    )

    return this_minion
