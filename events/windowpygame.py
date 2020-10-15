#! /usr/bin/python

import os
import pygame as pg
from pygame.locals import *#display, set_mode, set_caption, Surface, get_size, convert, fill, transform, scale, scale2x, render, set_font, get_rect, Rect
import config.settings as constants
from data.images.spritesheet import spritesheet
from data.load_font.set_font import set_font


class WindowPygame():
    """print the surface on the screen"""

    def __init__(self):
        pg.init()

        self.screen_size = constants.SCREEN_SIZE
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("MacGyver - V1.0")
        self.fps = constants.FPS

        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(constants.BLACK)

        self.wall_ss = spritesheet("floor-tiles-20x20.png")
        # How to get the wanted img in sprite :
        # (pos_x, pos_y, img_width, img_height)
        self.wall_rect = constants.WALL_RECT
        self.wall = self.wall_ss.image_at(self.wall_rect)
        self.wall = pg.transform.scale2x(self.wall)

        self.startpol_rect = constants.STARTPOL_RECT
        self.startpol = self.wall_ss.image_at(self.startpol_rect)
        self.startpol = pg.transform.scale2x(self.startpol)

        self.gatekeeper_ss = spritesheet("gardien.png")
        self.gatekeeper_rect = constants.STANDARD_IMG_RECT
        self.gatekeeper = self.gatekeeper_ss.image_at(self.gatekeeper_rect)

        self.macgyver_ss = spritesheet("MacGyver.png")
        self.macgyver_rect = constants.STANDARD_IMG_RECT
        self.macgyver = self.macgyver_ss.image_at(self.macgyver_rect)

        self.plastic_tube_ss = spritesheet("tube_plastique_3.png")
        self.plastic_tube_rect = constants.PLASTIC_TUBE_RECT
        self.plastic_tube_img = self.plastic_tube_ss.image_at(self.plastic_tube_rect)
        self.plastic_tube = pg.transform.scale(self.plastic_tube_img, constants.IMG_SIZE)
        self.plastic_tube2 = pg.transform.scale(self.plastic_tube_img, constants.IMG_SIZE)

        self.ether_ss = spritesheet("ether.png")
        self.ether_rect = constants.ETHER_RECT
        self.ether_img = self.ether_ss.image_at(self.ether_rect)
        self.ether = pg.transform.scale(self.ether_img, constants.IMG_SIZE)
        self.ether2 = pg.transform.scale(self.ether_img, constants.IMG_SIZE)

        self.needle_ss = spritesheet("aiguille.png")
        self.needle_rect = constants.NEEDLE_RECT
        self.needle_img = self.needle_ss.image_at(self.needle_rect)
        self.needle = pg.transform.scale(self.needle_img, constants.IMG_SIZE)
        self.needle2 = pg.transform.scale(self.needle_img, constants.IMG_SIZE)

        self.syringe_ss = spritesheet("seringue.png")
        self.syringe_rect = constants.SYRINGE_RECT
        self.syringe_img = self.syringe_ss.image_at(self.syringe_rect)
        self.syringe = pg.transform.scale(self.syringe_img, constants.IMG_SIZE)

        self.take_tube = False
        self.take_needle = False
        self.take_ether = False

        self.font = set_font("Ranchers-Regular.ttf")
        self.make_syringe = self.font.render("Make a syringe", True, constants.WHITE, constants.BLACK)
        self.you_win = "Congrats, you win!"
        self.loose = "You lose! you die... GAME OVER !!!"
        self.bvo = self.font.render("Nice job! Now, you can get out.", True, constants.WHITE, constants.BLACK)
        self.endgame_w = self.font.render(self.you_win, True, constants.GREEN, constants.BLACK)
        self.endgame_l = self.font.render(self.loose, True, constants.RED, constants.BLACK)

        self.cadre = self.endgame_w.get_rect(topleft=constants.CADRE_POS)
        self.cadre_box = pg.Rect(constants.CADRE_BOX_RECT)


    def blit_wall(self, struct):
        for wall_pos in struct.wall_lst:
            self.screen.blit(self.wall, tuple(wall_pos))

    def blit_start(self, struct):
        self.screen.blit(self.startpol, tuple(struct.start))

    def blit_player(self, player_pos):
        self.screen.blit(self.macgyver, player_pos)

    def blit_gatekeeper(self, struct):
        self.screen.blit(self.gatekeeper, tuple(struct.finnish))

    def blit_tube(self, tube_pos):
        self.screen.blit(self.plastic_tube, tuple(tube_pos))

    def blit_needle(self, needle_pos):
        self.screen.blit(self.needle, tuple(needle_pos))

    def blit_ether(self, ether_pos):
        self.screen.blit(self.ether, tuple(ether_pos))

    def blit_syringe(self):
        self.screen.blit(self.syringe, (410,612))

    def blit_border(self):
        pg.draw.rect(self.background, constants.WHITE, self.cadre_box, 10)

    def blit_make_syringe(self):
        self.screen.blit(self.make_syringe, constants.CADRE_POS)

    def blit_you_win(self):
        self.screen.blit(self.endgame_w, constants.CADRE_POS)

    def blit_you_lose(self):
        self.screen.blit(self.endgame_l, constants.CADRE_POS)

    def blit_you_can_get_out(self):
        self.screen.blit(self.bvo, constants.CADRE_POS)

    def take_tool_and_put_in_toolbox(self, tool):
        if tool == self.ether:
            self.ether = pg.transform.scale(tool, constants.IMG_HIDE_SIZE)
            self.screen.blit(self.ether2, constants.ETHER_POS)
        if tool == self.needle:
            self.needle = pg.transform.scale(self.needle, constants.IMG_HIDE_SIZE)
            self.screen.blit(self.needle2, constants.NEEDLE_POS)
        if tool == self.plastic_tube:
            self.plastic_tube = pg.transform.scale(self.plastic_tube, constants.IMG_HIDE_SIZE)
            self.screen.blit(self.plastic_tube2, constants.PLASTIC_TUBE_POS)