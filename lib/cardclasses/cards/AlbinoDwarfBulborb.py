from ..bases.minion import *


class AlbinoDwarfBulborb(Minion):
    pass


def load_me():
    this_minion = AlbinoDwarfBulborb(
        set="0",  # str
        number=0,  # int
        fifth=False,  # bool
        rarity=-1,  # int
        name="Albino Dwarf Bulborb",  # str
        image="Albino_Dwarf_Bulborb.png",  # str
        cardclass=0,  # int
        base_energy=2,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=2,  # int
        base_health=3,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Crush", "First Strike"],  # list[str](optional)
        base_abilities=["Transform"],  # list[str](optional)
    )

    return this_minion
