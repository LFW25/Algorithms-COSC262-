from vector_basics import is_ccw

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