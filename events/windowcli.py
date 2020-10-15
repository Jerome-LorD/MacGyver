import config.settings as constants
from termcolor import colored
from models.labyrinth import Labyrinth

class WindowCLI:
    """print the surface on the screen"""

    def __init__(self):
        self.holster = []
        self.take_tube = False
        self.take_needle = False
        self.take_ether = False

        self.dashes = [
            "# ---------------------------------- #",
            "# --------------------------------------- #",
        ]


    def home(self):
        print(
            f"{self.dashes[0]}\n# ---- MacGyver -- Get out vc-1 ---- #\n\
{self.dashes[0]}\n# commands: up, down, right, left #\n{self.dashes[0]}\n"
        )


    def get_holster(self):
        if len(self.holster) >= 1:
            print(f'In your possession -> {"".join(self.holster)}')
        if len(self.holster) == 3:
            print("You got the syringe, you can get out -> '\U0001F489'")


    def grid(self, player_pos, tools):

        tube_pos = tuple(tools.__getitem__(0)[0])
        needle_pos = tuple(tools.__getitem__(1)[0])
        ether_pos = tuple(tools.__getitem__(2)[0])

        start, walls, finnish, width, height = self.get_structure()
        print(f"{self.dashes[1]}")
        for pos_y in range(height):
            print()

            for pos_x in range(width):
                position = pos_x, pos_y

                if position == player_pos:
                    char = constants.PLAYER_CHAR
                elif position == tube_pos:
                    char = constants.TUBE_CHAR
                elif position == needle_pos:
                    char = constants.NEEDLE_CHAR
                elif position == ether_pos:
                    char = constants.ETHER_CHAR
                elif position in walls:
                    char = constants.WALL_CHAR
                elif position in start:
                    char = constants.START_CHAR
                elif position in finnish:
                    char = constants.FINNISH_CHAR
                else:
                    char = " "

                print(char, end="  ")
        print(f"\n{self.dashes[1]}")


    def get_structure(self):
        walls = []
        start = []
        finnish = []
        width = height = 0

        for pos_y, line in enumerate(Labyrinth("maze.txt").struct):
            for pos_x, char in enumerate(line):
                position = pos_x, pos_y

                if char == constants.WALL_CHAR:
                    walls.append(position)
                elif char == constants.START_CHAR:
                    start.append(position)
                elif char == constants.FINNISH_CHAR:
                    finnish.append(position)

            width = max(width, pos_x + 1)
        height = pos_y + 1

        return start, walls, finnish, width, height

    def you_win(self):
        print("Congats, You WIN")

    def you_lose(self):
        print("You lose, you die\nGAME OVER")
