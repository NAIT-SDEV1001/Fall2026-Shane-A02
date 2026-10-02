#range() - generates a sequence of numbers (think of it as a list of numbers)
#can be used as a loop counter
#syntax
#range(start, stop, step)
#start is inclusive, stop is exclusive

#print 1-5
for number in range(1,6):
    print (number)
    print("Hello World")

#print the cubes of numbers 0 to 4
for number in range(0,5):
    print(f"{number} cubed is {number ** 3}")
#OR
for number in range(5):
    print(f"{number} cubed is {number ** 3}")

#print the even numbers between 4 and 20
for number in range (4,21,2):
    print(number)

#count down 10-1
for number in range (10,0,-1):
    print (number)

count = int(input("How many times to say Happy Friday? "))
for number in range(0,count ):
    print("Happy Friday")
