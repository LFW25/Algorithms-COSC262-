def adjacency_list(graph_str):
    """takes a textual graph representation
    and formats it into an adjacency list
    """
    adj_list = []
    form_str = ''
    for char in graph_str:
        if char != '\n':
            form_str += char
        else:
            form_str += ' '
    form_list = form_str.split(' ')[:-1]

    for i in range(0, len(form_list)):
        if form_list[i] not in 'DWU':
            form_list[i] = int(form_list[i])
    
    for i in range(0, int(form_list[1])):
        adj_list.append([])

    if form_list[2] == 'W':
        n = 3
    else:
        n = 2

    for i in range(n, len(form_list)-1, n):
        source = form_list[i]
        target = form_list[i+1]
        if n == 3:
            weight = form_list[i+2]
        else:
            weight = None
        if form_list[0] == 'U':
            adj_list[target] += [(source, weight)]
        adj_list[source] += [(target, weight)]
    
    
    return adj_list

def distance_matrix(adj_list):
    """takes an adjacency matrix
    and formats it into a distance matrix
    """
    dist_mat = []    
    
    for i in range(0, len(adj_list)):
        dist_mat.append([])
        for j in range(0, len(adj_list)):
            dist_mat[i].append(float('inf'))    
        dist_mat[i][i] = 0

    for i in range(0, len(adj_list)):
        source = i
        for tup_set in adj_list[i]:
            target = tup_set[0]
            weight = tup_set[1]

            dist_mat[source][target] = weight

    return dist_mat

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

def permutations(s):
    """ takes a set s
    and returns a list of all the permutations
    of items in s"""
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions

def dfs_backtrack(candidate_path, destination, output_data, adj_list):
    if should_prune(candidate_path):
        return
    if is_solution(candidate_path, destination):
        add_to_output(candidate_path, output_data)
    else:
        for child_candidate in children(candidate_path, adj_list):
            dfs_backtrack(child_candidate, destination, output_data, adj_list)
    
    return output_data
    
def add_to_output(candidate, output_data):
    output_data.append(candidate)
  
def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """
    Returns True if the candidate is complete solution
    Compares the lengths of the candidate to the desired length
    """
    # Complete the code
    if destination not in candidate_path:
        return False
    
    return True

def children(candidate_path, adj_list):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    children = []
    i = candidate_path[-1]
    # Complete the code
    for char in adj_list[i]:
        if char[0] not in candidate_path:
            if type(candidate_path) is tuple:
                temp = list(candidate_path)
                temp.append(char[0])
                children.append(tuple(temp))
            else:
                children.append(candidate_path + char[0])
    
    return children

def all_paths(adj_list, source, destination):
    """
    Takes the adjacency list of a graph, 
    a source vertex (integer), and a destination vertex (integer)
    and returns a list of all simple paths
    from the source vertex to the destination vertex.
    A path is a sequence (tuple) of vertices where the first
    element is the source vertex, and the last element is the
    destination vertes, and the elements in between, if any, are
    vertices along the path.
    """
    path = dfs_backtrack((source, ), destination, [], adj_list)

    return path

# triangle_graph_str = """\
# U 3
# 0 1
# 1 2
# 2 0
# """
# adj_list = adjacency_list(triangle_graph_str)
# print(sorted(all_paths(adj_list, 0, 2)))
# print(all_paths(adj_list, 1, 1))
# #[(0, 1, 2), (0, 2)]
# #[(1,)]


# graph_str = """\
# U 5
# 0 2
# 1 2
# 3 2
# 4 2
# 1 4
# """
# adj_list = adjacency_list(graph_str)
# print(sorted(all_paths(adj_list, 0, 1)))
# #[(0, 2, 1), (0, 2, 4, 1)]

# from pprint import pprint
# # graph used in tracing bfs and dfs
# graph_str = """\
# D 7
# 6 0
# 6 5
# 0 1
# 0 2
# 1 2
# 1 3
# 2 4
# 2 5
# 4 3
# 5 4
# """
# adj_list = adjacency_list(graph_str)
# pprint(sorted(all_paths(adj_list, 6, 3)))
# #[(6, 0, 1, 2, 4, 3),
# # (6, 0, 1, 2, 5, 4, 3),
# # (6, 0, 1, 3),
# # (6, 0, 2, 4, 3),
# # (6, 0, 2, 5, 4, 3),
# # (6, 5, 4, 3)]