import random as random

class randomConnections:

    def __init__(self, Graph, n):
        self.listOfNoConnections = []
        self.randomIndex = 0
        self.listOfZeroes(Graph, n)

    def listOfZeroes(self, Graph, n):
        for i in range(1, Graph.V):
            for j in range(i):
                if Graph.graph[i][j] == n:
                    nonConnectedPair = [i, j]
                    self.listOfNoConnections.append(nonConnectedPair)

        random.shuffle(self.listOfNoConnections)

    def createRandomNewConnection(self, Graph, n):
        Graph.addEdge(self.listOfNoConnections[self.randomIndex], n)
        self.randomIndex+=1



