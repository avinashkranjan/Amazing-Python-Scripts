'''
This algorithm calculates the Nth Fibonacci Nummber in log(N) time complexity
The key idea behind this algorimth is to use matrix exponentiation technique (matrix multiplication + binary exponentiation)
This algorithm uses the fact that the Fibonacci Numbers can be converted to a 2D matrix of 2x2 size, [[1, 1][1, 0]], and the Fibonacci 
Number which is to be calculated with the help of matrix multiplication will be nothing but cell, (0,0) of (Matrix)^n ,i.e, our resultant 
matrix. 
'''
def fib(n):
 
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)
 
    return F[0][0]
 
'''
Matrix multiplication is calculated using Strassen Algorithm which calculates the product of Two Matrices in o(N^3) time complexity.
Since, the size of matrix here is fixed, i.e, 2x2, so, the Time Complexity will be O(1). 
'''
def multiply(F, M):
 
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
 
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w
 
'''
Power function uses Binary Exponentiation Technique to calculate the value of x^n in O(logN) time instead of O(N) time.
'''
def power(F, n):
 
    if(n == 0 or n == 1):
        return
    M = [[1, 1],
         [1, 0]]
 
    power(F, n // 2)
    multiply(F, F)
 
    if (n % 2 != 0):
        multiply(F, M)
 
 
# Driver Code
if __name__ == "__main__":
    n = 5  
    print(fib(n))

'''
I hope you have a fun time reading this algorithm. 
Problems for practice: 
https://practice.geeksforgeeks.org/problems/generalised-fibonacci-numbers1820/1
https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1
https://practice.geeksforgeeks.org/problems/37f36b318a7d99c81f17f0a54fc46b5ce06bbe8c/0
'''
