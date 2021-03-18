import pygame as pg
import sys
from pygame.locals import *
import time
from functions.JcJ_Component import *
from functions.P1_mov_Component import *
from functions.P2_mov_Component import *
from functions.State_Update import *
def decision(n,decision1,decision2,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    if decision1 == "ninguna":
        print("Esperando a Jugador 1")
    elif decision1 == "up":
        posXG,posYG,posXR,posYR = move_cat_up(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision1 == "down":
        posXG,posYG,posXR,posYR = move_cat_down(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision1 == "right":
        posXG,posYG,posXR,posYR = move_cat_right(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision1 == "left":
        posXG,posYG,posXR,posYR = move_cat_left(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    
    if decision2 == "ninguna":
        print("Esperando a Jugador 2")
    elif decision2 == "up":
        posXG,posYG,posXR,posYR = move_mouse_up(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision2 == "down":
        posXG,posYG,posXR,posYR = move_mouse_down(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision2 == "right":
        posXG,posYG,posXR,posYR = move_mouse_right(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision2 == "left":
        posXG,posYG,posXR,posYR = move_mouse_left(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    return posXG,posYG,posXR,posYR