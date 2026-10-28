def get_ticket_price(age):

    if age <= 12:
        price = 8.00         
    elif age <= 64:
        price =  12.00
    else:
        price =  9.00
    return price

def calculate_total(quantity, ticket_price):
    total = quantity * ticket_price
    return total

