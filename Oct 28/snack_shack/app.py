#Should use relative pathing when using a package.

from .validation import get_valid_quantity#import one function from the validation module
from .pricing import calculate_total
# import pricing #need to use pricing.calculate_total()
from .display import display_receipt,display_welcome

def main():
    UNIT_PRICE = 3.00
    display_welcome()
    item_name = input("Snack Name: ")
    quantity = get_valid_quantity()
    #total = calculate_total(quantity,UNIT_PRICE)#Overriding the default
    #total = calculate_total(quantity)#using the default
    total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)#using keyword arguments
    display_receipt(item_name, quantity, total)

#If running the app from this module (__name__ == __main__)
#If importing and running __name__ is the name of the module being imported
if __name__ == "__main__":
    main()


