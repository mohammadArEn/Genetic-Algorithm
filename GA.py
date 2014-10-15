class GA(object):
    def __init__(self , gen , chromosome , numOfGensInChromo , fitnessFunc , populationCount , crossOverRate , mutateRate):
        self.coRate , self.muRate , self.popCount = crossOverRate , mutateRate , populationCount
        self.fnFunc = fitnessFunc
        self.chromo = chromosome

        self.Gen = [ self.chromo(gen,numOfGensInChromo) for i in range(0,self.popCount)]
 
    def crossOver(self , inputGen):
        newGen = list()
        for i in range(0,math.ceil(coRate*popCount)) :
            newGen.append(inputGen[randint(0,len(inputGen))].crossOver(inputGen[randint(0,len(inputGen))]))
        return newGen


    def mutate(self , inputGen):
        newGen = inputGen
        for i in range(0 , math.ceil(self.muRate * self.popCount)):
            newGen[randint(len(newGen))].mutate()
        return newGen

    def pioneer(self,Gen):
        Gen = bubbleSort(Gen)
        return Gen[0:(1-coRate)*len(Gen)]


    def bubbleSort(self,Gen):
        for i in range(0,len(Gen)):
            for j in range(0,len(Gen)):
                if fnFunc(Gen[i]) > fnFunc(Gen[j]) :
                    tmp = Gen[i]
                    Gen[i] = Gen[j]
                    Gen[j] = tmp

    def getGeneration(num):
        for i in range(0,num):
            newGen = self.‍crossOver(Gen) + self.pioneer(Gen)
            newGen = self.mutate(newGen)
            Gen = newGen
    return Gen
