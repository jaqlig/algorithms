from math import inf

class FloydWarshall:
    def __init__(self, size, graph):
        self.size = size
        self.matrixInit(size, graph)

        for u in range(self.size):
            for v in range(self.size):
                if v == u:
                    continue
                for w in range(self.size):
                    if w == u or w == v:
                        continue
                    
                    l = self.d[v][u] + self.d[u][w]
                    if l < self.d[v][w]:
                        self.d[v][w] = l
                        self.p[v][w] = self.p[u][w]

    def matrixInit(self, size, graph):
        self.d = []
        for i in range(size):
            self.d.append([])
            for j in range(size):
                self.d[i].append(inf)

        for i in range(size):
            for j in range(size):
                if i == j:
                    self.d[i][j] = 0
                elif graph[i][j] != 0 and graph[i][j] != inf:
                    self.d[i][j] = graph[i][j]

        self.p = []
        for i in range(size):
            self.p.append([])
            for j in range(size):
                self.p[i].append(0)
            
        for i in range(size):
            for j in range(size):
                if graph[i][j] != 0:
                    self.p[i][j] = i + 1

    def printMatrices(self):
        print("Matrix d:")
        for i in range(self.size):
            print(self.d[i])

        print("Matrix p:")
        for i in range(self.size):
            print(self.p[i])

# Example:

graph =  [
            [0,1,5,0,0,0,0],
            [0,0,2,0,0,0,0],
            [0,0,0,0,0,0,0],
            [7,0,0,0,1,0,0],
            [0,0,0,0,0,1,0],
            [2,0,0,4,0,0,0],
            [6,0,0,0,0,3,0]
        ]

floyd_warshall = FloydWarshall(7, graph)
floyd_warshall.printMatrices()
