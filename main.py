import sys
import pygame as pg

from state_engine import Game
import prepare
import splash, carving

states = {"SPLASH": splash.Splash(),
               "CARVING": carving.Carving()}
              
game = Game(prepare.SCREEN, states, "SPLASH")
game.run()
pg.quit()
sys.exit()