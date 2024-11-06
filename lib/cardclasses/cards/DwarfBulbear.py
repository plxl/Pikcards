from ..bases.minion import *

# Dwarf Bulbear will instantly die to Crush and First Strike attacks
class DwarfBulbearWeakness(TakeDamageModifier):
    def modify(self_card: Card, attack_class: AttackClass):
        
        if "First Strike" in attack_class.attacker_card.traits:
            print(f"{self_card.name} is weak to the attack")
            attack_class.instakill = True

        elif "Crush" in attack_class.attacker_card.elements:
            print(f"{self_card.name} is weak to the attack")
            attack_class.instakill = True
        
        return attack_class



class DwarfBulbear(Minion):
    def __init__(self,
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
                 defense,
                 maxcarry,

                 weaknesses: list[TakeDamageModifier],

                 weakness_descriptions: list[str] = [],
                 ability_descriptions: list[str] = [],
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

        self.weakness_description = weakness_descriptions  # Descriptions of all weaknesses
        self.base_wd = weakness_descriptions  # Weaknesses which the base card has
        self.ability_description = ability_descriptions  # Descriptions of all abilities
        self.base_ad = ability_descriptions  # Abilities which the base card has

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.

        # Attributes unique to Minions
        self.base_attack = base_attack  # Standard attack power of the card
        self.attack = base_attack  # Current attack power of the card
        self.base_health = base_health  # Standard Max Health of the card, used to prevent a card from healing over this number
        self.max_health = base_health  # Max Health of the card in gameplay, can be changed by Overhealing and such
        self.health = base_health  # Current Health of the card, used to calculate how much damage was taken
        self.base_defense = defense  # Standard max Defense of the card
        self.defense = defense  # Defense of the card
        self.maxcarry = maxcarry  # Maximum number of Items this card can hold
        self.held_items: list['Item'] = []  # Items that this is holding

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
        self.take_damage_modifiers: list[TakeDamageModifier] = weaknesses
        self.be_killed_modifiers: list[BeKilledModifier] = []


def load_me():
    this_minion = DwarfBulbear(
        set = "1", # str
        number = 15, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Dwarf Bulbear", # str
        image = "15_Dwarf_Bulbear.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ["GrubDog"], # list[str]
        base_attack = 3, # int
        base_health = 3, # int
        defense = 0, # int
        maxcarry = 1, # int
        weaknesses = [DwarfBulbearWeakness], # Weaknesses
        weakness_descriptions = ["Instantly dies to CRUSH and FIRST STRIKE attacks"], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion