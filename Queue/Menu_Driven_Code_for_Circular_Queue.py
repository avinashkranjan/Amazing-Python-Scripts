"""
Author: Himanshu Agarwal
Github: himanshu-03 (http://github.com/himanshu-03)
LinkedIn: agarwal-himanshu (https://linkedin.com/in/agarwal-himanshu)

# Menu Driven Code for Circular Queue
"""


class Q:
    queue = []
    count = 0
    front = 0
    rear = 0

    def createQueue(self, size):
        Q.front = 0
        Q.rear = -1
        Q.MaxSize = size
        for i in range(0, Q.MaxSize):
            Q.queue.append(0)
        print('\nQueue created of size: ', len(Q.queue))
        print(Q.queue)

    def enqueue(self, e):
        Q.rear = (Q.rear+1) % Q.MaxSize
        Q.count += 1
        Q.queue[Q.rear] = e
        print(e, 'enqueued in Queue')
        print('')

    def dequeue(self):
        temp = Q.queue[Q.front]
        Q.front = (Q.front+1) % Q.MaxSize
        Q.count -= 1
        print(temp, 'dequeued from Queue')
        print('')

    def isFull(self):
        if Q.count == Q.MaxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if Q.count == 0:
            return True
        else:
            return False

    def printQueue(self):
        print('\nData')
        c = 0
        i = Q.front
        while c < Q.count:
            print(Q.queue[i], end="-->")
            i = (i+1) % self.MaxSize
            c += 1
        print('')


# Main Code:
o = Q()
o.createQueue(int(input('Enter size of the queue: ')))

while True:
    print('------------')
    print('1.Enqueue\n2.Dequeue\n3.Print\n0.Exit')
    print('------------')

    ch = int(input('\nEnter your choice: '))

    if ch == 1:
        if o.isFull() != True:
            data = int(input('\nEnter data to be enqueued: '))
            o.enqueue(data)
        else:
            print('\nQueue is full..\n')

    elif ch == 2:
        if o.isEmpty() != True:
            o.dequeue()
        else:
            print('\nQueue is empty..\n')

    elif ch == 3:
        if o.isEmpty() != True:
            o.printQueue()
        else:
            print('\nQueue is empty..\n')

    elif ch == 0:
        break

    else:
        print('\nWrong Input..\nEnter the correct choice..!!\n')
