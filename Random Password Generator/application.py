
import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
digits = "0123456789"
symbols = "!@#"
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += upper_case
if lower:
    all += lower_case
if nums:
    all += digits
if syms:
    all += symbols

length = 5
amount = 5

for x in range(amount):
    password = "".join(random.sample(all, length))
    print("Some Passwords for you to try: "+password)
