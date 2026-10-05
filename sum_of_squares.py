# my_square = int(input("Enter a number to sum the squares: "))

# sum = 0

# for number in range(1,my_square + 1):
#     sum += number ** 2

#     print(f"The sum of squares is: {sum}")

#print running sum after each calculation
#prompting for the lower and upper range of the numbers
#ensure that the upper range is > lower range


# lower = int(input("Enter lower number: "))
# upper = int(input("Enter upper number: "))

# sum = 0

# if lower > upper:
#     print("Invalid Range")
# else:
#     for number in range(lower,upper + 1):
#         sum += number ** 2

#     print(f"The sum of squares is: {sum}")

# #Use list comprehension to create a list of squares from 1 to my_number
# my_square = int(input("Enter a number to sum the squares: "))

# squares = [number ** 2 for number in range(1,my_square + 1)]

# print(squares)

#Only sum the squares of even numbers
my_square = int(input("Enter a number to sum the squares: "))

squares = [number ** 2 for number in range(1,my_square + 1) if number % 2 == 0]

print(squares)




