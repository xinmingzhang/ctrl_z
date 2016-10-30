import os
import pygame as pg
import tools


SCREEN_SIZE = (1280, 720)
ORIGINAL_CAPTION = "Happy Halloween!"

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
SCREEN_RECT = SCREEN.get_rect()

GFX = tools.load_all_gfx(os.path.join("resources", "graphics"))
SFX = tools.load_all_sfx(os.path.join("resources", "sounds"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
