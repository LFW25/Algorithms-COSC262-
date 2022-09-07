def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_ccw(a, b, c):
    """True if triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    if area == 0:
        print("Not strictly ccw")
    elif area > 0:
        print("Strictly ccw")
    else:
        print("Not ccw")

    return area >= 0 
 

def is_on_segment(p, a, b):
    """
    Returns True if the point p is somewhere
    on the line segment from a -> b,
    including at either end.
    """
    if signed_area(p, a, b) == 0:
        if ((p - a).lensq() <= (a - b).lensq()) and ((p - b).lensq() <= (a - b).lensq()):
            return True
        else:
            return False
    else:
        return False

def classify_points(line_start, line_end, points):
    """
    returns a two-tuple of 
    first element is the number of points
        from the points list that lie to the right of the given line
    second element is the number of points
        that lie to the left of the line
    """
    left = 0
    right = 0
    for point in points:
        if signed_area(line_start, line_end, point) > 0:
            left += 1
        else:
            right += 1
    
    return(right, left)

def intersecting(a, b, c, d):
    """
    returns True if line segment from a to b
    intersects the line from c to d
    otherwise returns False
    """
    if is_ccw(a, d, b) != is_ccw(a, c, b) and is_ccw(c, a, d) != is_ccw(c, b, d):
        return True
    else:
        return False

def is_strictly_convex(vertices):
    """
    Takes a list of 3 or more points
    returns True if the vertices
    in the given order
    define a strictly-convex counter-clockwise polygon.
    otherwise, return False
    """
    for i in range(1, len(vertices)-1):
        if is_ccw(vertices[i-1], vertices[i], vertices[i+1]) == False:
            return False
    if is_ccw(vertices[-1], vertices[0], vertices[1]) == False:
        return False
    elif is_ccw(vertices[-2], vertices[-1], vertices[0]) == False:
        return False
    return True