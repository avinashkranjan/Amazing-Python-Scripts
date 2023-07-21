import re
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # username
    @                               # @ symbol
     [a-zA-Z0-9.-]+           # domain name
     (\.[a-zA-Z]{2,4})         # dot-something
  )''', re.VERBOSE)

# store matched addresses in an array called "matches"
matches = []
text = """
An example text containing an email address, such as user@example.com or something like hello@example.com
"""

# search the text and append matched addresses to the "matches" array
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# matches => ['user@example.com', 'hello@example.com']
print(matches)
