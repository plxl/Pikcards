import json
from os import listdir
import random
from copy import deepcopy
from enum import Enum
from prettytable import PrettyTable
from os import path, getcwd

def oprint(obj):
    print(json.dumps(
            obj,
            default=lambda o: o.__dict__,
            indent=4
        ))

class Class():
    NONE = 0
    FIGHTING = 1
    TRAPPERS = 2
    SURVIVAL = 3
    BOOSTER = 4
    HANDY = 5
    
class Type():
    Minion = 0
    Item = 1
    Area = 2
    Exploration = 3
    
Rarity = Enum(
    value='Rarity',
    names=[
        ('Plain', 0),
        ('Common', 1),
        ('Rare', 2),
        ('Very Rare', 3)
    ])

class Card:
    def __init__(self, set, number, fifth, rarity, name, image, class_, type,
                 energy, time, attack, health, additions, elements, immunities, weaknesses,
                 traits, abilities, notes) -> None:
        self.set: str = set
        self.number: int = number
        self.fifth: bool = fifth
        self.rarity: int = rarity
        self.name: str = name
        self.image: str = image
        self.class_: int = class_
        self.type: int = type
        self.energy: int = energy
        self.time: int = time
        self.attack: int = attack
        self.health: int = health
        self.additions: list = additions
        self.elements: list = elements
        self.immunities: list = immunities
        self.weaknesses: list = weaknesses
        self.traits: list = traits
        self.abilities: list = abilities
        self.notes: str = notes
        
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            indent=4
        )
        
    def load_cards():
        folder = path.join(getcwd(), 'cards', 'json')
        jsons = [path.join(folder, j) for j in listdir(folder) if j.lower().endswith('.json')]
        
        print('Loading Cards...')
        for j in jsons:
            # print(f'Loading {j}...')
            f = open(j, 'r')
            Cards.append(json.loads(
                f.read(),
                object_hook=lambda d: Card(**d)
            ))
            f.close()
Cards: list[Card] = []
            
class Player:
    def __init__(self, name: str, is_p1: bool) -> None:
        self.name: str = name
        self.is_p1: bool = is_p1
        self.health: int = 20
        self.energy: int = 1
        self.original_deck: list[Card] = []
        self.deck: list[Card] = []
        self.hand: list[Card] = []
        
    def SetDeck(self, deck: list) -> None:
        if all(isinstance(element, str) for element in deck):
            self.original_deck = []
            
            for card in deck:
                self.original_deck.append(
                    [deepcopy(c) for c in Cards if c.name.lower().strip() == card.lower().strip()][0]
                )
            
        else: self.original_deck = deck
        self.deck = deepcopy(self.original_deck)
        print(f"[LOG] Set {self.name}'s deck")
        self.ShuffleDeck()
        
    def ShuffleDeck(self) -> None:
        random.shuffle(self.deck)
        print(f"[LOG] Shuffled {self.name}'s deck")
        
    def Draw(self, number_of_cards: int) -> None:
        if number_of_cards > len(self.deck):
            raise Exception("Ran out of cards in the deck, can't draw anymore")
        
        for i in range(0, number_of_cards):
            self.hand.append(self.deck.pop(0))
        print(f"[LOG] Gave {self.name} {number_of_cards} card{'s' if number_of_cards != 1 else ''}")
        
    def DrawSpecific(self, card: Card) -> None:
        if not card in self.deck:
            raise Exception("Attempted to give specific card when does not exist in deck")
        
        self.hand.append(card)
        self.deck.remove(card)
        print(f"[LOG] Gave {self.name} a specific card")
        
    def GetFifths(self) -> list[Card]:
        # if there multiple valid fifths, the selected fifth must be the bottom-most copy
        # i reverse the deck to get these cards bottom-up
        available: list[Card] = []
        for c in reversed(self.deck):
            if c.fifth:
                if not c.name in [card.name for card in available]:
                    available.append(c)
                    
        return available
        
    def PrintHand(self, redrawn: int = 0) -> None:
        print('')
        print('Your Hand')
        
        columns: list[str] = ['#', 'Name', '⚡︎', 'ೱ', '🗡', '♥']
        if redrawn > 0: columns.append('Redrawn')
        table = PrettyTable(columns)
        
        for i in range(len(self.hand)):
            c = self.hand[i]
            fields = [
                str(i + 1),
                c.name,
                str(c.energy),
                str(c.time),
                str(c.attack),
                str(c.health)
            ]
            if redrawn > 0:
                if i >= len(self.hand) - redrawn:
                    fields.append('✔')
                else: fields.append('')
            
            table.add_row(fields)
        print(table)
        print('')
        
    def HasMinions(self) -> bool:
        if any(c.type == Type.Minion for c in self.hand):
            return True
        
        return False
        
    def HasItems(self) -> bool:
        if any(c.type == Type.Item for c in self.hand):
            return True
        
        return False