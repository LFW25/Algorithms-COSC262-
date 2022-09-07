from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

def binary_search_tree(nums, is_sorted=False, low = 0, high = float('inf')):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
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