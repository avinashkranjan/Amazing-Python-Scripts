# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Merge Sort
"""


def merger(a, start, mid, end):
    temp = []
    for i in range(len(a)):
        temp.append(0)
    i = start
    j = mid + 1
    ti = start
    while i <= mid and j <= end:
        if a[i] < a[j]:
            temp[ti] = a[i]
            ti += 1
            i += 1
        else:
            temp[ti] = a[j]
            ti += 1
            j += 1
    while i <= mid:
        temp[ti] = a[i]
        ti += 1
        i += 1
    while j <= end:
        temp[ti] = a[j]
        ti += 1
        j += 1

    for i in range(start, end+1):
        a[i] = temp[i]


def mergesort(a, start, end):
    if start < end:
        mid = (start+end)//2
        mergesort(a, start, mid)
        mergesort(a, mid+1, end)
        merger(a, start, mid, end)


a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ', a)

mergesort(a, 0, len(a)-1)
print('After sorting elements are: ', a)
