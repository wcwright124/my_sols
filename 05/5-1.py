"""
Variant 1
Assuming that keys take one of three values, reorder the array so that all objects with the same key appear together. 
The order of the subarrays is not important.
Use O(1) additional space and O(n) time.

Variant 2
Given an array A of n objects with keys that take one of four values, reorder the array so that all objects
that have the same key appear together. Use O(1) additional space and O(n) time.

Variant 3
Given an array A of n objects with boolean-valued keys. Reorder the array so that objects that have the key
False appear first. Use O(1) additional space and O(n) time. 

Variant 4
Given an array A of n objects with boolean-valued keys. Reorder the array so that objects that have the key
False appear first. The relative ordering of objects with key True should not change.
Use O(1) additional space and O(n) time. 
"""

import random

def reorder1(arr):
    vals = set(arr)
    a = vals.pop()
    b = vals.pop()
    c = vals.pop()
    left, right = 0, len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == a:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] == b:
            i += 1
        elif arr[i] == c:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
    return arr

def reorder2(arr):
    vals = set(arr)
    a = vals.pop()
    b = vals.pop()
    c = vals.pop()
    d = vals.pop()
    i1, i2, i3, i4 = 0, 0, len(arr) - 1, len(arr) - 1
    while i2 <= i3:
        if arr[i2] == a:
            arr[i1], arr[i2] = arr[i2], arr[i1]
            i1 += 1
            i2 += 1
        elif arr[i2] == b:
            i2 += 1
        else:
            arr[i2], arr[i3] = arr[i3], arr[i2]
            i3 -= 1
    while i3 <= i4:
        if arr[i3] == d:
            arr[i4], arr[i3] = arr[i3], arr[i4]
            i4 -= 1
        else:
            i3 += 1
    return arr

def reorder3(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    return arr

def reorder4(arr):
    def bubble_swap(start, end):
        for j in range(end-1, start-1, -1):
            arr[j], arr[j+1] = arr[j+1], arr[j]
        return end + 1
    def update_true_idx(start_idx):
        next_idx = start_idx + 1
        while next_idx < len(arr) and not arr[next_idx][0]:
            next_idx += 1
        return next_idx
    j = update_true_idx(-1)
    i = j + 1
    while i < len(arr) and j < len(arr):
        if not arr[i][0]:
            i = bubble_swap(j, i)
        else:
            i += 1
    return arr
    

if __name__ == '__main__':
    arr1 = [random.randrange(3) for _ in range(20)]
    print(reorder1(arr1))
    arr2 = [random.randrange(4) for _ in range(20)]
    print(reorder2(arr2))
    arr3 = [random.choice([True, False]) for _ in range(19)]
    print(reorder3(arr3))
    arr4 = [(random.choice([True, False]), i) for i in range(10)]
    print(arr4)
    print(reorder4(arr4))

