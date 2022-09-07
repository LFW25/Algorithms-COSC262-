from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25    
    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for the root) and the maximum depth
           allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth: # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points = sorted(points, key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)
            
    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or
           on the boundary of the given query rectangle, which is defined by
           a pair of points (bottom_left, top_right), both of which are Vecs.
        """
        if self.is_leaf == True:
            matches = []
            for point in self.points:
                if point.in_box() == True:
                    matches.append(point)
        else:
            matches = []
            if self.axis == 0:
                if query_rectangle[0].x < self.coord:
                    matches.append(self.points_in_range(self.left, query_rectangle))
                else:
                    matches.append(self.points_in_range(self.right, query_rectangle))
            else:
                if query_rectangle[0].y < self.coord:
                    matches.append(self.points_in_range(self.left, query_rectangle))
                else:
                    matches.append(self.points_in_range(self.right, query_rectangle))
                    
        return matches