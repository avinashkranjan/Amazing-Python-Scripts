# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Bubble Sort
"""


def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]  # Swap


a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ', a)

bubblesort(a)
print('After sorting elements are: ', a)
