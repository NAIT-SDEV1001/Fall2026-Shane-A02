def display_welcome():
    print("Welcome to the snack shack")
    print("Most snacks are $4.00")

def display_receipt(item_name,quantity,total):
    print(f"Snack: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")    

def main():
    print("Display_welcome example: ")
    display_welcome()
if __name__ == "__main__":
    main()


