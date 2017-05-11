import random
import time

# 유전자 알고리즘 참고 자료 > http://twinw.tistory.com/1
class CGeneticAlg:

    def __init__(self,chromocnt,geneCnt,mutantProb,maxGeneration,targetScore):   # 염색체 갯수,유전자 갯수,돌연변이 확율,최고세대수,목표점수

        if geneCnt%2 != 0  and chromocnt <= 0 or  (mutantProb < 0.01 and mutantProb > 100) or maxGeneration <= 0:
            print("입력된 항목들을 확인하세요.")
            raise NotImplementedError

        self.chromoCnt = chromocnt   # 유전자 갯수 . __init__ 애서 초기화됨.  항상 짝수 이어야 함.
        self.geneCnt   = geneCnt     #
        self.MUTANT_PROBABILITY = mutantProb     # 5%  __init__ 에서 초기화를 함.
        self.MAX_GENERATION     = maxGeneration  # 최고 세대 수
        self.TARGET_SCORE       = targetScore
        self.chromo    = [[]]     # 염색체 리스트. __init__ 에서 초기화를 함. 이차원 배열로 1차원은 염색체,2차원은 유전자를 나타냄
        self.newChromo = [[]]  # 새로 생성된 염색체 리스트
        self.curGeneration = 0 # 현 세대
        self.fitness    = []

        self.fitness.clear()
        for i in range(0,self.chromoCnt):
            self.fitness.append(0)

        self.fitnessSum  = 0

    # 유전자를 random하게 리턴한다.  인터페이스
    def getGeneByRandom(self):
        return

    # 목표점수를 리턴한다. 자식객체에서 구현
    def isTargetScore(self,score):
        return True

    # 입력된 확율(0.01~100%)에 따라서 random하게 true/false 를 리턴
    def byProb(sef,iProbability):
        return random.randint(1, 10000) < iProbability * 100

    # 염색체 2개를 받아 들여 새로운 염색체를 만든다.
    def crossover(self, iNewChromoNo, iChromoNo1, iChromoNo2):
        if self.byProb(50):  # 반반 분할해서 합침
            for i in range(0, int(self.geneCnt / 2)):
                self.newChromo[iNewChromoNo][i] = self.chromo[iChromoNo1][i]
                self.newChromo[iNewChromoNo][int(self.geneCnt / 2) + i] = self.chromo[iChromoNo2][
                    int(self.geneCnt / 2) + i]
        else:  # 유전자를 서로 홀짝수위치를 교차하여 합침
            for i in range(0, int(self.geneCnt / 2)):
                self.newChromo[iNewChromoNo][i * 2] = self.chromo[iChromoNo1][i * 2]
                self.newChromo[iNewChromoNo][i * 2 + 1] = self.chromo[iChromoNo2][i * 2 + 1]

                # 돌연변이를 생성한다. 입력파라미터로는 변이를 일으킬 새로운 염색체의 번호를 입력한다.

    def mutate(self, iNewChromoNo):
        if self.byProb(self.MUTANT_PROBABILITY):  # 유전자 변이 확율
            for i in range(0, self.geneCnt):
                if self.byProb(50):  # 50%의 확률로 유전자를 변이 시킨다.
                    self.newChromo[iNewChromoNo][i] = self.getGeneByRandom()  # getGeneByRandom는 자식 클래스에서 생성

     # 염색체에 의해 만들어진개체의 적합도를  계산한다.
    def calFitness(self, iChromoNo):  # 자식클래스에서 구현해야 함.
        return

    # 룰렛휠 방식으로 염색체를 선택한다.
    def selectChromoByRoulette(self,exceptChromoNo=-1):

        vRoulette         = []
        vSelectedChromoNo = 0
        vFitnessSum       = 0

        # 룰렛테이블 만들기
        for i in range(0, self.chromoCnt):
            vFitnessSum+=self.fitness[i]
            vRoulette.append(vFitnessSum)

        # Roulette 방식에 의해서 염색체 선별
        while True:
            r = random.randint(1, vFitnessSum)
            for i in range(0, self.chromoCnt):
                if vRoulette[i] >= r:
                    vSelectedChromoNo = i
                    break
            if  vSelectedChromoNo != exceptChromoNo:
                 break

        return (vSelectedChromoNo)

    # 현세대가 세대의 임계치를 넘어갔는지 판다.
    def isMaxGeneration(self):
        return self.MAX_GENERATION <= self.curGeneration

    # 초기 결과를 출력
    def printInit(self):
        print("=============================================================================================")
        print("시간:{}".format(time.asctime()))

    # 진행과정 출력
    def printProcessing(self,topScore,chromoNo):
        print("시간:{},세대:{},염색체:{},적합도:{}".format(time.asctime(),self.curGeneration,self.chromo[chromoNo],topScore))
    # 성공 결과를 출력
    def printSuccess(self,topScore,chromoNo):
        print("##성공## 시간:{},세대:{},염색체:{},적합도:{}".format(time.asctime(),self.curGeneration,self.chromo[chromoNo],topScore))
    #  실패 결과를 출력
    def printFail(self):
        print("##실패## 시간:{},세대:{}".format(time.asctime(),self.curGeneration))

    # 현 유전자(self.chromo)으로 자손을 만든다.
    def makeSon(self):
        for i in range(0,self.chromoCnt):
            vSelectedChromo1 = self.selectChromoByRoulette()                # 최초호출은 -1
            vSelectedChromo2 = self.selectChromoByRoulette(vSelectedChromo1)  # 첫번째 리턴된 염색체를 제외한 염색체 선택
            self.crossover(i, vSelectedChromo1, vSelectedChromo2)
            self.mutate(i)
            self.chromo[i]=self.newChromo[i]

    #최초 염색체
    def createFirstChromo(self):
        pass

    # 유전알고리즘에 의한 문제 해결. 경과시간을 리턴,성공여부,세대를 리턴한다.
    def solve(self):

        vTopScore = 0
        vStartTime = time.time()

        self.printInit()

        # 최초 유전자 만들기
        self.createFirstChromo()

        while not self.isMaxGeneration():
            self.curGeneration += 1
            # 적합도 평가
            vTopChromoNo=0
            for i in range(0,self.chromoCnt):
                vScore=self.calFitness(i)
                if self.isTargetScore(vScore):
                    vTopScore=vScore
                    self.printSuccess(vTopScore,i)
                    return  ((time.time() - vStartTime),True,self.curGeneration)
                if vScore > vTopScore:
                    vTopScore   =vScore
                    vTopChromoNo=i
                    self.printProcessing(vTopScore, vTopChromoNo)

            #초기세대 생성
            self.makeSon()

        self.printFail()

        return ((time.time() - vStartTime), True, self.curGeneration)


