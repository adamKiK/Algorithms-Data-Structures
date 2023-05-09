import time

"""
Player class keeps information about:
- player scored points
- the figure chosen by a player
- player's name

Implemented methods 
"""


class Player:
    def __init__(self):
        self.match_points = 0
        self.chosen_figure = ""
        self.player_name = ""

    def set_player_name(self) -> None:
        time.sleep(0.5)
        self.player_name = input("Enter your name: ")
        time.sleep(0.25)
        print("Thank you " + self.player_name + "!")
        time.sleep(1)

    def set_figure(self, new_figure) -> None:
        self.chosen_figure = new_figure

    def add_match_point(self) -> None:
        self.match_points += 1

    def get_name(self) -> str:
        return self.player_name

    def get_score(self) -> int:
        return self.match_points

    def get_figure(self) -> str:
        return self.chosen_figure
