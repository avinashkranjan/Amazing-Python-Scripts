# -*- coding: utf-8 -*-
"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Linear Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insertLeft(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
        else:
            n.next = self.root
            self.root = n

    def deleteLeft(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            temp = self.root
            self.root = self.root.next
            print('\nDeleted element: ', temp.data)

    def insertRight(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
        else:
            temp = self.root
            while temp.next != None:
                temp = temp.next
            temp.next = n

    def deleteRight(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            temp = self.root
            temp2 = self.root
            while temp.next != None:
                temp2 = temp
                temp = temp.next
            temp2.next = None
            if temp == self.root:
                self.root = None
            print('\nDeleted element: ', temp.data)

    def printList(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        temp = self.root
        print('\nElements in Linked List are: ')
        while temp != None:
            print('|', temp.data, '| -> ', end='')
            temp = temp.next
        print('None')
        print()

    def searchList(self, data):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            count = 0
            temp = self.root
            while temp != None:
                if temp.data == data:
                    print('\nElement', data, 'found at node: ', count)
                    return
                temp = temp.next
                count += 1
            return ('\nElement not found')

    def deleteElement(self, data):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            count = 0
            temp = self.root
            temp2 = self.root
            while temp != None and temp.data != data:
                temp2 = temp
                temp = temp.next
                count += 1
            if temp != None:
                if temp == self.root:
                    self.root = self.root.next
                elif temp.next == None:
                    temp2.next = None
                else:
                    temp2.next = temp.next
                print('\nDeleted Element:', temp.data,
                      'from position: ', count)
            else:
                print(data, 'not found in Linked List')


o = LinkedList()

while True:
    print('----------------------')
    print('\n1. Insert from Left\n2. Insert from Right\n3. Delete from Left\n4. Delete from Right\n5. Delete Element x\n6. Print Linked List\n7. Search Element x\n0. Exit')
    print('----------------------')

    ch = int(input('\nEnter your choice: '))

    if ch == 1:
        data = int(input('\nEnter value to be inserted in left: '))
        o.insertLeft(data)

    elif ch == 2:
        data = int(input('\nEnter value to be inserted in right: '))
        o.insertRight(data)

    elif ch == 3:
        o.deleteLeft()

    elif ch == 4:
        o.deleteRight()

    elif ch == 5:
        x = int(input('\nEnter the value of Element x: '))
        o.deleteElement(x)

    elif ch == 6:
        o.printList()

    elif ch == 7:
        data = int(input('Enter the value of Element x: '))
        o.searchList(data)

    elif ch == 0:
        print('You are out of the program..!!')
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
