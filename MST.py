import makeRandomEdge as mRE
import numpy as np
from random import *
import scipy.linalg as la
import scipy.sparse as spr
import networkx as nx


class Graph:

    # Creates an empty matrix using numpy. Also creates
    # an a place to store the total distances in network,
    # Finally creates new connections in network
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.array([[0 for column in range(vertices)]
                      for row in range(vertices)])
        self.totalDistanceList = []
        self.r = None


    # Creates random connection, uses dijikstra to check if there's already
    # a connection, and guarantees no repeats
    def newMST(self):
        parent = [None] * (self.V - 1)

        for x in range(len(parent)):
            dist = spr.csgraph.dijkstra(self.graph, directed=False, unweighted=True, indices=x, min_only=True).tolist()
            nodes = list(range(self.V))
            nodes.remove(x)

            while(parent[x] is None):
                n = choice(nodes)
                nodes.remove(n)
                if np.isinf(dist[n]):
                    parent[x] = n
                    self.addEdge([x, n], 2)
        #Creates list of the 0's in matrix

        self.r = mRE.randomConnections(self, 0)

    def newScaleFree(self):
        pass



    def newConnection(self, groups, n):
        for x in range(groups):
            self.r.createRandomNewConnection(self, n)

    #Creates a new connection between a pair list witha  given length
    def addEdge(self, pairList, length):
        self.graph[pairList[0]][pairList[1]] = length
        self.graph[pairList[1]][pairList[0]] = length

    #Runs dijikstra's algorithim for all nodes and adds to list
    def dist(self):
        self.totalDistanceList.clear()
        print(n)
        dist = spr.csgraph.shortest_path(self.graph, method='FW', directed=False, unweighted=True)
        for x in dist:
            self.totalDistanceList.extend(x)

    def dijkstra(self):
        self.totalDistanceList.clear()
        dist = spr.csgraph.shortest_path(self.graph, method='D', directed=False, unweighted=True)
        for x in dist:
            self.totalDistanceList.extend(x)


    def eigenvalues(self):
        eval, evec = la.eig(self.graph)
        return (eval)

# def apd(A, n: int):
#     """Compute the shortest-paths lengths."""
#     if all(A[i][j] for i in range(n) for j in range(n) if i != j):
#         return A
#     Z = np.linalg.matrix_power(A, 2)
#     B = np.array([
#         [1 if i != j and (A[i][j] == 1 or Z[i][j] > 0) else 0 for j in range(n)]
#         for i in range(n)])
#     T = apd(B, n)
#     X = np.dot(T, A)
#     degree = np.sum(A, axis=1)
#     D = np.array([
#         [2 * T[i][j] if X[i][j] >= T[i][j] * degree[j] else 2 * T[i][j] - 1 for j in range(n)]
#     for i in range(n)])
#     return D
