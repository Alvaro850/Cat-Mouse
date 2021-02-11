import pygame as pg
import sys
from pygame.locals import *
import time
from JcJ_Component import *

def move_cat_up(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if posYG > 60:
        while posYG >= y1:
            posYG -= velocidad
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR
def move_cat_down(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):   
    if posYG < 660:
        while posYG <= y1:
            posYG += velocidad
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR
def move_cat_right(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if posXG < 840:
        while posXG <= x1:
            posXG += velocidad
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR
def move_cat_left(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if posXG > 240:
        while posXG >= x1:
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            posXG -= velocidad
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR


def move_mouse_up(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if posYR > 60:
        while posYR >= y2:
            posYR -= velocidad
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR
def move_mouse_down(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):   
    if posYR < 660:
        while posYR <= y2:
            posYR += velocidad
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR
def move_mouse_right(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if posXR < 840:
        while posXR <= x2:
            posXR += velocidad
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR
def move_mouse_left(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if posXR > 240:
        while posXR >= x2:
            Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
            posXR -= velocidad
            Robot_1(posXG,posYG,window)
            Robot_2(posXR,posYR,window)
            pg.display.update()
    return posXG,posYG,posXR,posYR