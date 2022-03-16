def problem1(L, m, n):
    i_m  = (L-1) // m
    i_n  = (L-1) // n
    i_mn = (L-1) // (m*n)

    S = (i_m+1)*i_m/2 * m + (i_n+1)*i_n/2 * n - (i_mn+1)*i_mn/2 * (m*n)
    return S

assert problem1(10, 3, 5) == 23, "Le cas test a échoué !"
print(problem1(1000, 3, 5))