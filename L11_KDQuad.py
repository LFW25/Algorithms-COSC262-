# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, low = 0, high = float('inf')):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """

    if high == float('inf'):
        high = len(nums)

    if not is_sorted:
        nums = sorted(nums)
        
    if high - low == 1:
        tree = Node(nums[low], None, None)  # A leaf

    else:
        mid = (low + high) // 2  # Halfway (approx)
        left = binary_search_tree(nums, True, low, mid)
        right = binary_search_tree(nums, True, mid, high)
        tree = Node(nums[mid - 1], left, right)

    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    box_calls = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

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

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
           boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
        
    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)
           
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

    
    
    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
           which to plot, top, right, bottom, left are the coordinates of
           the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                    xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth+1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)
       
    
    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s

point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
points = [Vec(*tup) for tup in point_tuples]
tree = KdTree(points)
in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
print(sorted(in_range))
# # [(0, 11), (1, 3), (5, 19)]

class QuadTree:
    """A QuadTree class for COSC262.
       Richard Lobb, May 2019
    """
    MAX_DEPTH = 20
    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.centre = centre
        self.size = size
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []
        # *** COMPLETE ME ***
        if len(points) > max_leaf_points and depth < self.MAX_DEPTH:
            child_size = 0.5*self.size
            for i in range(4):
                if i == 0:
                    child_centre = Vec(self.centre.x - child_size/2, self.centre.y - child_size/2)
                elif i == 1:
                    child_centre = Vec(self.centre.x - child_size/2, self.centre.y + child_size/2)
                elif i == 2:
                    child_centre = Vec(self.centre.x + child_size/2, self.centre.y - child_size/2)
                else:
                    child.centre = Vec(self.centre.x + child_size/2, self.centre.y + child_size/2)

                child = QuadTree(points, child_centre, child_size, depth + 1)
                self.children.append(child)

        return Node(points, centre, size, children)

    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)
                
    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s

# import matplotlib.pyplot as plt
# points = [(60, 15), (15, 60), (30, 58), (42, 66), (40, 70)]
# vecs = [Vec(*p) for p in points]
# tree = QuadTree(vecs, Vec(50, 50), 100)
# print(tree)

# # Plot the tree, for debugging only
# axes = plt.axes()
# tree.plot(axes)
# axes.set_xlim(0, 100)
# axes.set_ylim(0, 100)
# plt.show()

# Node((50, 50), 100, [
#   Leaf((25.0, 25.0), 50.0, []),
#   Node((25.0, 75.0), 50.0, [
#     Leaf((12.5, 62.5), 25.0, [(15, 60)]),
#     Leaf((12.5, 87.5), 25.0, []),
#     Node((37.5, 62.5), 25.0, [
#       Leaf((31.25, 56.25), 12.5, [(30, 58)]),
#       Leaf((31.25, 68.75), 12.5, []),
#       Leaf((43.75, 56.25), 12.5, []),
#       Leaf((43.75, 68.75), 12.5, [(42, 66), (40, 70)]),
#     ]),
#     Leaf((37.5, 87.5), 25.0, []),
#   ]),
#   Leaf((75.0, 25.0), 50.0, [(60, 15)]),
#   Leaf((75.0, 75.0), 50.0, []),
# ])