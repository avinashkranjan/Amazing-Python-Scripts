import random
import string
import csv
import progressbar
''' Ask user for total number of emails required'''


def getcount():
    rownums = input("How many email addresses?: ")
    try:
        rowint = int(rownums)
        return rowint
    except ValueError:
        print("Please enter an integer value")
        return getcount()


'''Below function creates a random length of email between 1-20 characters length and adds domain and extension to give the resulting email'''


def makeEmail():
    extensions = ['com', 'net', 'org', 'gov']
    domains = [
        'gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail',
        'outlook', 'frontier'
    ]

    finalext = extensions[random.randint(0, len(extensions) - 1)]
    finaldom = domains[random.randint(0, len(domains) - 1)]

    accountlen = random.randint(1, 20)

    finalacc = ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(accountlen))

    finale = finalacc + "@" + finaldom + "." + finalext
    return finale


# Take the total count of emails and pass them to getcount()
howmany = getcount()

# counter for While loop
counter = 0

# empty array to add emails
emailarray = []

print("Creating email addresses...")
print("Progress: ")

prebar = progressbar.ProgressBar(maxval=int(howmany))

for i in prebar(range(howmany)):
    while counter < howmany:
        emailarray.append(str(makeEmail()))
        counter += 1
        prebar.update(i)

print("Creation completed.")

for i in emailarray:
    print(i)
