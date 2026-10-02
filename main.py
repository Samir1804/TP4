from noeud import Noeud

n2 = Noeud(2)
ny = Noeud("y")

n_add = Noeud("+", [n2, ny])

arbre = Noeud("exp", [n_add])

print(arbre.afficher_polonais())

# Test de l'évaluation avec y = 0 : exp(2 + 0) = exp(2) ≈ 7.389
res = arbre.evaluer({"y": 0})
print("Résultat pour y=0 :", res)

# Test de l'erreur si variable absente
try:
    arbre.evaluer({})
except ValueError as e:
    print("Erreur attendue bien levée :", e)

valeurs_y = [i * 0.1 for i in range(-20, 21)]

arbre.tracer("y", valeurs_y)