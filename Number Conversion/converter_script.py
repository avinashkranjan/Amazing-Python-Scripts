class Definations:
    '''Contains the actual logic for base conversion.

    Parent class to Converter class
    '''
    def __init__(self,number):
        self.number = number
    def Decimal_to_Binary(self):
        return bin(int(self.number))[2:]
    def Binary_to_Decimal(self):
        return int(str(self.number),2)
    def Decimal_to_Octal(self):
        return oct(int(self.number))[2:]
    def Octal_to_Decimal(self):
        return int(str(self.number),8)
    def Decimal_to_Hexadecimal(self):
        return hex(self.number)[2:]
    def Hexadecimal_to_Decimal(self):
        return int(str(self.number),16)
    def Hexadecimal_to_Binary(self):
        num = int(str(self.number),16)
        return bin(num)[2:]
    def Hexadecimal_to_Octal(self):
        num = int(str(self.number),16)
        return oct(num)[2:]
    def Binary_to_Octal(self):
        num = int(str(self.number),2)
        return oct(num)[2:]
    def Binary_to_Hexadecimal(self):
        num = int(str(self.number),2)
        return hex(num)[2:]
    def Octal_to_Hexadecimal(self):
        num = int(str(self.number),8)
        return hex(num)[2:]
    def Octal_to_Binary(self):
        num = int(str(self.number),8)
        return bin(num)[2:]

class Converter(Definations):
    '''Inherits the Definations Class and converts the number based on user input'''
    def __init__(self,number):
        super().__init__(number)
    def convert(self,FROM="d",TO="b"):
        '''
        By Default conversion takes place from decimal to binary.
        specify the FROM and TO parameters from the following:
        d-decimal,
        b-binary,
        x-hexadecimal,
        o-octal
        '''
        bases = {'d':"DECIMAL",'b':"BINARY",'x':'HEXADECIMAL','o':"OCTAL"} 
        if FROM == 'd':
            if TO == 'b':
                ans = Definations.Decimal_to_Binary(self)
            elif TO == 'x':
                ans = Definations.Decimal_to_Hexadecimal(self)
            elif TO == 'o':
                ans = Definations.Decimal_to_Octal(self)
        if FROM == 'b':
            if TO == 'd':
                ans = Definations.Binary_to_Decimal(self)
            elif TO == 'x':
                ans = Definations.Binary_to_Hexadecimal(self)
            elif TO == 'o':
                ans = Definations.Binary_to_Octal(self)
        if FROM == 'x':
            if TO == 'b':
                ans = Definations.Hexadecimal_to_Binary(self)
            elif TO == 'd':
                ans = Definations.Hexadecimal_to_Decimal(self)
            elif TO == 'o':
                ans = Definations.Hexadecimal_to_Octal(self)
        if FROM == 'o':
            if TO == 'b':
                ans = Definations.Octal_to_Binary(self)
            elif TO == 'd':
                ans = Definations.Octal_to_Decimal(self)
            elif TO == 'x':
                ans = Definations.Octal_to_Hexadecimal(self)
        return f"\n{self.number} in {bases[FROM]} = {ans} in {bases[TO]}"

def header_decoration():
    print('''
    -------------- WELCOME TO NUMBER CONVERTER --------------
    -------------- --------------------------- --------------
    ''')
def footer_decoration():
    print('''
    -------------- --------------------------- -----------
    ''')
    
header_decoration()
Num = Converter(input("Enter number = "))
print(Num.convert(input("From = "),input("To = ")))
footer_decoration()