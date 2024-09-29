from ..bases.exploration import *

class TestExploration(Exploration):
    # When overwriting a def, make sure to put the original loop in as well
    def onNightStart(self):
        print(f"EXPLORATION {self.name} is excited for the upcoming battle")

        for nsMod in self.nightStartModifiers:
            nsMod.modify(self)


def load_me():
    this_exploration = TestExploration("0", 0, True, 0, "TEST_EXPLORATION", "Dud.png", 0,
                      2, 2, [], [], [],
                      "Empty Exploration Description")
    
    print(f"\nEXPLORATION: {this_exploration.getDescription()}\n")
    return this_exploration
