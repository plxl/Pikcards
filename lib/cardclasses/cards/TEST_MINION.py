from ..bases.minion import *

class TestMinion(Minion):
    # When overwriting a def, make sure to put the original loop in as well
    def performAttack(self):
        attacks: list[AttackClass] = []

        print("\nSpecial TESTMINION attack ability modifier")

        if self.stun:
        # If stunned, do not attack, but remove the Stun
            self.stun = False
            return attacks
        
        elif not self.burrowed and not self.petrified:
            # If not burrowed and not petrified, perform attack in this lane
            targetside = 0
            damage = self.attack

            if self.owner == 0:
                targetside = 1

            # If Panicked, only deal 1 damage
            if self.panic:
                damage = 1

            # Create the attack
            ac = AttackClass(damage, self.lane_index, targetside, self)

            for attMod in self.dealDamageModifiers:
                ac = attMod.modify(ac)
            attacks.append(ac)

            return attacks

        # Else it is always either burrowed or petrified, so don't attack
        return attacks


def load_me():
    this_minion = TestMinion("0", 0, True, 0, "TEST_MINION", "Dud.png", 0,
                      1, 5, [], [], [], 3, 3, 1, 1,
                      ["Weak1: Testweaknessdesc", "Weak2: Other testdesc"],
                      ["Empty Ability 1", "Empty Ability 2"])
    
    print(f"\nMINION: {this_minion.getDescription()}\n")
    return this_minion
