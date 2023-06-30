
# importing the date module from the datetime package  
from datetime import date  
  
# defining a function calculate the age  
def calculate_age(birthday):  
  
    # using the today() to retrieve today's date and stored it in a variable  
    today = date.today()  
  
    # a bool representing if today's day, or month precedes the birth day, or month  
    day_check = ((today.month, today.day) < (birthday.month, birthday.day))  
  
    # calculating the difference between the current year and birth year  
    year_diff  = today.year - birthday.year  
  
    # The difference in years is not enough.  
    # We must subtract 0 or 1 based on if today precedes the   
    # birthday's month/day from the year difference to get it correct.      
    # we will subtract the 'day_check' boolean from 'year_diff'.  
    # The boolean value will be converted from True to 1 and False to 0 under the hood.  
    age_in_years = year_diff - day_check  
  
    # calculating the remaining months  
    remaining_months = abs(today.month - birthday.month)  
  
    # calculating the remaining days  
    remaining_days = abs(today.day - birthday.day)  
  
    # printing the age for the users  
    print("Age:", age_in_years, "Years", remaining_months, "Months and", remaining_days, "days")  
  
# main function  
if __name__ == "__main__":  
  
    # printing an opening statement  
    print("Simple Age Calculator")  
  
    # asking user to enter birth year, birth month, and birth date  
    birthYear = int(input("Enter the birth year: "))  
    birthMonth = int(input("Enter the birth month: "))  
    birthDay = int(input("Enter the birth day: "))  
  
    # converting integer values to date format using the date() method  
    dateOfBirth = date(birthYear, birthMonth, birthDay)  
  
    # calling the function to calculate the age of a person  
    calculate_age(dateOfBirth)  
from datetime import date

def calculate_age(birthday):
    today = date.today()

    # Check if the birthdate is in the future
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    day_check = ((today.month, today.day) < (birthday.month, birthday.day))
    year_diff = today.year - birthday.year - day_check
    remaining_months = abs(today.month - birthday.month)
    remaining_days = abs(today.day - birthday.day)

    # Return the age as a formatted string
    age_string = f"Age: {year_diff} years, {remaining_months} months, and {remaining_days} days"
    return age_string

if __name__ == "__main__":
    print("Simple Age Calculator")

    try:
        birthYear = int(input("Enter the birth year: "))
        birthMonth = int(input("Enter the birth month: "))
        birthDay = int(input("Enter the birth day: "))
        dateOfBirth = date(birthYear, birthMonth, birthDay)
        age = calculate_age(dateOfBirth)
        print(age)
    except ValueError:
        print("Invalid input. Please enter valid integers for the year, month, and day.")

