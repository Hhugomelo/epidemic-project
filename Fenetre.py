import pygame

class Window:

    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
   
    def affichage(self,WIN):
        pygame.init()
        pygame.display.set_caption("Simulation")
        WIN.fill(self.color)

    def draw(WIN,color,x,y,rayon):

        pygame.draw.circle(WIN,color,(x,y),rayon)