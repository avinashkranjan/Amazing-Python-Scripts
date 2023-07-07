# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Quick Sort
"""


def quicksort(a, start, end):
    i = start
    j = end
    pivot = start
    while i < j:
        while a[i] < a[pivot]:
            i += 1
        while a[j] > a[pivot]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    if i < end:
        quicksort(a, i+1, end)
    if j > start:
        quicksort(a, start, j-1)


a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ', a)

quicksort(a, 0, len(a)-1)
print('After sorting elements are: ', a)
