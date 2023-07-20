from datetime import date


def calculate_age(birthday):
    today = date.today()

    # Check if the birthdate is in the future
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    day_check = ((today.month, today.day) < (birthday.month, birthday.day))
    year_diff = today.year - birthday.year - day_check
    remaining_months = abs((12-birthday.month)+today.month)
    remaining_days = abs(today.day - birthday.day)

    # Return the age as a formatted string
    age_string = f"Age: {year_diff} years, {remaining_months} months, and {remaining_days} days"
    return age_string


if __name__ == "__main__":
    print(" Age Calculator By Python")

    try:
        birthYear = int(input("Enter the birth year: "))
        birthMonth = int(input("Enter the birth month: "))
        birthDay = int(input("Enter the birth day: "))
        dateOfBirth = date(birthYear, birthMonth, birthDay)
        age = calculate_age(dateOfBirth)
        print(age)
    except ValueError:
        print("Invalid input. Please enter valid integers for the year, month, and day.")
