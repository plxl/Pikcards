from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .card import Card
    from .minion import Minion
    from lib.game import Lane, Game
    

# Data needed to perform an attack
class AttackClass:
    def __init__(self, damage_value: int, target_lane: int, target_player: int, instakill: bool = False, attacker_card: 'Minion' = None):
        self.damage_value = damage_value  # Amount of damage being sent
        self.attacker_card = attacker_card  # The one performing the Attack
        self.target_lane = target_lane  # Lane which is targeted
        self.target_player = target_player  # Side which is targeted (int)
        self.instakill = instakill # Whether this attack is guaranteed to kill

# Base for all other modifier
class Modifier(ABC):
    @abstractmethod
    def modify(self):
        pass



# Modifier for when the card is played
class BePlayedModifier(Modifier):
    def modify(self, self_card: 'Card', entered_lane: 'Lane'):
        pass

# Modifier for when the card enters a lane
class EnterLaneModifier(Modifier):
    def modify(self, self_card: 'Card', entered_lane: 'Lane'):
        pass

# Modifier for when a Round starts
class RoundStartModifier(Modifier):
    def modify(self, self_card: 'Card', round: int):
        pass

# Modifier for when a turn starts
class TurnStartModifier(Modifier):
    def modify(self, self_card: 'Card'):
        pass

# Modifier for when a Night starts
class NightStartModifier(Modifier):
    def modify(self, self_card: 'Card'):
        pass

# Modifier for when a Night ends
class NightEndModifier(Modifier):
    def modify(self, self_card: 'Card'):
        pass

# Modifier for when a Round ends
class RoundEndModifier(Modifier):
    def modify(self, self_card: 'Card'):
        pass

# Modifier for when the card is Returned
class ReturnedModifier(Modifier):
    def modify(self, self_card: 'Card', returned_by: 'Card'):
        pass

# Modifier for when the card is Discarded
class DiscardedModifier(Modifier):
    def modify(self, self_card: 'Card', was_killed: bool):
        pass

# Modifier for when the card is Killed by another
class BeKilledModifier(Modifier):
    def modify(self, self_card: 'Card', killed_by: 'Card' = None):
        pass

# Modifier for when a different card is played
class OtherCardPlayedModifier(Modifier):
    def modify(self, self_card: 'Card', other_card: 'Card', played_in_lane: 'Lane'):
        pass

# Modifier for when a different card leaves the field in any way
class OtherCardLeavesModifier(Modifier):
    # leftThrough is either "Moved", "Returned" or "Discarded"
    def modify(self, self_card: 'Card', other_card: 'Card', leaves_lane: 'Lane', left_because: str):
        pass

# Modifier for when performing an attack
class DealDamageModifier(Modifier):
    def modify(self, attack_class: AttackClass):
        return attack_class

# Modifier when a card takes damage: Mostly Weaknesses, but also certain bonus things
class TakeDamageModifier(Modifier):
    def modify(self, self_card: 'Card', attack_class: AttackClass):
        return attack_class
