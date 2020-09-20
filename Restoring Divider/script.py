def main():
    A=""
    Q=int(input("Enter the Dividend => "))
    M=int(input("Enter the Divisor => "))
    Q=bin(Q).replace("0b", "")
    M=bin(M).replace("0b", "")
    size=0
    
    if len(M)==len(Q):
            M="0"+M
    else:
        if len(Q)>len(M):
            how=len(Q)-len(M)
            for i in range (0,how,1):
                M="0"+M
        else:
            how=len(M)-len(Q)
            for i in range (0,how-1,1):
                Q="0"+Q
    for i in range (0,len(M),1):
        A="0"+A
    size=len(M)
    A="0"+A
    M="0"+M
    M2=twos_complement(M)
    print("Solution=>")
    print("A=",A)
    print("Q=",Q)
    print("M=",M)
    print("M2=",M2)
    printer="A\t\tQ\t\tSize\t\tSteps"
    print(printer)
    printer=A+"\t\t"+Q+"\t\t"+str(size)+"\t\tInitialization"
    print(printer)
    #print("A=",A)
    #print("Q=",Q)
    #print("size=",size)
    
    for i in range(size,0,-1):
        
        A=A[1:len(A)]+Q[0]
        Q=Q[1:len(Q)]
        printer=A+"\t\t"+Q+"\t\t"+str(size)+"\t\tLeft Shift"
        print(printer)
        A=add(A,M2)
        printer=A+"\t\t"+Q+"\t\t"+str(size)+"\t\tSubtraction"
        print(printer)
        if A[0]=='0':
            Q=Q+"1"
        else:
            Q=Q+"0"
            A=add(A,M)
        printer=A+"\t\t"+Q+"\t\t"+str(size)+"\t\tBit Checking"
        print(printer)
        size=size-1
        printer=A+"\t\t"+Q+"\t\t"+str(size)
        print(printer)

def twos_complement(n):
    a=""
    c=""
    for i in range(0,len(n)):
        if n[i]=='1':
            a=a+"0"
        else:
            a=a+"1"
    d=""
    for i in range (0,len(a)-1):
        d=d+"0"
    d=d+"1"
    c=add(a,d)
    return c

def add(x,y):
    carry=""
    result=""
    carry="0"
    for i in range(len(x)-1,-1,-1):
        a=carry[0]
        b=x[i]
        c=y[i]
        
        if a==b and b==c and c=='0':
            result="0"+result
            carry="0"
        elif a==b and b==c and c=='1':
            result="1"+result
            carry="1"
        else:
            if a=='1' and b==c and c=='0':
                result="1"+result
                carry="0"
            elif a=='0' and b=='1' and c=='0':
                result="1"+result
                carry="0"
            elif a=='0' and b=='0' and c=='1':
                result="1"+result
                carry="0"
            elif a=='0' and b=='1' and c=='1':
                result="0"+result
                carry="1"
            elif a=='1' and b=='0' and c=='1':
                result="0"+result
                carry="1"
            elif a=='1' and b=='1' and c=='0':
                result="0"+result
                carry='1'
    return result

def left_shift(A,Q):
    A=A[1:len(A)]+Q[0]
    Q=Q[1:len(Q)]

main()
