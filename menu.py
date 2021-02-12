import pygame,sys
import time

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1) #Se crea un rectangulo
    def update(self):
       self.left,self.top = pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=500,y=500):
        self.imagen_normal= imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: 
            self.imagen_actual=self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)
            

def main():
    pygame.init() 
    
    pantalla=pygame.display.set_mode((1080,720))
    
    pygame.display.set_caption("El Gato & El Ratón") # Titulo de la Ventana
    #reloj para controlar los fps
    reloj1=pygame.time.Clock()

    
    milogo = pygame.image.load("fondo.png")
    
    juego1 = pygame.image.load("marron1.png")
    juego11 = pygame.image.load("azul1.png")

    juego2 = pygame.image.load("marron2.png")
    juego22 = pygame.image.load("azul2.png")

    conf1 = pygame.image.load("ajus1.png")
    conf2 = pygame.image.load("ajus2.png")

    #logo1 = logo(milogo)
    boton1 = Boton(juego1,juego11,450,450)
    boton2 = Boton(juego2,juego22,450,580)
    boton3 = Boton(conf1,conf2,1000,30)
    cursor1 = Cursor()


    color_fondo=(46,158,163) # color en RGB
    
    salir=False
    
    while salir!=True:
        #recorro todos los eventos producidos
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    time.sleep(3)
                    salir = True

            # si el evento es del tipo 
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(color_fondo)
        
        pantalla.blit(milogo,(350,0))
        
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        boton3.update(pantalla,cursor1)

        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
main() 