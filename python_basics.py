print("Intro to Python")
# Comment - do not execute
# to comment 
# multiple lines, highlite the
# lines and ctrl /

# Case sensitive
# Extra spaces do not matter around commands, operators
# Spaces DO matter in indentation (code blocks).
# Strings can use "" OR ''. BE CONSISTENT
print("Hello World")
print('Hello World')
#"" is more common
# print ('Let's have a groovy day!')
print("Let's have a groovy day!")

# Escape characters/sequences - provide a way to perform an action in a string
print("It's a \"groovy\" day")
print('It\'s a "groovy" day')
print("Hello\nWorld") # New line
print("Name:\tShane") # Tab
print("To go to a new line in a string use \\n")

# Variables
# A named box that holds value
# value can change
# names contain only letters, numbers, and _ and cannot start with a number
# use snake_case
# We do not need to declare/create them before use
# cannot be named keywords

# examples of assigning values to variables
first_name = "Shane" # String
age = 54 # integer
price = 12.54 # float
is_valid = True # Boolean

# Using variables with strings
# string contatonation
# + is string contatonation operator in Python
print("Welcome " + first_name)

# To use + with non strings you must cast the variables to strings
print("You are " + str(age) + " years old")

# use a , instead of + and datatype does matter
print("You are",age,"years old")

# preferred way (format strings)
print(f"Hello {first_name}! You are {age} years old")

# Constants - Like a variable but its value must stay the same
# use SCREAMING_SNAKE_CASE
# gives a name to a value
# if the value of the constant changes, everywhere it is used also changes
GST_RATE = 0.04
gst = 100 * GST_RATE










 





