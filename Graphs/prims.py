from math import inf

class Prims:
    def __init__(self, size, graph):
        self.k = []
        self.pred = []
        self.pq = []

        for i in range(size):
            self.k.append(inf)
            self.pred.append(0)
            self.pq.append(inf)
        self.k[0] = 0
        self.pq[0] = 0

        while not (self.isEmpty()):
            u = self.findLowest()
            for v in range(len(self.pq)):
                if (self.pq[v] == None):
                    continue 

                if(graph[u][v] != 0):
                    weight = graph[u][v]
                    if(weight < self.k[v]):
                        self.pred[v] = u+1
                        self.k[v] = weight
                        self.pq[v] = weight
            self.pq[u] = None

    def findLowest(self):
        min = inf
        for i in range(len(self.pq)):
            if self.pq[i] == None:
                continue
            elif self.pq[i] < min:
                min = self.pq[i]
        
        for i in range(len(self.pq)):
            if self.pq[i] == min:
                return i

    def isEmpty(self):
        for i in self.pq:
            if i != None:
                return False
        return True

    def printValues(self):
        for i in range(len(self.k)):
            print(i+1, '', end = '')        
        print("- v")

        for i in range(len(self.k)):
            print(self.pred[i], '', end = '')
        print("- pred")

        for i in range(len(self.k)):
            print(self.k[i], '', end = '')
        print("- k")
            

# Example:

graph =  [
            [0,3,0,3,5],
            [3,0,5,1,0],
            [0,5,0,2,0],
            [3,1,2,0,1],
            [5,0,0,1,0]            
        ]

prims = Prims(5, graph)
prims.printValues()
