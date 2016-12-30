import pyGene

nOfGen = 10; #염색체 당 유전자 수 
mOfSpin = 7; #최소히전 수 
k = None; #선택압
generation = [ [[None]*7]*(nOfGen) ]; #세대 리스트
icube = [] #큐브 원형


def fitness(gene): #염색체를 넘기면 적합도를 반환
    for p in range(mOfSpin) : c = spin(gene[p], icube)
    result = None#c에 대해서 방향/순열성을 따진다??
    return result

def spin(spin, cube): #회전 방향를 넘기면 회전된 큐브를 반환 cube : 원래 큐브
    pass

gen = pyGene.Generation(generation, 2, 1, 0, 0, 0, fitness) #세대 객체

l = input("반복 횟수 : ")
for i in range(l):
    gen = gen.evol(k)
    print(gen)
    print(i)