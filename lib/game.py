from .classes import *
from beautifultable import BeautifulTable
import platform, subprocess
from time import sleep
import sys
from os import path, getcwd


class Lane:
    def __init__(self, index: int, num_players: int = 2) -> None:
        self.minions: list[list[Minion]] = [[] for i in range(num_players)]
        self.items: list[list[Item]] = [[] for i in range(num_players)]
        self.area: list[Area] = None
        self.area_owner: int = -1
        self.lane_index: int = index

    def GetItems(self, player_index: int):
        return self.items[player_index]

    def GetMinion(self, player_index: int) -> Minion:
        if self.HasMinions(player_index):
            return self.minions[player_index][0]

    def HasMinions(self, player_index: int = -1) -> bool:
        if player_index >= 0:
            return len(self.minions[player_index]) > 0

        return any(minions for minions in self.minions)

    def HasArea(self) -> bool:
        return self.area is not None and self.area_owner != -1


class Playable:
    def __init__(self, card: Card, lanes: list[bool]):
        self.card = card
        self.lanes = lanes


class Game:
    def __init__(self, players, morning_player: Player, num_lanes: int = 5) -> None:
        self.round: int = 0
        self.players: list[Player] = players
        self.morning_player: Player = morning_player
        self.lanes = [Lane(i) for i in range(5)]
        self.num_lanes: int = num_lanes
        self.time: int = 1


    def GetEmptyLanes(
        self, player: Player | None = None, lanes: list[Lane] = None
    ) -> list[Lane]:
        if player is not None:
            player_index = self.players.index(player)
            return [
                lane
                for lane in (lanes if lanes is not None else self.lanes)
                if not lane.HasMinions(player_index)
            ]

        return [
            lane
            for lane in (lanes if lanes is not None else self.lanes)
            if not lane.HasMinions()
        ]


    def GetEmptyLaneIndices(
        self, player: Player | None = None, lanes: list[Lane] = None
    ) -> list[int]:
        return [self.lanes.index(lane) for lane in self.GetEmptyLanes(player, lanes)]


    def GetLanesWithAreas(self) -> list[Lane]:
        return [lane for lane in self.lanes if lane.HasArea()]


    def GetEmptyLaneIndicesWithAreas(self, player: Player | None = None) -> list[int]:
        area_lanes = self.GetLanesWithAreas()
        return self.GetEmptyLaneIndices(player, area_lanes)


    def GetLaneIndicesWithAreas(self) -> list[int]:
        return [self.lanes.index(lane) for lane in self.GetLanesWithAreas()]


    def GetCardPlayableLanes(self, player: Player, card: Card) -> list[bool]:
        """
        Gets the playability for a card in the game board's lanes

        Returns:
            list[bool]: A list of bool representing their corresponding lane and whether this card
                can be placed there.
        """

        lanes = [False] * self.num_lanes

        # ensure this card is in this player's hand
        if not card in player.hand:
            return lanes

        # force the card to be a minion (temporary)
        if not isinstance(card, Minion):
            return lanes

        # Check energy requirements
        if card.energy > player.energy:
            # Cards with Explorer trait need 1 less energy in lanes with an area
            if "Explorer" in card.traits and player.energy + 1 <= card.energy and isinstance(card, Minion):
                # get all empty lanes on the board that have an area set
                area_lanes = self.GetEmptyLaneIndicesWithAreas(player)
                for i in area_lanes:
                    lanes[i] = True

            return lanes

        # check time requirements if this is an afternoon player
        if player is not self.morning_player and card.time > self.time:
            return lanes

        # set playable lanes to those without any of this player's minions currently in
        empty_lanes = self.GetEmptyLaneIndices(player)
        for i in empty_lanes:
            lanes[i] = True

        return lanes


    def GetHandPlayableLanes(self, player: Player) -> list[Playable]:
        return [
            Playable(card, self.GetCardPlayableLanes(player, card))
            for card in player.hand
        ]


    def IsValidMove(self, move: str, player: Player) -> bool:
        if not "l" in move.lower():
            return False

        move: list[str] = move.lower().split("l")
        if len(move) != 2:
            return False

        if not move[0].isnumeric() or not move[1].isnumeric():
            return False

        card_index = int(move[0]) - 1
        lane_index = int(move[1]) - 1

        if card_index < 0 or lane_index < 0:
            return False

        if card_index >= len(player.hand) or lane_index >= self.num_lanes:
            return False

        playable = self.GetHandPlayableLanes(player)
        card_playable = playable[card_index]
        if not card_playable.lanes[lane_index]:
            print(
                f"You're unable to play '{card_playable.card.name}' in Lane {lane_index + 1}."
            )
            return False

        player_index = self.players.index(player)
        self.lanes[lane_index].minions[player_index].append(card_playable.card)
        player.hand.remove(card_playable.card)
        if self.morning_player == player:
            self.time += card_playable.card.time
        else:
            self.time -= card_playable.card.time
        player.energy -= card_playable.card.energy

        # Make card perform actions it has upon being played
        card_playable.card.on_being_played(self.lanes[lane_index])

        self.print_board()
        player.PrintHand()
        print(
            f'{player.name} played "{card_playable.card.name}" in Lane {lane_index + 1}!'
        )

        return True


    def print_board(self):
        print()
        print(f"ROUND {self.round + 1}")
        p1 = self.players[0]
        p2 = self.players[1]

        print(f"{p2.name} - {p2.energy} ⚡︎ - {self.time} ೱ - {p2.health} ♥")

        p1_row = ["   "] * self.num_lanes
        p2_row = ["   "] * self.num_lanes

        for i in range(self.num_lanes):
            minions = self.lanes[i].minions
            if len(minions[0]) > 0:
                p1_row[i] = " * "
            if len(minions[1]) > 0:
                p2_row[i] = " * "

        lane_names = list[str](range(1, self.num_lanes + 1))
        t = BeautifulTable()
        t.rows.append(p2_row)
        t.rows.append(lane_names)
        t.rows.append(p1_row)
        print(t)

        print(f"{p1.name} - {p1.energy} ⚡︎ - {self.time} ೱ - {p1.health} ♥")

    

    # Processes attacks from an AttackClass
    def process_attacks(self, attacks: list[AttackClass]):
        for att in attacks:
            target_lane = self.lanes[att.target_lane]
            target_player = self.players[att.target_player]
            
            # If the side has a Minion, attack said Minion
            if len(target_lane.minions[att.target_player]) > 0:
                target_minion = target_lane.minions[att.target_player][0]
                target_minion.take_damage(att)
                self.process_damage_taken(target_player, target_lane, target_minion)
            # Otherwise, attack the player
            else:
                target_player.health -= att.damage_value
                print(f"{target_player.name} took {att.damage_value} damage.")
                self.process_damage_taken(target_player)


    # Call this once something should have taken damage, to see if it has died.
    # If a Player was attacked, do not send a Minion and Lane
    def process_damage_taken(self, target_player: Player, lane: Lane = None, target_minion: Minion = None):

        # If a Minion was said to be attacked and it's health 0, kill and discard it
        if target_minion is not None and target_minion.health <= 0:
            print(
            f"{target_player.name}'s {target_minion.name} was defeated!"
            )

            # This block should later refer to on-being-killed() instead
            # That can only be done once cards can call the game to remove themselves instead
            target_minion.reset_stats()
            if target_player == self.players[0]:
                lane.minions[0].remove(target_minion)
            else:
                lane.minions[1].remove(target_minion)
            
        # If no Minion was attacked, check if the players are still alive
        if self.players[0].health <= 0:
            print("You lost...")
            input("Press enter to see CPU hand")
            self.players[1].PrintHand()
            input("Press enter to end game")
            exit()
        elif self.players[1].health <= 0:
            print("YOU GOT THE WWWWWWWWW!")
            input("Press enter to see CPU hand")
            self.players[1].PrintHand()
            input("Press enter to end game")
            exit()




    # Main game loop
    def game_loop(self):
        p1 = self.players[0]
        p2 = self.players[1]

        while True:
            morning_index = self.players.index(self.morning_player)
            if morning_index == 0:
                self.print_board()
                self.player_turn(self.players[0])
                for move in self.cpu_turn():
                    print(move)
                    sleep(0.5)
            else:
                for move in self.cpu_turn():
                    print(move)
                    sleep(0.5)
                self.print_board()
                self.player_turn(self.players[0])


            # START NIGHT PHASE
            input(f"Press enter to start the battle!")
            self.battle_phase()
            sleep(1)
            input(f"\nPress enter to continue to Round {self.round + 2}...\n")

            self.morning_player = self.players[
                1 - self.players.index(self.morning_player)
            ]
            self.round += 1
            self.time = self.round + 1
            for player in self.players:
                player.Draw(1)
                player.energy = self.round + 1



    # Night Phase
    def battle_phase(self):
        for lane in self.lanes:
            lane_index = lane.lane_index

            ls = f"Lane {lane_index + 1}: "
            minions = lane.minions

            p1_has_minion = len(minions[0]) > 0
            p2_has_minion = len(minions[1]) > 0

            attacksP1: list[AttackClass] = []
            attacksP2: list[AttackClass] = []

            # Register the attacks that may be performed later
            m1 = None
            if p1_has_minion:
                m1 = minions[0][0]
                attacksP1 = m1.perform_attack()
                
            m2 = None
            if p2_has_minion:
                m2 = minions[1][0]
                attacksP2 = m2.perform_attack()


            # First Strike check on p1, only applies if there are two minions in a lane
            fs = "First Strike"
            if p1_has_minion and fs in m1.traits and p2_has_minion and not (fs in m2.traits):

                print(f"\n{ls}{m1.name} has the first strike!")
                self.process_attacks(attacksP1)

                # Second Minion only attacks if still alive
                if len(minions[1]) > 0:
                    print(f"\n{ls}Now {m2.name} gets to attack!")
                    self.process_attacks(attacksP2)

                continue


            # First Strike check on p2, only applies if there are two minions in a lane
            elif p2_has_minion and fs in m2.traits and p1_has_minion and not (fs in m1.traits):

                print(f"\n{ls}{m2.name} has the first strike!")
                self.process_attacks(attacksP2)

                # Second Minion only attacks if still alive
                if len(minions[0]) > 0:
                    print(f"\n{ls}Now {m1.name} gets to attack!")
                    self.process_attacks(attacksP1)

                continue


            # neither has First Strike or both have First Strike, so simultaneous attack
            # P1 has priority, so if P1 and P2 minions would both kill the opposing player, P2 would lose.
            # However, if P1 Minion defeats P2 Minion, P2 Minion still gets to process its attack.
            else:
                if p1_has_minion and not p2_has_minion:
                    print(f"\n{ls}{m1.name} attacks!")
                    self.process_attacks(attacksP1)

                elif p2_has_minion and not p1_has_minion:
                    print(f"\n{ls}{m2.name} attacks!")
                    self.process_attacks(attacksP2)
                        
                elif p1_has_minion and p2_has_minion:
                    print(f"\n{ls}{m1.name} and {m2.name} both attack!")
                    self.process_attacks(attacksP1)
                    self.process_attacks(attacksP2)
    


    def player_turn(self, player: Player):
        player.PrintHand()
        print("It's your turn!")
        sleep(0.2)
        print("...")
        sleep(0.2)
        print(
            "Place Card: xLy  | x = card#, y = lane#   | "
            "e.g. 1L3 (puts card 1 from hand in lane 3)"
        )
        print(
            "Board Info: ixLy | x = player#, y = lane# | "
            "e.g. i2L4 (gives info on your opponents card in lane 4)"
        )
        print(
            "Hand Info:  ihx  | x = card#              | "
            "e.g. ih2 (gives info on card 2 in your hand)"
        )
        print("End Turn:   end  |")
        sleep(0.2)
        print("...")
        sleep(0.2)

        move = ""
        while True:
            move = input("Type your move: ")
            if move == "debugme":
                print("These are your playable options:")
                t = BeautifulTable()
                t.columns.header = ["Card", "1", "2", "3", "4", "5"]
                for p in self.GetHandPlayableLanes(player):
                    t.rows.append(
                        [
                            p.card.name,
                            "✔" if p.lanes[0] else "",
                            "✔" if p.lanes[1] else "",
                            "✔" if p.lanes[2] else "",
                            "✔" if p.lanes[3] else "",
                            "✔" if p.lanes[4] else "",
                        ]
                    )
                print(t)
                continue

            elif move == "debugcpu":
                print("These are the CPU's playable options:")
                t = BeautifulTable()
                t.columns.header = ["Card", "1", "2", "3", "4", "5"]
                for p in self.GetHandPlayableLanes(self.players[1]):
                    t.rows.append(
                        [
                            p.card.name,
                            "✔" if p.lanes[0] else "",
                            "✔" if p.lanes[1] else "",
                            "✔" if p.lanes[2] else "",
                            "✔" if p.lanes[3] else "",
                            "✔" if p.lanes[4] else "",
                        ]
                    )
                print(t)
                continue

            if len(move) >= 3 and move[0] == "i":
                if move[1] == "h":
                    if move[2:].isnumeric():
                        i = int(move[2:]) - 1
                        if i < 0 or i >= len(player.hand):
                            continue

                        card = player.hand[i]
                        card_image = path.join(getcwd(), "cards", "images", card.image)

                        if platform.system() == "Darwin":
                            subprocess.call(("open", card_image))
                        elif platform.system() == "Windows":
                            subprocess.call(["start", card_image])

                else:
                    if "l" in move.lower():
                        options = move[1:].lower().split("l")
                        if len(options) == 2:
                            if all(opt.isnumeric() for opt in options):
                                pnum = int(options[0]) - 1
                                cnum = int(options[1]) - 1
                                if pnum < 0 or pnum >= len(self.players):
                                    continue
                                if cnum < 0 or cnum >= self.num_lanes:
                                    continue
                                if len(self.lanes[cnum].minions[pnum]) == 0:
                                    continue

                                card = self.lanes[cnum].minions[pnum][0]
                                card_image = path.join(
                                    getcwd(), "cards", "images", card.image
                                )

                                if platform.system() == "Darwin":
                                    subprocess.call(("open", card_image))
                                elif platform.system() == "Windows":
                                    subprocess.call(["start", card_image])

            elif move == "end":
                break

            self.IsValidMove(move, player)


    def cpu_turn(self, player_index: int = 1) -> list[str]:
        print(f"It's {self.players[player_index].name}'s turn!")
        sleep(0.5)
        moves = []
        while True:
            # get this player's current hand playable lanes (list of card + its playable lanes)
            playable = self.GetHandPlayableLanes(self.players[player_index])
            playable = [p for p in playable if any(l for l in p.lanes)]
            if "--debug" in sys.argv:
                for p in playable:
                    print(f"[DEBUG] Playable [{player_index}]: {p.card.name}, {p.lanes}")

            # if there are no playable cards in hand, end the turn
            if len(playable) == 0:
                break

            # get any empty lanes that cards could be played in
            empty_lanes = self.GetEmptyLaneIndices(self.players[player_index])
            # if there are none, end the turn
            if len(empty_lanes) == 0:
                break

            # grab a random lane index that's empty
            lane = empty_lanes[random.randint(0, len(empty_lanes) - 1)]

            # grab a random playable card
            card = playable[random.randint(0, len(playable) - 1)].card

            # place the card in the lane and remove it from the player's hand
            self.lanes[lane].minions[player_index].append(card)
            self.players[player_index].hand.remove(card)
            card.on_being_played(self.lanes[lane])

            # update time
            if self.morning_player == self.players[player_index]:
                self.time += card.time
            else:
                self.time -= card.time
            # update energy
            self.players[player_index].energy -= card.energy

            moves.append(f'CPU [{player_index}] played "{card.name}" in Lane {lane + 1}!')

        if len(moves) == 0:
            moves.append(f"CPU [{player_index}] made no moves this round.")
        return moves
