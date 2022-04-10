#-----1. Scope and user-defined functions
# Crash course on scope in functions
    # Not all objects are accessible everywhere in a script
    # Scope - part of the program where an object or name may be accessible
        # Global scope - de,ned in the main body of a script
        # Local scope - de,ned inside a function
        # Built-in scope - names in the pre-de,ned built-ins module

# Global vs. local scope (2)
import pandas as pd

new_val = 10
def square(value):
    """Returns the square of a number."""
    new_val = value ** 2
    return new_val
print(square(3))  # 9
#  In short, any time we call the name in the global scope, it will access the name in the global,
#  such as you see here. Any time we call the name in the local scope of the function, it will look
#  first in the local scope. That's why calling square(3) results in 9 and not 10. If Python cannot
#  find the name in the local scope, it will then and only then look in the global scope.

# Global vs. local scope (3)
new_val = 10
def square(value):
    """Returns the square of a number."""
    new_value2 = new_val ** 2
    return new_value2
print(square(3))  # 100
new_val = 20
print(square(3))  # 200

# Global vs. local scope (4)
new_val = 10
def square(value):
    """Returns the square of a number."""
    global new_val
    new_val = new_val ** 2
    return new_val
print(square(3))  # 100
print(new_val)  # 100
#------------------------------
## Pop quiz on understanding scope
num = 5
def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)
func1()  # 3
func2()  # 10
print(num)  # 6

## The keyword global
# Create a string: team
team = "teen titans"
# Define change_team()
def change_team():
    """Change the value of the global variable team."""
    # Use team in global scope
    global team
    # Change the value of team in global scope to the string "justice league": team
    team = "justice league"
print(team)  # teen titans
change_team()
print(team)  # justice league

import builtins
print(dir(builtins))  # print a list of all the names in the module builtins

#-----2. Nested functions
# Nested functions (3)
def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""
    def inner(x):
        """Returns the remainder plus 5 of a value."""
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))
print(mod2plus5(1, 2, 3))  # (6, 5, 6)

# Returning functions
def raise_val(n):
    """Return the inner function."""
    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised
    return inner
square = raise_val(2)
cube = raise_val(3)
print(square(2), cube(4))  # 4 64

#Using nonlocal
def outer():
    """Prints the value of n."""
    n = 1
    def inner():
        nonlocal n
        n = 2
        print(n)
    inner()  # 2
    print(n)  # 2
outer()
#------------------------------
## Nested Functions I
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings concatenated with '!!!'."""
    # Complete the function header of the nested function with the function name
    # inner() and a single parameter word.
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # Complete the return value: each element of the tuple should be a call to inner(),
    # passing in the parameters from three_shouts() as arguments to each call.
    return (inner(word1), inner(word2), inner(word3))
# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))  # ('a!!!', 'b!!!', 'c!!!')

## Nested Functions II
# Define echo
def echo(n):
    """Return the inner_echo function."""
    # Complete the function header of the inner function with the function name
    # inner_echo() and a single parameter word1.
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    # Complete the function echo() so that it returns inner_echo.
    return inner_echo
# Call echo: twice
twice = echo(2)
# Call echo: thrice
thrice = echo(3)
# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))  # hellohello hellohellohello

## The keyword nonlocal and nested functions
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    # Print echo_word
    print(echo_word)  # hellohello
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    # Call function shout()
    shout()
    # Print echo_word
    print(echo_word)  # hellohello!!!
# Call function echo_shout() with argument 'hello'
echo_shout('hello')

#-----3. Default and flexible arguments
## Add a default argument
def power(number, pow=1):
    """Raise number to the power of pow."""
    new_value = number ** pow
    return new_value
power(9, 2)  # 81
power(9)  # 9

# Flexible arguments: *args (1)
def add_all(*args):
    """Sum all values in *args together."""
    # Initialize sum
    sum_all = 0
    # Accumulate the sum
    for num in args:
        sum_all += num
    return sum_all
add_all(1, 2)  # 2
add_all(5, 10, 15, 20)  # 50

# Flexible arguments: **kwargs
def print_all(**kwargs):
    """Print out key-value pairs in **kwargs."""
    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)
print_all(name="dumbledore", job="headmaster")  # name: dumbledore / job: headmaster
#------------------------------

## Functions with one default argument
# Define shout_echo. It accepts an argument word1 and a default argument echo with default value 1, in that order.
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")
# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", echo=5)
# Print no_echo and with_echo
print(no_echo)  # Hey!!!
print(with_echo)  # HeyHeyHeyHeyHey!!!

## Functions with multiple default arguments
# # Complete the function header with the function name shout_echo. It accepts an argument word1,
# a default argument echo with default value 1 and a default argument intense with default value False
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # Return echo_word_new
    return echo_word_new
# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo=5, intense=True)
# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)
# Print with_big_echo and big_no_echo
print(with_big_echo)
print(big_no_echo)

## Functions with variable-length arguments (*args)
# Complete the function header with the function name gibberish. It accepts a single flexible argument *args.
def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge = ''
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge
# Call gibberish() with the single string, "luke".: one_word
one_word = gibberish("luke")
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")
# Print one_word and many_words
print(one_word)  # luke
print(many_words)  # lukeleiahanobidarth

# Functions with variable-length keyword arguments (**kwargs)
# Complete the function header with the function name report_status.
# It accepts a single flexible argument **kwargs.
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)  # name: anakin / affiliation: sith lord / status: deceased
    print("\nEND REPORT")
# In the first call to report_status(), pass the following keyword-value pairs: name="luke",
# affiliation="jedi" and status="missing".
report_status(name="luke", affiliation="jedi", status="missing")
# In the second call to report_status(), pass the following keyword-value pairs: name="anakin",
# affiliation="sith lord" and status="deceased".
report_status(name="anakin", affiliation="sith lord", status="deceased")

## Bringing it all together (1)
tweets_df = pd.read_csv('tweets.csv')
# Complete the function header by supplying the parameter for a DataFrame df and the parameter col_name with a default value of 'lang' for the DataFrame column name.
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
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
# Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1. Note that since 'lang' is the default value of the col_name parameter, you don't have to specify it here.
result1 = count_entries(tweets_df, col_name='lang')
# Call count_entries() by passing the tweets_df DataFrame and the column name 'source'. Assign the result to result2.
result2 = count_entries(tweets_df, col_name='source')
# Print result1 and result2
print(result1)
print(result2)

## Bringing it all together (2)
# Complete the function header by supplying the parameter for the DataFrame df and the flexible argument *args.
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Complete the for loop within the function definition so that the loop occurs over the tuple args.
    for col_name in args:
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
# Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1.
result1 = count_entries(tweets_df, 'lang')
# Call count_entries() by passing the tweets_df DataFrame and the column names 'lang' and 'source'. Assign the result to result2.
result2 = count_entries(tweets_df, 'lang', 'source')
# Print result1 and result2
print(result1)
print(result2)