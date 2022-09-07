
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

def adjacency_matrix(graph_str):
    """takes a textual graph representation
    and formats it into an adjacency matrix
    """
    adj_mat = []
    form_str = ''
    for char in graph_str:
        if char != '\n':
            form_str += char
        else:
            form_str += ' '
    form_list = form_str.split(' ')[:-1]

    for i in range(0 ,len(form_list)):
        if form_list[i] not in 'DWU':
            form_list[i] = int(form_list[i])
    
    for i in range(0, int(form_list[1])):
        adj_mat.append([])
        for j in range(0, int(form_list[1])):
            if len(form_list) >= 3 and form_list[2] == 'W':
                adj_mat[i].append(None)
            else:
                adj_mat[i].append(0)

    if len(form_list) >= 3 and form_list[2] == 'W':
        n = 3
    else:
        n = 2
        
    for i in range(n, len(form_list)-1, n):
        source = form_list[i]
        target = form_list[i+1]
        if n == 3:
            weight = form_list[i+2]
        else:
            weight = 1
        if form_list[0] == 'U':
            adj_mat[target][source] = weight
        adj_mat[source][target] = weight
    
    
    return adj_mat

from collections import deque

def bfs_tree(adj_list, start):
    """takes an adjacency list and a starting vertex
    performs a breadth first search 
    and returns the parent array
    """
    state = []
    parent = []
    queue = deque([])

    for i in range(0, len(adj_list)):
        parent.append(None)
        state.append('U')
    
    state[start] = 'D'

    queue.append(start)

    return bfs_loop(adj_list, queue, state, parent)

def bfs_loop(adj_list, queue, state, parent):
    while len(queue) > 0:
        par_node = queue.popleft()
        for adj_node in adj_list[par_node]:
            node = adj_node[0]
            if state[node] == 'U':
                state[node] = 'D'
                parent[node] = par_node
                queue.append(node)
        state[par_node] = 'P'
    return parent

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