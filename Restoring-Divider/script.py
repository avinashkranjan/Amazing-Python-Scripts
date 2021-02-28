def main():
    A = ""
    Q = int(input("Enter the Dividend => "))
    M = int(input("Enter the Divisor => "))
    Q = bin(Q).replace("0b", "")
    M = bin(M).replace("0b", "")
    size = 0
    """
    This part makes the initialisation of required for the Restoring Division to occur.
    Which includes:
    1) Setting an extra to M compared to A
    2) Filling up A with zeroes
    3) Setting the size
    """
    if len(M) == len(Q):
        M = "0" + M
    else:
        if len(Q) > len(M):
            how = len(Q) - len(M)
            for i in range(0, how, 1):
                M = "0" + M
        else:
            how = len(M) - len(Q)
            for i in range(0, how - 1, 1):
                Q = "0" + Q
    for i in range(0, len(M), 1):
        A = "0" + A
    size = len(M)
    """
    The Calculation and Line by Line Display begins from here
    """
    A = "0" + A
    M = "0" + M
    M2 = twos_complement(M)
    print("Solution=>")
    print("A=", A)
    print("Q=", Q)
    print("M=", M)
    print("M2=", M2)
    printer = "A\t\tQ\t\tSize\t\tSteps"
    print(printer)
    # Printing the Initialisation step
    printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tInitialization"
    print(printer)
    """
    The division will be taking place until the size of the Divisor becomes zero
    """
    for i in range(size, 0, -1):
        """
        Left Shift Operation
        """
        A = A[1:len(A)] + Q[0]
        Q = Q[1:len(Q)]
        printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tLeft Shift"
        print(printer)
        """
        Subtraction
        """
        A = add(A, M2)
        printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tSubtraction"
        print(printer)
        """
        Bit Checking and AAddition if required
        """
        if A[0] == '0':
            Q = Q + "1"
        else:
            Q = Q + "0"
            A = add(A, M)
        printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tBit Checking"
        print(printer)
        """
        Decreasing Size
        """
        size = size - 1
        printer = A + "\t\t" + Q + "\t\t" + str(size)
        print(printer)


def twos_complement(n):
    a = ""
    c = ""
    """
    Performing 1's Complement by changing all zeroes to one
    """
    for i in range(0, len(n)):
        if n[i] == '1':
            a = a + "0"
        else:
            a = a + "1"
    """
    Performing 2's complement by adding 1 to the 1's complement
    """
    d = ""
    for i in range(0, len(a) - 1):
        d = d + "0"
    d = d + "1"
    c = add(a, d)
    return c


def add(x, y):
    """
    Binary Adddition bing carried out
    """
    carry = ""
    result = ""
    carry = "0"
    for i in range(len(x) - 1, -1, -1):
        a = carry[0]
        b = x[i]
        c = y[i]

        if a == b and b == c and c == '0':
            result = "0" + result
            carry = "0"
        elif a == b and b == c and c == '1':
            result = "1" + result
            carry = "1"
        else:
            if a == '1' and b == c and c == '0':
                result = "1" + result
                carry = "0"
            elif a == '0' and b == '1' and c == '0':
                result = "1" + result
                carry = "0"
            elif a == '0' and b == '0' and c == '1':
                result = "1" + result
                carry = "0"
            elif a == '0' and b == '1' and c == '1':
                result = "0" + result
                carry = "1"
            elif a == '1' and b == '0' and c == '1':
                result = "0" + result
                carry = "1"
            elif a == '1' and b == '1' and c == '0':
                result = "0" + result
                carry = '1'
    return result


main()
