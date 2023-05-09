import time


class Player:
    def __init__(self):
        self.match_points = 0
        self.chosen_figure = ""
        self.player_name = ""

    def set_player_name(self):
        time.sleep(0.5)
        self.player_name = input("Enter your name: ")
        time.sleep(0.25)
        print("Thank you " + self.player_name + "!")
        time.sleep(1)

    def set_figure(self, new_figure):
        self.chosen_figure = new_figure

    def get_name(self):
        return self.player_name

    def add_match_point(self):
        self.match_points += 1

    def get_score(self):
        return self.match_points

    def get_figure(self):
        return self.chosen_figure
