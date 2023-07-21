''' SETS 
    Sets are a collection of unordered elements that are unique.
'''

set = {1, 2, 1, 4, 'A', 'B', 'A', 5}

print(f"All the Unique elements of Set are {set}", end="\n\n")


''' ADDING ELEMENTS '''

print("**********Adding Elements**********", end="\n\n")

set.add('Z')

print(f"Set after adding Z is {set}", end="\n\n")

''' 
Set Operations 
    The union() function combines the data present in both sets.
    The intersection() function finds the data present in both sets only.
    The difference() function deletes the data present in both and outputs data present only in the set passed.
    The symmetric_difference() does the same as the difference() function but outputs the data which is remaining in both sets.
'''

print("**********Set Operations**********", end="\n\n")

set = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6, 'B'}

print("UNION ", set.union(set_2), '----------', set | set_2, end="\n\n")

print("INTERSECTION ", set.intersection(set_2),
      '----------', set & set_2, end="\n\n")

print("DIFFERENCE ", set.difference(set_2),
      '----------', set - set_2, end="\n\n")

print("SYMMETRIC-DIFFERENCE ", set.symmetric_difference(set_2),
      '----------', set ^ set_2, end="\n\n")

set.clear()

print(f"Deleted all elements of set {set}", end="\n\n")
