import MST as mst

def getEfficiency(Graph):
        Graph.dijkstra()
        return (sum(Graph.totalDistanceList) / (Graph.V * (Graph.V - 1)))**(-1)