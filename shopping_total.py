print("Shopping Total")

item_count = 0
total_cost = 0.0
price_input = input("Enter an item price (q to quit): ")

# Challenge: lower() allows either q or Q to quit.
while price_input.lower() != "q":
    price = float(price_input)
    total_cost += price
    item_count += 1
    price_input = input("Enter an item price (q to quit): ")

print(f"Items purchased: {item_count}")
print(f"Total cost: ${total_cost:.2f}")



items_count = 0
total_cost = 0.0

while True:
    user_input = input("Enter an item price (q to quit): ")

    if user_input.lower() == 'q':
        break     # exit loop

    items_count += 1
    total_cost += float(user_input)

print()
print(f"Items purchased: {items_count}")
print(f"Total cost: ${total_cost:.2f}")