### Assignment 1 ###
### Lily Williams ###
## 42415299, lfw25 ##
# April 2021 #

## Supporting Functions ##
# dfs_backtrack(candidate_path, destination, output_data, adj_list)
# add_to_output(candidate, output_data)
# should_prune(candidate)
# is_solution(candidate_path, destination)
# children(candidate_path, adj_list)
# all_paths(adj_list, source, destination)
# adjacency_list(graph_str)
# transpose(adj_list)
# dfs_tree(adj_list, start)
# dfs_loop(adj_list, par_node, state, parent)
# dfs_tree_q3(adj_list, start)
# dfs_loop_q3(adj_list, par_node, state, parent, stack)
# is_strongly_connected(adj_list)
# next_vertex(in_tree, distance)
# dijkstra(adj_list, start)
# distance_matrix(adj_list)

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
    performs a depth first search 
    and returns the parent array
    """
    state = []
    parent = []

    for i in range(0, len(adj_list)):
        parent.append(None)
        state.append('U')
    
    state[start] = 'D'

    dfs_loop(adj_list, start, state, parent)
    return state

def dfs_loop(adj_list, par_node, state, parent):
    for adj_node in adj_list[par_node]:
        node = adj_node[0]
        if state[node] == 'U':
            state[node] = 'D'
            parent[node] = par_node
            dfs_loop(adj_list, node, state, parent)
    state[par_node] = 'P'


def dfs_tree_q3(adj_list, start):
    """takes an adjacency list and a starting vertex
    performs a depth first search 
    and returns the parent array
    """
    state = []
    parent = []
    stack = []
    for i in range(0, len(adj_list)):
        parent.append(None)
        state.append('U')
    
    state[start] = 'D'

    dfs_loop_q3(adj_list, start, state, parent, stack)
    return stack

def dfs_loop_q3(adj_list, par_node, state, parent, stack):
    for adj_node in adj_list[par_node]:
        node = adj_node[0]
        if state[node] == 'U':
            state[node] = 'D'
            parent[node] = par_node
            dfs_loop_q3(adj_list, node, state, parent, stack)
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
    i_return = 0
    ret_dist = float('inf')
    for i in range(0, len(in_tree)):
        if in_tree[i] == False:
            if distance[i] <= ret_dist:
                ret_dist = distance[i]
                i_return = i
    return i_return

def dijkstra(adj_list, start):
    """ takes an adjacency list
    and runs Dijkstra's shortest path algorithm
    starting from vertex 'start'
    and returns  a (parent, distance) pair
    containing the parent and distance arrays
    """
    n = len(adj_list)

    in_tree = []
    distance = []
    parent = []

    for i in range(0, n):
        in_tree.append(False)
        distance.append(float('inf'))
        parent.append(None)
    
    distance[start] = 0

    while False in in_tree:
        n_vertex = next_vertex(in_tree, distance)
        in_tree[n_vertex] = True
        for v_vertex, weight in adj_list[n_vertex]:
            if in_tree[v_vertex] == False and distance[n_vertex] + weight < distance[v_vertex]:
                distance[v_vertex] = distance[n_vertex] + weight
                parent[v_vertex] = n_vertex
    return parent, distance

def prim(adj_list, start):
    """ takes an adjacency list
    and runs Prim's shortest path algorithm
    starting from an arbitrary vertex
    and returns  a (parent, distance) pair
    containing the parent and distance arrays
    """
    n = len(adj_list)

    in_tree = []
    distance = []
    parent = []

    for i in range(0, n):
        in_tree.append(False)
        distance.append(float('inf'))
        parent.append(None)
    
    distance[start] = 0

    while False in in_tree:
        n_vertex = next_vertex(in_tree, distance)
        in_tree[n_vertex] = True
        for v_vertex, weight in adj_list[n_vertex]:
            if in_tree[v_vertex] == False and weight < distance[v_vertex]:
                distance[v_vertex] = weight
                parent[v_vertex] = n_vertex
    return parent, distance

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

##### Question 1 #####
# Write a function format_sequence(converters_info, source_format, destination_format) 
# that returns the shortest sequence of formats (and therefore converters) required 
# in order to convert a video from the source format to the destination format.
## Shortest Path algorithm? ##
# Needs:
# - adjacency_list(graph_str)
# - all_paths(adj_lsit, source, destination)
### CORRECT ###

def format_sequence(converters_info, source_format, destination_format):
    """ Finds the shortest path from the source format to the destination format """
    """ Inputs:
            converters_info - is the string representation of a directed graph. Each vertex is a video format. The number of vertices is the nnumber of possible video formats.
                                For each converter that is available to the producer, there is an edge from the input format of the converter to the output format of the converter.
            source_format - is a natural number that specifies the format of the original video.
            destination_format - is a natural number that specifies the desired format.

        Outputs:
            Must return a shortest list of formats that, when converter in order (from left to right), the video will be in the destination format.
                OR
            If the conversion is not possible (i.e. no path from source to destination) then return "No solution!".
    """
    """
        Plan:
            - Convert converters_info to an adjacency list
            - Use an all_paths function to find all the paths from source to destination
            - Choose the shortest of the all_paths OR return "No solution!".
    """
    adj_list = adjacency_list(converters_info)

    possible_routes = sorted(all_paths(adj_list, source_format, destination_format))

    if len(possible_routes) == 0:
        return "No solution!"
    else:
        shortest_path = list(possible_routes[0])
        for path in possible_routes:
            if len(path) < len(shortest_path):
                shortest_path = list(path)

        return shortest_path

## Tests ##

# converters_info_str = """\
# D 2
# 0 1
# """
# source_format = 0
# destination_format = 1
# print(format_sequence(converters_info_str, source_format, destination_format))
# """ [0, 1] """


