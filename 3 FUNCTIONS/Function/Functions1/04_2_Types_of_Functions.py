
#! filter() function:
# We can use filter() function to filter values from the given sequence based on some
# condition.

# filter(function, sequence)
# where function argument is responsible to perform conditional check
# sequence can be list or tuple or string.


#! map() function:
# For every element present in the given sequence, apply some functionality and generate 
# new element with the required modification. For this requirement we should go for
# map() function.

# Eg: For every element present in the list perform double and generate new list of doubles.

# Syntax:

# map(function, sequence)
# The function can be applied on each element of sequence and generates new sequence.
# We can apply map() function on multiple lists also.But make sure all list should have same
# length.

# Syntax: map(lambda x, y: x*y, l1, l2))
#     x is from l1 and y is from l2

#! reduce() function:
# reduce() function reduces sequence of elements into a single element by applying the
# specified function.

# reduce(function, sequence)

# reduce() function present in functools module and hence we should write import
# statement.


#! Function Aliasing:
# For the existing function we can give another name, which is nothing but function aliasing.


# Note: In the above example only one function is available but we can call that function by using
# either wish name or greeting name.
# If we delete one name still we can access that function by using alias name


