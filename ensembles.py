# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:08:12 2020

@author: roux
"""

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
    
    print(*produit(A,B,C,D),sep='\n')