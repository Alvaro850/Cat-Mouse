import pygame as pg
import sys
from pygame.locals import *
import time
from functions.JcJ_Component import *


def P1_mov(window, negro, blanco, posrect, mi_imagen, posYG, posXG, posYR, posXR, velocidad, posXQ, posYQ, dx, dy, gridData):
    bk1 = True
    bk2 = False
    decision1 = "ninguna"
    x1 = 0
    y1 = 0
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
            sys.exit()
        elif evento.type == pg.KEYDOWN:
            if evento.key == K_UP:
                if gridData.poscYG - 1 >= 0:
                    y1 = posYG-dy
                    decision1 = "up"
                    bk1 = False
                    bk2 = True
                    gridData.poscYG -= 1
                    print("Y:")
                    print(gridData.poscYG)
                    print("X:")
                    print(gridData.poscXG)
                else:
                    print("no se puede coger pa aca")
            elif evento.key == K_DOWN:
                if gridData.poscYG + 1 <= gridData.n1:
                    decision1 = "down"
                    y1 = posYG+dy
                    bk1 = False
                    bk2 = True
                    gridData.poscYG += 1
                    print("Y:")
                    print(gridData.poscYG)
                    print("X:")
                    print(gridData.poscXG)
                else:
                    print("no se puede coger pa aca")
            elif evento.key == K_RIGHT:
                if gridData.poscXG + 1 <= gridData.n1:
                    decision1 = "right"
                    x1 = posXG+dx
                    bk1 = False
                    bk2 = True
                    gridData.poscXG += 1
                    print("Y:")
                    print(gridData.poscYG)
                    print("X:")
                    print(gridData.poscXG)
                else:
                    print("no se puede coger pa aca")
            elif evento.key == K_LEFT:
                if gridData.poscXG - 1 >= 0:
                    decision1 = "left"
                    x1 = posXG-dx
                    bk1 = False
                    bk2 = True
                    gridData.poscXG -= 1
                    print("Y:")
                    print(gridData.poscYG)
                    print("X:")
                    print(gridData.poscXG)
                else:
                    print("no se puede coger pa aca")
    
    return decision1, x1, y1, bk1, bk2,gridData
