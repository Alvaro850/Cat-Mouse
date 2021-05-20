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
            

def main(window,n):
    
    pantalla=window
    
    pygame.display.set_caption("El Gato & El Ratón") # Titulo de la Ventana
    #reloj para controlar los fps
    reloj1=pygame.time.Clock()

    
    milogo = pygame.image.load("./imagenes/ajuste.png")
    modificar = pygame.image.load("./imagenes/modificar.png")
    
    flecha1 = pygame.image.load("./imagenes/flecha1.png")
    flecha11 = pygame.image.load("./imagenes/flecha2.png")

    cinco1 = pygame.image.load("./imagenes/cinco1.png")
    cinco11 = pygame.image.load("./imagenes/cinco2.png")

    seis1 = pygame.image.load("./imagenes/seis1.png")
    seis11 = pygame.image.load("./imagenes/seis2.png")

    siete1 = pygame.image.load("./imagenes/siete1.png")
    siete11 = pygame.image.load("./imagenes/siete2.png")

    ocho1 = pygame.image.load("./imagenes/ocho1.png")
    ocho11 = pygame.image.load("./imagenes/ocho2.png")

    nueve1 = pygame.image.load("./imagenes/nueve1.png")
    nueve11 = pygame.image.load("./imagenes/nueve2.png")

    diez1 = pygame.image.load("./imagenes/diez1.png")
    diez11 = pygame.image.load("./imagenes/diez2.png")

    #logo1 = logo(milogo)
   
    boton1 = Boton(flecha1,flecha11,10,10)
    boton2 = Boton(cinco1,cinco11,150,500)
    boton3 = Boton(seis1,seis11,450,500)
    boton4 = Boton(siete1,siete11,750,500)
    boton5 = Boton(ocho1,ocho11,150,610)
    boton6 = Boton(nueve1,nueve11,450,610)
    boton7 = Boton(diez1,diez11,750,610)
    cursor1 = Cursor()


    color_fondo=(46,158,163) # color en RGB
    
    salir=False
    
    while salir!=True:
        #recorro todos los eventos producidos
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    MododeJuego = "Ninguno"
                    return MododeJuego,n
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton2.rect):
                    MododeJuego = "Ninguno"
                    n = 5
                    return MododeJuego,n
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton3.rect):
                    MododeJuego = "Ninguno"
                    n = 6
                    return MododeJuego,n
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton4.rect):
                    MododeJuego = "Ninguno"
                    n = 7
                    return MododeJuego,n
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    MododeJuego = "Ninguno"
                    n = 8
                    return MododeJuego,n
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton6.rect):
                    MododeJuego = "Ninguno"
                    n = 9
                    return MododeJuego,n
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton7.rect):
                    MododeJuego = "Ninguno"
                    n = 10
                    return MododeJuego,n
                    

            # si el evento es del tipo 
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(color_fondo)
        
        pantalla.blit(milogo,(350,0))
        pantalla.blit(modificar,(400,430))
        
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        boton3.update(pantalla,cursor1)
        boton4.update(pantalla,cursor1)
        boton5.update(pantalla,cursor1)
        boton6.update(pantalla,cursor1)
        boton7.update(pantalla,cursor1)

        pygame.display.update() #actualizo el display
        
    pygame.quit()