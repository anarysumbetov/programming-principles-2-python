def countDown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countDown(n - 1)

countDown(5)

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibbonacci(n):
    if n <= 1:
        return n
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2)

print(fibbonacci(7))

def sum_list(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_list(nums[1:])

list1 = [1, 2, 3, 4, 5]
print(sum_list(list1))

def find_max(numers):
    if len(numers) == 1:
        return numers[0]
    else:
        max_of_rest = find_max(numers[1:])
        return numers[0] if numers[0] > max_of_rest else max_of_rest

list2 = [3, 7, 2, 9, 1]
print(find_max(list2))

import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())