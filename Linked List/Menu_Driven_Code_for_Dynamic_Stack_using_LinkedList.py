# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Dynamic Stack using Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DynamicStack:
    def __init__(self):
        self.tos = None

    def push(self, data):
        n = Node(data)
        if self.tos == None:
            self.tos = n
        else:
            n.next = self.tos
            self.tos = n

    def pop(self):
        if self.tos == None:
            print('\nStack is empty..!!')
        else:
            temp = self.tos
            self.tos = self.tos.next
            print('Popped Element from Stack: ', temp.data)

    def peek(self):
        if self.tos == None:
            print('\nStack is empty..!!')
        else:
            print('Peeked Element: ', self.tos.data)

    def printStack(self):
        if self.tos == None:
            print('\nStack is empty..!!')
        else:
            print('Stack Data')
            temp = self.tos
            while temp != None:
                print(temp.data)
                temp = temp.next

# Main Code


o = DynamicStack()

while True:
    print('-----------')
    print('\n1. Push\n2. Pop\n3. Peek\n4. Print\n0. Exit')
    print('-----------')

    ch = int(input('\nEnter your choice: '))

    if ch == 1:
        data = int(input('\nEnter value to push in stack: '))
        o.push(data)

    elif ch == 2:
        o.pop()

    elif ch == 3:
        o.peek()

    elif ch == 4:
        o.printStack()

    elif ch == 0:
        print('You are out of the program..!!')
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
