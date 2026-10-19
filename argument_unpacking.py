#function is expecting 2 parameters
def show_info(name,age):
    print(f"{name} is {age} years old")
#One tuple of info
person = ("Bob", 37)
# * is unpacking the tuple into seperate positional arguments
# equivalent to show_person("Bob",37) 
show_info(*person)

person = {"name": "Bob", "age": 25}

#** unpacks the dictionary into keyword arguments
#Equivalent to show_info(name = "Bob", age = 25)
show_info(**person)

# in a function definition , *args and **kwargs collect arguments.
# In a function call, * and ** unpack values into arguments


def print_delivery(customer, city, parcels):
    print(f"{customer} has {parcels} parcels going to {city}.")

delivery = ("Maya", "Edmonton", 3)
print_delivery(*delivery)
