from ..bases.exploration import *

class TestExploration(Exploration):
    # When overwriting a def, make sure to put the original loop in as well
    def on_night_start(self):
        print(f"EXPLORATION {self.name} is excited for the upcoming battle")

        for nsMod in self.night_start_modifiers:
            nsMod.modify(self)


def load_me():
    this_exploration = TestExploration("0", 0, True, 0, "TEST_EXPLORATION", "Dud.png", 0,
                      2, 2, [], [], [],
                      "Empty Exploration Description")
    
    print(f"\nLOADED:\n{this_exploration.get_description()}\n")
    return this_exploration
