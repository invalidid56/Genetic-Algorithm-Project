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
    def __str__(self, k):
        return str(self.Generation[0])
    def choice_R(self, k): #품질 비례 룰렛휠         
        pass
    
    def choice_T(self, k): #토너먼트 0<k<100 k값 - 선택압
        for c in range(2) :
            chrom_rec = random.choice(self.Generation)
            chrom_dom = random.choice(self.Generation)
            if self.func(chrom_dom)<self.func(chrom_rec):chrom_dom, chrom_rec = chrom_rec, chrom_dom        
            p = random.randint(100)
            if c == 1:
                if p<k : a = chrom_dom 
                else : a = chrom_rec
            else : 
                if p<k : b = chrom_dom 
                else : b = chrom_rec
        return a, b          
    def cross_U(self, k, dad, mom): #균등 교차(k = 선택압)
        result = []
        for i in range(len(dad)):
            p = random.randint(100)
            if p<k : result.append(dad[i])
            else : result.append(mom[i])
        return result                
    def cross_P(self, p, dad, mom): #일점 교차
        pass    
    def mutant(self, k): #비균등 변이(k = 변이 확률)
        pass
    
    def __init__(self, GeneList, choice, crossover, mutantChance, mutMax, mutMin, func):
        self.Generation = GeneList
        self.count = 1
        self.len = len(self.Generation)
        self.choice = choice
        self.cross = crossover
        self.func = func
        self.mutchance = mutantChance        
    def evol(self, k):
        self.Generation = self.offspring(k)
        self.Generation = self.mutant(self.mutchance)
        mxa = self.func(Generation[0])
        for i in range(self.len) :
            if mxa < self.func(self.Generation[i]) :
                self.Generation.insert(0, self.Generation[i].pop)                     
    def offspring(self, k):
        result = []
        
        for _ in range(self.len):
            if self.choice == 1 : parents = self.choice_R(k)
            elif self.choice == 2 : parents = self.choice_T(k)
            dad, mom = parents
            #선택연산으로 두 부모를 추리기
            
            if self.cross == 1 : son = self.cross_U(k, dad, mom)
            elif self.cross == 2 :  son = self.cross_P(k, dad, mom)
            result.append(son)
            
        return result