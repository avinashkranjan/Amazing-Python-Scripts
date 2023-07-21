# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Dynamic Linear Queue using Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DynamicQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        n = Node(data)
        if self.front == None:
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        print('\nElement Enqueued in Queue: ', data)

    def dequeue(self):
        if self.front == None:
            print('\nQueue is empty..!!')
        else:
            temp = self.front
            self.front = self.front.next
            print('\nElement Dequeued from Queue: ', temp.data)

    def printQueue(self):
        if self.front == None:
            print('\nQueue is empty..!!')
        else:
            temp = self.front
            while temp != None:
                print(temp.data, ' --> ', end='')
                temp = temp.next
            print()


o = DynamicQueue()

while True:
    print('-----------')
    print('\n1. Enqueue\n2. Dequeue\n3. Print\n0. Exit')
    print('-----------')

    ch = int(input('\nEnter your choice: '))

    if ch == 1:
        data = int(input('\nEnter value to enqueue in Queue: '))
        o.enqueue(data)

    elif ch == 2:
        o.dequeue()

    elif ch == 3:
        o.printQueue()

    elif ch == 0:
        print('You are out of the program..!!')
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
