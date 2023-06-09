#function which finds out individual term of the fibonacci sequence
def fibo(x):
    if(x == 1 or x == 2): #base case
        return 1
    else:
        return fibo(x-1) + fibo(x-2) 
        #following the actual way how the fibonacci series is generated i.e. adding the previous two terms

n = 0
while(n<=0):
    n = int(input("Enter how many terms do you need in your Fibonacci Sequence? "))
    #this loop is just to ensure that the user inputs a valid number

for i in range(1,n): 
    #finding out individual terms of the series and printing till (n-1) terms since we don't want an extra comma at the end
    print(fibo(i), end=", ")
print(fibo(n)) #printing the last(i.e. nth term)
