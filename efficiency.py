import MST as mst

def getEfficiency(Graph):
        return (sum(Graph.totalDistanceList) / (Graph.V * (Graph.V - 1)))**(-1)

def getEfficiency2(Graph):
        totalFloat = []
        for x in Graph.totalDistanceList:
                if x != 0:
                        totalFloat.append(x**-1)
        return sum(totalFloat)/(Graph.V * (Graph.V - 1))
