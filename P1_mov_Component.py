import pygame as pg
import sys
from pygame.locals import *
import time
from JcJ_Component import *


def P1_mov(window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,posXQ,posYQ):
    bk1 = True
    bk2 = True
    decision1 = "ninguna"
    x1 = 0
    y1 = 0
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
            sys.exit()
        elif evento.type == pg.KEYDOWN:
            if evento.key == K_UP:
                y1 = posYG-100
                decision1 = "up"
                bk1 = False
                bk2 = True
            elif evento.key == K_DOWN:
                decision1 = "down"
                y1 = posYG+100
                bk1 = False
                bk2 = True
            elif evento.key == K_RIGHT:
                decision1 = "right"
                x1 = posXG+100
                bk1 = False
                bk2 = True
            elif evento.key == K_LEFT:
                decision1 = "left"
                x1 = posXG-100
                bk1 = False
                bk2 = True
    return decision1,x1,y1,bk1,bk2