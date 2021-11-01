# -*- coding: utf-8 -*-

class Ensemble(frozenset):
    def __new__(cls, *elements):
        return super().__new__(cls, elements)
    def __repr__(self):
        return "{" + ", ".join(map(str,self)) + "}"
    def __and__(self, autre):
        return Ensemble(*frozenset.intersection(self, autre))
    def __or__(self, autre):
        return Ensemble(*frozenset.union(self, autre))
    def __sub__(self, autre):
        return Ensemble(*frozenset.difference(self, autre))
    def intersection(self, autre):
        return Ensemble(*frozenset.intersection(self, autre))
    def union(self, autre):
        return Ensemble(*frozenset.union(self, autre))
    def difference(self, autre):
        return Ensemble(*frozenset.difference(self, autre))
    def parties(self):
        p = []
        liste = list(self)
        n = len(liste)
        for i in range(2**n):
            p_ = []
            for j in range(n):
                if (1 << j) & i:
                    p_.append(liste[j])
            p.append(Ensemble(*p_))
        print(p)
        return Ensemble(*p)
def ensemble(*args):
    return set(args)

def ensemble_iterable(*args):
    return set((a,) for a in args)

def rendre_iterable(ensemble):
    return set((x,) for x in ensemble)

def produit_cartesien(A,B):
    return set((a,b) for a in A for b in B)

def produit(*ensembles):
    print(len(ensembles))
    if len(ensembles) == 2:
        return produit_cartesien(*ensembles)
    else:
        *ensembles, dernier = ensembles
        return produit_cartesien(produit(*ensembles), dernier)

if __name__ == '__main__':
    A = ensemble(1,2,3)
    B = ensemble(1,20,30)
    C = ensemble('a','b','c')
    D = ensemble("ti", "to")
    
    print(A,B,C)
    
    #x = produit_cartesien
    #print(x(A,x(B,C)))
    
    #print(*produit(A,B,C,D),sep='\n')

    a = Ensemble(4,2,45,42)
    b = Ensemble('a','b')
    c = Ensemble(a,b)
    d = Ensemble(4,3)
    print(a, b, c, d, a.intersection(d), a.union(b), Ensemble(a))
    print(a.parties())
