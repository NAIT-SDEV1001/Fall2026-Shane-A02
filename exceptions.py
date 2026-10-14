#We want trap exceptions gracefully
#keep program running AND give nice error messages

#Use Try/Except

sum = 0 
count = 0
while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break
    sum += number
    count += 1
average = sum/count
print(f"The average is {average}")
#what exceptions could occur
#String input  - ValueError
#Zero count - ZeroDivisionError
#decimal input - ValueError

#Use try/except
sum = 0 
count = 0
while True:
    try:#try this code. if it fails go to except
        number = int(input("Enter an integer number: "))
    except ValueError as error_message:#trap any Value Errors in try block. error_message holds pythons error message. optional to use
        print(f"Invalid Input. Must be a integer. Error Message: {error_message}")       
        continue#loop until valid input
    if number == -1:
        break
    sum += number
    count += 1
try:
    average = sum/count
    print(f"The average is {average}")
except ZeroDivisionError: #don't want the error_message. Optional
    print("No numbers were entered")

#else and finally
sum = 0 
count = 0
while True:
    try:#try this code. if it fails go to except
        number = int(input("Enter an integer number: "))
    except ValueError as error_message:#trap any Value Errors in try block. error_message holds pythons error message. optional to use
        print(f"Invalid Input. Must be a integer. Error Message: {error_message}")       
        continue#loop until valid input
    else:#executes if no exception
        print("Number Accepted")
    if number == -1:
        break
    sum += number
    count += 1    
try:
    average = sum/count
    print(f"The average is {average}")    
except ZeroDivisionError: #don't want the error_message. Optional
    print("No numbers were entered")
#finally always executes
finally:
    print("Always Executes")

# #multiple exceptions for one try and a catch all at the end
try:
    number = int(input("Enter an integer: "))
    result = 100/number
except ValueError:
    print("Invalid input. Must be an integer")
except ZeroDivisionError:
    print("Cannot have a zero denominator")
except:
    print("Unknown error")    


#custom exception
sum = 0 
count = 0
while True:
    try:#try this code. if it fails go to except
        number = int(input("Enter an integer number: "))
        if number < -1:
            raise ValueError ("Number must not be negative")
    except ValueError as error_message:#trap any Value Errors in try block. error_message holds pythons error message. optional to use
        print(f"Invalid Input. Must be a integer. Error Message: {error_message}")       
        continue#loop until valid input
    if number == -1:
        break
    sum += number
    count += 1
try:
    average = sum/count
    print(f"The average is {average}")
except ZeroDivisionError: #don't want the error_message. Optional
    print("No numbers were entered")






