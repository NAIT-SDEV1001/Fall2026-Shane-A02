bands = ["Judas Priest", "Metallica","Bee Gees","Abba"]
print(bands)
#For loops loop through every element in a list
for band in bands:
    print(band)

 #get the index AND the value
 #enumerate returns the index AND the value
for index, band in enumerate(bands):
    print(f"{band} is in index {index}")

#list of bands starting at 1
for index, band in enumerate(bands, start = 1):
    print(f"{index}. {band}")

#Create a list of menu options that displays a menu
#only use 1 print statement
#1. Add
#2. Edit
#3. Delete
#4. Exit

options = ["Add customer", "Edit customer", "Delete customer", "Exit"]
for number, option in enumerate(options, start = 1):
    print (f"{number}. {option}")







