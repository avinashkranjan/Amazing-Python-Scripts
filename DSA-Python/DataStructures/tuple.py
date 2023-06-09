''' TUPLE
    A tuple is a collection which is ordered and unchangeable(immutable).
'''

''' Adding Elements '''
print("**********Adding Elements**********", end="\n\n")


tuple = (1, 2, 3, 'Alphabet') 
print(f"Tuple is {tuple}", end="\n\n") 


''' Accessing Elements '''
print("**********Accessing Elements**********", end="\n\n")


for x in tuple:
    print(f"Element of tuple is {x}")


print(f"\nGetting whole Tuple {tuple}", end="\n\n")

print(f"0th Elements of Tuple is {tuple[0]}", end="\n\n")

print(f"Can be accessed through ':' Operator {tuple[:]}", end="\n\n")

print(f"Reversed Tuple is {tuple[::-1]}", end="\n\n")

print(f"Letter-at-3-index of 3rd-Index-elements is {tuple[3][3]}", end="\n\n")


''' Appending Elements '''
print("**********Appending Elements**********", end="\n\n")


tuple = tuple + (4, 5, ['B', 'C']) #add elements
print(f"Tuple after appending elements is {tuple}", end="\n\n")
# (1, 2, 3, 'Alphabet', 4, 5, ['B','C'])


''' Other Functions '''
print("**********Other Functions**********", end="\n\n")


tuple[6][0] = 'K'
print(f"Changed 6th-index-element to K {tuple}", end="\n\n")

print(f"2 has been repeated {tuple.count(2)} time", end="\n\n")

print(f"Index of ['K','C'] is {tuple.index(['K', 'C'])}", end="\n\n")

