bands = ["Abba", "Journey", "Max Rebo Band", "Styx", "The Beatles"]
#For loops allow us to look at each element in a list

for band in bands:
    print(f"{band} is a great band")
#loops through entire list
#each value in the list populates band

fruits = ["blueberry","durian","Stawberry"]

for index, fruit in enumerate(fruits):
    print(f"{fruit} is at index {index}")

#Start list at 1
for index, fruit in enumerate(fruits):
    print(f"{fruit} is at index {index + 1}")

#or
for index, fruit in enumerate(fruits, start = 1):
    print(f"{fruit} is at index {index}")

#Create a list that displays a menu
#only use 1 print statement
#1. Add
#2. Edit
#3. Delete
#4. Exit

options = ("Add customer", "Edit customer", "Delete customer", "Exit")
for number, option in enumerate(options, start = 1):
    print (f"{number}. {option}")

names = ["Han Solo", "Luke Skywalker", "Darth Vader", "Princess Leia", "Darth Vader", "Boba Fett"]

bad_names = ("Darth Vader", "Boba Fett")

#show the good names
for name in names:
    if name not in bad_names:
        print(f"{name} is a good name!")

for name in names:
    if name in bad_names:
        continue
    print(f"{name} is a good name!")




