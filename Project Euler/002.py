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