def concat_list(strings):
    """ Concatenates strings recursively """
    if len(strings) == 0:
        return ''
    else:
        return strings[0] + concat_list(strings[1:])

def product(data):
    """ returns the product of the elements in the list data or returns 1 if the list is empty, recursively"""
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])

def backwards(s):
    """ takes a string
    and prints in reverse
    using recursion"""
    if len(s) == 0:
        return ''
    else:
        return backwards(s[1:]) + s[0]

def odds(data):
    """ takes a list of integers
    returns a list of the odd elements"""
    if len(data) == 0:
        return []
    else:
        if data[0] % 2 == 1:
            return [data[0]] + odds(data[1:])
        return odds(data[1:])

def find(data, value):
    """ returns the first occurrence of value in data
    or -1 if its not found"""
    if len(data) == 0:
        return -1
    elif data[0] == value:
        return 0
    ret_val = find(data[1:], value)
    if ret_val < 0:
        return ret_val
    return ret_val + 1

def almost_all(numbers):
    """ returns a list of the sum of the list
    minus the current item """
    total = sum(numbers)
    return [total - current_number for current_number in numbers]

def sort_of(numbers): 
    result = [] 
    for i in range(len(numbers)): 
        sub = sorted(numbers[i:]) 
        result.append(sub[0]) 
    return result