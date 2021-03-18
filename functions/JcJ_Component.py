import pygame as pg
import sys
from pygame.locals import *
import time
import numpy as np

def Grid_Create(n,window,negro,blanco,posrect,mi_imagen,posXQ,posYQ):
    PI_x = 240 
    PF_x = 840
    PI_y = 60
    PF_y = 660
    dx = (PF_x-PI_x)/(n-1)   
    dy = (PF_y-PI_y)/(n-1)
    window.fill((0,115,229))
    pg.draw.rect(window,blanco,posrect)
    countx = 0
    county = 0
    while countx < n:
        while county < n:
            pg.draw.line(window,negro,(PI_x,PI_y+(dy*county)),(PF_x,PI_y+(dy*county)),5)                 
            county += 1
        pg.draw.line(window,negro,(PI_x+(dx*countx),PI_y),(PI_x+(dx*countx),PF_y),5)
        countx += 1
    window.blit(mi_imagen,(posXQ-32,posYQ-29))    

def Robot_2(posXR,posYR,window):
    pg.draw.circle(window,(68,68,68),(posXR,posYR),25)
    pg.draw.circle(window,(180,20,20),(posXR,posYR),20)
    pg.draw.circle(window,(0,0,0),(posXR,posYR),10)
    pg.draw.circle(window,(167,173,186),(posXR,posYR),5)

def Robot_1(posXG,posYG,window):
    pg.draw.circle(window,(68,68,68),(posXG,posYG),25)
    pg.draw.circle(window,(125,220,31),(posXG,posYG),20)
    pg.draw.circle(window,(0,0,0),(posXG,posYG),10)
    pg.draw.circle(window,(167,173,186),(posXG,posYG),5)