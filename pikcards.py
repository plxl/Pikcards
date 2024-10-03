import sys
from lib.game import *
from time import sleep
import json
from copy import deepcopy


# Load all cards from JSON into memory
load_cards()


# load sample decks
with open("decks.json") as f:
    decks = json.loads(f.read())


# sample deck functions
def get_random_deck() -> list[Card]:
    return decks[random.randint(0, len(decks) - 1)]["cards"]


# debug function (uses ./debug.json for configuration)
def start_debugging():
    # easy debug print
    def dprint(s: str):
        print(f"[DEBUG] {s}")

    # read debug options from debug.json
    dprint("Reading debug options...")
    # open file, read, then close using with statement
    with open("debug.json") as f:
        debug_options: object = json.loads(f.read())
    # po for player options, co for cpu options
    po = debug_options["player"]
    co = debug_options["cpu"]

    # initialise player objects
    dprint(f"Creating player objects... ['{po["name"]}', '{co["name"]}']")
    player = Player(po["name"], True)
    cpu = Player(co["name"], False)

    # note: we must initialise decks before hands in the event that they still need to draw cards
    # get debugging deck for player
    # if the deck index is -1, then check if there is a deck override
    dprint("Creating player deck from debug options...")
    if po["deck_index"] == -1:
        # if there are elements in the deck override, use them as the deck
        if len(po["deck_override"]) > 0:
            player.SetDeck(po["deck_override"])
        # otherwise, choose a random deck
        else:
            player.SetDeck(get_random_deck())
    # otherwise, set the deck to the specified index
    else:
        player.SetDeck(decks[po["deck_index"]]["cards"])
    # Make cards know who their owner is
    for c1 in player.deck:
        c1.owner = 0

    # same as above, but for cpu
    dprint("Creating CPU deck from debug options...")
    if co["deck_index"] == -1:
        if len(co["deck_override"]) > 0:
            cpu.SetDeck(co["deck_override"])
        else:
            cpu.SetDeck(get_random_deck())
    else:
        cpu.SetDeck(decks[co["deck_index"]]["cards"])
    for c2 in cpu.deck:
        c2.owner = 1

    # get debugging hand for player
    dprint("Creating player hand from debug options...")
    if len(po["hand"]) > 0:
        for c in po["hand"]:
            # gets a deepcopy of the card and puts it in the player's hand
            startcard = deepcopy([C for C in Cards if C.name == c][0])
            startcard.owner = 0
            player.hand.append(startcard)
    # draw any remaining cards up until specified in the starting hand quantity debug
    # unless it is -1, then don't draw any more
    if po["starting_hand_num"] != -1:
        player.Draw(po["starting_hand_num"] - len(po["hand"]))

    # same as above, but for cpu
    dprint("Creating CPU hand from debug options...")
    if len(co["hand"]) > 0:
        for c in co["hand"]:
            startcard = deepcopy([C for C in Cards if C.name == c][0])
            startcard.owner = 1
            cpu.hand.append(startcard)
    if co["starting_hand_num"] != -1:
        cpu.Draw(co["starting_hand_num"] - len(co["hand"]))

    # get starting player
    dprint(f"Setting starting player... [{debug_options["starting_player"]}]")
    sp = [player, cpu][debug_options["starting_player"]]

    # create game object
    # important: num_lanes is very experimental
    # only some functions have been designed to support more/less than 5 lanes
    dprint(f"Creating game object... [num_lanes: {debug_options["num_lanes"]}]")
    game = Game([player, cpu], sp, debug_options["num_lanes"])

    # simulate days (rounds)
    game.round = debug_options["current_day"]
    if debug_options["simulate_days"]:
        for i in range(debug_options["current_day"]):
            dprint(f"Simulating day {i + 1}...")
            if game.morning_player == player:
                game.cpu_turn(0)
                game.cpu_turn(1)
            else:
                game.cpu_turn(1)
                game.cpu_turn(0)
                
            game.morning_player = game.players[1 - game.players.index(game.morning_player)]
            game.battle_phase()
            game.time = i + 1
            for player in game.players:
                player.Draw(1)
                player.energy = i + 1
    else:
        game.time = game.round + 1
        player.energy = game.round + 1
        cpu.energy = game.round + 1

    dprint("Beginning game loop...")
    game.game_loop()


# get argument variables
if "--debug" in sys.argv:
    start_debugging()


# Get player name (or options such as "debug")
pname = input("What is your name?\n")


if pname == "debug":
    start_debugging()

else:
    print("Select a deck:")
    for deck in decks:
        i = decks.index(deck)
        print(f"{i + 1}. {deck["name"]}")

    deck_selection = input("Select a number or leave blank for random: ")
    if (
        not deck_selection.isnumeric()
        or int(deck_selection) <= 0
        or int(deck_selection) > len(decks)
    ):
        deck_selection = random.randint(1, len(decks))

    deck = decks[int(deck_selection) - 1]["cards"]
    del decks[int(deck_selection) - 1]

    cpu_deck = get_random_deck()

    p1: Player = Player(pname, True)
    p1.SetDeck(deepcopy(deck))
    for c1 in p1.deck:
        c1.owner = 0

    p2: Player = Player("CPU", False)
    p2.SetDeck(cpu_deck.copy())
    for c2 in p2.deck:
        c2.owner = 1

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
        p1.Draw(1)

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
    elif pref == 2 and p2pref == 1:
        starting_player = 0
    elif pref == 2 and p2pref == 0:
        starting_player = 1
    elif p2pref == 0:
        starting_player = 1

    starting_player: Player = p1 if starting_player == 0 else p2

    print(f"{p2.name}'s Preference: {p2pref+1}")
    print(f"{p1.name}'s Preference: {pref+1}")
    sleep(0.8)
    print(f"{starting_player.name} will be the Starting Player!")

    # Create game object and start the game loop
    game = Game([p1, p2], starting_player)
    game.game_loop()
