"""
Bubble Sort
    Simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order
    known as BubbleSort because the maximum element comes to surface(correct/last position) as a bubble
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def BubbleSort(elements):
    size = len(elements)  # get size of list for iteration purpose

    for i in range(size-1):  # runs following loop (sizeof(array)-1) times
        # If list is already swapped, loop would run only once
        swapped = False  # list is not swapped yet
        # swaps greatest element each time
        # no element after last element to compare with: that's why size-1
        for j in range(size-1-i):
            # size-1-i: if last 2 elements of list are already sorted, run loop for previous elements only
            if elements[j] > elements[j+1]:  # if element[left] > element[right]
                # Swapping Variables in traditional way
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True  # list is swapped successfully

        if not swapped:
            break


if __name__ == '__main__':
    elements = [10, 9, 7, 8, 6, 28, 2, 3, 1]
    BubbleSort(elements)
    print(elements)
    # sorting alphabets using bubble sort
    elements = ['c', 'e', 'a', 'b', 'd', 'python']
    BubbleSort(elements)
    print(elements)
