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