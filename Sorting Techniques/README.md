# **Sorting Techniques**

Sorting techniques are algorithms that arrange a collection of data elements in a particular order, typically ascending or descending. These techniques aim to organize the data to make it easier to search, retrieve, and analyze. Sorting algorithms compare elements within the data set and rearrange them based on their values or specific criteria.

## **Explanation**
1. ### **Bubble Sort**
    Bubble sort is a simple comparison-based sorting algorithm. It repeatedly compares adjacent elements and swaps them if they are in the wrong order. The algorithm continues iterating through the list until the list is sorted.

    🔗 View here: [Bubble Sort](./Bubble_Sort.py)

2. ### **Insertion Sort**
    Insertion sort is another comparison-based sorting algorithm. It builds the final sorted array one item at a time by inserting each element into its proper position within the sorted portion of the array.

    🔗 View here: [Insertion Sort](./Insertion_Sort.py)

3. ### **Merge Sort**
    Merge sort is a divide-and-conquer algorithm that divides the unsorted list into sublists, sorts them, and then merges them to produce the final sorted list. It is an efficient sorting algorithm with a time complexity of O(n log n)

    🔗 View here: [Merge Sort](./Merge_Sort.py)

4. ### **Quick Sort**
    Quick sort is another divide-and-conquer algorithm that works by selecting a pivot element and partitioning the array around the pivot. It recursively sorts the sub-arrays created by the partitioning. Quick sort has an average-case time complexity of O(n log n).

    🔗 View here: [Quick Sort](./Quick_Sort.py)

5. ### **Selection Sort**
    Selection sort is an in-place comparison-based sorting algorithm. It works by dividing the array into two sub-arrays: the sorted sub-array at the beginning and the unsorted sub-array at the end. It repeatedly selects the minimum element from the unsorted sub-array and swaps it with the leftmost unsorted element.

    🔗 View here: [Selection Sort](./Selection_Sort.py)


## **Comparing Time Complexities**

Sorting Technique | Worst Time | Best Time | Average Time
:--- | :---: | :---: | :---:
Bubble Sort | O(n^2) |  O(n) | O(n^2)
Insertion Sort | O(n^2) |  O(n) | O(n^2)
Merge Sort | O(n log n) | O(n log n) | O(n log n)
Quick Sort | O(n^2) |O(n log n) | O(n log n)
Selection Sort | O(n^2) | O(n^2) | O(n^2)

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