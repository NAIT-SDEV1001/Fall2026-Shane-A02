# *args must be before **kwargs
def order_summary(*foods, **extras):
    print("Items ordered:")

    #loop through food tuple
    for food in foods:
        print(f"- {food}")

    #loop through dictionary
    for key, value in extras.items():
        print(f"{key}: {value}")

order_summary("burger","fries",drink = "coke", size = "large")