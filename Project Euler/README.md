Mes solutions aux problèmes archivés sur [ProjectEuler.net](https://projecteuler.net/).

| **Problème** | **Résolu ?** |
|--------------|--------------|
| 1            | Non          |

--- 

# Solutions

## Problème 1

- [énoncé](https://projecteuler.net/problem=1)

On note

- `L` la borne supérieure
- `m` le premier diviseur
- `n` le second diviseur

de sorte que la solution est `problem1(1000, 3, 5)`.

### Solution naïve

Il suffit de parcourir les entiers entre $1$ et `L` exclu et d'additionner lorsque l'entier est divisible par `m` ou par `n`.

```python
def problem1(L, m, n):
    S = 0
    for i in range(L):
        if i % m == 0 or i % n == 0:
            S += i
    return S

assert problem1(10, 3, 5) == 23, "Le cas test a échoué !"

print(problem1(1000, 3, 5))
```

La somme $S$ cherchée est $$ \boxed{ S = 233168 } $$

### Un peu plus élégant

```python
def problem1(L, m, n):
    i_m  = (L-1) // m
    i_n  = (L-1) // n
    i_mn = (L-1) // (m*n)    # (m*n) est à remplacer par PPCM(m,n) dans un cas plus général

    S = (i_m+1)*i_m/2 * m + (i_n+1)*i_n/2 * n - (i_mn+1)*i_mn/2 * (m*n)
    return S

assert problem1(10, 3, 5) == 23, "Le cas test a échoué !"
print(problem1(1000, 3, 5))
```

La somme $S$ cherchée est $$ \boxed{ S = 233168 } $$

## Problème 2

- [énoncé](https://projecteuler.net/problem=2)

On note
- `L` la borne supérieure des valeurs $4.000.000.000$
- `p` la valeur du modulo $2$

### Solution naïve

Il suffit de construire récursivement les éléments de la suite de Fibonacci tant que leur valeur n'excède pas $4.000.000.000$ et de sommer ceux qui sont pairs.

```python
def problem2(L, p):

    def suivant(i, j):
        return i + j

    S = 0
    k = 0
    l = 1
    m = suivant(k, l)
    while m < L:
        if m % p == 0:
            S += m
        k = l
        l = m
        m = suivant(k, l)
    return S

print(problem2(4000000000, 2))
```

La somme cherchée est $$ \boxed{ S = 1485607536 } $$

## Problème 3

- [énoncé](https://projecteuler.net/problem=3)
