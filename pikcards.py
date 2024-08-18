from lib.game import *
from time import sleep
import json

# Load all cards from JSON into memory
Card.load_cards()

# Load sample deck
f = open("sample_deck.json")
sample_deck = json.loads(f.read())
f.close()

# sample CLI game with random CPU player (no intelligence)
pname = input("What is your name?\n")
p1: Player = Player(pname, True)
p1.SetDeck(sample_deck.copy())

p2: Player = Player("CPU", False)
p2.SetDeck(sample_deck.copy())

p1.Draw(4)

p2.Draw(4)

p1.PrintHand()

# re draw any of the four cards (once only)
redrawn = 0
print(f"You have the option to re-draw any of your initial 4 cards once.")
rsel = "-1"
while redrawn < 4:
    rsel = input(
        "Select a number to re-draw or leave blank to continue with your current hand: "
    )
    if not rsel.isnumeric():
        break

    r = int(rsel) - 1
    if r >= 0 and r < 4 - redrawn:
        # return card randomly into the deck (but not into the top 10 cards as per rules)
        c = p1.hand[r]
        top_deck = p1.deck[:10]
        half_deck = p1.deck[10:]
        half_deck.insert(random.randint(0, len(half_deck) - 1), c)
        p1.deck = top_deck + half_deck
        p1.hand.remove(c)
        p1.Draw(1)
        redrawn += 1
        p1.PrintHand(redrawn)
    else:
        print("Invalid input")

# fifth
available = p1.GetFifths()
if len(available) == 0:
    print("There are no cards left in your deck that can be selected as a 5th...")
    print("Instead, you will simply draw the next card.")

else:

    print("You can pick one more card to join your hand from your deck...")
    print("Choose from the following:")
    available = p1.GetFifths()
    for i in range(len(available)):
        print(f"{i + 1}. {available[i].name}")
        sleep(0.1)

    fsel = "0"
    while True:
        fsel = input(
            "Select an option or leave blank to draw your next card from your deck: "
        )
        if fsel == "":
            p1.Draw(1)
            break

        if fsel.isnumeric:
            fsel = int(fsel)
            if fsel <= len(available) and fsel > 0:
                p1.DrawSpecific(available[fsel - 1])
                break
# CPU simply draws its next card for its fifth
p2.Draw(1)

p1.PrintHand()

# Starting player preference deciding
print("Would you prefer to start as the morning player?")
print("1. (Y)es\n2. (N)o\n3. (I) don't care\n")

pref = -1
while pref == -1:
    preference: str = input("Select an option and press enter: ")
    if preference == "1" or preference.lower() == "y":
        pref = 0
    elif preference == "2" or preference.lower() == "n":
        pref = 1
    elif preference == "3" or preference.lower() == "i" or len(preference) == 0:
        pref = 2

p2pref = random.randint(0, 2)
starting_player: int = 0
if p2pref == pref:
    starting_player = random.randint(0, 1)
elif p2pref == 2:
    starting_player = pref
elif p2pref == 1:
    if pref == 2:
        starting_player = 0
    elif pref == 0:
        starting_player = 1
elif p2pref == 0:
    starting_player = 1 - pref

starting_player: Player = p1 if starting_player == 0 else p2

print(f"{p2.name}'s Preference: {p2pref+1}")
print(f"{p1.name}'s Preference: {pref+1}")
sleep(0.8)
print(f"{starting_player.name} will be the Starting Player!")

# Create game object and start the game loop
game = Game([p1, p2], starting_player)
game.game_loop()
