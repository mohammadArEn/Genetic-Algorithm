fro
class chromo(object):
    
    def __init__(self,gen,num):
        self.gen = list()
        for i in range(1,num):
            self.gen.append(gen())
    
    def crossOver(self,other):
        party = self.gen + self.other
        child = random.sample(party , len(self.gen))
