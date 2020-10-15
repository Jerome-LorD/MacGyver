import pygame as pg
from pygame.locals import *
from models.labyrinth import Labyrinth
from models.player import Player
from events.windowpygame import WindowPygame
from controllers.controls import ControllerPygame

def main():
    lab = Labyrinth("maze.txt")
    window = WindowPygame()
    player = Player(lab)
    controls = ControllerPygame(player)

    window.blit_border()

    while 1:
        if controls.get_player_input() == 0:
            return

        window.blit_wall(lab)
        window.blit_start(lab)
        window.blit_gatekeeper(lab)
        window.blit_tube(lab.tools_rand.__getitem__(0)[0])
        window.blit_needle(lab.tools_rand.__getitem__(1)[0])
        window.blit_ether(lab.tools_rand.__getitem__(2)[0])
        if lab.collide_tube(player.position):
            window.take_tube = True
        if window.take_tube is True:
            window.take_tool_and_put_in_toolbox(window.plastic_tube)
        if lab.collide_needle(player.position):
            window.take_needle = True
        if window.take_needle is True:
            window.take_tool_and_put_in_toolbox(window.needle)
        if lab.collide_ether(player.position):
            window.take_ether = True
        if window.take_ether is True:
            window.take_tool_and_put_in_toolbox(window.ether)
        if window.take_tube and window.take_needle and window.take_ether\
             and not lab.collide_gatekeeper(player.position):
            window.blit_you_can_get_out()
            window.blit_syringe()
        elif window.take_tube and window.take_needle and window.take_ether\
             and lab.collide_gatekeeper(player.position):
            window.blit_you_win()
        elif (not window.take_tube or not window.take_needle or not window.take_ether)\
             and lab.collide_gatekeeper(player.position):
            window.blit_you_lose()
        elif (not window.take_tube or not window.take_needle or not window.take_ether)\
             and not lab.collide_gatekeeper(player.position):
            window.blit_make_syringe()
        if player.position in lab:
            window.blit_player((player.position.__getitem__(0), player.position.__getitem__(1)))
        pg.display.flip()
        window.screen.blit(window.background, (0, 0))
    pg.display.update()
    pg.time.Clock().tick(window.fps)
    pg.quit()

if __name__ == "__main__":
    main()