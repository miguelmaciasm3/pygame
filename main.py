import pygame
import sys
class Game():
    corredores = []
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("carrera de bichos")
        self.background = pygame.image.load("background/image.png")
        self.runner = pygame.image.load("background/smallball.png")
        
    def competir(self):
        x = 0
        hayganador = False
        while not hayganador:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                #renderizar la pantalla
                self.__screen.blit(self.background, (0,0))
                self.__screen.blit(self.runner, (x, 240))
                pygame.display.flip()
                
                x += 3
                if x >= 250:
                    hayganador = True
        pygame.quit()
        sys.exit()





if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    