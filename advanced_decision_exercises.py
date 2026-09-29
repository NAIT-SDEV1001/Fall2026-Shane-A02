# Advanced Decision Making Exercises
# 1.	Create a file named heads_or_tails.py in this folder. Write a program that lets the user guess whether the flip of a coin results in heads or tails. The program randomly generates an integer 0 to 1, which represents heads or tails. The program prompts the user to enter a guess and reports whether the guess is correct or incorrect.
# a.	import the random module to generate a random numbers
# b.	use random.randint(0, 1) to generate a random number between 0 and 1
# import random

# #heads will be 0, tails will be 1
# random_number = random.randint(0,1)

# user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ").upper()

# #display the results of the random coin toss
# if random_number == 0:
#     print("The coin flip was: heads")
# else:
#     print("The coin flip was: tails")

# #Compare flip to guess and display message
# if random_number == 0 and user_guess == "H" or random_number == 1 and user_guess == "T":
#     print("You guess correct!")
# else:
#     print("You guessed wrong")

 
# 2.	create a file named leap_year.py in this folder. Write a program to determine if a user input year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400. 
# year = int(input("Enter a year: "))

# year = int(input("Enter a year: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"Is {year} a leap year? True")
# else:
#     print(f"Is {year} a leap year? False")

# #1 print and no decision
# print(f"Is {year} a leap year? {year % 4 == 0 and year % 100 != 0 or year % 400 == 0}")


# 3.	Create a file named rock_paper_scissors.py in this folder. Write a program that plays the scissor-rock-paper game. (A scissor cuts paper, a rock can crush a scissor, and a paper can cover a rock.) The program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or 2 and displays a message indicating whether the user or the computer wins, loses, or draws. 
import random

result = "You lose"

user_input = int(input("scissors (0), rock (1), paper (2): "))
computer_input = random.randint(0,2) 

#translate user input into string
if user_input == 0:
    user_word = "scissors"
elif user_input == 1:
    user_word = "rock"
elif user_input == 2:
    user_word = "paper"

#translate computer input into string
match computer_input:            
    case 0:
        computer_word = "scissors"
    case 1:
        computer_word = "rock"
    case 2:
        computer_word = "paper"

#tie
if user_word == computer_word:
    result = "It is a draw"
#User wins
elif (user_word == "paper" and computer_word == "rock") or (user_word == "rock" and computer_word == "scissors") or (user_word == "scissors" and computer_word == "paper"):
    result = "You win!"

print(f"The computer is {computer_word}. You are {user_word}. {result}")











# 4.	Create a file named month_name.py in this folder. Write a program that will take a month number from the user and print the name of the month. If the user enters a number that is out of the range 1 to 12, the program should print an error message. Do this using a match statement. 
# month_number = int(input("Enter a month number (1-12): "))

# print("Month is: ")
# match month_number:
#     case 1:
#         print("January")
#     case 2:
#             print("February")
#     case 3:
#             print("March")
#     case 4:
#             print("April")
#     case 5:
#             print("May")
#     case 6:
#             print("June")
#     case 7:
#             print("July")
#     case 8:
#             print("August")
#     case 9:
#             print("September")
#     case 10:
#             print("October")
#     case 11:
#             print("November")
#     case 12:
#             print("December")
#     case _:
#             print("Not a valid month")  
         
   
# 5.	Create file named package_selector.py in this folder. Write a program for a gym so that it can determine which membership package a person should purchase. There are three packages:
# Package A: $40/month, 4 months
# Package B: $55/month, 8 months
# Package C: $75/month, 12 months
# Package D: $100/month, 12 month Note: ensure you have the words "You have selected Package A" or which ever package you select
 
package = input("Enter the package letter (A/B/C/D): ")

is_valid = True

match package.upper():
    case "A":
        monthly_fee = "$40"
        total_fee = "$160"
    case "B":
        monthly_fee = "$55"
        total_fee = "$440"  
    case "C":
        monthly_fee = "$75"
        total_fee = "$900"   
    case "D":
        monthly_fee = "$100"
        total_fee = "$1200"
    case _:
        is_valid = False
        print("Invalid package")

if is_valid:
    print(f"You have selected Package {package}")
    print(f"Your monthly fee is {monthly_fee}")
    print(f"Your total fee is {total_fee}")
