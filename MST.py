import makeRandomEdge as mRE
import numpy as np
from random import *
import scipy.linalg as la


class Graph:

    # Creates an empty matrix using numpy. Also creates
    # an a place to store the total distances in network,
    # Finally creates new connections in network
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.array([[0 for column in range(vertices)]
                      for row in range(vertices)])
        self.totalDistanceList = []
        self.r = mRE.randomConnections(self)


    # Creates random connection, uses dijikstra to check if there's already
    # a connection, and guarantees no repeats
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
                if dist[n] == np.iinfo(np.int32).max:
                    parent[x] = n
                    self.addEdge([x, n], 1)
        #Creates list of the 0's in matrix
        self.r = mRE.randomConnections(self)



    def newConnection(self):
        self.r.createRandomNewConnection(self)

    #Creates a new connection between a pair list witha  given length
    def addEdge(self, pairList, length):
        self.graph[pairList[0]][pairList[1]] = length
        self.graph[pairList[1]][pairList[0]] = length
        if (pairList[0] == pairList[1]):
            self.graph[i][j] = 0

    #Helps run dijikstra
    def minDistance(self, dist, sptSet):
        min = np.iinfo(np.int32).max
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    #Runs dijikstra's algorithim for all nodes and adds to list
    def dijkstra(self):
        self.totalDistanceList.clear()
        for src in range(self.V):
            dist = self.dijkstraIndividual(src)
            self.totalDistanceList.extend(dist)

    #Runs dijikstra for a specific node
    def dijkstraIndividual(self, src):
        dist = [np.iinfo(np.int32).max] * self.V
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

    def eigenvalues(self):
        eval, evec = la.eig(self.graph)
        return (eval)

