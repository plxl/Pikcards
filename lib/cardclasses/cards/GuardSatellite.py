from ..bases.item import *


class GuardSatellite(Item):
    pass


def load_me():
    this_item = GuardSatellite(
        set="1",  # str
        number=66,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Guard Satellite",  # str
        image="66_Guard_Satellite.png",  # str
        cardclass=1,  # int
        base_energy=3,  # int
        base_time=7,  # int
        elements=[],  # list[str]
        immunities=["First Strike"],  # list[str]
        traits=["First Strike", "Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_item
