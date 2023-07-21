"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Stack
"""


class S:
    stack = []
    MaxSize = 0
    tos = 0

    def createStack(self, size):
        S.tos = -1
        S.MaxSize = size
        for i in range(0, S.MaxSize):
            S.stack.append(0)
        print('Stack created of size', len(S.stack))
        print(S.stack)

    def push(self, e):
        S.tos += 1
        S.stack[S.tos] = e
        print('Element pushed')

    def pop(self):
        temp = S.stack[S.tos]
        S.tos -= 1
        return temp

    def isFull(self):
        if S.tos == S.MaxSize-1:
            return True
        else:
            return False

    def isEmpty(self):
        if S.tos == -1:
            return True
        else:
            return False

    def peek(self):
        return (S.stack[S.tos])

    def printStack(self):
        for i in range(S.tos, -1, -1):
            print(i, S.stack[i])


# Main Code
o = S()
o.createStack(int(input('Enter size: ')))
while True:
    print('------------')
    print('1.Push\n2.Pop\n3.Peek\n4.Print\n0.Exit')
    print('------------')

    ch = int(input('Enter your choice: '))

    if ch == 1:
        if o.isFull() != True:
            data = int(input('Enter the element to push: '))
            o.push(data)
            print('Element pushed:', data)
        else:
            print('\nStack is full..!!')

    elif ch == 2:
        if o.isEmpty() != True:
            print('Element popped:', o.pop())
        else:
            print('\nStack is empty..!!')

    elif ch == 3:
        if o.isEmpty() != True:
            print('Peeked Element', o.peek())
        else:
            print('\nStack is empty..!!')

    elif ch == 4:
        if o.isEmpty() != True:
            print('ELements in stack are: ')
            o.printStack()
        else:
            print('\nStack is empty..!!')

    elif ch == 0:
        break

    else:
        print('Wrong Input')
1
