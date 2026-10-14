print("Rocket Countdown")
starting_number = int(input("Enter a starting number: "))
#keep asking until positive number
while starting_number < 1:
    starting_number = int(input(f"Hey! Gotta be positive! {starting_number} aint that! Enter a starting number: "))

counter = starting_number

while counter >= 1:
    print(counter)
    counter -= 1

print("Blast off!")


    