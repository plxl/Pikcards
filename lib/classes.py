import json
import random
from .card import *
from copy import deepcopy
from beautifultable import BeautifulTable


def oprint(obj):
    print(json.dumps(obj, default=lambda o: o.__dict__, indent=4))


class Player:
    def __init__(self, name: str, is_p1: bool) -> None:
        self.name: str = name
        self.is_p1: bool = is_p1
        self.health: int = 20
        self.energy: int = 1
        self.original_deck: list[Card] = []
        self.deck: list[Card] = []
        self.hand: list[Card] = []

    def SetDeck(self, deck: list[str]) -> None:
        if all(isinstance(element, str) for element in deck):
            self.original_deck = []

            for card in deck:
                cards_found = [
                    deepcopy(c)
                    for c in Cards
                    if c.name.lower().strip() == card.lower().strip()
                ]
                if len(cards_found) == 0:
                    raise Exception(f'"{card}" was not found in the card database')

                self.original_deck.append(cards_found[0])

        else:
            self.original_deck = deck
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
        print(
            f"[LOG] Gave {self.name} {number_of_cards} card{'s' if number_of_cards != 1 else ''}"
        )

    def DrawSpecific(self, card: Card) -> None:
        if not card in self.deck:
            raise Exception(
                "Attempted to give specific card when does not exist in deck"
            )

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
        print()
        print("Your Hand")

        columns: list[str] = ["#", "Name", "⚡︎", "ೱ", "🗡", "♥"]
        if redrawn > 0:
            columns.append("Redrawn")

        t = BeautifulTable()
        t.columns.header = columns

        for i in range(len(self.hand)):
            c = self.hand[i]
            fields = [
                i + 1,
                c.name,
                c.energy,
                c.time,
                c.attack,
                c.health,
            ]
            if redrawn > 0:
                if i >= len(self.hand) - redrawn:
                    fields.append("✔")
                else:
                    fields.append("")

            t.rows.append(fields)
        print(t)
        print()

    def HasMinions(self) -> bool:
        if any(c.cardtype == CardType.Minion for c in self.hand):
            return True

        return False

    def HasItems(self) -> bool:
        if any(c.cardtype == CardType.Item for c in self.hand):
            return True

        return False
