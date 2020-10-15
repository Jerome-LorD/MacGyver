from models.player import Player as player


class ControlCLI:
    """docstr"""
    def __init__(self, player):
        self.player = player
        self.command = ""
        self.board = ["up", "right", "down", "left", "q"]
    def get_player_input(self):
        board = ["up", "right", "down", "left", "q"]

        while 1:
            try:
                self.command = str(input("Chose the direction: "))
            except ValueError:
                print('Invalid input! Type character please.')
                return 1
            if self.command == "q":
                print("thx, until next time")
                return 0
            if self.command not in board:
                print("Command not in the board")
                return 1
            return self.command
        return 1