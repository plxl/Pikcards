from ..bases.area import *


class TheDistantSpring(Area):
    pass


def load_me():
    this_area = TheDistantSpring(
        set="1",  # str
        number=79,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="The Distant Spring",  # str
        image="79_The_Distant_Spring.png",  # str
        cardclass=3,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=["Water", "W-Immune"],  # list[str](optional)
        base_abilities=["Distant Spring"],  # list[str](optional)
    )

    return this_area
