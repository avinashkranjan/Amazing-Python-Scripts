def to_binary(n):    #Function to convert to Binary
    binary = ''
    while n>=1:
        binary = str(n%2)+binary
        n = n//2
    return int(binary)

#Alternate method to convert to Binary
'''
def to_binary(n):
    return(int(bin(n).replace('0b','')))
'''


def to_hexadecimal(n):    #Function to convert to Hexadecimal
    hexa = ''
    digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    while n>=1:
        hexa = digits[n%16] + hexa
        n = n//16
    return hexa

#Alternate method to convert to Hexadecimal
'''
def to_hexadecimal(n):
    return(hex(n).replace('0x',''))
'''
    

    
def to_octal(n):    #Function to convert to Octal
    octal = ''
    while n>=1:
        octal = str(n%8)+octal
        n = n//8
    return int(octal)
   
#Alternate method to convert to Octal
'''
def to_octal(n):
    return(oct(n).replace('0o',''))
'''
    

choice = int(input("Enter Number to Convert : "))
print(f'Binary = {to_binary(choice)}')
print(f'Hexa = {to_hexadecimal(choice)}')
print(f'Octal = {to_octal(choice)}')

