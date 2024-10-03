from ..bases.minion import *


class DwarfBulbear(Minion):
    pass


def load_me():
    this_minion = DwarfBulbear(
        set="1",  # str
        number=15,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Dwarf Bulbear",  # str
        image="15_Dwarf_Bulbear.png",  # str
        cardclass=1,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=3,  # int
        base_health=3,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Crush", "First Strike"],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
