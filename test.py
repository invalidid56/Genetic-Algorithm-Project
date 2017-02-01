#-*- coding: utf-8 -*-
import pyGene
import random

olist = [0, 0, 0, 0, 0]
gen = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)] for i in range(10)] 

def func(l):
    f = 0
    for i in range(5):
        if olist[i] == l[i]:
            f+=1
    return f
#def __init__(self, GeneList, choice, crossover, mutantChance, mutMax, mutMin, func, MaxGeneration):
Gen = pyGene.Generation(gen, 2, 1, 0, 1, 0, func, 100)
    
for i in range(100):
    g = Gen.evol(50, 50, i)[0]
    print(g)
    if g == 5 : break