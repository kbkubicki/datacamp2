#-----1. User-defined functions
# There's a quicker way to write functions on the fly and these are called lambda functions
# because you use the keyword lambda.
raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3)

# Anonymous functions
    # Function map takes two arguments: map(func, seq)
    # map() applies the function to ALL elements in the sequence
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(square_all)  # <map object at 0x015FB890>
print(list(square_all))  # print(list(square_all))
#------------------------------
# How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?
# How would you call add_bangs with the argument 'hello'?
add_bangs = lambda x: x + "!!!"
print(add_bangs('hello'))

## Writing a lambda function you already know
echo_word = (lambda x, y: x * y)
result = echo_word('hey', 5)
print(result)

## Map() and lambda functions
nums = [2, 4, 6, 8, 10]
result = map(lambda a: a ** 2, nums)
print(result)  # <map object at 0x01E6BDF0>
print(list(result))  # [4, 16, 36, 64, 100]

spells = ["protego", "accio", "expecto patronum", "legilimens"]
# Use map() to apply a lambda function over spells: shout_spells
# In the map() call, pass a lambda function that concatenates the string '!!!'
# to a string item; also pass the list of strings, spells.
shout_spells = map(lambda x: x + '!!!', spells)
# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
print(shout_spells_list)

## Filter() and lambda functions
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# In the filter() call, pass a lambda function and the list of strings, fellowship. The lambda function should
# check if the number of characters in a string member is greater than 6; use the len() function to do this.
result = filter(lambda x: len(x) > 6, fellowship)
# Convert result to a list: result_list
result_list = list(result)
print(result_list)

## Reduce() and lambda functions
def gibberish(*args):
    """Concatenate strings in *args together."""
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge
print(gibberish('1', '2', '3'))
# gibberish() simply takes a list of strings as an argument and returns, as a single-value result,
# the concatenation of all of these strings. In this exercise, you will replicate this functionality
# by using reduce() and a lambda function that concatenates strings together.
# Import reduce from functools
from functools import reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
# In the reduce() call, pass a lambda function that takes two string arguments item1 and item2 and
# concatenates them; also pass the list of strings, stark. Assign the result to result. The first argument
# to reduce() should be the lambda function and the second argument is the list stark.
result = reduce(lambda item1, item2: item1 + item2, stark)
print(result)

#-----2. Introduction to error handling
# Errors and exceptions
def sqrt(x):
    """Returns the square root of a number."""
    try:
        return x ** 0.5
    except:
        print('x must be an int or float')
    sqrt(4)

def sqrt(x):
    """Returns the square root of a number."""
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')
#------------------------------

## Error handling with try-except
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    return shout_words
shout_echo("particle", echo="accelerator")

## Error handling by raising an error
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Raise an error with raise
    # Complete the if statement by checking if the value of echo is less than 0.
    # In the body of the if statement, add a raise statement that raises a ValueError with message 'echo must be greater than or equal to 0' when the value supplied by the user to echo is less than 0.
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    return shout_word
shout_echo("particle", echo=5)

#-----3. Bringing it all together

## Bringing it all together (1)
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the Twitter DataFrame: result
# In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text'].
# The lambda function should check if the first 2 characters in a tweet x are 'RT'. Assign the resulting
# filter object to result. To get the first 2 characters in a tweet x, use x[0:2]. To check equality,
# use a Boolean filter with ==.
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])
# Create list from filter object result: res_list
res_list = list(result)
# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

## Bringing it all together (2)
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        # Iterate over the column in DataFrame
        for entry in col:
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
        # Return the cols_count dictionary
        return cols_count
    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')
result1 = count_entries(tweets_df, 'lang')
print(result1)

## Bringing it all together (3)

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Raise a ValueError if col_name is NOT in DataFrame
    # If col_name is not a column in the DataFrame df, raise a ValueError
    # 'The DataFrame does not have a ' + col_name + ' column.'
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over the column in DataFrame
    for entry in col:
        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        # Return the cols_count dictionary
    return cols_count
result1 = count_entries(tweets_df, 'lang')
print(result1)