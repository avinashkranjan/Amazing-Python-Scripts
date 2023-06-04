# **Queue**
Queues are a common data structure that follows the First-In-First-Out (FIFO) principle, where elements are inserted at the rear and removed from the front.


## **Explanation**

1. ### **Linear Queue**
    A linear queue is a basic implementation of a queue using a fixed-size array. The menu-driven code for a linear queue typically includes options to enqueue (add) elements, dequeue (remove) elements, display the queue, check if it is empty, check if it is full, and exit the program. The code must handle cases where the queue becomes full or empty.

    🔗 View here: [Linear Queue](./Menu_Driven_Code_for_Linear_Queue.py)


2. ### **Circular Queue**
    A circular queue overcomes the limitation of a linear queue by reusing empty spaces at the beginning of the queue. It uses a circular buffer or a modulo operation to wrap around and fill the empty spaces. The menu-driven code for a circular queue offers options to enqueue, dequeue, display the queue, check if it is empty, check if it is full, and exit. Special attention should be given to handle the circular nature of the queue when performing enqueue and dequeue operations.

    🔗 View here: [Circular Queue](./Menu_Driven_Code_for_Circular_Queue.py)


3. ### **Priority Queue**
    A priority queue assigns a priority value to each element, and the element with the highest priority is dequeued first. The menu-driven code for a priority queue provides options to enqueue elements with their respective priorities, dequeue elements based on priority, display the queue, check if it is empty, check if it is full, and exit. It typically employs a suitable data structure like a heap or a binary search tree to maintain the priority order efficiently.

    🔗 View here: [Priority Queue](./Menu_Driven_Code_for_Priority_Queue.py)


4. ### **Dynamic Linear Queue using Linked List**
    A dynamic linear queue implemented using a linked list allows for a queue with dynamic memory allocation. The menu-driven code for this structure includes options to enqueue elements, dequeue elements, display the queue, check if it is empty, check if it is full (not applicable for linked list implementation), and exit.

    🔗 View here: [Dynamic Linear Queue using Linked List](./Menu_Driven_Code_for_Dynamic_Linear_Queue_using_LinkedList.py)


## **Setup Instructions**

1. Install Python
2. Verify Python Installation

    ```bash
    python --version
    ```

3. Run the Python Script
    ```bash
    python filename.py
    ```

    Note: Replace `filename.py` with the name of the python file which is to be executed.


## **Author**

- [Himanshu Agarwal](https://github.com/himanshu-03)