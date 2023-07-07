''' 
LISTS
    A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements

Advantage of List over Linked List:
    Elements can be accessed through their index value

BigO of Array:
    Indexing -----> O(1)
    Insert/Delete element at Start -----> O(n)
    Insert/Delete element at End -----> O(1)
    Insert element at Middle -----> O(n)
'''

# Empty List
list = []
print(f"This is an Empty List: {list}\n")

# List with Elements
list = [1, 2, 3.1, "A"]
print(f"Elements of the list are: {list}\n")


''' Adding elements '''

print("**********Adding Elements**********", end="\n\n")

# add as a single element
list.append(["B", 4])
print("Appended List ", list, end="\n\n")

# add as different elements
list.extend([5, 'E'])
print("Entended List ", list, end="\n\n")

# add element at 1st Index
list.insert(0, 0)
list.insert(5, "F")
print("Inserted Element ", list, end="\n\n")


''' Deleting Elements '''

print("**********Deleting Elements**********", end="\n\n")
# delete element at index 5
del list[5]
print("Deleted element ", list, end="\n\n")

# remove element with value '<val>'
list.remove('E')
print("Removed element ", list, end="\n\n")

# pop element from list at i^th index
a = list.pop(1)
print('Popped Element: ', a, ' List remaining: ', list, end="\n\n")

# empty the list
list.clear()
print("Empty List ", list, end="\n\n")


''' Accessing Elements '''

print("**********Accessing Elements**********", end="\n\n")

list = [1, 2, 3.5, "A", True]
print("This is new list ", list, end="\n\n")

# access elements one by one
print("Accessing all Elements one by one\n")
for element in list:
    print(element, end="\n")

# access all elements
print("\nAccessing all elements\n")
print(list, end="\n\n")

# access index i element
print("Element at index=2 is", list[2], end="\n\n")

# access elements from 0 to 1 and exclude 2
print("Elements from index(0 to 1) are ", list[0:2], end="\n\n")

# access elements in reverse
print("Elements in reverse order ", list[::-1], end="\n\n")


''' 
Other Functions 
    len() : returns length of the list.
    index() : finds index value of value passed where it has been encountered the first time.
    count()  : finds count of the value passed to it.
    sorted() and sort() : to sort the values of the list. 
    sorted() has a return type whereas the sort() modifies the original list.
'''

print("**********Other Functions**********", end="\n\n")

list = [1, 2, 3, 10, 20, 50]

# find length of list
print("No of elements in the list ", len(list), end="\n\n")

# find index of element that occurs first
print("Index of element 20 is ", list.index(20), end="\n\n")

# find count of the element
print(f"Elements has been repeated {list.count(10)} time", end="\n\n")

# print sorted list but not change original
print("Sorted list is [AESC] ", sorted(list), end="\n\n")

# sort original list
list.sort(reverse=True)
print("Sorted list is [DESC]", list, end="\n\n")
