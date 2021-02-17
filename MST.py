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

    def newConnection(self):
        self.r.createRandomNewConnection(self)

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
