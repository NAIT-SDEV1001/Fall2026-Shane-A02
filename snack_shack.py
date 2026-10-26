
#A function is block of code that performs a task. You define it once and call it when needed
#Why
#code reuse
#maintainable
#Simple testing
#large problem into smaller problems

#Ask for a quantity and return a valid quantity(int)
def get_valid_quantity():
    while True:
    #keep looping until a valid quantity is entered (integer > 0)
        try:
            return int(input("Enter a quantity: "))            
        except ValueError:
            print("Please enter a whole number")
   

def display_welcome():
    print("Welcome to the snack shack")
    print("Most snacks are $4.00")

def calculate_total(quantity, unit_price = 4.00):
    total = quantity * unit_price
    return total

def display_receipt(item_name,quantity,total):
    print(f"Snack: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")

UNIT_PRICE = 3.00


display_welcome()
item_name = input("Snack Name: ")
quantity = get_valid_quantity()
#total = calculate_total(quantity,UNIT_PRICE)#Overriding the default
#total = calculate_total(quantity)#using the default
total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)#using keyword arguments
display_receipt(item_name, quantity, total)



