"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ... <--- ряд чисел Фибоначчи

0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12,  ... <--- порядковый номер числа

Формула F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
"""
# O(n)
def fib_linear(n):
    num0, num1 = 0, 1 # O(1)

    count = 2 # O(1)
    while count <= n: # O(n)
        count += 1 # O(1)
        num0, num1 = num1, num0 + num1 # O(1)
    return num1 # O(1)


# O(2^n)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2) # O(2^n)

print(fib_linear(35))
print(fib(35))
