import matplotlib.pyplot as plt


def graph(Ptime,Pi,Pm,L1,L2,L3):
 
    plt.title("Représentation graphique du nombre d'individu en fonction du temps\n")
    #plt.plot(Ptime,Pi, label="Infecté")
    #plt.plot(Ptime,Pm, label="morts")
    plt.plot(Ptime,L1, label="Nombre d'individus P1")
    plt.plot(Ptime,L2, label="Nombre d'individus P2")
    plt.plot(Ptime,L3, label="Nombre d'individus P3")
    plt.legend()
    plt.show()