# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Binary Search (Recursive)
"""

# Recursive Method


def binarysearch(a, start, end, key):
    if start == end:
        if a[start] == key:
            return start
        else:
            return -1
    else:
        mid = (start+end)//2

        if a[mid] == key:
            return mid

        elif a[mid] > key:
            return binarysearch(a, start, mid-1, key)

        else:
            return binarysearch(a, mid+1, end, key)


a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ', a)

key = int(input('Enter key to search: '))

res = binarysearch(a, 0, len(a)-1, key)
if res == -1:
    print(key, 'not found..!!')
else:
    print(key, 'found at', res+1, 'location')
