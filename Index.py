import pygame as pg
import sys
from pygame.locals import *
import time
from JcJ_Component import *
from P1_mov_Component import *
from P2_mov_Component import *
from decision import *
import random
import numpy as np
from array_construction import *
from menu import *

def start():
    PI_x = 240 
    PF_x = 840
    PI_y = 60
    PF_y = 660
    n = 7
    dx = (PF_x-PI_x)/(n-1)   
    dy = (PF_y-PI_y)/(n-1)
    coord = coord_array(n,PI_x,PI_y,PF_x,PF_y)
    bk1 = True
    bk2 = True
    p1 = False
    p2 = False
    azul = (0,0,180)
    rojo = (180,0,0)
    color = pg.Color(255,0,0)
    blanco = pg.Color(245,245,245)
    negro =pg.Color(0,0,0)
    pg.init()
    window = pg.display.set_mode((1080,720))
    pg.display.set_caption("Cat & Mouse")
    posi = (60,80)
    posf = (160,100)
    poscircle =(20,20)
    posrect = (190,10,700,700)
    mi_imagen = pg.image.load("Imagenes/queso_opt.png")
    verde = (0,180,0)
    miFuente = pg.font.Font(None,30)
    miTexto1 = miFuente.render("Jugador 1",0,verde)
    miTexto2 = miFuente.render("Jugador 2",0,rojo)
    miTexto3 = miFuente.render("Jugador 1 Ganó",0,verde)
    miTexto4 = miFuente.render("Jugador 2 Ganó",0,rojo)
    velocidad = 0.1
    MododeJuego = "Ninguno"
    posXG,posYG = coord[random.randrange(7),random.randrange(7)]
    posXR,posYR = coord[random.randrange(7),random.randrange(7)]
    posXQ,posYQ = coord[random.randrange(7),random.randrange(7)]
    while True:
        if MododeJuego == "Ninguno":
            MododeJuego = main(window)
        if MododeJuego == "JcJ":
            if bk1 == False and bk2 == False:
                if p1 == True:
                    Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                    Robot_1(posXG,posYG,window)
                    Robot_2(posXR,posYR,window)
                    window.blit(miTexto3,(470,20))
                    pg.display.update()
                    time.sleep(3)
                    start()
                elif p2 == True:
                    Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                    Robot_1(posXG,posYG,window)
                    Robot_2(posXR,posYR,window)
                    window.blit(miTexto4,(470,20))
                    pg.display.update()
                    time.sleep(3)
                    start()
            else:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                pg.display.update()

            while bk1 == True:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                window.blit(miTexto1,(470,20))
                pg.display.update()
                decision1,x1,y1,bk1,bk2 = P1_mov(window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,posXQ,posYQ)
            while bk2 == True:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                window.blit(miTexto2,(470,20))
                pg.display.update()
                decision2,x2,y2,bk1,bk2 = P2_mov(window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,posXQ,posYQ)
            posXG,posYG,posXR,posYR = decision(n,decision1,decision2,window,negro,blanco,posrect,mi_imagen,posYG,posXG,posYR,posXR,velocidad,x1,y1,x2,y2,posXQ,posYQ)
            if abs(posXR-posXQ) <= dx+1 and abs(posYR-posYQ) <= 1:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                window.blit(miTexto4,(470,20))
                pg.display.update()
                bk1 = False
                bk2 = False
                p2 = True
            elif abs(posYR-posYQ) <= dy+1 and abs(posXR-posXQ) <= 1:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                window.blit(miTexto4,(470,20))
                bk1 = False
                bk2 = False
                p2 = True
            elif abs(posXR-posXG) <= dx+1 and abs(posYR-posYG) <= 1:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                window.blit(miTexto3,(470,20))
                pg.display.update()
                bk1 = False
                bk2 = False
                p1 = True
            elif abs(posYR-posYG) <= dy+1 and abs(posXR-posXG) <= 1:
                Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ)
                Robot_1(posXG,posYG,window)
                Robot_2(posXR,posYR,window)
                window.blit(miTexto3,(470,20))
                pg.display.update()
                bk1 = False
                bk2 = False
                p1 = True
                
start()

        
