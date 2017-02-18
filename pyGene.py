#-*- coding: utf-8 -*-
import random #@UnresolvedImport
import math


def pick(a, b, p):
    l = []
    for _ in range(p):
        l.append(a)
    for _ in range(100-p):
        l.append(b)
    return random.choice(l)


class Generation:

    def choice_r(self, k):
        pass

    def choice_t(self, k):
        for c in range(2):
            chrom_rec = random.choice(self.Generation)
            chrom_dom = random.choice(self.Generation)
            if self.func(chrom_dom)<self.func(chrom_rec):chrom_dom, chrom_rec = chrom_rec, chrom_dom        
            p = random.randint(0, 100)
            if c == 1:
                if p<k:a = chrom_dom
                else:a = chrom_rec
            else:
                if p<k:b = chrom_dom
                else:b = chrom_rec
        return a, b

    def cross_u(self, t, dad, mom):
        result = []
        for i in range(len(dad)):
            p = random.randint(0, 100)
            if p < t:
                result.append(dad[i])
            else:
                result.append(mom[i])
        return result

    def cross_p(self, t, dad, mom):
        pass

    def cross_o(self, p, q, dad, mom):  #순서 교차 연산(p>q)
        result=[]
        for j in range(p-q):result.append(dad.pop(p+j))
        for j in range(len(mom)):
            if __eq__(0, result.count(mom[j])):result.append(mom[j])
        return result

    def mutant(self, g):
        result = [[0]*self.wid for _ in range(self.hei)]
        d = lambda t, y: y*(1-r*((t+1)/self.Mg))
        for h in range(self.hei):
            for w in range(self.wid):
                r = pick(0, 1, self.mutchance)
                s = random.randint(0,1)
                if s == 0:
                    result[h][w] = self.Generation[h][w]+math.floor(d(g, self.mutMax-self.Generation[h][w]))
                elif s == 1:
                    result[h][w] = self.Generation[h][w]-math.floor(d(g, self.Generation[h][w]-self.mutMin))
        return result

    def __init__(self, genelist, choice, crossover, mutantchance, mutmax, mutmin, func, maxgeneration):
        self.Generation = genelist
        self.count = 1
        self.len = len(self.Generation)
        self.choice = choice
        self.cross = crossover
        self.func = func
        self.mutchance = mutantchance
        self.Mg = maxgeneration
        self.wid = len(self.Generation[0])
        self.hei = len(self.Generation)  
        self.mutMax = mutmax
        self.mutMin = mutmin

    def evol(self, k, t, g):
        self.Generation = self.offspring(k, t)
        self.Generation = self.mutant(g)
        mxa = self.func(self.Generation[0])
        for i in range(self.len):
            if mxa < self.func(self.Generation[i]):
                self.Generation.insert(0, self.Generation.pop(i))
        return self.Generation

    def offspring(self, k, t):
        result = []
        
        for _ in range(self.len):
            if self.choice == 1:
                parents = self.choice_r(k)
            elif self.choice == 2:
                parents = self.choice_T(k)
            dad, mom = parents
            
            if self.cross == 1:
                son = self.cross_u(t, dad, mom)
            elif self.cross == 2:
                son = self.cross_p(t, dad, mom)
            result.append(son)
        return result
