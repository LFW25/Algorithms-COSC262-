class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

        
class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0
        
        
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

def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate is None or is_ccw(hull[-1], candidate, p) == False:  # ** FIXME **
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull

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

    # points = [
    #     Vec(100, 100),
    #     Vec(0, 100),
    #     Vec(50, 0)]
    # verts = graham_scan(points)
    # for v in verts:
    #     print(v)
    # # (50, 0)
    # # (100, 100)
    # # (0, 100)

    # print('--------------------------')
    # points = [
    #     Vec(100, 100),
    #     Vec(0, 100),
    #     Vec(100, 0),
    #     Vec(0, 0),
    #     Vec(49, 50)]
    # verts = graham_scan(points)
    # for v in verts:
    #     print(v)
    # # (0, 0)
    # # (100, 0)
    # # (100, 100)
    # # (49, 50)
    # # (0, 100)