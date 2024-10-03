from ..bases.exploration import *


class ShowerRoom(Exploration):
    pass


def load_me():
    this_exploration = ShowerRoom(
        set="2",  # str
        number=116,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Shower Room",  # str
        image="116_Shower_Room.png",  # str
        card_class=1,  # int
        base_energy=2,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Shower Room"],  # list[str](optional)
    )

    return this_exploration
