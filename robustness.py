import math
import numpy as np
import MST as mst

def getNetworkConnectivity(Graph):
    eigensum = 0
    for x in Graph.eigenvalues():
        eigensum += math.e ** x
    return(np.log(np.real(eigensum) / Graph.V))

def getCriticalRemovalFraction(Graph):
    try:
        squaredK = 0
        K = 0
        for i in range(Graph.V):
            temp = 0
            for j in range(Graph.V):
                temp += Graph.graph[i][j]
            K+= temp
            squaredK+=temp**2
        K/=Graph.V
        squaredK/=Graph.V
        return(1-(1/((squaredK/K)-1)))
    except RuntimeWarning:
        print("Matrix Empty")



