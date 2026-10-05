#ask the user for number of rows and seats in each row
rows = int(input("Enter number of rows: "))
seats = int(input("Enter number of seats: "))
for row in range(1,rows + 1):
    for seat in range(1, seats + 1):
        name = input("Enter your name: ")
        print(f"Row {row}, Seat {seat} is purchased by {name}")