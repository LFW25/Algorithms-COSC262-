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