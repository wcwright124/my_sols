"""
Variant 1

Implement a function which takes as input an array and a key, and updates the array so
that all occurences of the input key have been removed and the remaining elements have been
shifted left to fill the emptied indices. Return the number of remaining elements. There are no
requireemnets as to the values stored beyond the last valid element.

Variant 2

Write a program which takes as input a sorted array A of integers and a positive integer m,
and updates A so that if x appears m times in A it appears exactly min(2, m) times in A. The updated
to A should be performed in one passs, and no additonal storage may be allocated.
"""

import random

def remove_duplicates1(arr, key):
    write_idx = 0
    i = 0
    while i < len(arr) and write_idx < len(arr):
        if arr[i] != key:
            arr[write_idx] = arr[i]
            write_idx += 1
            i += 1
        else:
            i += 1
    return arr, write_idx


def remove_duplicates2(arr, m):
    i = 0
    while i < len(arr):
        j = i + 1
        if j < len(arr) and arr[i] == arr[j]:
            while j < len(arr) and arr[i] == arr[j]:
                j += 1
            if j - i >= m:
                for _ in range(j - i - min(2, m)):
                    del arr[i + min(2, m)]
                i = i + min(2, m)
            else:
                i = j
        else:
            i += 1
    return arr

def remove_duplicates(arr, m):
    i = 0
    write_idx = 0
    while i < len(arr):
        j = i + 1
        if j < len(arr) and arr[i] == arr[j]:
            while j < len(arr) and arr[i] == arr[j]:
                j += 1
            if j - i >= m:
                for _ in range(min(2, m)):
                    arr[write_idx] = arr[i]
                    write_idx += 1 
                    i += 1
                i = j
            else:
                for _ in range(j - i):
                    arr[write_idx] = arr[i]
                    write_idx += 1
                    i += 1
        else:
            arr[write_idx] = arr[i]
            write_idx += 1
            i += 1
    return arr, write_idx


if __name__ == '__main__':
    a1 = [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    random.shuffle(a1)
    print(a1)
    k1 = 2
    a, idx = remove_duplicates1(a1, k1)
    print(a[:idx])
    print()

    a2 = [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 0, 0, 0, 2, 2, 2, 4]
    print(a2)
    ans, idx = remove_duplicates(a2, 2)
    print(ans[:idx])