# converters_info_str = """\
# D 2
# 0 1
# """
# print(format_sequence(converters_info_str, 1, 1))
# """[1]"""

# converters_info_str = """\
# D 2
# 0 1
# """
# print(format_sequence(converters_info_str, 1, 0))
# """No solution!"""

# converters_info_str = """\
# D 5
# 1 0
# 0 2
# 2 3
# 1 2
# """
# print(format_sequence(converters_info_str, 1, 2))
# """[1, 2]"""

# converters_info_str = """\
# D 1
# """
# print(format_sequence(converters_info_str, 0, 0))
# """[0]"""

##### Question 2 #####
# Write a function bubbles(physical_contact_info) 
# that takes physical contact information about a group of people and 
# returns the bubbles.
## Cycles? Tree search stuff? ##
# Needs:
# - adjacency_list(graph_str)
# - dfs_tree
### CORRECT ###

def bubbles(physical_contact_info):
    """ Finds the list of components within a graph"""
    """ Inputs:
            physical_contact_info - textual representation of an undirected graph

        Outputs:
            Must return a list. The order of the elements in the list does not matter.
            The number of elements in the list must be equal to the number of bubbles.
            Each element of the list is a set of people who are part of the same bubble.
            (Use a Python set or a list but the order does not matter).
    """
    """
        Plan:
            - Convert physical_contact_info to an adjacency list
            - Adapt the is_strongly_connected function and use dfs_tree things to find the components of the tree
    """
    adj_list = adjacency_list(physical_contact_info)
    bubbles = []

    if len(adj_list) > 0:
        starting_vertex = 0
        component = 0
        in_list = []
        while len(in_list) < len(adj_list):
            bubbles.append([])
            state_list = dfs_tree(adj_list, starting_vertex)
            for i in range(0, len(state_list)):
                if state_list[i] != 'U':
                    bubbles[component].append(i)
                    in_list.append(i)
                else:
                    if i not in in_list:
                        starting_vertex = i
            component += 1
                
    
    return bubbles
        



## Tests ##

# physical_contact_info = """\
# U 2
# 0 1
# """
# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# """[[0, 1]]"""

# physical_contact_info = """\
# U 2
# """
# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# """[[0], [1]]"""

# physical_contact_info = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """
# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# """[[0], [1, 2, 3, 4, 5, 6]]"""

# physical_contact_info = """\
# U 0
# """
# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# """[]"""

# physical_contact_info = """\
# U 1
# """
# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
# """[[0]]"""


##### Question 3 #####
# Write a function build_order(dependencies) 
# that takes a description of the dependencies between a number of programs
# and returns a valid order for the build process.
# You can assume that there will always be a solution.
## Topological Sorting? ##
# Needs:
# - adjacency_list(graph_str)
# - dfs_tree_q3
# - dfs_loop_q3
### CORRECT ###

def build_order(dependencies):
    """ Finds the list of components within a graph"""
    """ Inputs:
            dependencies - is a string representation of a directed graph.
                            The number of vertices n is the number of programs of interest.
                            When there is a directed edge from one program to another, the former should be built before the latter.
        Outputs:
            The function must return a length of n programs in a valid order build process (from left to right).
            If there are multiple solutions, any one of them is acceptable.
    """
    """
        Plan:
            - Convert dependencies to an adjacency list
            - Run a dfs on the graph (multiple times if there are is more than one component). If the dfs is recursive, when a call ends (when the current vertex is processed), the current vertex is pushed on a stack.
                Once the entire graph is processed, pop elements from stack one by one. this pop order is a topological ordering.
    """
    adj_list = adjacency_list(dependencies)
    ordered_stack = []

    for i in range(0, len(adj_list)):
        start_vertex = i
        stack = dfs_tree_q3(adj_list, start_vertex)
        for num in stack:
            if num not in ordered_stack:
                ordered_stack.insert(0, num)
    return ordered_stack


## Tests ##
# dependencies = """\
# D 2
# 0 1
# """
# print(build_order(dependencies))
# """[0, 1]"""

# dependencies = """\
# D 3
# 1 2
# 0 2
# """
# print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])
# """True"""

