"""
Write a program that takes an array of integers and finds the length of a longest subarray
all of whose entries are equal.

Solution in this file assumes a subarray must be contiguous, i.e. of the form
a[i], a[i+1], a[i+2], ..., a[i+k]
"""

def longest_constant_subarray_length(arr):
    longest = 0
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr) and arr[i] == arr[j]:
            j += 1
        longest = max(longest, j - i)
        i = j
    return longest

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 3, 3, 3, 3, 4, 1, 2, 3, 3, 2, 2, 1, 1, 0, 0]
    print(longest_constant_subarray_length(arr)) # 5