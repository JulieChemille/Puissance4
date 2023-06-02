import os
import numpy as np
from PIL import Image
#pour colorer la grille, ne marche pas sur jupyter notebook!
from colorama import Fore, Style
#https://pypi.org/project/colorama/

#On définit une classe 

class Jeu:
    #On définit le "constructeur de la classe", self = instance de l'objet en cours de création
    #En d'autres termes on ajoute des caractéristiques
    def __init__(self, rows, columns):
        self.plato = np.zeros((rows,columns))
        self.j1 = 1
        self.j2 = 2
        self.resultat = 0 #0 = le jeu n'est pas terminé

    #On peut commencer à définir nos fonctions (ou méthode)

    def play(self):
    #Tant qu'il n'y a pas de vainqueur, on joue !
        while True:
            # Pour que ce soit un peu plus clair, on change le plateau de couleur quand c'est à tel
            # ou tel joueur de jouer.
            if (self.plato == 1).sum() <= (self.plato == 2).sum():
                j = self.j1
                print(Fore.RED + 'C\'est au tour du joueur Rouge')
            else:
                j = self.j2
                print(Fore.YELLOW + 'C\'est au tour du joueur Jaune')

            x = self.input_joueur() #on récupère l'input

            for i in np.r_[:self.plato.shape[0]]:
                i = self.plato.shape[0] - 1 - i #on retourne le tableau, les jetons tombent en bas !
                if self.plato[int(i), int(x)] == 0:
                    self.plato[i,int(x)] =  j
                    if j == 1:
                        print(Fore.RED + str(self.plato))
                    else:
                        print(Fore.YELLOW + str(self.plato))
                    break
                elif i == 0:
                    print("La colonne est pleine. Essayez une autre colonne.")
                    continue

            if self.victoire(j, i):
                break

            if np.all(self.plato != 0):
                print ("Egalité, voulez vous recommencer?")
                break

    def victoire(self,j ,i):
        #vérification des victoires
        #victoire en lignes
        for r in np.r_[:self.plato.shape[0]]: #indices des lignes du plateau    
            for d in  np.r_[:self.plato.shape[1]-3]: # -3 pour pas dépasser les limites
                f = d + 4
                s = np.prod(self.plato[r, d:f]) #calcul le produit des élmts
                if s == 1**4 or s == 2**4: #1 = victoire de 1, 16 = victoire de 2
                    self.resultat  = 1 #victoire
                    
        #victoire en colonnes
        for c in np.r_[:self.plato.shape[1]]:    
            for d in  np.r_[:self.plato.shape[0]-3]:
                f = d + 4
                s = np.prod(self.plato[d:f, c])
                if s == 1**4 or s == 2**4:
                    self.resultat  = 1

        #victoire en diag 1
        for r in np.r_[:self.plato.shape[0]-3]:    
            for c in  np.r_[:self.plato.shape[1]-3]:
                s = 1
                for i in np.r_[:4]:
                    p = self.plato[r+i, c+i]
                    s *= p
                if s == 1**4 or s == 2**4:
                    self.resultat  = 1     

        #victoire en diag 2
        for r in np.r_[3:self.plato.shape[0]]:    
            for c in  np.r_[3:self.plato.shape[1]]:
                s = 1
                for i in np.r_[:4]:
                    p = self.plato[r-i, c-i]
                    s *= p
                if s == 1**4 or s == 2**4:
                    self.resultat  = 1

        #Si le résultat est égal à 1, le jeu est terminé !
        if self.resultat  == 1:
            if j == 1: #joueur 1 qui gagne
                print(Fore.RED + f'Le joueur Rouge a gagné!')
            else: #sinon joueur 2 qui gagne
                print(Fore.YELLOW + f'Le joueur Jaune a gagné!')
            return True
        return False
    1
    def input_joueur(self):
        
            #On demande au joueur d'entrer un numéro de colonne entre 1 et 7
            while True:
                try:
                    x = int(input('à vous de jouer (entre 1 et 7): ').strip()) - 1
                    if x in range(self.plato.shape[1]):
                        if self.plato[0, int(x)] == 0: 
                            break
                        else:
                            print("Cette colonne est pleine. Essayez une autre colonne.")
                    else:
                        print("Veuillez entrer un numéro entre 1 et 7.")
                except ValueError: 
                    print("Ce n\'est pas un nombre. Essayez encore.")
            return x


rows=6
columns=7

game = Jeu(rows,columns)
game.play()
