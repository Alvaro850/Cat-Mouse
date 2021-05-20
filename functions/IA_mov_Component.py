import pygame as pg
import sys
from pygame.locals import *
import time
from functions.JcJ_Component import *
from functions.P1_mov_Component import *
from functions.P2_mov_Component import *
from functions.decision import *
import random
import numpy as np
from functions.array_construction import *
from functions.menu import *
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
from PIL import Image


def IA_mov(start_q_table,dx,dy,posYR,posXR,gridData,n,cont):
    bk1 = False
    bk2 = True
    x2 = 0
    y2 = 0
    decision2 = "ninguna"
    class Blob:
        def __init__(self):
            self.x = random.randrange(n)  
            self.y = random.randrange(n)
        def __str__(self):
            return f"{self.x},{y}"
        def __sub__(self, other):
            return (self.x-other.x, self.y-other.y)
        def action(self, choice):
            if choice == 0:
                self.move(y=-1)
            elif choice == 1:
                self.move(x=1)
            elif choice == 2:
                self.move(y=1)
            elif choice == 3:
                self.move(x=-1)
        def move(self, x=False, y=False):
            if not x:
                self.x += x
            else:
                self.x += x
            if not y:
                self.y += y
            else:
                self.y += y
            
            if self.x < 0:
                self.x = 0
            elif self.x > n-1:
                self.x = n-1
            
            if self.y < 0:
                self.y = 0
            elif self.y > n-1:
                self.y = n-1
    if start_q_table is None:
        q_table = {}
        for x1 in range(-n+1, n):
            for y1 in range(-n+1, n):
                for x2 in range(-n+1, n):
                    for y2 in range(-n+1, n):
                        q_table[((x1,y1), (x2,y2))] = [np.random.uniform(-5,0) for i in range(4)]
    else:
        with open(start_q_table, "rb") as f:
            q_table = pickle.load(f)
    
    player = Blob()
    enemy = Blob()
    food = Blob()
    player.x = gridData.poscXR
    player.y = gridData.poscYR
    enemy.x =gridData.poscXG
    enemy.y = gridData.poscYG
    food.x = gridData.poscXQ
    food.y = gridData.poscYQ
    obs = (player-food, player-enemy)
    if cont == 0:
        action = np.argmax(q_table[obs])
        cont += 1
    else:
        action = np.random.randint(0, 4)
    if action == 0:
        if gridData.poscYR - 1 >= 0:
            decision2 = "up"
            y2 = posYR-dy
            gridData.poscYR -= 1
            bk2 = False
            bk1 = True
        else:
            print("no se puede coger pa aca")
    elif action == 1:
        if gridData.poscXR + 1 <= gridData.n1:
            decision2 = "right"
            x2 = posXR+dx
            gridData.poscXR += 1
            bk2 = False
            bk1 = True
        else:
            print("no se puede coger pa aca")
    elif action == 2:
        if gridData.poscYR + 1 <= gridData.n1:
            decision2 = "down"
            y2 = posYR+dy
            gridData.poscYR += 1
            bk2 = False
            bk1 = True
        else:
            print("no se puede coger pa aca")
    elif action == 3:
        if gridData.poscXG - 1 >= 0:
            decision2 = "left"
            x2 = posXR-dx
            gridData.poscXR -= 1
            bk2 = False
            bk1 = True
        else:
            print("no se puede coger pa aca")

    return decision2, x2, y2, bk1, bk2, gridData