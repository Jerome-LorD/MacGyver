import config.settings as constants
from models.labyrinth import Labyrinth
from models.player import Player
from events.windowcli import WindowCLI
from controllers.controlscli import ControlCLI
from events.switch import Event


def main():
    switched = Event.setval    
    window = WindowCLI()
    lab = Labyrinth("maze.txt", switched)
    player = Player(lab)


    window.home()
    window.grid((player.position.__getitem__(0),player.position.__getitem__(1)), lab.tools_rand)

    controls = ControlCLI(player)

    while 1:
        if controls.get_player_input() == 0:
            return

        player.move(controls.command)

        window.grid((player.position.__getitem__(0), player.position.__getitem__(1)),\
        lab.tools_rand)

        if lab.collide_tube(player.position):
            window.holster.append(constants.TUBE_CHAR)
            constants.TUBE_CHAR = " "
            window.get_holster()
        if lab.collide_needle(player.position):
            window.holster.append(constants.NEEDLE_CHAR)
            constants.NEEDLE_CHAR = " "
            window.get_holster()
        if lab.collide_ether(player.position):
            window.holster.append(constants.ETHER_CHAR)
            constants.ETHER_CHAR = " "
            window.get_holster()
        if lab.collide_gatekeeper(player.position) and len(window.holster) > 2:
            window.you_win()
            return 0
        if lab.collide_gatekeeper(player.position) and len(window.holster) < 3:
            window.you_lose()
            return 0

if __name__ == "__main__":
    main()