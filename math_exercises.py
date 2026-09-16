# Math Exercises

# # Solve the following problems by identifying the steps the smaller problems first and then code the solution. Use the prompts and output that is showin in the sample runs that have been provided for each question.
    
# # 1. Ask the user for a temperature in Celsius and convert it to Fahrenheit. Round the answer to one decimal place. 
# # Enter the temperature in Celsius: 32
# # 32.0 C is equal to 89.6 F.

# # get celcius
# celsius = float(input("Enter a temperature in Celsius: "))
# #calculate to fahrenheit
# fahrenheit = celsius * 9 / 5 + 32
# # display fahrenheit
# print(f"Celsius: {celsius} => Fahrenheit: {fahrenheit:.1f}")

# # 2. Ask the user for a number of miles and print out how many kilometres it is.  Display to 2 decimal places. The conversion rate is 1 mile = 1.609344 kilometers.
# # Enter the number of miles: 50
# # 50.0 miles is equal to 80.47 kilometres
  
# KILOMETERS_PER_MILE = 1.609344

# miles = float(input("Enter the number of miles: "))
# kilometres = miles * KILOMETERS_PER_MILE
# print(f"{miles} miles is {kilometres:.2f} kilometres.")


# # 3. One acre of land is equal to 43,560 square feet. Write a program that asks the user to enter the number of acres and display the number of square feet. Display to 2 decimal places
# # Enter the number of acres: 120
# # 120.0 acres is equal to 5227200.00 square feet.

# CONVERSION_RATE = 43560

# acres = float(input("Acre to Square foot converter. How many acres do you have? "))
# square_feet = acres * CONVERSION_RATE
# print(f"You have {acres} acres which is equal to: {square_feet} square feet")


# # 4. Write a program that asks the user to enter three test scores. The program should display each test score, as well as the average test of the users' scores.
# # Enter the first test score: 50
# # Enter the second test score: 60
# # Enter the third test score: 75

# # Test Score Summary
# # Test 1: 50.0
# # Test 2: 60.0
# # Test 3: 75.0

# # Average: 61.7

# score1 = float(input("Enter the first test score: "))
# score2 = float(input("Enter the second test score: "))
# score3 = float(input("Enter the third test score: "))

# average = (score1 + score2 + score3)/3

# print (f"Test Score 1: {score1}")
# print (f"Test Score 2: {score2}")
# print (f"Test Score 3: {score3}")

# print(f"Average Score: {average}")

# # 5. A bag of cookies holds 40 cookies. The calorie information on the bag claims that there are 10 "servings" in the bag and that a serving equals 300 calories. Write a program that asks the user to input how many cookies they ate and then reports how many total calories were consumed.
# # How many cookies did you eat? 14
# # You consumed 1050 calories.

# COOKIES_PER_BAG = 40
# SERVINGS_PER_BAG = 10
# CALORIES_PER_SERVING = 300

# cookies = int(input("How many cookies did you eat? "))

# #how much of bag consumed
# percentage_of_bag_consumed = cookies/COOKIES_PER_BAG

# #how many calories are in the whole bag
# calories_per_bag = SERVINGS_PER_BAG * CALORIES_PER_SERVING

# #calculate the calories consumed
# calories_consumed = percentage_of_bag_consumed * calories_per_bag


# # calories_consumed = cookies/COOKIES_PER_BAG * SERVINGS_PER_BAG * CALORIES_PER_SERVING

# #DIsplay cookies and calories
# print (f"You ate {cookies} cookies")
# print (f"Which is equal to {calories_consumed} calories")

# # 6. Ask the user for:
	
# # number of pizzas (int)
# # price per pizza (float, dollars)
# # tip percent (float; e.g., 15 for 15%)
# # number of people sharing (int)

# # Calculate and print: subtotal, tip amount, total, and amount per person.
# # formatting currency to 2 decimals. Display appropriate inputs and outputs.
# # Enter the number of pizzas: 6 
# # Enter the price per pizza: $20
# # Enter the tip percentage (for example, 15): 18
# # Enter the number of people sharing: 8

# # Pizza Bill
# # Subtotal:         $120.00
# # Tip:              $21.60
# # Total:            $141.60

# # Amount per person: $17.70

# pizzas = int(input("How many pizzas? "))
# price_each = float(input("Price per pizza ($): "))
# tip_percent = float(input("Tip percent (e.g., 15 for 15%): "))
# people = int(input("How many people sharing? "))

# # calculate subtotal, tip, total, per_person
# subtotal = pizzas * price_each
# tip = subtotal * (tip_percent / 100)
# total = subtotal + tip
# per_person = total / people

# #display results
# print(f"Subtotal: ${subtotal:.2f}")
# print(f"Tip: ${tip:.2f}")
# print(f"Total: ${total:.2f}")
# print(f"Each person pays: ${per_person:.2f}")

# 7. Ask the user for a currency amount and display the number of dollars, quarters, dimes, nickels, and pennies in that amount.  
# Enter a currency amount: $1.39

# Currency Breakdown for $1.39
# Dollars:  1
# Quarters: 1
# Dimes:    1
# Nickels:  0
# Pennies:  4
import math
#get amount from user
amount = float(input("Enter a dollar amount (e.g. 3.87): "))
amount = round(amount * 100) #turn the amount into cents 387. round to avoid floating point errors
#Determine Dollars
#options for Dollars
dollars = amount // 100 # 3
amount = amount % 100 #87
#Determine Quarters
quarters = amount // 25 # 3
amount = amount % 25 # 12
#Determine Dimes
dimes = amount // 10 # 1
amount = amount % 10 # 2
#Determine Nickels
nickels = amount // 5 # 0
amount = amount % 5 # 2
#Determine Pennies
pennies = amount

#Display
print("Coin Breakdown")
print(f"Dollars: {int(dollars)}")
print(f"Quarter: {int(quarters)}")
print(f"Dimes: {int(dimes)}")
print(f"Nickels: {int(nickels)}")
print(f"Pennies: {int(pennies)}")


