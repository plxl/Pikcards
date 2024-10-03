from ..bases.minion import *


class DwarfBulborb(Minion):
    pass


def load_me():
    this_minion = DwarfBulborb(
        set="1",  # str
        number=13,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Dwarf Bulborb",  # str
        image="13_Dwarf_Bulborb.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=2,  # int
        base_health=3,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Crush", "First Strike"],  # list[str](optional)
        base_abilities=["Iconic"],  # list[str](optional)
    )

    return this_minion
