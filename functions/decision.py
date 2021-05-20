import pygame as pg
import sys
from pygame.locals import *
import time
from functions.JcJ_Component import *
from functions.P1_mov_Component import *
from functions.P2_mov_Component import *
from functions.State_Update import *
import serial 
def decision(n,decision1,decision2,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ):
    # ser = serial.Serial('COM3', 9600, timeout = 0)
    if decision1 == "ninguna":
        print("Esperando a Jugador 1")
    elif decision1 == "up":
        # ser.write(b"0\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_cat_up(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision1 == "down":
        # ser.write(b"2\n")
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_cat_down(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision1 == "right":
        # ser.write(b"1\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_cat_right(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision1 == "left":
        # ser.write(b"3\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_cat_left(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
        

    # ser = serial.Serial('COM6', 9600, timeout = 0)
    if decision2 == "ninguna":
        print("Esperando a Jugador 2")
    elif decision2 == "up":
        # ser.write(b"0\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_mouse_up(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision2 == "down":
        # ser.write(b"2\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_mouse_down(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision2 == "right":
        # ser.write(b"1\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_mouse_right(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    elif decision2 == "left":
        # ser.write(b"3\n")  
        # ser.flush()
        # ser.close
        posXG,posYG,posXR,posYR = move_mouse_left(n,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
    return posXG,posYG,posXR,posYR