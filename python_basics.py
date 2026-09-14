print("Intro to Python")
# Comment - does not execute
# Describes your code for others

# Multi lines 
# comment Use 
# ctrl /

# Case sensitive
# Extra spaces in your code do not usually matter
# Strings can use "" OR ''
print("Hello")
print('Hello')

print("Let's go crazy")
# print('Let's go crazy')

# Escape character/sequences - provide a way to perform an action IN a string
print("It's a \"groovy\" day")
print('It\'s a "groovy" day')
print("Hello\nWorld") # New line
print("Name:\tShane") # Tab

print("To go to a new line in a string use \\n")

# Variables
# a named box that holds a value
# value can change
# use snake_case for the names
# names can only contain letters, numbers and _. Cannot start with a number
# not explicitly declared (in Python)

# datatypes
first_name = "Shane" # String
age = 54 # integer
price = 12.23 # float
is_valid = True # Boolean (True/False)

# String formatting
# String concatonation
print("Your name is " + first_name)
print("Your name is " + first_name + " and you are " + str(age) + " years young")

# OR
print("Your name is",first_name,"and you are",age,"years young")

# OR (Best way)
print(f"Your name is {first_name} and you are {age} years young")

# constants
# like a variable that does not change
# Use SCREAMING_SNAKE_CASE

GST_RATE = 0.05
subtotal = 100
total = subtotal * 0.05
total = subtotal * GST_RATE

# Input from user
# Input always returns a string
# name = input("Enter your name: ")
# print(f"Welcome {name}")

# #add to numbers and display the sum
# number1 = input("Enter number 1: ")
# number2 = input("Enter number 2: ")

# sum = int(number1) + int(number2)
# print(f"{number1} + {number2} = {sum}")
# # OR
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))

# sum = number1 + number2
# print(f"{number1} + {number2} = {sum}")

#Prompt the user for 2 numbers and place them in 2 variables
#print out the values in the variables
    #Number1: 20
    #Number2: 40
#Swap the numbers in the variables so the value in number2 is the value from number1 and vice versa
#print out the values in the variables
    #Number1: 40
    #Number2: 20

