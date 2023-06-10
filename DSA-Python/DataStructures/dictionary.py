''' 
DICTIONARY
    Dictionaries are used to store key-value pairs which are mutable, or changeable, and ordered.
'''

#empty dictionary
dict = {} 
print("This is an empty Dictionary ", dict, end="\n\n")

#dictionary with elements
dict = {
    1: 'Python', 'Two': 'Java', 3: 'Swift',
    } 
print("Elements of dictionary are \n", dict, end="\n\n")


''' Adding Elements '''

print("**********Adding Elements**********")

#changing element
dict[3] = 'C++' 
print(f"Changed 3rd element \n {dict}", end="\n\n")

#adding key-value pair
dict['Fourth'] = 'Swift' 
print("Added element \n", dict, end="\n\n")


''' Accessing Elements '''

print("**********Accessing Elements**********")

#access elements using keys
print("First element is ", dict[1], end="\n\n") 
print("Fourth Element is ", dict.get('Fourth'), end="\n\n")

#get keys
print(f"Keys of the dictionary are \n{dict.keys()}", end="\n\n") 

#get values
print(f"Values of the dictionary are \n{dict.values()}", end="\n\n") 

#get key-value pairs
print(f"Dictionary is \n{dict.items()}", end="\n\n") 


''' Deleting Elements '''

print("**********Deleting Elements**********")

#pop element
a = dict.pop('Fourth') 
print(f"Deleted {a} \nNew dictionary {dict}", end="\n\n")

#pop the key-value pair
b = dict.popitem() 
print(f"Popped {b} \nNew dictionary {dict}", end="\n\n")

#empty dictionary
dict.clear() 
print(f"Cleared dictionary {dict}", end="\n\n")

