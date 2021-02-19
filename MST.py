import makeRandomEdge as mRE
import numpy as np
from random import *
import scipy.linalg as la
import scipy.sparse as spr


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
        parent = [None] * (self.V - 1)

        for x in range(len(parent)):
            dist = spr.csgraph.dijkstra(self.graph, indices=x, min_only=True).tolist()
            nodes = list(range(self.V))
            nodes.remove(x)

            while(parent[x] is None):
                n = choice(nodes)
                nodes.remove(n)
                if np.isinf(dist[n]):
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

    #Runs dijikstra's algorithim for all nodes and adds to list
    def dijkstra(self):
        self.totalDistanceList.clear()
        dist = spr.csgraph.dijkstra(self.graph)
        for x in dist.tolist():
            self.totalDistanceList.extend(x)


    def eigenvalues(self):
        eval, evec = la.eig(self.graph)
        return (eval)
