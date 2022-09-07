def transpose(adj_list):
    """ Takes an adjacency list
    and returns the transpose of that adjacency list.
    The transpose of an undirected graph is the same as the original
    (Gt = G)
    otherwise flip the directions.
    """
    transpose = []

    for i in range(0, len(adj_list)):
        transpose.append([])
    
    for vertex in range(0, len(adj_list)):
        for edge in adj_list[vertex]:
            new_source = edge[0]
            new_target = vertex
            weight = edge[1]
            transpose[new_source].append((new_target, weight))
    return transpose