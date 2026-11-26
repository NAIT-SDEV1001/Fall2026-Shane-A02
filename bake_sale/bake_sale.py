from pathlib import Path
import csv
from datetime import datetime

DATE_FORMAT = "%d/%m/%y"
CSV_PATH = Path(__file__).parent/"bake_sale_orders.csv"
FIELD_NAMES = ["order_id", "customer_name", "item", "quantity", "pickup_date", "collected","order_type","gift_message"]

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

    #Return a dictionary from an object
    def to_csv_row(self)-> dict[str, str | int]:
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "item" : self.item,
            "quantity":self.quantity,
            "pickup_date":self.pickup_date.strftime(DATE_FORMAT),
            "collected": "yes" if self.collected else "no",
            "order_type": "regular",
            "gift_message": ""
        }

    

class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, gift_message: str)->None:
        if not gift_message.strip():
            raise ValueError ("A gift order must have a gift message")        
        super().__init__(order_id,customer_name, item, quantity, pickup_date,collected)
        self.gift_message = gift_message

    def __str__(self)->str:
        return f"{super().__str__()} | Gift Message: {self.gift_message}"  

    def to_csv_row(self)-> dict[str, str | int]:
        row = super().to_csv_row()
        row["order_type"] = "gift"
        row["gift_message"] = self.gift_message
        return row
        

class BakeSale:
    def __init__(self)->None:
        self.orders: list[BakeSaleOrder] = []
    

    def load_orders(self, csv_path: Path)->None:
        try:
            with open(csv_path,'r',encoding = "utf-8") as file:
                reader = csv.DictReader(file)              
                for row in reader:
                    order_id = row["order_id"]
                    customer_name = row["customer_name"]
                    item = row["item"]
                    quantity = int(row["quantity"])
                    pickup_date = datetime.strptime(row["pickup_date"],DATE_FORMAT).date()
                    collected = row["collected"] == "yes"
                    order_type = row["order_type"]
                    #what kind of object to create
                    if order_type =="regular":
                        order = BakeSaleOrder(order_id,customer_name,item,quantity,pickup_date,collected)
                    else:
                        order = GiftOrder(order_id,customer_name,item,quantity,pickup_date,collected,row["gift_message"])

                    self.add_order(order)

        except FileNotFoundError:
            print("File not found")

    def find_order(self,order_id: str)->BakeSaleOrder | None:
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
    
    #add the order to the list only if it is not already in the list based on its order_id
    def add_order(self, order: BakeSaleOrder)->None:
        if self.find_order(order.order_id) is not None:
            raise ValueError(f"OrderID: {order.order_id} is already in the list")
        self.orders.append(order)

    def list_orders(self)->None:
        if not self.orders:
            print("No orders")
        else:
            for order in self.orders:
                print(order)

    def save_orders(self,csv_path: Path)->None:
        with open(CSV_PATH,'w',newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file,FIELD_NAMES)
            writer.writeheader()
            for order in self.orders:
                writer.writerow(order.to_csv_row())


    def show_pickups(self) -> None:
        date_text = input("Pickup date (dd/mm/yy): ").strip()
        try:
            pickup_date = datetime.strptime(date_text, DATE_FORMAT)
        except ValueError:
            print("Enter a valid date in dd/mm/yy format.")
            return

        total_quantity = 0
        for order in self.orders:
            if order.pickup_date == pickup_date.date() and not order.collected:
                print(order)
                total_quantity += order.quantity

        if total_quantity:
            print(f"Total quantity: {total_quantity}")
        else:
            print("There are no pickups remaining for that date.")

    def prompt_for_order(self)-> None:
        order_id = input("Order ID: ").strip()
        customer_name = input("Customer name: ").strip()
        item = input("Item: ").strip()

        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Quantity must be a positive whole number.")
            return

        try:
            pickup_date = datetime.strptime(input("Pickup date (dd/mm/yy): ").strip(), DATE_FORMAT)
        except ValueError:
            print("Enter a valid date in dd/mm/yy format.")
            return

        try:
            order_type = input("Order type (regular/gift): ").strip().lower()
            if order_type == "regular":
                order = BakeSaleOrder(order_id, customer_name, item, quantity, pickup_date,False)
            elif order_type == "gift":
                gift_message = input("Gift message: ").strip()
                order = GiftOrder(order_id, customer_name, item, quantity, pickup_date, False, gift_message)
            else:
                raise ValueError("Order type must be regular or gift.")
            self.add_order(order)
        except ValueError as error:
            print(error)
            return

        print(f"Added order {order.order_id}.")

    def mark_collected(self) -> None:
        order_id = input("Order ID: ").strip()
        order = self.find_order(order_id)
        if order is None:
            print(f"No order found with ID {order_id}.")
        elif order.collected:
            print(f"Order {order_id} has already been collected.")
        else:
            order.collected = True
            print(f"Marked {order_id} as collected.")



def main() -> None:
    bake_sale = BakeSale()
    try:
        bake_sale.load_orders(CSV_PATH)
    except FileNotFoundError:
        print(f"Could not load the orders")
        return

    while True:
        print(
            "\n=== Bake Sale Pickup Tracker ===\n"
            "1. List all orders\n"
            "2. Show pickups for a date\n"
            "3. Add an order\n"
            "4. Mark an order as collected\n"
            "5. Save and exit"
        )
        choice = input("Choice: ").strip()

        if choice == "1":
            bake_sale.list_orders()
        elif choice == "2":
            bake_sale.show_pickups()
        elif choice == "3":
            bake_sale.prompt_for_order()
        elif choice == "4":
            bake_sale.mark_collected()
        elif choice == "5":            
            bake_sale.save_orders(CSV_PATH)                     
            print("Orders saved. Goodbye!")
            break
        else:
            print("Choose a menu option from 1 to 5.")

if __name__ == "__main__":
    main()
































# bake_sale = BakeSale()
# bake_sale.load_orders(CSV_PATH)
# bake_sale.list_orders()

# #add an order object manually to test the write to file
# pickup_date_object= datetime.strptime("20/01/72",DATE_FORMAT).date()
# order1 = BakeSaleOrder("abc123","Homer Simpson","Donut",20,pickup_date_object,False)
# bake_sale.orders.append(order1)

# #write the expanded list of orders (4 orders to the file)
# bake_sale.save_orders(CSV_PATH)
# bake_sale.list_orders()

# # print (order1)

# # gift_order1 = GiftOrder("abc123","Homer Simpson","Donut",20,pickup_date_object,False,"Happy Friday!")

# #load
# #list

# #to_csv methods
# #save orders

