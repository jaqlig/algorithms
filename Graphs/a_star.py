from math import inf

class aStar:
    def __init__(self, size, graph, h, destination):
        self.pred = []
        self.Q = []
        self.h = h
        self.g = []
        self.f = []
        self.size = size
        self.d = destination-1

        for i in range(size):
            self.pred.append(0)
            self.Q.append(inf)
            self.g.append(inf)
            self.f.append(inf)
        self.Q[0] = self.h[0]
        self.f[0] = self.h[0]
        self.g[0] = 0

        while (self.f[self.d] == inf):
            v = self.findLowest()

            for u in range(self.size):
                if(graph[v][u] != 0):
                    d = self.g[v] + graph[v][u]
                    if(d < self.g[u]):
                        self.g[u] = d
                        self.f[u] = self.g[u] + self.h[u]
                        self.Q[u] = self.f[u]
                        self.pred[u] = v+1
            self.Q[v] = None

    def findLowest(self):
        min = inf
        for i in range(self.size):
            if self.Q[i] == None or self.Q[i] == inf:
                continue
            elif self.Q[i] < min:
                min = self.Q[i]
        for i in range(self.size):
            if self.Q[i] == min:
                return i

    def printValues(self):
        for i in range(self.size):
            print(i+1, '', end = '')        
        print("- v")

        for i in range(self.size):
            print(self.h[i], '', end = '')
        print("- h(v)")
        for i in range(self.size):
            print(self.g[i], '', end = '')
        print("- g(v)")
        for i in range(self.size):
            print(self.f[i], '', end = '')
        print("- f(v)")

        for i in range(self.size):
            print(self.pred[i], '', end = '')
        print("- pred")

# Example:

graph =  [
            [0,5,0,1,0,0,0,0],
            [0,0,2,0,1,0,0,0],
            [0,0,0,0,0,0,0,3],
            [0,0,0,0,1,2,0,0],
            [0,0,4,0,0,0,0,0],
            [4,0,0,0,0,0,2,0],
            [0,0,0,0,1,0,0,1],
            [0,0,0,0,2,0,0,0]
        ]

h = [4,8,3,4,5,2,1,0]

# aStar(<amount of graph's elements>, <graph>, <weight array>, <destination>)
a_star = aStar(8, graph, h, 8)
a_star.printValues()
