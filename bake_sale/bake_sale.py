from datetime import datetime
DATE_FORMAT = "%m/%d/%Y"
class BakeSaleOrder:
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool)->None:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive whole number.")

        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity
        self.pickup_date = pickup_date
        self.collected = collected

# Give BakeSaleOrder a __str__() method that displays a line like this.
# *for the last attribute it is based on collected. True = “Collected”, False = “Awaiting pickup”
# B101 | Sam Lee | 6 x Chocolate chip cookies | 21/11/26 | Awaiting pickup
    def __str__(self)->str:
        return (
            f"{self.order_id} | {self.customer_name} | {self.quantity} x {self.item}"
            f" | {self.pickup_date.strftime(DATE_FORMAT)}"
            f" | {"Collected" if self.collected else "Awaiting Pickup"}"                 
        )

class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, gift_message: str)->None:
        if not gift_message.strip():
            raise ValueError ("A gift order must have a gift message")        
        super().__init__(order_id,customer_name, customer_name, quantity, pickup_date,collected)
        self.gift_message = gift_message

  

pickup_date_object= datetime.strptime("01/20/1972",DATE_FORMAT).date()

order1 = BakeSaleOrder("abc123","Homer Simpson","Donut",20,pickup_date_object,False)
print (order1)

gift_order1 = GiftOrder("abc123","Homer Simpson","Donut",20,pickup_date_object,False,"Happy Friday!")
