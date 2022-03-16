Mes solutions aux problèmes archivés sur [ProjectEuler.net](https://projecteuler.net/).

| **Problème** | **Résolu le** |
|--------------|---------------|
| 1            | 16/03/2022    |
| 2            | 16/03/2022    |
| 3            | 

--- 

# Solutions <!-- omit in toc -->

- [Problème 1](#problème-1)
  - [Solution naïve](#solution-naïve)
  - [Un peu plus élégant](#un-peu-plus-élégant)
- [Problème 2](#problème-2)
  - [Solution naïve](#solution-naïve-1)
  - [Un peu plus élégant](#un-peu-plus-élégant-1)
- [Problème 3](#problème-3)
  - [Solution naïve](#solution-naïve-2)
  - [Améliorer `estPremier()`](#améliorer-estpremier)

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

print(problem2(4000000, 2))
```

La somme cherchée est $$ \boxed{ S = 4.613.732 } $$

### Un peu plus élégant

```python
from math import sqrt

def problem2(L):

    def fib(n):
        "Implémente la formule de Binet"
        return int( ( ( (1 + sqrt(5))/2 )**n - ( (1 - sqrt(5))/2 )**n ) / sqrt(5) )

    S = 0
    i = 3
    f = fib(i)
    while f < L:
        print(f)
        S += f
        i += 3
        f  = fib(i)
    return S

print(problem2(4000000))
```

renvoie

$$ \boxed{ S = 4.613.732 } $$

## Problème 3

- [énoncé](https://projecteuler.net/problem=3)

On note

- `L` le nombre à factoriser : $600851475143$

### Solution naïve

```python
from math import floor, sqrt

def probleme3(L):

    def estPremier(i):
        drapeau = True
        if i < 2: drapeau = False
        for j in range(2, floor(sqrt(i))+1):
            if i % j == 0:
                drapeau = False
        return drapeau

    def facteurListe(i):
        l = list()
        for j in range(i):
            if estPremier(j):
                if i % j == 0:
                    l.append(j)
                    i = i/j
        return l

    liste = facteurListe(L)
    print(f"La liste des facteurs premiers du cas test est\n{liste}")
    return liste[-1]

print("\n", probleme3(13195))
```

Cet algorithme fonctionne sur le cas test, on trouve comme liste `[5, 7, 13, 29]` et la solution renvoyée par `probleme3(13195)` est bien $29$. Cependant, le nombre cité par le problème est bien trop grand pour le factoriser de la sorte (exécution > 15 min). Heureusement, il y a des pistes d'amélioration.

### Améliorer `estPremier()`

