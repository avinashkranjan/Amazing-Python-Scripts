## **Sorting Techniques**

### **Bubble Sort**
Bubble sort is a simple comparison-based sorting algorithm. It repeatedly compares adjacent elements and swaps them if they are in the wrong order. The algorithm continues iterating through the list until the list is sorted.

🔗 View here: [Bubble Sort](./Bubble_Sort.py)

<br />

### **Insertion Sort**
Insertion sort is another comparison-based sorting algorithm. It builds the final sorted array one item at a time by inserting each element into its proper position within the sorted portion of the array.

🔗 View here: [Insertion Sort](./Insertion_Sort.py)

<br />

### **Merge Sort**
Merge sort is a divide-and-conquer algorithm that divides the unsorted list into sublists, sorts them, and then merges them to produce the final sorted list. It is an efficient sorting algorithm with a time complexity of O(n log n)

🔗 View here: [Merge Sort](./Merge_Sort.py)

<br />

### **Quick Sort**
Quick sort is another divide-and-conquer algorithm that works by selecting a pivot element and partitioning the array around the pivot. It recursively sorts the sub-arrays created by the partitioning. Quick sort has an average-case time complexity of O(n log n).

🔗 View here: [Quick Sort](./Quick_Sort.py)

<br />

### **Selection Sort**
Selection sort is an in-place comparison-based sorting algorithm. It works by dividing the array into two sub-arrays: the sorted sub-array at the beginning and the unsorted sub-array at the end. It repeatedly selects the minimum element from the unsorted sub-array and swaps it with the leftmost unsorted element.

🔗 View here: [Selection Sort](./Selection_Sort.py)

<br />

## **Comparing Time Complexities**
<br />

Sorting Technique | Worst Time | Best Time | Average Time
:--- | :---: | :---: | :---:
Bubble Sort | O(n^2) |  O(n) | O(n^2)
Insertion Sort | O(n^2) |  O(n) | O(n^2)
Merge Sort | O(n log n) | O(n log n) | O(n log n)
Quick Sort | O(n^2) |O(n log n) | O(n log n)
Selection Sort | O(n^2) | O(n^2) | O(n^2)