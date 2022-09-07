from vector_basics import is_ccw
import PointSortKey

def simple_polygon(points):
    """
    Takes a list of points
    returns a simple polygon that passes through all points
    """
    anchor = min(points, key = lambda p: (p.y, p.x))

    L = sorted(points, key = lambda p: PointSortKey(p, anchor))
    H = [L[0], L[1], L[2]]

    for p in L[3:]:
        H.append(p)
        while len(H) > 1 and not is_ccw(H[-2], H[-1], p):
            H.pop(-2)
        
    return H