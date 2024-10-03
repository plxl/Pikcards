from ..bases.area import *


class ValleyofRepose(Area):
    pass


def load_me():
    this_area = ValleyofRepose(
        set="2",  # str
        number=103,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Valley of Repose",  # str
        image="103_Valley_of_Repose.png",  # str
        cardclass=3,  # int
        base_energy=1,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Valley of Repose"],  # list[str](optional)
    )

    return this_area