class C22CubeGene(CGeneticAlg):

    # 2x2 큐브의 위치 표시
    #  ---윗면---  --바닥면--  ----왼쪽면---  ---오른쪽면---  -----앞면-----  -----뒷면-----
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    #

    CUBE_SIZE = 24
    # 큐브의 정답상태.
    solvedCube = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)

    # 큐브의 회전 기호
    DIR = ('U', 'U`', 'D', 'D`', 'F', 'F`', 'B', 'B`', 'R', 'R`', 'L', 'L`')

    def __init__(self,chromocnt,geneCnt,mutantProb,maxGeneration,targetScore):   # 염색체 갯수,유전자 갯수,돌연변이 확율,최고세대수
        CGeneticAlg.__init__(self,chromocnt,geneCnt,mutantProb,maxGeneration,targetScore)

        ##  Object variable 에 대한 초기화
        # 큐브를 회전시켰을 때, 위치 변환 테이블
        self.transform = [[4, 1, 2, 3, 5, 6, 7, 8, 17, 18, 11, 12, 13, 14, 23, 24, 15, 16, 19, 20, 21, 22, 9, 10],  # U  0
                          [2, 3, 4, 1, 5, 6, 7, 8, 23, 24, 11, 12, 13, 14, 17, 18, 9, 10, 19, 20, 21, 22, 15, 16],  # U' 1
                          [1, 2, 3, 4, 8, 5, 6, 7, 9, 10, 21, 22, 19, 20, 15, 16, 17, 18, 11, 12, 13, 14, 23, 24],  # D  2
                          [1, 2, 3, 4, 6, 7, 8, 5, 9, 10, 19, 20, 21, 22, 15, 16, 17, 18, 13, 14, 11, 12, 23, 24],  # D' 3
                          [1, 2, 24, 21, 20, 17, 7, 8, 12, 9, 10, 11, 13, 14, 15, 16, 4, 18, 19, 3, 6, 22, 23, 5],  # F  4
                          [1, 2, 20, 17, 24, 21, 7, 8, 10, 11, 12, 9, 13, 14, 15, 16, 6, 18, 19, 5, 4, 22, 23, 3],  # F' 5
                          [18, 19, 3, 4, 5, 6, 22, 23, 9, 10, 11, 12, 16, 13, 14, 15, 17, 7, 8, 20, 21, 1, 2, 24],  # B  6
                          [22, 23, 3, 4, 5, 6, 18, 19, 9, 10, 11, 12, 14, 15, 16, 13, 17, 1, 2, 20, 21, 7, 8, 24],  # B' 7
                          [1, 10, 11, 4, 5, 14, 15, 8, 9, 6, 7, 12, 13, 2, 3, 16, 20, 17, 18, 19, 21, 22, 23, 24],  # R  8
                          [1, 14, 15, 4, 5, 10, 11, 8, 9, 2, 3, 12, 13, 6, 7, 16, 18, 19, 20, 17, 21, 22, 23, 24],  # R' 9
                          [13, 2, 3, 16, 9, 6, 7, 12, 1, 10, 11, 4, 5, 14, 15, 8, 17, 18, 19, 20, 24, 21, 22, 23],  # L 10
                          [9, 2, 3, 12, 13, 6, 7, 16, 5, 10, 11, 8, 1, 14, 15, 4, 17, 18, 19, 20, 22, 23, 24, 21]]  # L'11

        # 초기 섞인 큐브 변수
        self.mixedCube = self.solvedCube[:]
        # 초기 큐브를 섞은 염색체
        self.mixedChromo = []
        self.cubeRotatedByGene=[[]]

        self.cubeRotatedByGene.clear()
        # 염색체에 의해서 회전된 cube 초기화
        self.cubeRotatedByGene.clear()
        for i in range(0,self.chromoCnt):
            self.cubeRotatedByGene.append(list(self.solvedCube[:]))

        self.mixedChromo.clear()
        for i in range(0,self.geneCnt):
            self.mixedChromo.append(0) # 염색체 리스트. __init__ 에서 초기화를 함. 이차원 배열로 1차원은 염색체,2차원은 유전자를 나타냄

        # 염색체 초기화
        self.chromo.clear()
        self.newChromo.clear()
        for i in range(0,self.chromoCnt):
            self.chromo.append(self.mixedChromo[:]) # 염색체 리스트. __init__ 에서 초기화를 함. 이차원 배열로 1차원은 염색체,2차원은 유전자를 나타냄
            self.newChromo.append(self.mixedChromo[:]) # 새로 생성된 염색체 리스트

    def createFirstChromo(self):
        for i in range(0,self.chromoCnt):
            for j in range(0, self.geneCnt):
                self.chromo[i][j]=self.getGeneByRandom()

        self.rotateCubeByChromo()

    def scrambleCube(self,inputChromo=[]):

        if len(inputChromo) == 0:
            for i in range(0,self.geneCnt):
                self.mixedChromo[i]=self.getGeneByRandom()
        else:
            if len(inputChromo) != self.geneCnt:
                print("입력 염색체의 유전자 갯수를 확인하세요.")
                raise NotImplementedError

            self.mixedChromo = inputChromo[:]


        for i in range(0, self.geneCnt):
            self.rotate(self.mixedChromo[i],-1)


    def getGeneByRandom(self):  # 유전자를 random하게 리턴한다.  인터페이스
        return random.randint(0,self.geneCnt-1)

    def calFitness(self, iChromoNo):  # 적합도 점수를 리턴

        vFitness=0
        for i in range(0, self.CUBE_SIZE):
            if self.cubeRotatedByGene[iChromoNo][i] == self.solvedCube[i]:
                vFitness += 2    # 맞으면 2점
            else:
                vFitness += 1    # 틀리면 1점
        self.fitness[iChromoNo] = vFitness
        self.fitnessSum         += vFitness

        return (vFitness)

    # 목표점수를 리턴한다. 자식객체에서 구현
    def isTargetScore(self,score):
        return (score >= self.TARGET_SCORE )

    # 큐브를 회전시킨다.  cubeRotatedByGene에 저장된 큐브중 n번째(cubeNo)큐브를 회전(direction)시킨다.
    def rotate(self,direction,cubeNo):
        tmpCube = self.cubeRotatedByGene[cubeNo][:]

        for i in range(0, self.CUBE_SIZE):
            self.cubeRotatedByGene[cubeNo][i]= tmpCube[(self.transform[direction][i] - 1)]

        # cubeNo == -1 인경우는 mixedCube에 복사한다.
        if cubeNo ==-1:
            self.mixedCube = self.cubeRotatedByGene[cubeNo][:]

    # 염색체들(self.gene)에 의한 큐브회전
    def rotateCubeByChromo(self):
        for i in range(0,self.chromoCnt):
            self.cubeRotatedByGene[i] = self.mixedCube[:]  # 최초의 큐브 상태를 복사
            for j in range(0, self.geneCnt):
                self.rotate(self.chromo[i][j],i)

    # 현 유전자(self.chromo)으로 자손을 만든다
    def makeSon(self):
        super().makeSon()
        self.rotateCubeByChromo()

    # 유전자 코드변화(염색체 객체 숫자->문자)
    def convertGeneCode(self,chromo):
        return list(self.DIR[chromo[i]] for i in range(0,self.geneCnt))

    # 유전자 코드변화(염색체 객체 문자->숫자)
    def convertCodeGene(self,chromo):
        return list( self.DIR.index(chromo[i]) for i in range(0,self.geneCnt) )

    # 초기 결과를 출력
    def printInit(self):
        super().printInit()
        print("초기염색체:{}  ,초기큐브상태{}".format(self.convertGeneCode(self.mixedChromo),self.mixedCube))

    # 진행과정 출력
    def printProcessing(self,topScore,chromoNo):
        super().printProcessing(topScore,chromoNo)
        print("     큐브섞음공식:{},큐브상태:{}".format(self.convertGeneCode(self.chromo[chromoNo]),self.cubeRotatedByGene[chromoNo]))

    # 성공 결과를 출력
    def printSuccess(self,topScore,chromoNo):
        super().printSuccess(topScore,chromoNo)
        print("     초기염색체:{},초기큐브상태{}".format(self.convertGeneCode(self.mixedChromo),self.mixedCube))
        print("     해답염색체:{},   큐브상태:{}".format(self.convertGeneCode(self.chromo[chromoNo]),self.cubeRotatedByGene[chromoNo]))



##################################################################
###  Main 프로그램
##################################################################
vElapsedTimeSum=0
vSuccessCnt    =0
vGenerationSum =0

"""
for i in range(0,100):
    cube=C22CubeGene(5,8,5,2000000,48)
    cube.scrambleCube()
    vElapsedTime,vSuccess,vGeneration = cube.solve()
    vElapsedTimeSum=(vElapsedTimeSum+vElapsedTime)
    vGenerationSum =(vGenerationSum+vGeneration)
    if vSuccess:
        vSuccessCnt+=1
        vElapsedTimeSum=(vElapsedTimeSum+vElapsedTime)
        vGenerationSum =(vGenerationSum+vGeneration)
"""
cube=C22CubeGene(11,8,5,2000000,40)
cube.scrambleCube(cube.convertCodeGene(['B', 'F', 'U', 'B', 'U', 'B', 'D`', 'B`']))
vElapsedTime,vSuccess,vGeneration = cube.solve()
print("   경과시간 {},성공여부  {},세대 {} ".format(vElapsedTimeSum,vSuccess,vGeneration))

#print("   평균경과시간 {},성공갯수 {},평균세대 {} ".format(vElapsedTimeSum/vSuccessCnt,vSuccessCnt,vGenerationSum/vSuccessCnt))