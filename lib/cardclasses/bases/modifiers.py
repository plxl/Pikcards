from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .card import Card
    from .minion import Minion
    from lib.game import Lane, Game
    

# Data needed to perform an attack
class AttackClass:
    def __init__(self, damageValue: int, targetLane: int, targetPlayer: int, attackerCard: 'Minion'):
        self.damageValue = damageValue  # Amount of damage being sent
        self.attackerCard = attackerCard  # The one performing the Attack
        self.targetLane = targetLane  # Lane which is targeted
        self.targetPlayer = targetPlayer  # Side which is targeted (int)

# Base for all other modifier
class Modifier(ABC):
    @abstractmethod
    def modify(self):
        pass



# Modifier for when the card is played
class BePlayedModifier(Modifier):
    def modify(self, selfCard: 'Card', enteredLane: 'Lane'):
        pass

# Modifier for when the card enters a lane
class EnterLaneModifier(Modifier):
    def modify(self, selfCard: 'Card', enteredLane: 'Lane'):
        pass

# Modifier for when a Round starts
class RoundStartModifier(Modifier):
    def modify(self, selfCard: 'Card', round: int):
        pass

# Modifier for when a turn starts
class TurnStartModifier(Modifier):
    def modify(self, selfCard: 'Card'):
        pass

# Modifier for when a Night starts
class NightStartModifier(Modifier):
    def modify(self, selfCard: 'Card'):
        pass

# Modifier for when a Night ends
class NightEndModifier(Modifier):
    def modify(self, selfCard: 'Card'):
        pass

# Modifier for when a Round ends
class RoundEndModifier(Modifier):
    def modify(self, selfCard: 'Card'):
        pass

# Modifier for when the card is Returned
class ReturnedModifier(Modifier):
    def modify(self, selfCard: 'Card', returnedBy: 'Card'):
        pass

# Modifier for when the card is Discarded
class DiscardedModifier(Modifier):
    def modify(self, selfCard: 'Card', killed: bool):
        pass

# Modifier for when the card is Killed by another
class BeKilledModifier(Modifier):
    def modify(self, selfCard: 'Card', killedBy: 'Card'):
        pass

# Modifier for when a different card is played
class OtherCardPlayedModifier(Modifier):
    def modify(self, selfCard: 'Card',otherCard: 'Card', playedInLane: 'Lane'):
        pass

# Modifier for when a different card leaves the field in any way
class OtherCardLeavesModifier(Modifier):
    # leftThrough is either "Moved", "Returned" or "Discarded"
    def modify(self, selfCard: 'Card', otherCard: 'Card', leavesLane: 'Lane', leftBecause: str):
        pass

# Modifier for when performing an attack
class DealDamageModifier(Modifier):
    def modify(self, attackClass: AttackClass):
        return attackClass

# Modifier when a card takes damage: Mostly Weaknesses, but also certain bonus things
class TakeDamageModifier(Modifier):
    def modify(self, selfCard: 'Card', attackClass: AttackClass):
        return attackClass
