from random import choice

class randomConnections:

    def __init__(self, Graph):
        self.listOfNoConnections = []
        self.listOfZeroes(Graph)

    def listOfZeroes(self, Graph):
        for i in range(1, Graph.V):
            for j in range(i):
                if Graph.graph[i][j] == 0:
                    nonConnectedPair = [i, j]
                    self.listOfNoConnections.append(nonConnectedPair)

    def createRandomNewConnection(self, Graph):
        randomConnection = choice(self.listOfNoConnections)
        self.listOfNoConnections.remove(randomConnection)
        Graph.addEdge(randomConnection, 1)




