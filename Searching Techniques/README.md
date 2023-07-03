# **Searching Techniques**
Searching techniques are algorithms used to find a specific element or value within a collection of data.


## **Explanation**

1. ### **Binary Search Technique (Iterative)**
    Binary search is a highly efficient searching technique for sorted arrays or lists. In the iterative approach, the search is divided into halves repeatedly until the target value is found or determined to be absent.
    <details>
    <summary><h3>Explanation</h3></summary>
    
        1. Initialize two pointers, 'low' and 'high', pointing to the start and end of the array respectively.
        2. While 'low' is less than or equal to 'high', do the following:
            - Calculate the mid-point index as the average of 'low' and 'high'.
            - If the mid-point value is equal to the target value, return the index.
            - If the target value is less than the mid-point value, set 'high' to mid - 1.
            - If the target value is greater than the mid-point value, set 'low' to mid + 1.
        3. If the target value is not found, return a sentinel value indicating its absence.

    </details>
    
    🔗 View here: [Binary Search Technique (Iterative)](./Binary_Search_Iterative.py)
---

2. ### **Binary Search Technique (Recursive)**
    Binary search can also be implemented recursively. The recursive approach follows the same principle of dividing the search space in half until the target value is found or determined to be absent.

    <details>
    <summary><h3>Explanation</h3></summary>

        1. Define a recursive function that takes the array, the target value, 'low', and 'high' as parameters.
        2. If 'low' is greater than 'high', return a sentinel value indicating the target value is not found.
        3. Calculate the mid-point index as the average of 'low' and 'high'.
        4. If the mid-point value is equal to the target value, return the index.
        5. If the target value is less than the mid-point value, recursively call the function with 'low' and 'mid - 1'.
        6. If the target value is greater than the mid-point value, recursively call the function with 'mid + 1' and 'high'.

    </details>

    🔗 View here: [Binary Search Technique (Recursive)](./Binary_Search_Recursive.py)
---

3. ### **Sequential Search**
    Sequential search, also known as linear search, is a simple and straightforward searching technique applicable to both sorted and unsorted data. It involves iterating through each element of the collection until the target value is found or the end of the collection is reached. 

    <details>
    <summary><h3>Explanation</h3></summary>

        1. Start at the beginning of the collection and iterate through each element.
        2. Compare each element with the target value.
        3. If the target value is found, return the index.
        4. If the end of the collection is reached without finding the target value, return a sentinel value indicating its absence.

    </details>

    🔗 View here: [Sequential Search](./Sequential_Search.py)


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
