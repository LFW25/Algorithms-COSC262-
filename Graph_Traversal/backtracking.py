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

def permutations(s):
    """ takes a set s
    and returns a list of all the permutations
    of items in s
    using dfs backtracking"""
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions

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
    Using dfs backtracking.
    """
    path = dfs_backtrack((source, ), destination, [], adj_list)

    return path