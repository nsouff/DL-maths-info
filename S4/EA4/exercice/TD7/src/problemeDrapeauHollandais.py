from enum import Enum
from colorama import init, Fore, Back, Style
import random

def permuter(T):
    for i in range(len(T)):
        indice = random.randint(i,len(T)-1)
        T[i], T[indice] = T[indice], T[i]
    return T

class Color(Enum):
    BLEU = 1
    BLANC = 2
    ROUGE = 3
    
def printTableau(T):
    for j in T:
        if   j[1] == Color.BLEU:  print(Fore.BLUE  + str(j[0]), end='')
        elif j[1] == Color.ROUGE: print(Fore.RED   + str(j[0]), end='')
        else:                     print(Fore.WHITE + str(j[0]), end='')
        print(" ", end='')
    print(Style.RESET_ALL)
    
def initTableau(b, w, r):
    T =  [ (i+1,Color.BLEU)  for i in range(b) ]
    T += [ (i+1,Color.BLANC) for i in range(w) ]
    T += [ (i+1,Color.ROUGE)   for i in range(r) ]
    T = permuter(T)
    return T

# T un tableau de paire (x, color) et color $\in$ {BLEU, BLANC, ROUGE}
def question1(T):
    bleus, blancs, rouges = [], [], []
    for elt in T:
        if   j[1] == Color.BLEU:  bleus  += [j]
        elif j[1] == Color.ROUGE: rouges += [j]
        else:                     blancs += [j]

    return bleus + blancs + rouges

# T un tableau de paire (x, color) et color $\in$ {BLEU, ROUGE}
def question2(T):
    bleu, rouge = 0, len(T)-1
    while bleu <= rouge:
        if T[bleu][1]  == Color.BLEU: bleu += 1
        elif T[rouge][1] == Color.ROUGE: rouge -= 1
        else: T[rouge], T[bleu] = T[bleu], T[rouge]

# T un tableau de paire (x, color) et color $\in$ {BLEU, BLANC, ROUGE}
def question3(T):
    bleu, blanc, rouge = 0, 0, len(T)-1
    while blanc <= rouge:
        if T[blanc][1] == Color.BLEU:
            T[blanc], T[bleu] = T[bleu], T[blanc]
            blanc += 1
            bleu += 1
        elif T[blanc][1] == Color.ROUGE:
            T[blanc], T[rouge] = T[rouge], T[blanc]
            rouge -= 1
        else:
            blanc += 1

def partition(T, deb, fin):
    if fin - deb == 2 and T[deb] < T[deb+1]:
        return deb+1, deb+1
    
    pivot = T[deb]
    gauche, milieu, droite = deb, deb+1, fin-1
    while milieu <= droite:
        if T[milieu] < pivot:
            T[milieu], T[gauche] = T[gauche], T[milieu]
            gauche += 1
            milieu += 1
        elif T[milieu] > pivot:
            T[milieu], T[droite] = T[droite], T[milieu]
            droite -= 1
        else:
            milieu += 1

    return gauche, milieu

def triRapide(T, deb=0, fin=None) :
    if fin is None:
        fin = len(T)
    if deb < fin:    
        sepInf, sepSup = partition(T, deb, fin)
        triRapide(T, deb, sepInf)
        triRapide(T, sepSup, fin)
    
            
init()

#T = initTableau(4, 2, 6)
#printTableau(T)

# T = question1(T)
# printTableau(T)

# T = initTableau(4, 0, 6)
# printTableau(T)

# question2(T)
# printTableau(T)


# T = initTableau(4, 2, 6)
# printTableau(T)

# question3(T)
# printTableau(T)

T = [7,1,9,6,7,3,10,7,0,1,9]
triRapide(T)
print(T)
