import random

def randomPerm(n):
    T = [i+1 for i in range(n)]
    for i in range(len(T)):
        indice = random.randint(i,len(T)-1)
        T[i], T[indice] = T[indice], T[i]
    return T

def associe(V, E):
    if len(V) <= 1 and len(E) <= 1:
        return V, E
    
    pivotVis = E[0] # pivotVis $\in E$
    gaucheVis, droiteVis = [], []
    # Partitionnement de V selon pivotVis
    for elt in V:
        if elt < pivotVis:
            gaucheVis += [elt]
        elif elt > pivotVis:
            droiteVis += [elt]
        else:
            pivotEcrou = elt 

    # Partitionnement de E selon pivotEcrou $\in V$
    gaucheEcrou = [elt for elt in E if elt < pivotEcrou]
    droiteEcrou = [elt for elt in E if elt > pivotEcrou]

    a, b = associe(gaucheVis, gaucheEcrou)
    c, d = associe(droiteVis, droiteEcrou)
    return a+[pivotEcrou]+c, b+[pivotVis]+d

n = 50
V = randomPerm(n)
E = randomPerm(n)

print("Vis    : ",V)
print("Ecrous : ",E)

V,E = associe(V, E)

print("Vis    : ",V)
print("Ecrous : ",E)
