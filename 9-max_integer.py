def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxN = my_list[0]
    for i in my_list:
        if i > maxN:
            maxN = i
    return maxN
    
    