def generate_table(number):
    """
    Generates and prints a multiplication table for a given number.

    Parameters:
        number (int): The number up to which the multiplication table will be generated.

    Returns:
        None
    """
    if number <= 0:
        print("Please enter a positive number")
        return
    # print heading
    print("Multiplication table upto", number, "\n")
    print("    ", end="")
    # print header row
    for i in range(1, number+1):
        print(f"{i:4}", end="")
    print("\n" + " "*4 + "-"*(number*4))
    # print table cells
    for i in range(1, number+1):
        print(f"{i:2} |", end="")
        for j in range(1, number+1):
            result = i*j
            print(f"{result:4}", end="")
        print()


if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        generate_table(num)
    except ValueError:
        print("Invalid number. Please enter a positive integer.")
