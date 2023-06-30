"""
Binary Search Algorithm
    Search Algorithm that finds the position of a target value within a sorted array(ASCE).
    Binary search compares the target value to the middle element of the array.
    Normal Zindagi (Linear Search):
        To find an element from a list, compare elements from index[0] till the element is found
    Mentos Zindagi (Binary Search):
        To find an element k from a list:
            > Sort the array in Ascending order
            > Find the middle element from the list
            > Compare it with key to be found
                > If middle element is less than key, find the middle element of the list at right-side of the middle element
                > If middle element is more than key, find the middle element of the list at left-side of the middle element
                > Repeat above 2 steps until the key is found
                > Return index of the key if it is found in the list
                > If key is not found in the list, return -1 or false
        With every iteration, search space is divided by 1/2
            Iteration 1 = n/2
            Iteration 2 = (n/2)/2 = n/2^2
            Iteration 3 = (n/2^2) = n/2^3
            Iteration k = (n/2^k)
                1 = n/2^k
                n = 2^k
                log2(n) = log2(2^k)
                log2(n) = k*log2(2)
                k = log(n)
            Time Complexity: O(log n)


key: 18
2 4 6 8 |10| 12 16 18 20    :: key not in {2, 4, 6, 8, 10}
~2 4 6 8 10~ 12 |16| 18 20  :: key not in {12}
~2 4 6 8 10 12 16~ |18| 20  :: key found in {18} at index[7]
Output:
7

Linear Search   7 iterations    O(n)
Binary Search   3 iterations    log(n)
"""

def LinearSearch(numList, key):
    for index, element in enumerate(numList):  # return index as well as element
        if element == key:
            return index  # if key is found in list, return index of key
    return -1

def BinarySearch(numList, key):
    left = 0  # index of elements at left of the mid value
    right = len(numList) - 1  # index of elements at right of the mid value
    mid_index = 0  # index of mid value

    while left <= right:  # while index[left] <= index[right]
        mid_index = (left + right)  // 2  # '//2' returns integer value
        mid_num = numList[mid_index]

        if mid_num == key:  # middle number is equal to key
            return mid_index
        if mid_num < key:
            left = mid_index + 1
        else:  # mid_num > key
            right = mid_index - 1

    return -1


"""Binary Search using Recursion"""
def BinarySearchRecursion(numList, key, leftIndex, rightIndex):  # will search within left and right
    if rightIndex < leftIndex:  # won't iterate in reverse order
        return -1

    mid_index = (leftIndex + rightIndex) // 2  # '//2' returns integer value
    if mid_index >= len(numList):  # if key is out of index of list, return -1
        return -1

    mid_num = numList[mid_index]
    if mid_num == key:  # middle number is equal to key
        return mid_index

    if mid_num < key:
        leftIndex = mid_index + 1
    else:  # mid_num > key
        rightIndex = mid_index - 1

    return BinarySearchRecursion(numList, key, leftIndex, rightIndex)






if __name__ == '__main__':
    numList = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    key = 18
    # Linear Search
    index = LinearSearch(numList, key)
    print(f"Linear Search: Number found at index {index}")
    # Binary Search
    index = BinarySearch(numList, key)
    print(f"Binary Search: Number found at index {index}")
    # Binary Search using Recursion
    index = BinarySearchRecursion(numList, key, 0, len(numList))
    print(f"Binary Search Recursion: Number found at index {index}")



