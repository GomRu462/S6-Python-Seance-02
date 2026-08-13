# S6-Python-Seance-02
# Séance 2 — Variables, types et opérateurs en Python

## 🎯 Objectifs

À la fin de cette séance, vous serez capable de :

- créer et utiliser des variables ;
- reconnaître les principaux types de données ;
- convertir une valeur d'un type vers un autre ;
- effectuer des calculs avec Python ;
- utiliser des données saisies avec `input()` dans un calcul.

---

## 1. Les variables

Une **variable** permet de stocker une information dans un programme.

Exemple :

```python
prenom = "Alice"
age = 16
```

Ici :

- `prenom` contient le texte `"Alice"` ;
- `age` contient le nombre `16`.

On peut ensuite utiliser ces variables :

```python
print(prenom)
print(age)
```

La valeur d'une variable peut également être modifiée :

```python
age = 16
age = 17
print(age)
```

Python affichera :

```text
17
```

---

## 2. Les principaux types de données

Python utilise différents types de données.

### Texte : `str`

```python
prenom = "Alice"
```

### Nombre entier : `int`

```python
age = 16
```

### Nombre décimal : `float`

```python
taille = 1.72
```

### Booléen : `bool`

Un booléen ne peut avoir que deux valeurs :

```python
vrai = True
faux = False
```

On peut connaître le type d'une variable avec `type()` :

```python
age = 16
print(type(age))
```

---

## 3. Attention à `input()`

Comme nous l'avons vu lors de la séance précédente :

```python
age = input("Quel âge as-tu ? ")
```

`input()` renvoie **toujours du texte**, même si l'utilisateur saisit `16`.

Pour effectuer un calcul, il faut convertir cette valeur.

```python
age = int(input("Quel âge as-tu ? "))
```

On peut également convertir en nombre décimal :

```python
taille = float(input("Quelle est ta taille ? "))
```

---

## 4. Les opérateurs arithmétiques

Python peut effectuer des calculs.

| Opérateur | Signification | Exemple |
|---|---|---|
| `+` | Addition | `5 + 2` |
| `-` | Soustraction | `5 - 2` |
| `*` | Multiplication | `5 * 2` |
| `/` | Division | `5 / 2` |
| `//` | Division entière | `5 // 2` |
| `%` | Reste de la division | `5 % 2` |
| `**` | Puissance | `5 ** 2` |

Exemple :

```python
a = 10
b = 3

print(a + b)
print(a * b)
print(a / b)
```

---

## 5. Utiliser des variables dans un calcul

On peut combiner `input()`, des variables et des opérateurs.

Exemple :

```python
nombre1 = int(input("Premier nombre : "))
nombre2 = int(input("Deuxième nombre : "))

somme = nombre1 + nombre2

print(f"La somme est {somme}.")
```

---

# 💻 Exercices

Les exercices de cette séance se trouvent dans les fichiers Python du repository.

Vous devez compléter les zones indiquées par :

```python
# TODO
```

Ne modifiez pas les consignes présentes dans les fichiers.

---

## ✅ Critère de réussite

À la fin de la séance, vous devez être capable de créer un programme qui :

1. demande une ou plusieurs valeurs à l'utilisateur ;
2. convertit les valeurs si nécessaire ;
3. effectue un calcul ;
4. stocke le résultat dans une variable ;
5. affiche le résultat.
