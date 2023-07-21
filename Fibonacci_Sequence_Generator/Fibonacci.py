def fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence


n = 0
while n <= 0:
    n = int(input("Enter how many terms you need in your Fibonacci Sequence: "))

fib_sequence = fibo(n)
print(", ".join(map(str, fib_sequence)))
