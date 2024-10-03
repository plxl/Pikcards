from ..bases.minion import *


class FieryDweevil(Minion):
    pass


def load_me():
    this_minion = FieryDweevil(
        set="2",  # str
        number=29,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Fiery Dweevil",  # str
        image="029_Fiery_Dweevil.png",  # str
        card_class=2,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=["Fire"],  # list[str]
        immunities=["Fire"],  # list[str]
        traits=[],  # list[str]
        base_attack=3,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Crush", "Piercing"],  # list[str](optional)
        base_abilities=["Terrified", "Carry Camo"],  # list[str](optional)
    )

    return this_minion
