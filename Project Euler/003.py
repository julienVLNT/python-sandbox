from math import floor, sqrt

def probleme3(L):

    def estPremier(i):
        drapeau = True
        if i < 2: drapeau = False
        for j in range(2, floor(sqrt(i))+1):
            if i % j == 0:
                drapeau = False
        return drapeau

    def facteurs(i):
        liste = list()
        for j in range(2, floor(i/2)+1):
            if i == 1: break
            if estPremier(j):
                if i % j == 0:
                    liste.append(j)
                    i = i/j
                    while(i%j==0):
                        i = i/j
        return liste

    liste = facteurs(L)
    return liste[-1]

print(probleme3(600851475143))
