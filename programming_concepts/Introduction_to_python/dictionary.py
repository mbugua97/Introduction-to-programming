# Dictionaries in Python

# Dictionaries are mutable, unordered collections of items in the form of key-value pairs.
# Syntax:
# dictionary_name = {
#     "key1": "value1",
#     "key2": "value2",
#     ...
# }

# Creating Dictionaries
# - A dictionary can be created with braces `{}` containing key-value pairs separated by commas.
# - Keys must be unique and can be of immutable types (e.g., strings, numbers).
# - Values can be of any data type.

# Accessing Dictionary Elements
# - Dictionary values are accessed by using the key in square brackets (dictionary_name[key]).
# - Attempting to access a non-existent key raises a KeyError, so using `.get()` can be safer.

# Nested Dictionaries
# - Dictionaries can contain other dictionaries, making them suitable for representing hierarchical data.
# - Access nested elements by chaining keys (e.g., dictionary["key1"]["nested_key"]).

# Modifying a Dictionary
# - Add or update items by assigning a value to a key (dictionary[key] = value).
# - If the key exists, the value will be updated; if not, a new key-value pair is added.

# Removing Items from a Dictionary
# - Use `del dictionary[key]` to remove an item by key.
# - `pop(key)` removes and returns the value of the specified key. If the key is not found, an optional default can be specified.
# - `popitem()` removes and returns the last inserted key-value pair (useful in Python 3.7+).

# Dictionary Methods
# - `items()`: Returns a view object that displays all key-value pairs as tuples.
# - `values()`: Returns a view object displaying all values in the dictionary.
# - `copy()`: Creates a shallow copy of the dictionary, allowing modifications without affecting the original.

# Best Practices for Working with Dictionaries
# - Keep key types consistent to avoid confusion.
# - Use descriptive, meaningful keys to make the dictionary self-explanatory.
# - Handle missing keys gracefully by using `.get(key, default_value)` when accessing items.

# Example of an empty dictionary for reference:
# empty_dict = {}

# This provides a quick overview of dictionary fundamentals for efficient and effective usage in Python.
