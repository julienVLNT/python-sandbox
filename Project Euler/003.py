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