# dependencies = """\
# D 3
# """
# # any permutation of 0, 1, 2 is valid in this case.
# solution = build_order(dependencies)
# if solution is None:
#     print("Wrong answer!")
# else:
#     print(sorted(solution))
# """[0, 1, 2]"""


##### Question 4 #####
# Write a function which_segments(city_map)
# that takes the map of the city
# and returns a list of road segments that must be cleared
# so that there is a clear path between any two locations
# and the total length of the cleaned-up road segments is minimised.
## Minimum Spanning Tree? Prim's Algorithm ##
# Needs:
# - adjacency_list(graph_str)
# - prim
# - from math import inf
### CORRECT ###

def which_segments(city_map):
    """ Finds the minimum spanning tree of a graph"""
    """ Inputs:
            city_map - is given as the textual representation of an undirected weighted graph. 
                        Each vertex in the graph corresponds to one location in the city.
                        Each (two-way) road segment is represented as an edge which connects two locations together
                        and the weight of the edge is the length of road segment.
                        Additionally, the following assumptions are made:
                            the given city has at least one location;
                            there is a path between any two locations;
        Outputs:
            The output is a list of road segments that must be cleared.
            Each segment is a tuple (pair) of two location numbers.
            The smaller number should appear first.
            If the solution is not unique, it does not matter which solution is returned by your function.
    """
    """
        Plan:
            - Convert city_map to an adjacency list
            - Use Prim's Algorithm to find the Minimum Spanning Tree
    """

    adj_list = adjacency_list(city_map)

    parent_array = prim(adj_list, 0)[0]
    paths_array = []

    for i in range(0, len(parent_array)):
        child = i
        parent = parent_array[i]
        if parent is not None:
            paths_array.append((min(parent, child), max(parent, child) ))
    return paths_array


## Tests ##

# city_map = """\
# U 3 W
# 0 1 1
# 2 1 2
# 2 0 4
# """
# print(sorted(which_segments(city_map)))
# """[(0, 1), (1, 2)]"""


# city_map = """\
# U 1 W
# """
# print(sorted(which_segments(city_map)))
# """[]"""


##### Question 5 #####
# A distribution company is upgrading its delivery fleet to electric vehicles.
# In doing so they have to determine the battery capacity required for vehicles.
# The following factors must be considered:
# - A vehicle can travel one unit of distance for every 3 units of battery capacity (that is charged).
# - It is assumed that given a destination, the vehicle will always take a path with the shortest distance in order to go to the destination and come back.
# - A vehicle with a battery that is charged to 80% or more (of the total capacity) should be able to make at least six return trips from the company's depot to any location in the city without the need to be charged in between.

# Write a function min_capacity(city_map, depot_position) 
# that takes the map of a city (described in terms of locations, segments of road in between locations, and the length of each segment),
# and the position of the depot,
# and returns the minimum battery capacity required to meet the above-mentioned criteria.
## Minimum Spanning Tree? Prim's Algorithm ##
# Needs:
# - adjacency_list(graph_str)
# - dijkstra
# - from math import inf
# - max_branch_length
### CORRECT ###

def min_capacity(city_map, depot_position):
    """ Finds the minimum spanning tree of a graph"""
    """ Inputs:
            city_map - is the textual representation of an undirected weighted graph.
                        There is a vertex for each location in the city.
                        There is an edge for each segment of road.
                        All roads are two-way.
                        The length of the road segment is the weight of the edge.
            depot_position -  is a location in the city where the depot is located
        Outputs:
            The function must return an integer
            that is the minimum capacity required for the battery.
    """
    """
        Plan:
            - Convert city_map to an adjacency list
            - Use Djikstra's Algorithm to find the Shortest Path Tree with depot as the starting vertex
            - Find the maximum branch length
            - Furthest city distance x12 x3 <= 0.8x battery capacity 
    """

    adj_list = adjacency_list(city_map)

    dijk = dijkstra(adj_list, depot_position)
    parent_array = dijk[0]
    dist_array = dijk[1]

    paths_array = []

 
    for i in range(0, len(parent_array)):

        child = i
        parent = parent_array[i]
        distance = dist_array[i]
        if parent is not None:
            paths_array.append((parent, child, distance))

    min_bat_cap = 0

    """ Somehow use the paths matrix to find the maximum branch length (= furthest city) """
    max_dist = 0
    for j in range(0, len(parent_array)):

        branch_len = max_branch_length(dist_array, parent_array, j)

        if branch_len != inf and branch_len is not None and branch_len> max_dist:
            max_dist = branch_len


    """ (furthest city distance x36)/0.8 = minimum battery capacity"""
    min_bat_cap = int((max_dist * 36)/0.8)
    return min_bat_cap

def max_branch_length(dist, par, child):
    if child in par and par[child] is not None:
        max_branch_length(dist, par, par.index(child))
    else:
        return 0 + dist[child]
## Tests ##

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""
print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))

"""
180
0
180
"""