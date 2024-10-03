from ..bases.area import *


class TheImpactSite(Area):
    pass


def load_me():
    this_area = TheImpactSite(
        set="1",  # str
        number=76,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="The Impact Site",  # str
        image="76_The_Impact_Site.png",  # str
        card_class=4,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Impact Site"],  # list[str](optional)
    )

    return this_area
