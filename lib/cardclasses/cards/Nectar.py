from ..bases.item import *


class Nectar(Item):
    pass


def load_me():
    this_item = Nectar(
        set="1",  # str
        number=70,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Nectar",  # str
        image="70_Nectar.png",  # str
        card_class=3,  # int
        base_energy=1,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Weightless", "Overheal", "Owner-able"],  # list[str](optional)
    )

    return this_item
