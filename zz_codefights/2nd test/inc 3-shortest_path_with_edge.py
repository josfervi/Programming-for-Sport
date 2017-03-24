def shortestPathWithEdge(start, finish, weight, graph):
    
    shortestPathWithOutEdge = dijkstra(start, finish, graph)
    
    if shortestPathWithOutEdge <= weight:
        return shortestPathWithOutEdge
    
    shortestPathWithEdgeToFinish = shortestPathWithEdgeTo(finish, start, weight, graph)
    
    shortestPathWithEdgeToStart = shortestPathWithEdgeTo(start, finish, weight, graph)
    
    return min(shortestPathWithOutEdge,
               shortestPathWithEdgeToFinish,
               shortestPathWithEdgeToStart)

def shortestPathWithEdgeTo(finish, start, weight, graph):
    
    # for each edge that is not directly connected to finish (e)
    #   find out the shortestPath from start to that edge (sp(start, e))
    
    # find the min of (sp(start, e)) over all e
    # and return that value + weight
    
    # it is not necessary to check all e

def dijkstra(start, finish, graph):
    pass