def get_valid_quantity():
    while True:
    #keep looping until a valid quantity is entered (integer > 0)
        try:
            return int(input("Enter a quantity: "))            
        except ValueError:
            print("Please enter a whole number")