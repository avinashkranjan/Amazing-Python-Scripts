"""
Selection Sort

Time Complexity: O(n^2)
"""


def FindMin(arr):
    """finds minimum element from the list"""
    min = 100000  # let list contain +ve numbers only: so minimum number is -1
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


def SelectionSort(arr):
    size = len(arr)
    for i in range(size-1):  # decreased 1 iteration: no need to iterate to the last element
        minIndex = i  # pointer initialised to ith index for selection sort
        for j in range(minIndex+1, size):
            if arr[j] < arr[minIndex]:  # if current index < minimum index of the array
                minIndex = j  # minimum index updated
        # swapping element
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]


if __name__ == '__main__':
    elements = [100, 19, 28, 14, 6, 1, 99]
    print(FindMin(elements))  # prints minimum element from the list
    SelectionSort(elements)
    print(elements)

    # running test cases

    tests = [
        [89, 78, 61, 23, 21, 53, 12, 1, 2, 6, 3, 17, 9],
        [],
        [1, 2, 3, 4, 5],
        [350, 3, 1, 99, 12, 78, 12, 1200],
        [9]
    ]
    # print("Tests case testing...")
    for elements in tests:
        SelectionSort(elements)
        print(elements)
