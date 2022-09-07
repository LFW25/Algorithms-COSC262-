def floyd(distance):
    """ Takes a distance matrix of a weighted graph
    uses the Floyd-Warshall algorithm to compute all-pairs shortest paths
    and returns a distance matrix
    """
    n = len(distance)
    dist_mat = distance

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                dist_mat[i][j] = min(dist_mat[i][k] + dist_mat[k][j], dist_mat[i][j])
        
    return dist_mat