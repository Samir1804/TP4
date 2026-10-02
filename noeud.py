import math
import matplotlib.pyplot as plt
"""Représente un nœud dans un arbre d'expression mathématique."""
class Noeud:
    def __init__(self, valeur, enfants=None):
        
        self.valeur = valeur
        if enfants is None:
            self.enfants = []
        else:
            self.enfants = enfants

    def ajouter_enfant(self, noeud_enfant):
        """Ajoute un nœud enfant à la liste des enfants du nœud courant."""
        self.enfants.append(noeud_enfant)

    def afficher_polonais(self):
        """Retourne la représentation de l'expression sous forme de chaîne en notation polonaise."""
        elements = [str(self.valeur)]
        for enfant in self.enfants:
            elements.append(enfant.afficher_polonais())
        return " ".join(elements)

    def evaluer(self, variables):
        """Évalue numériquement l'expression selon un dictionnaire de variables donné."""
        # 1. Cas d'une constante numérique
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        # 2. Cas d'une variable (nom de chaîne qui n'est pas un opérateur connu)
        operateurs = {"+", "-", "*", "/", "exp", "log", "sin", "cos"}
        if self.valeur not in operateurs:
            if self.valeur in variables:
                return float(variables[self.valeur])
            else:
                raise ValueError(f"Variable manquante dans le dictionnaire : '{self.valeur}'")

        # 3. Cas des opérateurs binaires (+, -, *, /)
        if self.valeur in {"+", "-", "*", "/"}:
            gauche = self.enfants[0].evaluer(variables)
            droite = self.enfants[1].evaluer(variables)
            if self.valeur == "+":
                return gauche + droite
            elif self.valeur == "-":
                return gauche - droite
            elif self.valeur == "*":
                return gauche * droite
            elif self.valeur == "/":
                return gauche / droite

        # 4. Cas des opérateurs unaires (exp, log, sin, cos)
        if self.valeur in {"exp", "log", "sin", "cos"}:
            arg = self.enfants[0].evaluer(variables)
            if self.valeur == "exp":
                return math.exp(arg)
            elif self.valeur == "log":
                return math.log(arg)
            elif self.valeur == "sin":
                return math.sin(arg)
            elif self.valeur == "cos":
                return math.cos(arg)

        raise ValueError(f"Opérateur inconnu : {self.valeur}")

    def tracer(self, nom_variable, valeurs):
        
        images = []
        for v in valeurs:
            y = self.evaluer({nom_variable: v})
            images.append(y)

        plt.figure()
        plt.plot(valeurs, images)
        plt.xlabel(nom_variable)
        plt.ylabel(self.afficher_polonais())
        plt.title(f"Graphe de {self.afficher_polonais()}")
        plt.grid(True)
        plt.show()