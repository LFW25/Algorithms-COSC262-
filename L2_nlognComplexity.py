def cycle_length(n):
    """ Counts the length of a Collatz cycle
    given the starting number n
    using only recursion """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + cycle_length(n/2)
    else:
        return 1 + cycle_length(3*n+1)

def recursive_divide(x, y):
    """ recursively divides x by y
    """
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x-y, y)

def my_enumerate(items, start = 0):
    """ returns a list of [index, item] tuples
    using only recursion """
    if start > len(items) - 1:
        return []
    else:
        return [(start, items[start])] + my_enumerate(items, start+1)

def num_rushes(slope_height, rush_height_gain, back_sliding):
    """ Herbert the Heffalump
    recursively"""
    if slope_height <= rush_height_gain:
        return 1
    else:
        slope_height = slope_height - rush_height_gain + back_sliding
        return 1 + num_rushes(slope_height, 0.95*rush_height_gain, 0.95*back_sliding)

import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, index = 0):
    """Takes a list of numbers and does weird stuff with it"""
    if index > len(data) - 1:
        return 0
    else:
        if (data[index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, index + 1)
        else:
            return dumbo_func(data, index + 1)

def all_pairs(list1, list2, index1 = 0, index2 = 0):
    """Creates a list of all the possible pairs
    recursively"""
    if index1 > len(list1) - 1:
        return []

    else:
        if index2 > len(list2) - 1:
            return all_pairs(list1, list2, index1 + 1, 0)

        else:
            return [(list1[index1], list2[index2])] + all_pairs(list1, list2, index1, index2 + 1)
            
def fib(n):
    """ computes and returns the n-th Fibonacci number
    in O(log n) time"""
    # Set up an initial fibonacci matrix like
    # [[Fn+1, Fn],
    #  [Fn, Fn-1]]
    # where Fn is initially 1
    fib_matrix = [[1, 1], 
                  [1, 0]]

    # If you have run out of numbers, stop!
    if n == 0:
        return 0
    
    # Call the power function
    power(fib_matrix, n - 1)
         
    return fib_matrix[0][0]
     
def multiply(fib_matrix, identity_matrix):
     
    f00 = fib_matrix[0][0] * identity_matrix[0][0] + fib_matrix[0][1] * identity_matrix[1][0] # fn+1 = fn+1 * 1 + fn * 1
    f01 = fib_matrix[0][0] * identity_matrix[0][1] + fib_matrix[0][1] * identity_matrix[1][1] # fn = fn+1 * 1 + fn * 0
    f10 = fib_matrix[1][0] * identity_matrix[0][0] + fib_matrix[1][1] * identity_matrix[1][0] # fn = fn * 1 + fn-1 * 1
    f11 = fib_matrix[1][0] * identity_matrix[0][1] + fib_matrix[1][1] * identity_matrix[1][1] # fn-1 = fn * 1 + fn-1 * 0

    fib_matrix[0][0] = f00
    fib_matrix[0][1] = f01
    fib_matrix[1][0] = f10
    fib_matrix[1][1] = f11

def power(fib_matrix, n):
 
    if n == 0 or n == 1:
        return
    identity_matrix = [[1, 1],
                       [1, 0]]
         
    power(fib_matrix, n // 2)
    multiply(fib_matrix, fib_matrix)
         
    if n % 2 != 0:
        multiply(fib_matrix, identity_matrix)

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(100))
print(fib(300))
print(fib(10**6) % 10**10)