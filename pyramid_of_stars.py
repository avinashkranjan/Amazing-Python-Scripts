# Program to print a centered full pyramid of stars based on user input

def get_positive_int(prompt: str) -> int:
    """Prompt the user until they provide a positive integer (> 0)."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Please enter a positive integer greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def draw_pyramid(rows: int) -> None:
    """Print a centered full pyramid of stars with the given number of rows."""
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '* ' * i
        # rstrip to avoid trailing space at line end
        print(f"{spaces}{stars.rstrip()}")


def main() -> None:
    rows = get_positive_int("Enter the number of rows: ")
    draw_pyramid(rows)


if __name__ == "__main__":
    main()
