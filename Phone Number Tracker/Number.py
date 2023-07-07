# pip install phonenumbers in cmd

# importing phonenumbers module
import phonenumbers

# calling timezone,geocoder and carrier from phonenumbers module
from phonenumbers import timezone, geocoder, carrier

# taking phone number as input from user
number = input("Enter your number (with +91): ")

# parse the string input to phonenumber format
phone = phonenumbers.parse(number)

# to get the timezone of a user
time = timezone.time_zones_for_number(phone)

# Getting carrier of a phone number
car = carrier.name_for_number(phone, "en")

# Getting region information
reg = geocoder.description_for_number(phone, "en")

# printing the details
print("Details :")
print(phone)
print(time)
print(car)
print(reg)
