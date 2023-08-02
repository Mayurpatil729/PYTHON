# Numpy Data Types

How to get/access elements of Numpy Array:
There are 2 ways available to get/access elements of Numpy Array
1. Indexing
2. Slicing


1. Indexing:
1. By using index, we can access single element of the array.
2. Numpy follows zero based indexing. ie index of first element is always zero.
3. Numpy supports both positive indexing and negative indexing.
Syntax :
a[index] ---> Returns element present at specified index.
              Accessing elements from iD of array:



Accessing elements of Numpy Array By using slice operator:

By using index, we can access only one element at a time. But if we want to access
multiple elements then we should go for slice operator.

slice--->means part of nd array.

Slice operation on Python's List:

Slice operator on ID array:

Syntax :
arrayname[begin : end : step]

l[begin: end]--->lt returns elements from begin index to end-1 index.
l[:end]---> it returns elements from index to end-1 index.
l[begin:]---> it returns elements from begin index to last index.
l[:] ---> it returns complete list.

  
Default value for begin: 0
Default value for end: len(l)

step: The default value is 1


l[begin : end: step] ----> returns elements from begin index to end-I index by
considering step value.


Note :
1. For begin, end and step, we can take both positive and negative values.
2. If step value is positive, then we have to consider elements from
    begin to end-1 in forward direction. (left to right)
3. If the step value is negative, then we have to consider elements from begin to
    end+1 in backward direction. (right to left)
4. In forward direction if end value 0 then result always empty.
5. In backward direction if end value -1 then result always empty.



slice in 2d array
Syntax :
arrayname[ row, column]
arrayname[begin : end : step,  begin:end:step]
 
first slics ==> rows
second slice ==> columns


slice in 3d array
a[i,j,k]
Syntax:
i--->represents which 2-D array
j-->represents which rows in that 2-D array
k >represents which columns in that 2 -D array


a[begin:end:step,begin:end:step,begin:end:step]




















