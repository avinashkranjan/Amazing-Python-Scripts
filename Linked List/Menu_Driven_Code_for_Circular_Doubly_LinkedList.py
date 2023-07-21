"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Circular Doubly Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.last = None

    def insertLeft(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
            self.last = n
            self.last.right = self.root
            self.root.left = self.last
        else:
            n.right = self.root
            self.root.left = n
            self.root = n
            self.last.right = self.root
            self.root.left = self.last
        print('\nInserted Element: ', self.root.data)
        self.printList()

    def deleteLeft(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            temp = self.root
            if self.root == self.last:
                self.root = None
            else:
                self.root = self.root.right
                self.root.left = self.last
                self.last.right = self.root
            print('\nDeleted element: ', temp.data)
        self.printList()

    def insertRight(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
            self.last = n
            self.last.right = self.root
            self.root.left = self.last
        else:
            self.last.right = n
            n.left = self.last
            self.last = n
            self.last.right = self.root
            self.root.left = self.last
        print('\nInserted Element: ', n.data)
        self.printList()

    def deleteRight(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            if self.root == self.last:
                self.root = None
            else:
                print('Deleted Element: ', self.last.data)
                self.last = self.last.left
                self.last.right = self.root
                self.root.left = self.last
        self.printList()

    def printList(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
            return
        temp = self.root
        print('\nElements in Linked List are: ')
        while True:
            print('|', temp.data, '| <-> ', end='')
            temp = temp.right
            if temp == self.root:
                break
        print('Root')
        print()

    def printReverseList(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
            return
        temp = self.last
        print('\nElements in Linked List are: ')
        while True:
            print('|', temp.data, '| <-> ', end='')
            temp = temp.left
            if temp == self.last:
                break
        print('Last')
        print()


o = LinkedList()

while True:
    print('----------------------')
    print('\n1. Insert from Left\n2. Insert from Right\n3. Delete from Left\n4. Delete from Right\n5. Print Linked List\n6. Print Reverse Linked List\n0. Exit')
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

    elif ch == 6:
        o.printReverseList()

    elif ch == 0:
        print('You are out of the program..!!')
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
