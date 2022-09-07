def radix_sort(numbers, d):
    """
    Takes a sequence of natural numbers called numbers 
    and uses counting sort iteratively to sort the sequence 
    up to the d-th digit from the right. 
    The argument d is a positive (and thus non-zero) integer
    """
    num_list = numbers
    for n in range(-1, (-1*d)-1, -1):
        num_list = digit_tup(num_list, n)

        num_list.sort(key= lambda x: x[1])
        num_list = tup_list(num_list)
    
    return num_list

def digit_tup(numbers, n):
    num_list = []
    for number in numbers:
        digit = str(number)
        if len(digit) >= (-1*n):
            num_list.append((number, int(digit[n])))
        else:
            num_list.append((number, 0))
    return num_list

def tup_list(tup):
    lis = []
    for thing in tup:
        lis.append(thing[0])
    return lis