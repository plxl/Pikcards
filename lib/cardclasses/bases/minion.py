from .card import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from item import Item


"""
    TO DO:
    - Make owner get nectar if card is killed while petrified in onDiscarded
    - Make walls discard upon reaching timer in onRoundStart
    - Stalemate/Staredown damage, using a Minion's hasBeenDamaged
    - Make hasBeenDamaged reset after round ended, after game checks if stalemate damage should be applied

    - If a Minion with Items is Discarded or Returned, first Discard their Items, then perform the Minion action

    - The entirity of Bubbled
"""


# Base minion data, stats and actions
class Minion(Card):
    def __init__(
        self,
        set,
        number,
        fifth,
        rarity,
        name,
        image,
        cardclass,
        base_energy,
        base_time,
        elements,
        immunities,
        traits,
        base_attack,
        base_health,
        base_defense,
        max_carry,
        base_weaknesses: list[str] = [],
        base_abilities: list[str] = [],
    ):
        # Attributes for Card class
        self.set = set
        self.number = number
        self.fifth = fifth
        self.rarity = rarity
        self.name = name
        self.image = image
        self.cardclass = cardclass

        self.base_energy = base_energy  # Standard energy cost of the card
        self.energy = base_energy  # current energy cost of the card
        self.base_time = base_time  # Standard time cost of the card
        self.time = base_time  # Current time cost of the card

        self.elements = elements
        self.immunities = immunities
        self.traits = traits

        self.base_weaknesses = base_weaknesses  # Weaknesses which the base card has
        self.weaknesses = base_weaknesses  # Descriptions of all weaknesses
        self.base_abilities = base_abilities  # Abilities which the base card has
        self.abilities = base_abilities  # Descriptions of all abilities

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.

        # Attributes unique to Minions
        self.base_attack = base_attack  # Standard attack power of the card
        self.attack = base_attack  # Current attack power of the card
        self.base_health = base_health  # Standard Max Health of the card, used to prevent a card from healing over this number
        self.max_health = base_health  # Max Health of the card in gameplay, can be changed by Overhealing and such
        self.health = base_health  # Current Health of the card, used to calculate how much damage was taken
        self.base_defense = base_defense  # Standard max Defense of the card
        self.defense = base_defense  # Defense of the card
        self.max_carry = max_carry  # Maximum number of Items this card can hold
        self.held_items: list["Item"] = []  # Items that this is holding

        self.blind = False  # Whether the card is displayed as a Blind Card
        self.burrowed = False  # Whether the card is burrowed
        self.just_unburrowed = False  # Whether the card has unburrowed during the round
        self.wall_counter = 0  # Counter for wall cards being on the field
        self.stun = False  # Whether the card is stunned
        self.petrified = False  # Whether the card is petrified
        self.petrified_nightstarted = False  # So petrified cards know Night has begun
        self.panic = False  # Whether the card is panicked
        self.panic_counter = 0  # Counts the rounds it has been panicked, max of 3
        self.bubble_time = 0  # Whether the card is bubbled. If the card has bubble, this is set to 12. If zero, it is not bubbled.
        self.has_been_damaged = False  # Whether the card took damage this turn, for stalemate/staredown damage

        # Modifiers
        self.be_played_modifiers: list[BePlayedModifier] = []
        self.enter_lane_modifiers: list[EnterLaneModifier] = []
        self.round_start_modifiers: list[RoundStartModifier] = []
        self.turn_start_modifiers: list[TurnStartModifier] = []
        self.night_start_modifiers: list[NightStartModifier] = []
        self.night_end_modifiers: list[NightEndModifier] = []
        self.round_end_modifiers: list[RoundEndModifier] = []
        self.returned_modifiers: list[ReturnedModifier] = []
        self.discarded_modifiers: list[DiscardedModifier] = []
        self.other_card_played_modifiers: list[OtherCardPlayedModifier] = []
        self.other_card_leaves_modifiers: list[OtherCardLeavesModifier] = []

        self.deal_damage_modifiers: list[DealDamageModifier] = []
        self.take_damage_modifiers: list[TakeDamageModifier] = []
        self.be_killed_modifiers: list[BeKilledModifier] = []

    # Provides description that shows what the abilities of the class are
    def get_description(self):
        description: str = f"Minion {self.name}\n"
        if len(self.weaknesses) > 0:
            description += "WEAKNESSES:\n"
            description += "\n".join(self.weaknesses)
            description += "\n"

        if len(self.abilities) > 0:
            description += "ABILITIES:\n"
            description += "\n".join(self.abilities)
        return description

    # Reset stats for when a card is Returned or Discarded
    def reset_stats(self):
        self.lane_index = -1
        self.attack = self.base_attack
        self.max_health = self.base_health
        self.health = self.base_health
        self.energy = self.base_energy
        self.time = self.base_time
        self.defense = self.base_defense
        self.blind = False
        self.burrowed = False
        self.just_unburrowed = False
        self.wall_counter = 0
        self.stun = False
        self.petrified = False
        self.petrified_nightstarted = False
        self.panic = False
        self.panic_counter = 0
        self.bubble_time = 0
        self.has_been_damaged = False
        self.weaknesses = self.base_weaknesses
        self.abilities = self.base_abilities

    # Basic attack function.
    # Returns a list of targets (temporary)
    def perform_attack(self):
        attacks: list[AttackClass] = []

        if self.stun:
            # If stunned, do not attack, but remove the Stun
            self.stun = False
            return attacks

        elif not self.burrowed and not self.petrified:
            # If not burrowed and not petrified, perform attack in this lane
            target_side = 0
            damage = self.attack

            if self.owner == 0:
                target_side = 1

            # If Panicked, only deal 1 damage
            if self.panic:
                damage = 1

            # Create the attack
            ac = AttackClass(damage, self.lane_index, target_side, self)

            for attMod in self.deal_damage_modifiers:
                ac = attMod.modify(ac)
            attacks.append(ac)

            return attacks

        # Else it is always either burrowed or petrified, so don't attack
        return attacks

    # Used by takeDamage only
    def apply_damage_on_defense(self, damage, traits):
        defense = self.defense
        final_damage = damage

        if self.petrified:
            defense = 0
            final_damage += 2
        elif "Gloom" in traits:
            defense = 0
        elif "Explosive" in traits and defense > 0:
            defense -= 1

        final_damage = max(0, final_damage - defense)
        self.health -= final_damage

        print(f"{self.name} took {final_damage} damage!")

        # Set to damage taken and remove Panic upon taking any damage
        if final_damage > 0:
            self.has_been_damaged = True

            if self.panic:
                self.panic = not self.panic
                self.panic_counter = 0
                print(f"{self.name} is no longer Panicking")

    # Basic function for taking damage, without weaknesses
    # If the card takes damage, remove Panicked state
    def take_damage(self, incoming_attack: AttackClass):
        # Apply take damage modifiers
        modified_attack = incoming_attack
        for attMod in self.take_damage_modifiers:
            modified_attack = attMod.modify(self, modified_attack)

        damage = modified_attack.damage_value

        attacker_traits = modified_attack.attacker_card.traits

        # Check if immune, whether both are passive or if burrowed and attacked by a digger
        # Else don't edit special damage rules
        if bool(set(modified_attack.attacker_card.elements).intersection(self.immunities)) or bool(
            set(attacker_traits).intersection(self.immunities)
        ):
            print(f"{self.name} was immune to the attack")

        elif "Passive" in self.traits and "Passive" in attacker_traits:
            self.apply_damage_on_defense(1, attacker_traits)

        elif self.burrowed and "Digging" in attacker_traits:
            damage += 2
            self.apply_damage_on_defense(damage, attacker_traits)

        else:
            self.apply_damage_on_defense(damage, attacker_traits)

    # Minion function for the card being discarded, checks if killed by another cards as well
    def on_discarded(self, killed_by: Card = None):
        if killed_by is not None:
            for killedMod in self.be_killed_modifiers:
                killedMod.modify(self, killed_by)

            if self.petrified:
                # Provide the owner with Nectar
                print(f"{self.name} was killed while Petrified, so its owner should get a Nectar!")

        for discMod in self.discarded_modifiers:
            discMod.modify(self)

        self.reset_stats()

        # Call remote function to discard this card

    # Minion Function for being healed
    def be_healed(self, amount: int, overheal: bool = False):
        if overheal:
            print(f"{self.name} overhealed by {amount} Health")
            self.health += amount
            if self.health > self.max_health:
                self.max_health = self.base_health
        else:
            self.health = min(self.max_health, self.health + amount)
            print(f"{self.name} healed by {amount} Health")

    def on_round_start(self, round: int):
        if "Wall" in self.traits:
            self.wall_counter += 1

        self.has_been_damaged = False

        if self.burrowed:
            self.burrowed = not self.burrowed
            self.just_unburrowed = True
            print(f"{self.name} just unburrowed")

        if self.wall_counter < 3:
            for rsMod in self.round_start_modifiers:
                rsMod.modify(self, round)
        else:
            print(f"{self.name} is a long-lasting wall and disappears")
            # Call remote function to discard this

    def on_round_end(self):
        if self.panic:
            self.panic_counter += 1

            if self.panic_counter > 2:
                self.panic = not self.panic
                self.panic_counter = 0
                print(f"{self.name} is no longer Panicking")

        if self.burrowed:
            self.be_healed(1)

        if self.just_unburrowed:
            self.just_unburrowed = not self.just_unburrowed

        for reMod in self.night_end_modifiers:
            reMod.modify(self)

    def on_night_start(self):
        if self.petrified:
            self.petrified_nightstarted = True

        for nsMod in self.night_start_modifiers:
            nsMod.modify(self)

    def on_night_end(self):
        if self.petrified and self.petrified_nightstarted:
            self.petrified = not self.petrified
            self.petrified_nightstarted = not self.petrified_nightstarted
            print(f"{self.name} is no longer Petrified")

        for neMod in self.night_end_modifiers:
            neMod.modify(self)
