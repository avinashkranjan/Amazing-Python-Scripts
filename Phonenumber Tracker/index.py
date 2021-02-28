import phonenumbers

# geocoder: to know the specific
# location to that phone number
from phonenumbers import geocoder

# carrier: to know the name of
# service provider of that phone number
from phonenumbers import carrier

phone_number = phonenumbers.parse("Enter phone number with country code")
# Indian phone number example: +91**********
# USA phone number example: +177**********

service_provider = phonenumbers.parse("Enter phone number with country code")
# Indian phone number example: +91**********
# USA phone number example: +177**********

# this will print the country's name
print(geocoder.description_for_number(phone_number, 'en'))
# this will print the service provider's name
print(carrier.name_for_number(service_provider, 'en'))
