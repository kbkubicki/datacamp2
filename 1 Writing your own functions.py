#-----1. User-defined functions
# Defining a function
def square(): # <- Function header
    new_value = 4 ** 2 # <- Function body
    print(new_value)
square()

# when you define a function, you write parameters in the function header.
# When you call a function, you pass arguments into the function.

# Docstrings
# Docstrings describe what your function does
# Serve as documentation for your function
# Placed in the immediate line a/er the function header
# In between triple double quotes """
def square(value):
    """Return the square of a value."""
    new_value = value ** 2
    return new_value
square(4)
#------------------------------
# Recapping built-in functions
x = 3.45
y2 = print(x)  # <class 'NoneType'>
# It is important to remember that assigning a variable y2 to a function that prints a value
# but does not return a value will result in that variable y2 being of type NoneType.

#-----2. Multiple parameters and return values
## A quick jump into tuples / krotki
# Make functions return multiple values: Tuples!
# Tuples:
    # Like a list - can contain multiple values
    # Immutable - can’t modify values!
    # Constructed using parentheses ()
even_nums = (2, 4, 6)

# Returning multiple values
def raise_both(value1, value2):
    """Raise value1 to the power of value2
    and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_both(2, 3)
print(result)
#------------------------------
#-----3. Bringing it all together
# Basic ingredients of a function
# Function Header
def raise_both(value1, value2):
    # Function body
    """Raise value1 to the power of value2
    and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple
#------------------------------
import pandas as pd
df = pd.read_csv('tweets.csv')
# Initialize an empty dictionary: langs_count
langs_count = {}
# Extract column from DataFrame: col
col = df['lang']
# Iterate over lang column in DataFrame
for entry in col:
    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
# Print the populated dictionary
print(langs_count)  # {'en': 97, 'et': 1, 'und': 2}

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    langs_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1
    # Return the langs_count dictionary
    return langs_count
# Call count_entries(): result
result = count_entries(df, 'lang')
# Print the result
print(result)