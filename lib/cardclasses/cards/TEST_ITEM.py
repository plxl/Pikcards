from ..bases.item import *

class TestItem(Item):
    # When overwriting a def, make sure to put the original loop in as well
    def on_round_start(self, round: int):
        print(f"ITEM {self.name} says it is the start of Round {round}")
        
        for rsMod in self.round_start_modifiers:
            rsMod.modify(self, round)


def load_me():
    this_item = TestItem("0", 0, True, 0, "TEST_ITEM", "Dud.png", 0,
                      1, 5, [], [], [],
                      ["WeakA: ItemTestWeakness", "WeakB: Other item testdesc"],
                      ["Empty Item Ability 1", "Empty Item Ability 2"])
    
    print(f"\nLOADED:\n{this_item.get_description()}\n")
    return this_item
