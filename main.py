#JUEGO DE PROGRAMACIÓN

#ZOE
#DIEGO
#GENARO
#JUAN
#

import pygame #IMPORTAMOS LA LIBRARIA PYGAME
import sys
#_____CLASES___________
class Juego: #CREAMOS UNA CLASE JUEGO
    def __init__(self):
        pygame.init() #INICIAMOS EL JUEGO
        pygame.display.set_caption("Yanshee") #CAMBIAMOS EL NOMBRE DEL JUEGO
        self.pantalla = pygame.display.set_mode((640, 480)) #ASIGNAMOS LAS DIMENSIONES DEL LA PANTALLA
        self.clock = pygame.time.Clock() #Establecemos los frames
        self.img = pygame.image.load("image/diamante.png")

        self.posicion_imagen = [100,200]

                         # Arriba, Abajo, Izquierda, Derecha
        self.movimiento = [False,False,False,False]
    def correr(self):
        while True:
            # Eje Y (Vertical): Abajo (índice 1) menos Arriba (índice 0)
            self.posicion_imagen[1] += (self.movimiento[1] - self.movimiento[0]) * 5
            # Eje X (Horizontal): Derecha (índice 3) menos Izquierda (índice 2)
            self.posicion_imagen[0] += (self.movimiento[3] - self.movimiento[2]) * 5
            self.pantalla.blit(self.img, self.posicion_imagen)
            for event in pygame.event.get(): #Utilizamos pygame.event.get() para iniciar el ciclo del juego
                if event.type == pygame.QUIT: #DE LA LINEA 22 A LA 24, SE ENCARGAN DE HACER QUE EL PROGRAMA SE CIERRE CORRECTAMENTE
                    pygame.quit()
                    sys.exit()

                    #AQUI CONTROLAREMOS AL PERSONAJES
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:    self.movimiento[0] = True
                    if event.key == pygame.K_DOWN:  self.movimiento[1] = True
                    if event.key == pygame.K_LEFT:  self.movimiento[2] = True
                    if event.key == pygame.K_RIGHT: self.movimiento[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:    self.movimiento[0] = False
                    if event.key == pygame.K_DOWN:  self.movimiento[1] = False
                    if event.key == pygame.K_LEFT:  self.movimiento[2] = False
                    if event.key == pygame.K_RIGHT: self.movimiento[3] = False


            pygame.display.update()#SE ACTUALIZA LA PANTALLA CONSTANMENTE PARA ACTUALIZAR LOS FRAMES Y LA LISTA DE EVENTOS
            self.clock.tick(60)

#______________________

Juego().correr()