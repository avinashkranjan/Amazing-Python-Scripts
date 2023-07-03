"""
Shell Sort
    Shell sort is an optimization over Insertion sort
    Aim is to reduce swaps and comparisons by swapping greater elements at right side of array and light element at left
Algorithm
    Start with gap = n/2 and sort sub arrays
    Keep reducing gap by n/2 and keep on sorting sub arrays
    Last iteration should have gap = 1. At this point it is same as insertion sort
        Actually, we are doing insertion sort but with some optimization
        so that number of swaps and comparisons can be reduced
Disadvantage of Insertion sort over Shell Sort
    When small elements are towards the end of array it takes many:
        Comparisons
        Swaps
Worst-case Performance
    O(n^2) (worst known worst-case gap sequence)
    O(n log^2(n)) (best known worst-case gap sequence)
Best-case Performance
    O(n log n) (most gap sequences)
    O(n log^2(n)) (best known worst-case gap sequence)

"""

def ShellSort(arr):
    # gap = 3  # initialised gap to 3
    size = len(arr)
    gap = size // 2  # initialised gap to half of size of array
    while gap > 0:
        for i in range(gap, size):
            pointer = arr[i]  # pointer initialised to array such that gap is maintained
            j = i
            # get element which is at gap 3 and compare with current pointer element AND j>=gap else (j-gap) would be negative
            while j >= gap and arr[j - gap] > pointer:
                arr[j] = arr[j-gap]  # swapped elements
                j -= gap  # In each while loop iteration, reduce by gap for comparison with previous elements
            arr[j] = pointer  # after while loop ends, all elements have been swapped
            # after function end, all heavy values are at right side and light values at left of partially-sorted array
        gap = gap // 2  # gap reduced by half


if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    # Partially sorted array after Shell Sort[11, 4, 9, 17, 32, 25, 21, 38, 29]
    ShellSort(elements)
    print(elements)

    # Test Cases
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],  # DESC sorted array
        [],  # empty array
        [1, 5, 8, 9],  # sorted array
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],  # array with uneven elements
        [5]  # array with single element
    ]

    for elements in tests:
        ShellSort(elements)
        print(elements)