import random
from math import *

class Individu:

    rayon = 5
    rayon_infection = 10

    RED = (255,0,0)
    zombies = 1
    nb_mort = 0
    nb_1 = 0
    nb_2 = 0
    nb_3 = 0
    Pi=[1] ###### liste des infectés / 1 car le programme commence avec un infecté
    Pm = [0]
    L1 = [70]
    L2 = [50]
    L3 = [30]

    def __init__(self,color,masque,vaccin,infecte,vitesse = 2):

        self.x = random.randint(100,700)
        self.y = random.randint(100,700)
        self.directionx = vitesse * (random.randint(-100,100)/100)
        self.directiony = vitesse - self.directionx

        self.color = color
        self.masque = masque
        self.vaccin = vaccin
        self.infecte = infecte
        
    def move(self,Fenetre):

        if self.x < 20 or self.x > Fenetre.width-20:
            self.directionx = -self.directionx
        if self.y < 20 or self.y > Fenetre.height-20:
            self.directiony = -self.directiony

        self.x += self.directionx
        self.y += self.directiony


    def proximité(self,Pt):
        for ind in Pt:
            if self == ind or self.infecte == True:
                pass
            else :
                if ind.infecte == True:
                    distance = sqrt((self.x-ind.x)**2+(self.y-ind.y)**2)
                    if distance <= Individu.rayon_infection:

                        Individu.proba_infection(self)              

    def contamination(self):
        if self.infecte != False:
            self.color = self.RED

    def proba_infection(self):
        if self.masque == False and self.vaccin == False:
            proba = random.randint(0,1)
            if proba == 1:
                self.infecte = True
                Individu.zombies += 1
                

        elif self.masque == True and self.vaccin == False:
            proba = random.randint(0,10)
            if proba == 1:
                self.infecte = True
                Individu.zombies += 1
        
        elif self.masque == True and self.vaccin == True:
            proba = random.randint(0,100)
            if proba == 1:
                self.infecte = True
                Individu.zombies += 1

    def mort(self,Pt):
        if self.infecte == True:
            if (self.masque == False or True) and self.vaccin == False:
                proba = random.randint(0,250)
                if proba == 1:
                    Pt.remove(self)
                    Individu.zombies -= 1
                    Individu.nb_mort += 1

            elif self.masque == True and self.vaccin == True:
                proba = random.randint(0,500)
                if proba == 1:
                    Pt.remove(self)
                    Individu.zombies -= 1
                    Individu.nb_mort += 1

    def comptage(Pt):
        Individu.nb_1 = 0
        Individu.nb_2 = 0
        Individu.nb_3 = 0

        for i in Pt:

            if i.masque == False & i.vaccin == False:
                Individu.nb_1 += 1

            elif i.masque == True:
                if i.vaccin == False:
                    Individu.nb_2 += 1
    
            else:
                Individu.nb_3 += 1
