"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Doubly Linked List
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

        else:
            n.right = self.root
            self.root.left = n
            self.root = n

    def deleteLeft(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            temp = self.root
            if self.root.right == self.root.left == None:
                self.root = None
            else:
                self.root = self.root.right
            print('Deleted: ', temp.data)

    def insertRight(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
        else:
            temp = self.root
            while temp.right != None:
                temp = temp.right
            temp.right = n
            n.left = temp
            n.right = None
        print('Inserted Element: ', n.data)

    def deleteRight(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
        else:
            if self.root.right == self.root.left:
                self.root = None
            else:
                temp = self.root
                while temp.right != None:
                    temp = temp.right
                print('\nDeleted: ', temp.data)
                temp = temp.left
                temp.right = None

    def printList(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
            return
        else:
            temp = self.root
            print('Elements of linked list are: ')
            while temp != None:
                print('|', temp.data, ' <-> ', end=" ")
                temp = temp.right
            print('None')
            print('')

    def printListReverse(self):
        if self.root == None:
            print('\nLinked List is empty..!!')
            return
        else:
            temp = self.root
            print('Elements of linked list are: ')
            while temp.right != None:
                temp = temp.right
            while temp != None:
                print('|', temp.data, ' <-> ', end=" ")
                temp = temp.left

            print('None')
            print('')


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
        o.printListReverse()

    elif ch == 0:
        print('You are out of the program..!!')
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
