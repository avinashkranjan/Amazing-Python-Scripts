# how to get transpose of a matrix.
# A normal coder may require some loops to get transpose but using ZIP function we can have it as one liner.
# Know the Basic Usage of the Zip Function
# The zip function aggregates items from different iterables, such as lists, tuples or sets, and returns an iterator.It works just like a physical zip.
# In fact, the zip function in Python is much powerful than a physical zipper. It can deal with any number of iterables at once rather than just two.
# Unfortunately, Python doesn’t have an unzip function. However, if we are familiar with the tricks of asterisks, unzipping is a very simple task.
# In the above example, the asterisk did the unpacking operation, which is unpacking all the four tuples from the record list.

# main code
matrix = [[1, 2, 3], [1, 2, 3]]  # the inputted matrix
# one liner code for taking transpose of matrix
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)  # print to validate
