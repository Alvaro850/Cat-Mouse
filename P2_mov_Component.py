import pygame as pg
import sys
from pygame.locals import *
import time
from JcJ_Component import *


def P2_mov(window, negro, blanco, posrect, mi_imagen, posYG, posXG, posYR, posXR, velocidad, posXQ, posYQ, dx, dy, gridData):
    bk2 = True
    bk1 = False
    decision2 = "ninguna"
    x2 = 0
    y2 = 0
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
            sys.exit()
        elif evento.type == pg.KEYDOWN:

            if evento.key == K_w:
                if gridData.poscYR - 1 >= 0:
                    y2 = posYR-dy
                    decision2 = "up"
                    bk2 = False
                    bk1 = True
                    gridData.poscYR -= 1
                else:
                    print("no se puede coger pa aca")
            elif evento.key == K_s:
                if gridData.poscYR + 1 <= gridData.n1:
                    y2 = posYR+dy
                    decision2 = "down"
                    bk2 = False
                    bk1 = True
                    gridData.poscYR += 1
                else:
                    print("no se puede coger pa aca")
            elif evento.key == K_d:
                if gridData.poscXR + 1 <= gridData.n1:
                    x2 = posXR+dx
                    decision2 = "right"
                    bk2 = False
                    bk1 = True
                    gridData.poscXR += 1
                else:
                    print("no se puede coger pa aca")
            elif evento.key == K_a:
                if gridData.poscXR - 1 >= 0:
                    x2 = posXR-dx
                    decision2 = "left"
                    bk2 = False
                    bk1 = True
                    gridData.poscXR -= 1
                else:
                    print("no se puede coger pa aca")
    return decision2, x2, y2, bk1, bk2, gridData
