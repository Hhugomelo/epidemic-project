#########BIBLIOTHEQUE et IMPORT FICHIER #####################

from Fenetre import *
from Individu import *
from Graphique import *
import time 

########INITIALISATION DES CODES COULEURS EN RGB ################
WHITE = (255,255,255)
BLUE = (100,150,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BEIGE = (245, 245, 220)
####################################INITIALISATION DES LISTES #################################################
Pt = []     #liste de tout les individus
Ptime = []  # liste du temps, servant au graphique de fin

############################## VARIABLE CONTENANT LE NOMBRE D INDIVIDU PAR POPULATION######################################################

effectif1 = 50
effectif2 = 50
effectif3 = 30
effectif4 = 20  #malade des le début

############################## CREATION DES INDIVIDUS ######################################################

for i in range(effectif1):
    Pt.append(Individu(BLUE,False,False,False))
for i in range(effectif2):
    Pt.append(Individu(GREEN,True,False,False))
for i in range(effectif3):
    Pt.append(Individu(BLACK,True,True,False))
for i in range(effectif4):
    
    Pt.append(Individu(BLUE,False,False,True))  # On fait rentrer un individu infécté

##############################################################################################################

Fenetre = Window(800,800,BEIGE)  #initialisation des paramètres de la fenetre par la classe Window

WIN = pygame.display.set_mode((Fenetre.width,Fenetre.height))  #creation de la fenetre

Window.affichage(Fenetre,WIN) #affiche la fenetre vierge

run = True # variable qui servira de break dans la boucle infini du programme

clock = pygame.time.Clock()  #initialition de la clock du programme
start = time.time()          #servira a calculer le temps d'execution du programme

while run:
    pygame.display.update()    #affiche les nouveauté sur la fenetre

    for individu in Pt:
        Window.draw(WIN,individu.color,individu.x,individu.y,individu.rayon) #boucle parcourant la liste des individus pour dessiner un cercle pour chacun

    pygame.display.update()     #affiche les nouveauté sur la fenetre
     

    while run:
        for event in pygame.event.get():         #permet de quitter la fenetre tout en stoppant l'execution du programme
            if event.type == pygame.QUIT:
                run = False

                diff = len(Individu.Pi) - len(Ptime)         #fait la difference de taille de deux listes, permettant l'affichage du graph
                for i in range(diff):
                    Ptime.append((end - start)) 
                
                
                graph(Ptime,Individu.Pi,Individu.Pm,Individu.L1,Individu.L2,Individu.L3)         #création du grpah par la fonction graph
                     
        WIN.fill(BEIGE)                                     #entre chaque boucle l'affichage redeviens vierge pour afficher le prochain deplacement
        for ind in Pt:
            
            Individu.proximité(ind,Pt)                     #calcul la distance entre deux individus si le premier est malade
            Individu.contamination(ind)                    #si l'individu est malade, le rend rouge 
            Individu.mort(ind,Pt)                          # calcul la proba qu'un individu malade meurs, et meurs avec une proba défini par son état
            Individu.move(ind,Fenetre)                     # fait déplacer les individus de position dans la fenetre
            Window.draw(WIN,ind.color,ind.x,ind.y,ind.rayon)  # dessine tout les individus restant avec leurs nouvelles positions
            Individu.comptage(Pt)

        end = time.time()               # stoke la variable final de temps pour etre utiliser dans le graph
        Ptime.append((end - start))     # stock la difference entre end et start pour avoir le temps de l'execution du programme

        Individu.Pi.append(Individu.zombies) #ajoute le nombre d'infecte actuellement en vie dans une liste
        Individu.Pm.append(Individu.nb_mort) #ajoute le nombre d'individu actuellement mort dans une liste
        #print(Individu.nb_1,Individu.nb_2,Individu.nb_3)
        Individu.L1.append(Individu.nb_1)   #ajoute le nombre d'individu de la pop 1 dans une liste
        Individu.L2.append(Individu.nb_2) #ajoute le nombre d'individu de la pop 2 dans une liste
        Individu.L3.append(Individu.nb_3)   #ajoute le nombre d'individu de la pop 3 dans une liste


        pygame.display.update()  #affiche les nouveauté sur la fenetre
        clock.tick(60)          #défini le taux de rafraichissement de la fenetre

pygame.quit()    #quitte la fenetre


