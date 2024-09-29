from ..bases.area import *

class TestArea(Area):
    # When overwriting a def, make sure to put the original loop in as well
    def onRoundEnd(self, round: int):
        print(f"AREA {self.name} says it is the end of Round {round}")

        for reMod in self.nightEndModifiers:
            reMod.modify(self)


def load_me():
    this_area = TestArea("0", 0, True, 0, "TEST_AREA", "Dud.png", 0,
                      1, 5, [], [], [],
                      "Empty Area Description, with Up-High explanation")
    print(f"\nAREA: {this_area.getDescription()}\n")
    return this_area
