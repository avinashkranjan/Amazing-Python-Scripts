"""
Linked Lists:
    Single Linked Lists:
        |data|LinkToNextData|--->|data|LinkToNextData|--->|data|null|
        (disadvantage: can't go back to previous data after one data point)

    Double Linked List:
        |Null|data|LinkToNextData|<--->|LinkToPreviousData|data|LinkToNextData|<--->|LinkToPreviousData|data|null|

    Advantage of Linked List over array:
        > No need to pre-allocate the space
        > Insertion is easier

    BigO of Linked List:
        Indexing -----> O(n)
        Insert/Delete element at Start -----> O(1)
        Insert/Delete element at End -----> O(n)
        Insert element at Middle -----> O(n)
        Linked List Traversal(Reverse) -----> O(n)
        Accessing Elements by Value -----> O(n)
"""

class Node:
    '''
    Working of Class Node:
        whenever this class is called, a data will be passed which will get saved in LinkedList as a node which has 2 parts: data & next
    '''
    def __init__(self, data=None, next=None):  # initialised data to None
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node()  # Head is starting point of a Linked List and points to no other value

    # def accept_data(self, data):
    def accept_data(self, *data): # args to get data at single go
        new_node = Node(data)  # created a new node to add data
        cur = self.head  # pointer set for the next data
        while cur.next != None:
            # let linked list have 5 elements; new node will be added as 6th node in linkedlistl;
            # so we will have to search for the last pointer (ptr of 5th ele)
            # so we will iterate until ptr of of curent ele becomes none; as it gets None we will come to know that this is the last node
            cur = cur.next
        cur.next = new_node  # pointer set to the new node


    # method to print each element of Linked List
    def display(self):
        disp = []
        cur = self.head
        disp.append(cur.data)  # to display head element

        while cur.next != None:  # will iterate until next val of current pointer gets None
            cur = cur.next  # accessing next element of the node
            disp.append(cur.data)  # appended the data of current element to the list disp[]
        print(disp)

    # Method to get length of elements in Linked List
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def removeAtIndex(self, index):
        # check if index is valid
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")

        if index == 0:  # removing head
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            # removing element at given index
            if count == index - 1:  # we need to stop at the element prior to element we are removing
                # After element(e1) is removed, address of e2 is linked to e0
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insertAtIndex(self, index, data):
        # check if index is valid
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")

        if index == 0:  # value is inserted at index[0]
            self.accept_data(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count+=1



l = LinkedList()  # created an object 'l' to call class LinkedList

# adding elements to linked list one-by-one

l.head = Node(1)  # Head of the Linked List
element2 = Node(2)
element3 = Node(3)
element4 = Node(4)

# Linking Nodes of the Linked List to each other
# if not linked, only value at head will be printed
l.head.next = element2  # head is pointing to element2
element2.next = element3  # element2 is pointing to element3
element3.next = element4  # element3 is pointing to element4

# display Linked List
l.display()
print("Length: ", l.getLength())
l.removeAtIndex(2)
l.display()
l.insertAtIndex(2, 3)  # (index, value)
l.display()

# adding elements of LinkedList at once
# l = LinkedList()
# l.accept_data(1,2,3,4,5)


# if function accept_data is used without (*data) as parameter
# adding values one-by-one
# l.accept_data(1)
# l.accept_data(2)
# l.accept_data(3)
# l.accept_data(4)
# l.accept_data(5)
# l.display()