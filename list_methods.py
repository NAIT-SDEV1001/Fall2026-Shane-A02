#Sorting
numbers = [42,7,19,100,3]
numbers.sort()#Sort ascending
print(numbers)

numbers.sort(reverse = True)
print(numbers)

#Add a value to a list
colors = ["blue","red"]
colors.append("purple")#end of the list
colors.insert(1,"orange")#inserts at an index
print(colors)

#append a list onto anothe list
new_list = ["Pink","Teal"]
colors.extend(new_list)
print(colors)

#Insert a list at an index
colors[2:2] = new_list
print(colors)

#removing values
#pop(by index) - removes the element AND returns the value of that element
pop_value = colors.pop(2)
print(f"You just deleted {pop_value}")
print(colors)

#del without returning deleted value
del colors[3]
print(colors)

#remove by value
colors.remove("Teal")
print(colors)

#what happens when you try to remove a non existant value
# colors.remove("blah")


cities = ["Edmonton", "Berlin", "Calgary", "Montreal", "Buruit"]
# check_city = input("Enter a city: ")

# result = check_city in cities#Returns True or False

# if result:
#     cities.remove(check_city)
# else:
#     print(f"{check_city} is not in the list")

# #index of a value
# print(f"The index of Calgary is: {cities.index("Calgary")}")
# print(cities)

#Ask the user for an existing city name and a new city name and replace the old value in the list with the new value. If the name is not in the list display a message

#Ask for old city name
# old_city = input("Enter a city to replace: ")
# #Ask for replacement city name
# new_city = input("Enter a new city: ")
# #is the old name in the list
# if old_city in cities:
#     cities[cities.index(old_city)] = new_city
#     #OR
#     # find index of old name
#     # old_city_index = cities.index(old_city)
#     # #replace value in the index with new name
#     # cities[old_city_index] = new_city
# else:
#     print(f"{old_city} is not in the list")    
# print(cities)

#Count the occurences of a value in a list
cities = ["Edmonton", "Berlin", "Calgary", "Montreal", "Buruit", "Edmonton"]
city = input("Enter a city to count: ")
print(f"{city} is in the list {cities.count(city)} times")

#clear a list
cities.clear()
print(cities)
