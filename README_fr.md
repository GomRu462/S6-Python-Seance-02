# Séance 2 — Variables, types et opérateurs

## Objectifs

- créer des variables et connaître les types (str, int, float, bool)
- convertir une valeur (int(), float())
- utiliser les opérateurs arithmétiques
- combiner input(), conversion et calcul

## 1. Variables et types

```python
prenom = "Alice"   # str
age = 16            # int
taille = 1.72        # float
vrai = True          # bool
```

`type(age)` donne le type d'une variable.

## 2. input() et conversion

`input()` renvoie toujours du texte. Pour calculer, il faut convertir :

```python
age = int(input("Quel âge as-tu ? "))
taille = float(input("Quelle est ta taille ? "))
```

## 3. Opérateurs arithmétiques

| Opérateur | Sens | Exemple |
|---|---|---|
| + | addition | 5 + 2 |
| - | soustraction | 5 - 2 |
| * | multiplication | 5 * 2 |
| / | division | 5 / 2 |
| // | division entière | 5 // 2 |
| % | reste | 5 % 2 |
| ** | puissance | 5 ** 2 |

## 4. Arrondir un résultat

`round(valeur, 2)` arrondit à 2 décimales — utile pour un prix :

```python
prix = 24.9 * 1.2
print(round(prix, 2))
```

## Exercices

Voir `exercice1_fr.py` à `exercice4_fr.py`.

## Critère de réussite

Créer un programme qui demande une valeur, la convertit, calcule, et affiche le résultat.
