''' 
STACK
    LIFO

All push and pop operations are to/from the top of the stack
    PUSH an item onto the stack
    POP an item off of the stack
    PEEK to get item on top of stack, without removing it
    CLEAR all items from stack

STACK USE CASE
Undo Command : track which command have been executed. Pop last command off the command stack to undo it
Calling Function: Function Calling in any programming language is managed using stack

Stack Class in Python:
    list
    collections.deque
    queue.LifoQueue

BigO of stack:
    Push/Pop element -----> O(1)
    Search element by value -----> O(n)

'''

''' CLASS STACK() '''
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)
''' CLASS STACK() END '''        

stack = list()
# .append method to append items to the stack
stack.append(1)
stack.append(4)
stack.append(9)
stack.append(16)
print(f"Stack is {stack}", end="\n\n")
stack.pop()
print(f"Deleted Last item of Stack (LIFO) {stack}", end="\n\n")

# Calling Stack() class
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push('B')

print(f"New Stack is {stack}")
print(f"Deleted item is {stack.pop()}")
print(f"Seek is at {stack.peek()}")



#TODO: Stack continue ( https://youtu.be/kQDxmjfkIKY?t=3077 )

