"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Circular Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.last = None

    def insertLeft(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
            self.last = n
            self.last.next = self.root
        else:
            n.next = self.root
            self.root = n
            self.last.next = self.root

    def deleteLeft(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            temp = self.root
            if self.root == self.last:
                self.last = self.root = None
            else:
                self.root = self.root.next
                self.last.next = self.root
            print('\nDeleted element: ', temp.data)

    def insertRight(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
            self.last = n
            self.last.next = self.root
        else:
            self.last.next = n
            self.last = n
            self.last.next = self.root

    def deleteRight(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            if self.root == self.last:
                self.root = self.last = None
            else:
                temp = self.root
                temp2 = self.root
                while temp.next != self.root:
                    temp2 = temp
                    temp = temp.next
                self.last = temp2
                temp2.next = self.root
            print('\nDeleted element: ', temp.data)

    def printList(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        temp = self.root
        print('\nElements in Linked List are: ')
        while True:
            print('|', temp.data, '| -> ', end='')
            temp = temp.next
            if temp == self.root:
                break
        print('None')
        print()


o = LinkedList()

while True:
    print('----------------------')
    print('\n1. Insert from Left\n2. Insert from Right\n3. Delete from Left\n4. Delete from Right\n5. Print Linked List\n0. Exit')
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
        o.printList()

    elif ch == 0:
        print('You are out of the program..!!')
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
