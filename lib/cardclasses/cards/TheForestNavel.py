from ..bases.area import *


class TheForestNavel(Area):
    pass


def load_me():
    this_area = TheForestNavel(
        set="1",  # str
        number=78,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="The Forest Navel",  # str
        image="78_The_Forest_Navel.png",  # str
        cardclass=2,  # int
        base_energy=3,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Forest Navel"],  # list[str](optional)
    )

    return this_area
