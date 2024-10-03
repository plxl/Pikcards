from ..bases.item import *


class UltraSpicySpray(Item):
    pass


def load_me():
    this_item = UltraSpicySpray(
        set="2",  # str
        number=95,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Ultra-Spicy Spray",  # str
        image="095_Ultra-Spicy_Spray.png",  # str
        cardclass=1,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Spice-it-up"],  # list[str](optional)
    )

    return this_item
