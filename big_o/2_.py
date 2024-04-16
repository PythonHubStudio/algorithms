k = 5 # O(1)

# O(1)
def sum(a, b):
    return a + b # O(1)

# O(n)
def print_list(lst):
    for i in lst: # O(n)
        print(i) # O(1)

# O(n)
def print_list2(lst):
    index = 0 # O(1)
    max_index = len(lst) - 1 # O(1)

    while index <= max_index: # O(n)
        print(lst[index]) # O(1)
        index += 1 # O(1)


lst = [1, 2, 3, 4, 5, 6, 7]
# O(n + n) > O(2n) > O(n)
def two_for(lst):
    square = [] # O(1)
    cube = [] # O(1)

    for i in lst: # O(n)
        square.append(i**2) # O(1) ---> # O(n)

    for i in lst: # O(n)
        cube.append(i**3) # O(1) ---> # O(n)

    return square, cube # O(1)


data = [[1,2,3], [4,5,6], [7,8,9]]
# O(n * m)
def unpack(data):
    for arr in data: # O(n)
        for element in arr: # O(m)
            print(element, end='') # O(1)
        print() # O(1)

# O(a * b)
def example(a, b):
    for arr in a: 
        for element in b:
            print(element, end='') # O(1)
        print()  # O(1)

 # O(n * n) > O(n^2)
def example(n):
    for i in n:  # O(n)
        print(i, end='')  # O(1)
        for element in n:  # O(n)
            print(element, end='')  # O(1)
        print()  # O(1)