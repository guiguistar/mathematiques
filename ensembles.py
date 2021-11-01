# -*- coding: utf-8 -*-

class Ensemble(frozenset):
    def __new__(cls, *elements):
        return super().__new__(cls, elements)
    def __repr__(self):
        return "{" + ", ".join(map(str,self)) + "}" if len(self) else "Ø" 
    def intersection(self, autre):
        return Ensemble(*frozenset.intersection(self, autre))
    def union(self, autre):
        return Ensemble(*frozenset.union(self, autre))
    def difference(self, autre):
        return Ensemble(*frozenset.difference(self, autre))
    def symmetric_difference(self, autre):
        return Ensemble(*frozenset.symmetric_difference(self, autre))
    def produit_cartesien(self, autre):
        return Ensemble(*[(a,b) for a in self for b in autre])
    def __and__(self, autre):
        return self.intersection(autre)
    def __or__(self, autre):
        return self.union(autre)
    def __sub__(self, autre):
        return self.difference(autre)
    def __xor__(self, autre):
        return self.symmetric_difference(autre)
    def __mul__(self, autre):
        return self.produit_cartesien(autre)
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
    def parties_rec(self):
        if len(self) == 0:
            return Ensemble(self)
        parties = Ensemble()
        for a in self:
            partie_avec_a = (self-Ensemble(a)).parties_rec()
            partie_sans_a = adjonction(partie_avec_a,a)
            parties = parties | partie_avec_a | partie_sans_a
        return parties
    
# (X = {X_1, ..., X_n}, a) -> { X_1 U {a}, ..., X_n U {a} }
def adjonction(X, a):
    return Ensemble(*map(lambda ens : ens|Ensemble(a), X))

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

Card = len
    
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
    e = Ensemble(Ensemble('a'), Ensemble(42))
    print(a, b, c, d, a.intersection(d), a.union(b), Ensemble(a))
    print(a.parties())
    print(a^b)
    print(Card(a))
    print(a*b)
    print(adjonction(c,'Toto'))
    print(Ensemble().union(Ensemble(2)))
    print(Ensemble("Toto").parties_rec())
    print(e.parties_rec())
    print(adjonction(Ensemble(), 'a'))
    print(adjonction(e,'b'))
    print(Ensemble('a', 'b').parties_rec())
    print(Ensemble().parties_rec().parties_rec().parties_rec())
    print(Card(Ensemble().parties_rec().parties_rec().parties_rec()))
