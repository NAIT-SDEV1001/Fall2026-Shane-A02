# Advanced Decision Making Exercises
# 1.	Create a file named heads_or_tails.py in this folder. Write a program that lets the user guess whether the flip of a coin results in heads or tails. The program randomly generates an integer 0 to 1, which represents heads or tails. The program prompts the user to enter a guess and reports whether the guess is correct or incorrect.
# a.	import the random module to generate a random numbers
# b.	use random.randint(0, 1) to generate a random number between 0 and 1


 
# 2.	create a file named leap_year.py in this folder. Write a program to determine if a user input year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400. 
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print(f"Is {year} a leap year? True")
else:
    print(f"Is {year} a leap year? False")

#1 print 
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    result = "True"
else:
    result = "False"

print(f"Is {year} a leap year? {result}")

#no else
result = "False"
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    result = "True"
print(f"Is {year} a leap year? {result}")

#no if
print(f"Is {year} a leap year? {(year % 4 == 0 and year % 100 !=0) or year % 400 == 0}")




# 3.	Create a file named rock_paper_scissors.py in this folder. Write a program that plays the scissor-rock-paper game. (A scissor cuts paper, a rock can crush a scissor, and a paper can cover a rock.) The program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or 2 and displays a message indicating whether the user or the computer wins, loses, or draws. 
 
 
 

# 4.	Create a file named month_name.py in this folder. Write a program that will take a month number from the user and print the name of the month. If the user enters a number that is out of the range 1 to 12, the program should print an error message. Do this using a match statement. 

month_number = int(input("Enter a month number (1-12): "))

print("Month is: ")
match month_number:
    case 1:
        print("January")
    case 1:
            print("February")
    case 1:
            print("March")
    case 1:
            print("April")
    case 1:
            print("May")
    case 1:
            print("June")
    case 1:
            print("July")
    case 1:
            print("August")
    case 1:
            print("September")
    case 1:
            print("October")
    case 1:
            print("November")
    case 1:
            print("December")
    case _:
            print("Not a valid month")
    
    
        





   
# 5.	Create file named package_selector.py in this folder. Write a program for a gym so that it can determine which membership package a person should purchase. There are three packages:
# Package A: $40/month, 4 months
# Package B: $55/month, 8 months
# Package C: $75/month, 12 months
# Package D: $100/month, 12 month Note: ensure you have the words "You have selected Package A" or which ever package you select
 
 
