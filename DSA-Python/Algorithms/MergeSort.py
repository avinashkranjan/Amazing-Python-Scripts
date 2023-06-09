"""
Merge Sort
    We have 2 unsorted arrays, we've to sort them and merge them in a way that merged array is also a sorted array
    Traditional Method
        Compare first element of each array
            Insert the smallest element into sorted array
        Compare greater element from previous array and 2nd element from 2nd array
            Insert the smallest element into sorted array
        Repeat until array is sorted


                    9 - 2 - 1 - 7 - 5 - 3 - 4 - 6
                  9 - 2 - 1 - 7       5 - 3 - 4 - 6
               9 - 2    1 - 7           5 - 3    4 - 6
             2 - 9    1 - 7               3 - 5    4 - 6
           1 - 2  -  7 - 9                 3 - 4  -  5 - 6
               1 - 2 - 7 - 9              3 - 4 - 5 - 6
                      1 - 2 - 3 - 4 - 5 - 6 - 7 - 9


Time Complexity: O(n log n)


"""

def Merge2SortedList(arr1, arr2):
    """Input: 2 sorted lists"""
    sortedList = []  # created an empty sorted list
    len_arr1 = len(arr1)  # length of array1
    len_arr2 = len(arr2)  # length of array2
    i = j = 0  # pointers initialised
    # iterate through both lists until end of any of them is reached
    while i < len_arr1 and j < len_arr2:
        if arr1[i] <= arr2[j]:  # compare elements between both the lists
            sortedList.append(arr1[i])  # append to sorted list
            i+=1  # i pointer is increased by 1 and j pointer is static
        else:
            sortedList.append(arr2[j])
            j+=1
    while i < len_arr1:
        sortedList.append(arr1[i])
        i+=1
    while j < len_arr2:
        sortedList.append(arr2[j])
        j += 1
    return sortedList  # sorted list returned


def MergeSort(arr):
    # if list is empty or contains 1 element only: return list
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2  # get middle index of array to divide it into 2 parts: left and right
    left = arr[:mid]  # dividing list into 2 parts: left and right
    right = arr[mid:]  # dividing list into 2 parts: left and right

    left = MergeSort(left)  # recursively call MergeSort function to sort left array
    right = MergeSort(right)  # recursively call MergeSort function to sort right array
    # MergeSort(left)  # recursively call MergeSort function to sort left array
    # MergeSort(right)  # recursively call MergeSort function to sort right array

    return Merge2SortedList(left, right)  # Merge Sort both sorted array
    # Merge2SortedList(left, right)  # Merge Sort both sorted array


if __name__ == '__main__':

    """arr1 = [2, 4, 6, 8]
    arr2 = [3, 6, 9, 12]
    print(Merge2SortedList(arr1, arr2))"""
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    print(MergeSort(arr))

    # test cases

    tests = [
        [20, 13, 5, 37, 8, 32, 98, 29],  # unsorted array
        [],  # empty array
        [5],  # array with single element
        [10, 8, 6, 4, 2],  # reverse array
        [1, 2, 3, 4, 5]  # sorted array
    ]
    for elements in tests:
        print(MergeSort(elements))
