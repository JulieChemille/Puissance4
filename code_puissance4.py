import numpy as np
#pour colorer la grille, ne marche pas sur jupyter notebook!
from colorama import Fore, Style
#https://pypi.org/project/colorama/
#gymnasium : "emballage" pour faire son jeu

# Rajouter une classe menu !!!!!
#Une classe Plateau
#Une classe Joueur
#Une classe Fin_de_partie
#Une classe IA

class Plateau:
    """ Classe représentant le plateau de jeu"""

    def __init__(self, rows, columns):
        """Constructeur de la classe, initialise le plateau et ses dimensions"""
        self.rows=rows
        self.columns=columns
        self.plato=np.zeros((rows,columns))

    #Cette fonction va renvoyer 'False' dans la boucle de la classe Jeu si la colonne est pleine
    def colonne_check(self, col):
        """Vérifie si la colonne est pleine"""
        return self.plato[0][col] == 0

    def placement_jeton(self, col, joueur):
        """Place le jeton du joueur dans la colonne qu'il sélectionne"""
        for i in np.r_[:self.rows][::-1]:
            if self.plato[i][col]==0:
                self.plato[i][col]=joueur
                return True
        return False
    
    def affichage(self, joueur):
        """Affiche le plateau de jeu à l'instant t"""
        couleur = Fore.RED if joueur == 1 else Fore.YELLOW
        print(couleur + str(self.plato) + Style.RESET_ALL)


class Joueur:
    """Classe représentant un joueur humain"""
    def __init__(self, numero, max_choix):
        """Iinitialise le joueur et son numéro et le nombre de choix possibles"""
        self.numero = numero
        self.max_choix = max_choix

    def jouer(self):
        """Demande au joueur de choisir une colonne"""
        while True:
            try:
                choix = int(input(f'A vous de jouer (entre 1 et {self.max_choix}): ')) - 1
                return choix
            except ValueError:
                print("Ce n'est pas un nombre. Essayez encore.")
    
class IA(Joueur):
    """Classe représentant le joueur IA"""
    pass


class Fin_de_partie:
    """Classe représentant la fin de partie"""
    def __init__(self,plato):
        self.plato = plato

    def check_victoire(self, joueur):
        """Vérifie si un joueur a gagné"""
        rows, columns = self.plato.rows, self.plato.columns

        #verif en ligne
        for r in np.r_[:rows]:
            for d in np.r_[:columns-3]:
                f = d+4
                s = np.prod(self.plato.plato[r,d:f])
                if s == joueur**4:
                    return True
        
        #verif en colonne
        for c in np.r_[:columns]:
            for d in np.r_[:rows-3]:
                f = d+4
                s = np.prod(self.plato.plato[d:f,c])
                if s == joueur**4:
                    return True
                
        #verif en diagonale (bas gauche vers haut droite)
        for r in np.r_[:rows-3]:
            for c in np.r_[:columns-3]:
                f = c+4
                s = np.prod([self.plato.plato[r+i,c+i] for i in range(4)])
                if s == joueur**4:
                    return True
                
        #verif en diagonale (haut gauche vers bas droite)
        for r in np.r_[3:rows]:
            for c in np.r_[:columns-3]:
                f = c+4
                s = np.prod([self.plato.plato[r-i,c+i] for i in range(4)])
                if s == joueur**4:
                    return True
                
        return False
    
class Jeu:
    """Classe représentant le jeu en lui-même"""
    def __init__(self, rows, columns):
        self.plato = Plateau(rows, columns)
        self.joueurs = [Joueur(1, columns), Joueur(2, columns)]
        self.check = Fin_de_partie(self.plato)

    """Fonction qui lance le jeu"""
    def play(self):
        while True:
            for joueur in self.joueurs:
                print(f"Joueur {joueur.numero}")
                choix_valide = False
                while not choix_valide:
                    choix = joueur.jouer()
                    if 0 <= choix < self.plato.columns and self.plato.colonne_check(choix):
                        if self.plato.colonne_check(choix):
                            self.plato.placement_jeton(choix, joueur.numero)
                            self.plato.affichage(joueur.numero)
                            if self.check.check_victoire(joueur.numero):
                                print(f"Joueur {joueur.numero} a gagné!")
                                return
                            elif np.all(self.plato.plato != 0):
                                print("Match nul!")
                                return
                            choix_valide = True
                        else:
                            print("Et non! la colonne est pleine. Essayez une autre colonne.")
                    else:
                        print(f"Choix invalide. Essayez un nombre entre 1 et {self.plato.columns}.")

"""Initialisation du jeu par l'utilisateur"""

rows = int(input("Nombre de lignes: "))
columns = int(input("Nombre de colonnes: "))
game = Jeu(rows, columns)

"""Lancement du jeu"""
game.play()
