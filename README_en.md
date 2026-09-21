# Session 2 — Variables, types and operators

## Objectives

- create variables and know the types (str, int, float, bool)
- convert a value (int(), float())
- use arithmetic operators
- combine input(), conversion and computation

## 1. Variables and types

```python
name = "Alice"      # str
age = 16             # int
height = 1.72        # float
is_true = True       # bool
```

`type(age)` gives the type of a variable.

## 2. input() and conversion

`input()` always returns text. To compute, you need to convert it:

```python
age = int(input("How old are you? "))
height = float(input("What's your height? "))
```

## 3. Arithmetic operators

| Operator | Meaning | Example |
|---|---|---|
| + | addition | 5 + 2 |
| - | subtraction | 5 - 2 |
| * | multiplication | 5 * 2 |
| / | division | 5 / 2 |
| // | integer division | 5 // 2 |
| % | remainder | 5 % 2 |
| ** | power | 5 ** 2 |

## 4. Rounding a result

`round(value, 2)` rounds to 2 decimals — useful for a price:

```python
price = 24.9 * 1.2
print(round(price, 2))
```

## Exercises

See `exercice1_en.py` to `exercice4_en.py`.

## Success criteria

Write a program that asks for a value, converts it, computes, and prints the result.
