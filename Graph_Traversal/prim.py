from math import inf

def prim(adj_list, start):
    """
    takes an adjacency list
    and runs Dijkstra's shortest path algorithm
    starting from vertex 'start'
    and returns  a (parent, distance) pair
    containing the parent and distance arrays
    """
    n = len(adj_list)

    in_tree = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]
    
    distance[start] = 0

    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if weight == None:
                weight = 1
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance

def next_vertex(in_tree, distance):
    """Takes two arrays
    and returns the vertex that should next be added
    """
    u = 0
    u_dist = float('inf')
    for i in range(0, len(in_tree)):
        if in_tree[i] == False and distance[i] <= u_dist:
                u_dist = distance[i]
                u = i
    return u