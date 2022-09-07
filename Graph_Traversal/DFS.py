def dfs_tree(adj_list, start):
    """takes an adjacency list and a starting vertex
    performs a breadth first search 
    and returns the parent array
    """
    state = []
    parent = []

    for i in range(0, len(adj_list)):
        parent.append(None)
        state.append('U')
    
    state[start] = 'D'

    dfs_loop(adj_list, start, state, parent)
    return parent 

def dfs_loop(adj_list, par_node, state, parent):
    for adj_node in adj_list[par_node]:
        node = adj_node[0]
        if state[node] == 'U':
            state[node] = 'D'
            parent[node] = par_node
            dfs_loop(adj_list, node, state, parent)
    state[par_node] = 'P'