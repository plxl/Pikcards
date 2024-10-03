from ..bases.item import *


class RepairTypeBolt(Item):
    pass


def load_me():
    this_item = RepairTypeBolt(
        set="1",  # str
        number=55,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Repair-Type Bolt",  # str
        image="55_Repair-Type_Bolt.png",  # str
        cardclass=3,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Heal"],  # list[str](optional)
    )

    return this_item
