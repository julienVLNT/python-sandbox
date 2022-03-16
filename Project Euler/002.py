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
