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