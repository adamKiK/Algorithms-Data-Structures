import random
import time
import player
# import os
""" import in case of trying to run in console to clear contents """


class Game:
    def __init__(self):
        self.match_count = None
        self.round_number = 1
        self.game_types = ["Bo1", "Bo3", "Bo5"]
        self.available_figures = ["Kamień", "Papier", "Nożyce"]
        self.player_1 = player.Player()
        self.player_2 = player.Player()

    def set_player_names(self) -> None:
        print("Let's set the first player's name!")
        self.player_1.set_player_name()
        print("Let's set the second player's name!")
        self.player_2.set_player_name()

    def set_match_count(self) -> None:
        while True:
            user_input = input("Choose Your Game Type: ")
            if self.input_is_valid(user_input):
                self.match_count = int(self.game_types[int(user_input) - 1][-1])
                break
            else:
                print("\nYour input has to be a number. Try again!")

    def set_players_figure(self, selected_player: player) -> None:
        chosen_figure_index = int(input("Enter the index of your chosen figure: ")) - 1
        figure = self.available_figures[chosen_figure_index]
        selected_player.set_figure(figure)

    def print_possible_game_types(self) -> None:
        print("Choose Your Match Count")
        print("______________")
        game_types_length = len(self.game_types)
        for game_type_index in range(game_types_length):
            game_type = self.game_types[game_type_index]
            time.sleep(0.25)
            print(game_type_index + 1, game_type)

    def print_figure_set(self) -> None:
        figure_set_size = len(self.available_figures)
        for figure_index in range(figure_set_size):
            indexed_figure = str(figure_index + 1) + ". " + self.available_figures[figure_index]
            time.sleep(0.25)
            print(indexed_figure)

    def input_is_valid(self, user_input) -> bool:
        return int(user_input) > 0 and int(user_input) - 1 < len(self.game_types)

    def shuffle_figure_set(self) -> None:
        random.shuffle(self.available_figures)

    def get_players_score(self) -> str:
        return str(self.player_1.match_points) + ":" + str(self.player_2.match_points)

    def evaluate_result(self) -> player:
        player1_figure = self.player_1.get_figure()
        player2_figure = self.player_2.get_figure()

        if player1_figure == player2_figure:
            return None
        elif player1_figure == "Kamień":
            if player2_figure == "Papier":
                return self.player_2
            else:
                return self.player_1
        elif player1_figure == "Papier":
            if player2_figure == "Kamień":
                return self.player_1
            else:
                return self.player_2
        elif player1_figure == "Nożyce":
            if player2_figure == "Papier":
                return self.player_1
            else:
                return self.player_2

    def sum_up_round_results(self) -> None:
        round_winner = self.evaluate_result()
        if round_winner is not None:
            round_winner.add_match_point()
            print("This round belongs to " + round_winner.get_name())
        else:
            print("This is a TIE!")
            print("You both chose -> " + self.player_1.get_figure() + " vs " + self.player_2.get_figure())

    def player_turn(self, current_player: player) -> None:
        current_player_name = current_player.get_name()
        if current_player == self.player_1:
            other_player = self.player_2
        else:
            other_player = self.player_1
        print(other_player.get_name() + " - Close Your Eyes!")
        time.sleep(2)
        print("Here is the table of available figures for " + current_player_name)
        self.shuffle_figure_set()
        self.print_figure_set()
        self.set_players_figure(current_player)
        self.clear_console()

    def game_round(self):
        print("Let's start round number " + str(self.round_number))
        time.sleep(0.5)
        print("The score is -> " + self.get_players_score())
        time.sleep(0.5)
        self.player_turn(self.player_1)
        self.player_turn(self.player_2)

    def continue_game(self):
        return self.player_1.get_score() < self.match_count // 2 + 1 \
            and self.player_2.get_score() < self.match_count // 2 + 1

    def print_final_result(self):
        self.get_players_score()
        time.sleep(0.5)
        print("THE WINNER IS")
        for i in range(5):
            time.sleep(0.1 * 5)
            print("!" * 2 * i)
        print("\n")
        if self.player_1.get_score() > self.player_2.get_score():
            print(self.player_1.get_name())
        else:
            print(self.player_2.get_name())

        print("With a score of " + self.get_players_score())

    def game(self) -> None:
        self.clear_console()
        self.print_game_starting_text()
        self.set_player_names()
        self.clear_console()
        self.print_possible_game_types()
        self.set_match_count()
        self.clear_console()
        while True:
            if self.continue_game():
                self.game_round()
                self.sum_up_round_results()
                self.round_number += 1
            else:
                self.print_final_result()
                break

    @staticmethod
    def clear_console():
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 100)

    @staticmethod
    def print_game_starting_text() -> None:
        print("\nHello Players!")
        print("______________")
        time.sleep(3)
