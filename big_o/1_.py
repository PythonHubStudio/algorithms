lst = [5, 2, 9, 6, 1, 7, 3, 8, 4]

# O(n)
def find_max_linear(lst):
    max_element = float('-inf')
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

# O(n*logn)
def find_max_sorted(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-1]


print(find_max_linear(lst))
print(find_max_sorted(lst))
