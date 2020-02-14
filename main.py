
import os, random, sys, math
import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funciones import *


#Funcion principal
def main():

        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #Preparar la ventana
        pygame.display.set_caption("Subtimpsons...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        pygame.mixer.music.load("The Simpsons Theme [8 Bit Tribute to The Simpsons] - 8 Bit Universe.mp3")#Cargamos musica del juego.

        while True:#Este ciclo mantiene corriendo el juego constantemente y solo podemos salir de el cerrando la ventana.
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                    return()
            pantallaInicio(screen)#Pantalla inicio, en ellas estan las reglas.
            pantallaJugando(screen)#De esta pantalla se despliega el juego, incluso dentro suyo se encuentra el llamado a la pantalla de records.




#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()










