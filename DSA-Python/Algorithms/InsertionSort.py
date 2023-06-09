"""
Insertion Sort
    Insertion sort is an simple sorting algorithm that builds the final sorted array one item at a time
Benefits of Insertion Sort
    Simple Implementation
    Efficient for quite small data sets
    Adaptive: efficient for data sets that are already substantially sorted
    Stable: does not change relative order of elements with equal keys
    In-Place: only requires a constant amount O(1) of additional extra space
    Online: can sort a list as it receives it
Traditional Approach
    Let unsorted array be Uarr and Sorted array be Sarr
    Create a sorted array namely 'Sarr'
    Put i(th) element from Uarr to Sarr
    put (i+1)th element in Sarr such that the array is still sorted
    put(i+2)th element such that array is still sorted by comparing and shuffling the elements, if required
Effective Approach
    Take a pointer at index[1] {considering index[0] is sorted}
    Let everything at left of the pointer be sorted
    compare the current pointed element with the elements of sorted side (i.e. left side)
        If CurrentElement < elements at sorted array: insert current element at appropriate place of sorted array
        If CurrentElement > elements at sorted array: repeat above processes until array is sorted

    For instance,
        Uarr: 2 5 8 1 3 4
        2 5 8 1 3 4     2,5
        2 5 8 1 3 4     5,8
        2 5 8 1 3 4     8,1
        1 2 5 8 3 4     8,3
        1 2 3 5 8 4     8,4
        1 2 3 4 5 8     Sarr

    Worst-Case Performance          O(n^2)-{Comparisons} and O(n^2)-{Swaps}
    Best-Case Performance           O(n)-{Comparisons} and O(1)-{Swaps}
    Average Performance             O(n^2)-{Comparisons} and O(n^2)-{Swaps}
    Worst-caseSpace Performance     O(n)-{Comparisons} and O(1)-{Auxiliary}

"""


def InsertionSort(elements):
    for i in range(1, len(elements)):  # starting with the 2nd element {index[1]}
        pointer = elements[i]  # current element named as pointer
        j = i - 1  # left element of pointer {index[current] - 1 = elements[left]}
        # compare current element (pointer) to sorted array (j)
        # iterate between j to index[0] and continue until elements of j > pointer
        while j >= 0 and pointer < elements[j]:
            elements[j + 1] = elements[j]  # swapped left element to right element
            j = j - 1  # same as j--
        # when loop is terminated, pointer will be assigned to next element
        elements[j + 1] = pointer  # increase pointer value and repeat until array is sorted


if __name__ == '__main__':
    elements = [2, 5, 8, 1, 3, 4]
    InsertionSort(elements)
    print(elements)
    # test cases
    tests = [
        [11, 9, 29, 7, 2, 15, 28],  # worst-case scenario
        [3, 7, 9, 11],  # sorted list
        [25, 22, 21, 10],  # DESC-sorted list
        [],  # empty list
        [6]  # single element list
    ]

    for elements in tests:
        InsertionSort(elements)
        print(f"Sorted array: {elements}")