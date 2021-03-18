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




n = 10
HM_EPISODES = 2
MOVE_PENALTY = 1
ENEMY_PENALTY = 300
FOOD_REWARD = 25
epsilon = 0.9
EPS_DECAY = 0.9998
SHOW_EVERY = 1

start_q_table = None

LEARNING_RATE = 0.1
DISCOUNT = 0.95

PLAYER_N = 1
FOOD_N = 2
ENEMY_N = 3
d = {1: (255, 175, 0),
     2:(0, 255, 0),
     3:(0, 0, 255)}

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


episode_rewards = []
for episode in range(HM_EPISODES):
    PI_x = 240
    PF_x = 840
    PI_y = 60
    PF_y = 660
    n = n
    dx = (PF_x-PI_x)/(n-1)
    dy = (PF_y-PI_y)/(n-1)
    coord = coord_array(n, PI_x, PI_y, PF_x, PF_y)
    bk1 = True
    bk2 = True
    p1 = False
    p2 = False
    player = Blob()
    food = Blob()
    enemy = Blob()
    posXG, posYG = coord[enemy.y, enemy.x]
    posXR, posYR = coord[player.y, player.x]
    posXQ, posYQ = coord[food.y, food.x]  
    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon: {epsilon}")
        print(f"{SHOW_EVERY} ep mean {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True
    else:
        show = False
    
    episode_reward = 0
    for i in range(200):
        obs = (player-food, player-enemy)
        if np.random.random() > epsilon:
            action = np.argmax(q_table[obs])
            actione = np.random.randint(0, 4)
        else:
            action = np.random.randint(0, 4)
            actione = np.random.randint(0, 4) 
        player.action(action)
        enemy.action(actione)
        #food.move()
        posXG, posYG = coord[enemy.y, enemy.x]
        posXR, posYR = coord[player.y, player.x]
        posXQ, posYQ = coord[food.y, food.x] 
        
        if abs(posXR-posXQ) <= dx+1 and abs(posYR-posYQ) <= 1:
            reward = FOOD_REWARD
            bk1 = False
            bk2 = False
            p2 = True
        elif abs(posYR-posYQ) <= dy+1 and abs(posXR-posXQ) <= 1:
            reward = FOOD_REWARD
            bk1 = False
            bk2 = False
            p2 = True
        elif abs(posXR-posXG) <= dx+1 and abs(posYR-posYG) <= 1:
            reward = -ENEMY_PENALTY
            bk1 = False
            bk2 = False
            p1 = True
        elif abs(posYR-posYG) <= dy+1 and abs(posXR-posXG) <= 1:
            reward = -ENEMY_PENALTY
            bk1 = False
            bk2 = False
            p1 = True
        else:
            reward = -MOVE_PENALTY

        new_obs = (player-food, player-enemy)
        max_future_q = np.max(q_table[new_obs])
        current_q = q_table[obs][action]
        if reward == FOOD_REWARD:
            new_q = FOOD_REWARD
        elif reward == -ENEMY_PENALTY:
            new_q = -ENEMY_PENALTY
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[obs][action] = new_q

        if show:
            azul = (0, 0, 180)
            rojo = (180, 0, 0)
            color = pg.Color(255, 0, 0)
            blanco = pg.Color(245, 245, 245)
            negro = pg.Color(0, 0, 0)
            pg.init()
            pg.display.set_caption("Cat & Mouse")
            window = pg.display.set_mode((1080, 720))
            posi = (60, 80)
            posf = (160, 100)
            poscircle = (20, 20)
            posrect = (190, 10, 700, 700)
            mi_imagen = pg.image.load("Imagenes/queso_opt.png")
            verde = (0, 180, 0)
            miFuente = pg.font.Font(None, 30)
            miTexto1 = miFuente.render("Jugador 1", 0, verde)
            miTexto2 = miFuente.render("Jugador 2", 0, rojo)
            miTexto3 = miFuente.render("Jugador 1 Ganó", 0, verde)
            miTexto4 = miFuente.render("Jugador 2 Ganó", 0, rojo)
            velocidad = 0.1
            time.sleep(0.5)
            if bk1 == False and bk2 == False:
                if p1 == True:
                    Grid_Create(n, window, negro, blanco, posrect, mi_imagen, posXQ, posYQ)
                    Robot_1(posXG, posYG, window)
                    Robot_2(posXR, posYR, window)
                    window.blit(miTexto3, (470, 20))
                    pg.display.update()           
                elif p2 == True:
                    Grid_Create(n, window, negro, blanco, posrect, mi_imagen, posXQ, posYQ)
                    Robot_1(posXG, posYG, window)
                    Robot_2(posXR, posYR, window)
                    window.blit(miTexto4, (470, 20))
                    pg.display.update()
            else:
                Grid_Create(n, window, negro, blanco, posrect, mi_imagen, posXQ, posYQ)
                Robot_1(posXG, posYG, window)
                Robot_2(posXR, posYR, window)
                pg.display.update()
        episode_reward += reward
        if reward == FOOD_REWARD or reward == -ENEMY_PENALTY:
            break
    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY
moving_avg = np.convolve(episode_rewards,np.ones((SHOW_EVERY, ))/ SHOW_EVERY, mode="valid")

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()

with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)













