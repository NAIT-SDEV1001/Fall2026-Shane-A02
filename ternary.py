#ternary condition
#if/else
#pass or fail if grade entered is >=50

# grade = int(input("Enter a grade: "))
# if grade >= 50:
#     print("Pass")
# else:
#     print("Fail")

#ternary
#value_if_true if condition else value_if_false
# result = "Pass" if grade >= 50 else "Fail"
# print (result)

# print("Pass" if grade >= 50 else "Fail")

#even or odd
number = int(input("Enter a number: "))
result  = "Even" if number % 2 == 0 else "Odd"
print (result)


#ask for 2 numbers and print the the largest number
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

largest = number1 if number1 > number2 else number2
print (largest)

print(number1 if number1 > number2 else number2)


grade = 25
result = "honours" if grade >=80 else "Pass" if grade >= 50 else "Fail"
print (result)