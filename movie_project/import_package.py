#import movie_night package
#package -->modules-->functions

# from movie_night import display,pricing,validation
# print(f"Ticket price: {pricing.get_ticket_price(54)}" )

from movie_night.pricing import get_ticket_price
print(f"Ticket price: {get_ticket_price(54)}" )
