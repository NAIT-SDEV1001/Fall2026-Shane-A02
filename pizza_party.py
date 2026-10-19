def calculate_order_total(pizza_count, price_each, delivery_fee=5.00):
    return pizza_count * price_each + delivery_fee

pizza_count = int(input("Number of pizzas: "))
price_each = float(input("Price per pizza: "))

delivery_total = calculate_order_total(pizza_count, price_each)

pickup_total = calculate_order_total(pizza_count, price_each, 0.00)

print(f"Delivery total: ${delivery_total:.2f}")
print(f"Pickup total: ${pickup_total:.2f}")

custom_fee = float(input("Custom delivery fee: "))
custom_total = calculate_order_total(pizza_count, price_each, custom_fee)
print(f"Custom delivery total: ${custom_total:.2f}")


