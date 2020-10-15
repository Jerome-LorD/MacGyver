import os
import pygame as pg
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
fonts_dir = os.path.join(main_dir, "Ranchers")

def set_font(file):
    if file is not None:
        font_base = os.path.join(fonts_dir, file)
        try:
            font_perso = pg.font.Font(font_base, 30)
        except pg.error:
            raise SystemExit(f"Cannot load font: {file} {pg.get_error()}")
        return font_perso