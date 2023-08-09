import sys


class Definations:
    '''Contains the actual logic for base conversion.

    Parent class to Converter class
    '''

    def __init__(self, number):
        self.number = number

    def Decimal_to_Binary(self):
        return bin(int(self.number))[2:]

    def Binary_to_Decimal(self):
        return int(str(self.number), 2)

    def Decimal_to_Octal(self):
        return oct(int(self.number))[2:]

    def Octal_to_Decimal(self):
        return int(str(self.number), 8)

    def Decimal_to_Hexadecimal(self):
        return hex(self.number)[2:]

    def Hexadecimal_to_Decimal(self):
        return int(str(self.number), 16)

    def Hexadecimal_to_Binary(self):
        num = int(str(self.number), 16)
        return bin(num)[2:]

    def Hexadecimal_to_Octal(self):
        num = int(str(self.number), 16)
        return oct(num)[2:]

    def Binary_to_Octal(self):
        num = int(str(self.number), 2)
        return oct(num)[2:]

    def Binary_to_Hexadecimal(self):
        num = int(str(self.number), 2)
        return hex(num)[2:]

    def Octal_to_Hexadecimal(self):
        num = int(str(self.number), 8)
        return hex(num)[2:]

    def Octal_to_Binary(self):
        num = int(str(self.number), 8)
        return bin(num)[2:]


class Converter(Definations):
    '''Inherits the Definations Class and converts the number based on user input'''

    def __init__(self, number):
        super().__init__(number)

    def helper(self, func_name):
        return getattr(Definations, func_name)(self)

    def convert(self, FROM="d", TO="b"):
        '''
        By Default conversion takes place from decimal to binary.
        specify the FROM and TO parameters from the following:
        d-decimal,
        b-binary,
        x-hexadecimal,
        o-octal
        '''
        bases = {'d': "Decimal", 'b': "Binary",
                 'x': 'Hexadecimal', 'o': "Octal"}
        to_call_function = bases[FROM] + '_to_' + bases[TO]
        return f"\n{self.number} in {bases[FROM]} = {self.helper(to_call_function)} in {bases[TO]}"


def header_decoration():
    print('''
    -------------- WELCOME TO NUMBER CONVERTER --------------
    -------------- --------------------------- --------------
    ''')


def footer_decoration():
    print('''
    -------------- --------------------------- -----------
    ''')


if __name__ == '__main__':
    header_decoration()
    Num = Converter(input("Enter number = "))
    print(Num.convert(input("From = "), input("To = ")))
    footer_decoration()
