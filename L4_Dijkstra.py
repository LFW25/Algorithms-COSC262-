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

def dfs_tree(adj_list, start):
    """takes an adjacency list and a starting vertex
    performs a breadth first search 
    and returns the parent array
    """
    state = []
    parent = []
    stack = []

    for i in range(0, len(adj_list)):
        parent.append(None)
        state.append('U')
    
    state[start] = 'D'

    dfs_loop(adj_list, start, state, parent, stack)
    return stack 

def dfs_loop(adj_list, par_node, state, parent, stack):
    for adj_node in adj_list[par_node]:
        node = adj_node[0]
        if state[node] == 'U':
            state[node] = 'D'
            parent[node] = par_node
            dfs_loop(adj_list, node, state, parent, stack)
    state[par_node] = 'P'
    stack.append(par_node)

def is_strongly_connected(adj_list):
    """Determines whether a graph is strongly connected
    returns True
    or not
    returns False
    """
    if len(adj_list) > 0:
        arb_vert = 0
        state_norm = dfs_tree(adj_list, arb_vert)
        state_trans = dfs_tree(transpose(adj_list), arb_vert)
        if 'U' in state_norm or 'U' in state_trans:
            return False
        else:
            return True
    else:
        return False

from math import inf

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

def dijkstra(adj_list, start):
    """ takes an adjacency list
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
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance

graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))

graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(dijkstra(adjacency_list(graph_string), 0))
print(dijkstra(adjacency_list(graph_string), 2))