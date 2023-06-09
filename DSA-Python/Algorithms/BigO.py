"""
BigO Notation
    Big O Notation is used to measure hoe running time or space requirements for your program grow as input size grows
Order of Magnitude
    A Time Complexity does not tell the exact number of times the code inside a loop is executed,
    but it only shows the order of magnitude. Whether code inside loop is executed for 3n, n+5, n/2 times;
    the time complexity of each code is O(n)

Rules for BigO Notation
    time = a * n + b
    > Keep fastest growing term
            BigO refers to very large value of n. Hence if you have a function like:
                time = 5*n^2 + 3*n + 20
                when value of n is very large (b*n + c) become irrelevant
                Example: n = 1000
                time = 5*1000^2 + 3*1000 + 20
                time = 5000000 + 3020
                time ~= 5000000  # terms other than 5*1000^2 contribute negligible

        time = a * n  # being b a constant and static

    > Drop constant
        time = n  # a being constant
        time = O(n)

Measuring running time growth (Time Complexity)

    Constant Time Complexity O(1)
        Running time of Constant-time algorithm does not depend on the input size
        time = a
        time = O(1)  # applying rules for Big O :: Keep fastest growing term (a) ->->-> Drop Constants(a)


        def foo(a):  # time is nearly constant with increase in input size
            size(arr) : 100   -> 0.22 milliseconds
            size(arr) : 1000  -> 0.23 milliseconds

    Logarithmic Time Complexity O(log n)
        A logarithmic algorithm often halves the input size at each step. The running time of such an algorithm is
        logarithmic, because log2 n equals the number of times n must be divided by 2 to get 1

    Square Root Algorithm O(sqrt(n))
        A square root algorithm is slower than O(log n) but faster than O(n) A special property of square roots is that
        sqrt(n) = n/(sqrt(n)), so the square root (sqrt(n)) lies, in some sense, in the middle of the input

    Linear Time Complexity O(n)
        A linear algorithm goes through the input a constant number of times
        time = a * n + b
        time = O(n)  # applying rules for Big O :: Keep fastest growing term (a*n) ->->-> Drop Constants(a, b)

        def foo(arr):
            size(arr) : 100   -> 0.22 milliseconds
            size(arr) : 1000  -> 2.30 milliseconds

    O(n log n)
        This time complexity often indicates that the algorithm sorts the input, because the time complexity of
        efficient sorting algorithms is O(n logn)

    Quadratic Time Complexity O(n^2)
        A quadratic time complexity often contains two nested loops
        time = a * (n^2) + b
        time = O(n^2)  # applying rules for Big O :: Keep fastest growing term (a*n^2) ->->-> Drop Constants(a, b)
        Exception O(n^2) not O(n^2 + n)
            time = a*(n^2) + (b * n) + c
            time = n^2  # applying rules for Big O :: Keep fastest growing term (a*n^2) ->->-> Drop Constants(a, b, c)

    Cubic Time Complexity O(n^3)
        A cubic algorithm often contains three nested loops

    O(2^n)
        This time complexity often indicates that the algorithm iterates through all subsets of the input elements

    O(n!)
        This time complexity often indicates that the algorithm iterates through all permutations of the input elements

    Note:
        An algorithm is polynomial if its time complexity is at most O(nk) where k is a constant.
        All the above time complexities except O(2n) and O(n!) are polynomial

Given the input size, we can try to guess the required time complexity of the algorithm that solves the problem.
The following table contains some useful estimates assuming a time limit of one second

    n <= 10     O(n!)
    n <= 20     O(2n)
    n <= 500    O(n3)
    n <= 5000   O(n2)
    n <= 106    O(n logn) or O(n)
    n is large  O(1) or O(log n)


"""
""" Time Complexity """

# Linear Time Complexity O(n)
def squareNum(numbers):
    """
    Time Complexity: O(n)  :: loop will iterate n time linearly
    """
    sqNum = []  # empty array for squared numbers initialised
    for n in numbers:  # loop will iterate n times
        sqNum.append(n*n)
    return sqNum


# Constant Time Complexity O(1)
def findPE(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe


# O(n^2)
def duplicateInArray(numbers):
    """ Running two for loops"""
    duplicate = None
    # (n^2) iterations
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(f"{numbers[i]} is duplicate")
                duplicate = numbers[i]
                break
    # n iterations
    for i in range(len(numbers)):
        if numbers[i] == duplicate:
            print(i)


""" Space Complexity """
def Search(numbers):
    """
    Search for 10 in list
    Time Complexity: O(n)
    """
    for i in range(len(numbers)):
        if numbers[i] == 10:
            print(i)




if __name__ == '__main__':
    # O(n)
    numbers = [2, 5, 7, 9]
    print(squareNum(numbers))

    # O(1)
    prices = [250, 500, 450]
    eps = [25, 50, 75]
    index = 1
    print(findPE(prices, eps, index))

    # O(n^2)
    numbers = [2, 4, 6, 8, 14, 9, 4]
    duplicateInArray(numbers)

    numbers = [1, 6, 8, 10, 4, 5]
    Search(numbers)

