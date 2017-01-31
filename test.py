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

Gen = pyGene.Generation(gen, 2, 1, 0, 1, 0, func)
    
for _ in range(1000):
    print(Gen.evol(50, 50))