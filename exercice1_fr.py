"""
Séance 2 — Exercice 1 : Mes informations
Notions : variables, types (str, int, float), f-string

Crée trois variables : nom (texte), age (entier), taille (décimal),
puis affiche-les dans une seule phrase avec une f-string.

Exemple attendu :
    Prénom : Nora, âge : 16 ans, taille : 1.68 m
"""

# TODO : crée les variables nom, age, taille

# TODO : affiche la phrase avec une f-string
name=input("entre ton nom")
age=int(input("entre ton age"))
taille=float(input("entre ta taille en metre"))
print(f"je m appele{name},j ai{age},jai{taille}")
