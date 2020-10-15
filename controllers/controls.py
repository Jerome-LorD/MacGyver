import pygame as pg
from pygame.locals import *
from models.player import Player as player


class ControllerPygame:
    """docstr"""
    def __init__(self, player):
        self.player = player

    def get_player_input(self):
        # player = Player(Labyrinth("maze.txt"))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.move("left")
                elif event.key == pg.K_UP:
                    self.player.move("up")
                elif event.key == pg.K_RIGHT:
                    self.player.move("right")
                elif event.key == pg.K_DOWN:
                    self.player.move("down")
        return 1