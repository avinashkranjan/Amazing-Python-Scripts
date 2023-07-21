# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Sequential Search
"""


def sequentialsearch(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ', a)

key = int(input('Enter key to search: '))

res = sequentialsearch(a, key)
if res == -1:
    print(key, 'not found..!!')
else:
    print(key, 'found at', res+1, 'location')
