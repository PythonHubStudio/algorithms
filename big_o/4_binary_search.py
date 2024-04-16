lst = [1, 3, 5, 6, 7, 9, 11, 13]
lst2 = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# O(logn)
# O(logn * m)
def binary_search(lst, target):
    left = 0  # O(1)
    right = len(lst) - 1  # O(1)

    while left <= right:  # O(logn)
        mid = left + (right - left) // 2  # O(1)
        if lst[mid] == target:  # O(1) ---> O(m)
            return mid  # O(1)
        elif lst[mid] < target:  # O(1) ---> O(m)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)
    return -1  # O(1)

print(binary_search(lst, 3))