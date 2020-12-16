from math import inf

class Dijkstra:
    def __init__(self, size, graph):
        self.dist = []
        self.pred = []
        self.Q = []
        self.size = size

        for i in range(size):
            self.dist.append(inf)
            self.pred.append(0)
            self.Q.append(inf)
        self.dist[0] = 0
        self.Q[0] = 0

        while not (self.isEmpty()):
            v = self.findLowest()
            
            for u in range(self.size):
                if(graph[v][u] != 0):
                    d = self.dist[v] + graph[v][u]
                    if(d < self.dist[u]):
                        self.dist[u] = d
                        self.pred[u] = v+1
                        self.Q[u] = d
            self.Q[v] = None

    def findLowest(self):
        min = inf
        for i in range(self.size):
            if self.Q[i] == None:
                continue
            elif self.Q[i] < min:
                min = self.Q[i]
        for i in range(self.size):
            if self.Q[i] == min:
                return i

    def isEmpty(self):
        for i in self.Q:
            if i != None:
                return False
        return True

    def printValues(self):
        for i in range(self.size):
            print(i+1, '', end = '')        
        print("- v")

        for i in range(self.size):
            print(self.pred[i], '', end = '')
        print("- pred")

        for i in range(self.size):
            print(self.dist[i], '', end = '')
        print("- dist")
            
# Example:

graph =  [
            [0,3,0,3,5],
            [3,0,5,1,0],
            [0,5,0,2,0],
            [3,1,2,0,1],
            [5,0,0,1,0]  
                       
        ]

dijkstra = Dijkstra(5, graph)
dijkstra.printValues()
