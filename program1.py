def square(n):
    return n**2

def max_from_list(l):
    max = l[0]
    for i in l:
       if i > max:
           max=i
    return max

def min_from_list(l):
    min = l[0]
    for i in l:
       if i < min:
           min=i
    return min

def sum_of_list(l):
    i=0
    for j in l:
        i+=j
    return i
