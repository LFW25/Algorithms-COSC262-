from DFS import dfs_tree
from DFS import dfs_loop
import transpose

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