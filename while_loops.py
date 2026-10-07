#while loops repeat a block of code as long as a condition is true
#useful when you do not know how many times to loop

number = int(input("Enter a number to count to: "))

counter = 1
while counter <= number:
    print(counter)
    counter += 1

#Add up numbers entered by the user until they enter "done"
#then display the sum

#Using a True loop
print("Enter a number to add. Type 'done' to display the sum")

sum = 0

while True: #an endless loop, unless break
    value = input("Enter a number: ")
    #did they enter done? Then break
    if value == "done":
        break#break exits the loop
    #add value to the sum
    sum += int(value)

print(sum)

#Boolean flag
keep_going = True

while keep_going:
    answer = input("Keep going? (y/n): ")
    if answer =="n":
        keep_going = False

print("Done looping")
#loop zero or many times

answer = input("Do you want to loop: (y/n)")
while answer == "y":
    print("looping is fun!")
    print("Have a groovy day!")
    answer = input("Do you want to loop again: (y/n)")

print("Bye")














