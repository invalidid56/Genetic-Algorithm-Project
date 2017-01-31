#-*- coding: utf-8 -*-
import random #@UnresolvedImport

def maxf(olist, func):
    l = len(olist)
    m = func(olist[0])
    for i in range(l):
        if m<=func(olist[i]):
            olist.insert(0, olist[i].pop)

def minf(olist, func):
    l = len(olist)
    m = func(olist[0])
    for i in range(l):
        if m>=func(olist[i]):
            olist.insert(0, olist[i].pop)


class Generation():

    def choice_R(self, k): #ǰ�� ��� �귿��         
        pass
    def choice_T(self, k): #��ʸ�Ʈ 0<k<100 k�� - ���þ�
        for c in range(2) :
            chrom_rec = random.choice(self.Generation)
            chrom_dom = random.choice(self.Generation)
            if self.func(chrom_dom)<self.func(chrom_rec):chrom_dom, chrom_rec = chrom_rec, chrom_dom        
            p = random.randint(0, 100)
            if c == 1:
                if p<k : a = chrom_dom 
                else : a = chrom_rec
            else : 
                if p<k : b = chrom_dom 
                else : b = chrom_rec
        return a, b          
    def cross_U(self, t, dad, mom): #�յ� ����(k = ���þ�)
        result = []
        for i in range(len(dad)):
            p = random.randint(0, 100)
            if p<t : result.append(dad[i])
            else : result.append(mom[i])
        return result                
    def cross_P(self, t, dad, mom): #���� ����
        pass    
    def mutant(self, k): #��յ� ����(k = ���� Ȯ��)
        pass  
    def __init__(self, GeneList, choice, crossover, mutantChance, mutMax, mutMin, func):
        self.Generation = GeneList
        self.count = 1
        self.len = len(self.Generation)
        self.choice = choice
        self.cross = crossover
        self.func = func
        self.mutchance = mutantChance        
    def evol(self, k, t):
        self.Generation = self.offspring(k, t)
        #self.Generation = self.mutant(self.mutchance)
        mxa = self.func(self.Generation[0])
        for i in range(self.len) :
            if mxa < self.func(self.Generation[i]) :
                self.Generation.insert(0, self.Generation.pop(i))
        return self.Generation
    def offspring(self, k, t):
        result = []
        
        for _ in range(self.len):
            if self.choice == 1 : parents = self.choice_R(k)
            elif self.choice == 2 : parents = self.choice_T(k)
            dad, mom = parents
            #���ÿ������� �� �θ� �߸���
            
            if self.cross == 1 : son = self.cross_U(t, dad, mom)
            elif self.cross == 2 :  son = self.cross_P(t, dad, mom)
            result.append(son)
        return result