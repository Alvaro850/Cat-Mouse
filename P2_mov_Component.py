import pygame as pg
import sys
from pygame.locals import *
import time
from JcJ_Component import *


def P2_mov(window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,posXQ,posYQ):
    bk2 = True
    bk1 = True
    decision2 = "ninguna"
    x2 = 0
    y2 = 0
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
            sys.exit()
        elif evento.type == pg.KEYDOWN:
            if evento.key == K_w:
                y2 = posYR-100
                decision2 = "up"
                bk2 = False
                bk1 = True
            elif evento.key == K_s:
                y2 = posYR+100
                decision2 = "down"
                bk2 = False
                bk1 = True
            elif evento.key == K_d:
                x2 = posXR+100
                decision2 = "right"
                bk2 = False
                bk1 = True
            elif evento.key == K_a:
                x2 = posXR-100
                decision2 = "left"
                bk2 = False
                bk1 = True
    return decision2,x2,y2,bk1,bk2