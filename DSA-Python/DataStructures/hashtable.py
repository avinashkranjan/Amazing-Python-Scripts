"""
LookUp by key -----> O(1)
Insertion/Deletion -----> O(1)

Classes to implement HashTable in different languages:
Python :: dictionary
Java :: HashMap
Java :: Linked HashMap
C++ :: std::map
"""


class HashTable():
    """
    In class hashTable, an array of size '100' is created which is initialised using list_comprehension; val in each
    element is None
    """

    def __init__(self):
        self.MAX = 100  # size of array = 100
        self.arr = [None for i in range(self.MAX)]  # list-comprehension

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # returns ASCII val of char
        return h % self.MAX  # hash: Sum(ASCII_Values(key)) % size(array)

    def add(self, key, val):
        h = self.get_hash(key)  # retrieving hash function
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()  # object of class HashTable
q = t.add('Google', 120)
r = t.get('Google')
# s = t.arr  # to get full array
# m = t.delete('Google')  # delete element by key
# n = t.arr  # to get full array after deleting
print(r)

# todo Collision Handling
# Collision Handling: When one or more elements are assigned the same hash

s = t.add('Google', 121)
z = t.get('Google')
print(z)
