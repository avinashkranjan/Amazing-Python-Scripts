"""
Recursion
"""
from docutils.nodes import field


def sumIteration(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def sumRecursion(n):
    if n == 1:
        return 1
    return n + sumRecursion(n - 1)


def fibonacci(n):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
    :param n: positive index of fibonacci series
    :return: number at nth position of fibonacci series
    """
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(f"Sum using Iteration: {sumIteration(15)}")
    print(f"Sum using Recursion: {sumRecursion(15)}")
    n = 10
    print(f"Fibonacci Series upto {n} terms:\n{fibonacci(-1)}")
