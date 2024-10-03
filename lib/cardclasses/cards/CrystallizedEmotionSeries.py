from ..bases.item import *


class CrystallizedEmotionSeries(Item):
    pass


def load_me():
    this_item = CrystallizedEmotionSeries(
        set="2",  # str
        number=70,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Crystallized Emotion Series",  # str
        image="070_Crystallized_Emotion_Series.png",  # str
        card_class=3,  # int
        base_energy=2,  # int
        base_time=16,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Crystal Immunify"],  # list[str](optional)
    )

    return this_item
