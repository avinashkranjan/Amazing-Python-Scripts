# decimal to hexa decimal converter
if __name__ == "__main__":
    print('decimal to hexa-decimal converter using python')

    def decimal_to_hexadecimal():
        try:
            decimal_input = int(input("Enter a decimal number: "))
            hexadecimal_output = hex(decimal_input)
            return hexadecimal_output
        except ValueError:
            raise ValueError(
                "Invalid input. Please enter a valid decimal number.")
try:
    hexadecimal_number = decimal_to_hexadecimal()
    print(hexadecimal_number)
except ValueError as e:
    print(str(e))
