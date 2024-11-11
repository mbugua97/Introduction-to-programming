# Tuples in Python

# Tuples are ordered collections of elements and are immutable, meaning their contents cannot be changed once created.
# They are useful for grouping data that should remain constant, like coordinates or fixed configurations.

# Creating a Tuple
# - Tuples are defined using parentheses `()`.
# - Tuples can hold elements of any data type (e.g., integers, strings, floats, other tuples).
# - Tuples with only one element require a trailing comma (e.g., single_elemnt_tuple = (42,)).

# Example: 
# my_tuple = (1, 2, 3, 4, "apple", 4.7, True, ("ugali", "chapo"))
# empty_tuple = ()

# Accessing Tuple Elements
# - Elements in a tuple can be accessed by their index, starting at 0.
# - Negative indexing is also supported (e.g., -1 accesses the last element).
# - Slicing can retrieve parts of a tuple without modifying the original.

# Modifying Tuples
# - Tuples are immutable, so elements cannot be added, removed, or changed directly.
# - However, you can concatenate tuples to create a new tuple with additional elements (e.g., new_tuple = my_tuple + (9,)).

# Counting Occurrences
# - `.count(value)`: Returns the number of times a specified value appears in the tuple.

# Finding an Index
# - `.index(value)`: Returns the index of the first occurrence of a specified value.
#   Raises a ValueError if the value is not found in the tuple.

# Summary:
# Tuples are an efficient and convenient way to handle collections of items that should remain constant.
# They support indexing, slicing, and basic methods like `count` and `index` for analyzing their contents.
