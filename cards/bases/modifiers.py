# Data needed to perform an attack
class AttackClass:
    def __init__(self, damageValue: int, targetLane: int, targetPlayer: int, attackElements, attackTraits):
        self.damageValue = damageValue  # Amount of damage being sent
        self.attackElements = attackElements  # Elements of the sent attack
        self.attackTraits = attackTraits  # Traits of the sent attack
        self.targetLane = targetLane  # Lane which is targeted
        self.targetPlayer = targetPlayer  # Side which is targeted (int)

