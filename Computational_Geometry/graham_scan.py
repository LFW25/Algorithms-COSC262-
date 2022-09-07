import PointSortKey
from vector_basics import is_ccw

def graham_scan(points):
    """
    takes a list of points
    and returns the convex hull of the points
    as a list of Vec points
    """
    anchor = min(points, key = lambda p: (p.y, p.x))

    point_list = sorted(points, key = lambda p: PointSortKey(p, anchor))
    stack = [point_list[0], point_list[1], point_list[2]]

    for p in point_list[3:]:
        while len(stack) > 1 and not is_ccw(stack[-2], stack[-1], p):
            stack.pop()
        stack.append(p)

    return stack