''' 
QUEUE
    FIFO

# All Enqueue and Dequeue operations are to/from the top of the stack, i.e., last modified elements
Enqueue add an item to the end of the line
Dequeue remove an item from the front of the line
Enqueue from the one end and Dequeue from the another

QUEUE USE CASE
    Bank Tellers, Placing an order at restaurent, SuperMarket CheckOut
# 
    append() 
        to enqueue an item to RightSide
    appendleft() 
        to enqueue an item to LeftSide
    pop() 
        to delete an item from RightSide
    popleft() 
        to dequeue an item off the queue from the LeftSide
    index(ele, beg, end) 
        returns first index of value mentioned in arguments from starting to end.
    insert(i, a) 
        inserts value mentioned in arguments(a) at index(i) specified in arguments.
    remove() 
        removes first occurrence of value mentioned in arguments. 
    count() 
        counts number of occurrences of value mentioned in arguments. 
'''


''' CLASS QUEUE() '''

''' CLASS QUEUE() END '''


from collections import deque
queue = deque()
queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append('A')

print(f"Queue is {queue}", end="\n\n")

queue.popleft()
print(f"Popping FIRST item {queue}", end="\n\n")

# insert(), index(), remove(), count()

# index(ele, begi, endi) : return First repetitive_index of element
print(f"Index of 2 between index 0&3 is {queue.index(3,1,4)}", end="\n\n")

queue.insert(3, 1)  # insert(index,val)
print(f"Queue after inserting 1 at index3 {queue}", end="\n\n")

print(f"1 has been repeated {queue.count(1)} times", end="\n\n")

queue.remove(3)
print(f"Deleting first occurrence of 3 is{queue}", end="\n\n")
