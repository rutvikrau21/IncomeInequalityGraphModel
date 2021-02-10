import sys  # Library for INT_MAX
from random import *
import makeRandomVertex as mR


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.totalDistanceList = []
        self.r = mR.randomConnections(self)

    def getNewMST(self, parent):
        initialMST = []
        for i in range(0, self.V):
            vertices = [parent[i], i]
            initialMST.append(vertices)
        return initialMST



    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    #Random MST

    def newMST(self):
        self.newAdjMattrix = False
        parent = [None] * (self.V - 1)

        for x in range(len(parent)):
            dist = self.dijkstraIndividual(x)
            nodes = list(range(self.V))
            nodes.remove(x)

            while(parent[x] is None):
                n = choice(nodes)
                nodes.remove(n)
                if dist[n] == sys.maxsize:
                    parent[x] = n
                    self.addVertex([x, n], 1)
        self.r = mR.randomConnections(self)






    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mstSet = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for cout in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and self.newAdjMatrix == False:
                    if mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
                    elif key[v] == self.graph[u][v] and random() > .5:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        return parent


    def addVertex(self, pairList, length):
        self.graph[pairList[0]][pairList[1]] = length
        self.graph[pairList[1]][pairList[0]] = length
        if (pairList[0] == pairList[1]):
            self.graph[i][j] = 0


    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self):
        self.totalDistanceList.clear()
        for src in range(self.V):
            dist = self.dijkstraIndividual(src)
            self.totalDistanceList.extend(dist)

    def dijkstraIndividual(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def newConnection(self):
        self.r.createRandomNewConnection(self)

def getEfficiency(Graph):
    Graph.dijkstra()
    return (sum(Graph.totalDistanceList) / (Graph.V * (Graph.V - 1)))**(-1)

def getRobustness(Graph):
    print()
