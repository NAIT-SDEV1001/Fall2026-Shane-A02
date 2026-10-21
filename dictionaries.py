#Dictionaries store key-value pairs
#Keys are unique. strings or numbers.
#Values can be any datatype, including other dictionaries, lists, tuples

# Example
student = {"name":"Homer","age":42,"email":"homer@gmail.com"}

#Access values by keys
print (student["name"])#retrieve a value
student["age"] = 52#update a value
student["city"] = "Springfield"

key = input("Enter a new key: ")
value = input("Enter a new value: ")

student[key] = value

print(student)

#remove a key and value
del student["email"]
print(student)
#Remove a key/value that does not exist? KeyError
# del student["blah"]
#can check first. If the key is in the dictionary
if "citie" in student:
    del student["citie"]
#accessing a key that does not exist is a KeyError
#use get to attempt to get the value in that key.
#If it does not exist it returns None
print(student.get("StudentNumber"))
#OR we can return a default value
print(student.get("StudentNumber","N/A"))

#Nested collection (value of a dictionary)
inventory = {
            "apple":{"price":0.50,"stock_count":50},
            "banana":{"price":0.30,"stock_count":150}
}

print(inventory["apple"]["price"])
print(inventory["banana"]["price"])

#Looping through a dictionary
#keys
for key in student:
    print(f"{key}: {student[key]}")

#Loop through the keys
grades = {"Homer":40, "Bart":85, "Lisa":98}
for name in grades.keys():
    print(name)

#Loop through the values
total = 0
for grade in grades.values():
    total += grade
    print(grade)

print(f"Average grade: {total/len(grades)}")

#Access both keys and values
for name,grade in grades.items():
    print(f"{name}: {grade}")

#sort by key
for name,grade in sorted(grades.items()):
    print(f"{name}: {grade}")
#reverse
for name,grade in sorted(grades.items(), reverse = True):
    print(f"{name}: {grade}")

inventory = {"apples":0,"bananas":0,"oranges":0}
purchases = ["apples","bananas", "apples","oranges","apples"]#purchases
#Loop through the list and add 1 to the inventory counts(currently 0) each time that item is purchased
# inventory = {"apples":3,"bananas":1,"oranges":1}

#print out the inventory and the counts
#apples: 3
#bananas: 1
#oranges: 1

for item in purchases:
    inventory[item]+=1

for item, count in inventory.items():
    print(f"{item}: {count}")

#for fun
# while(purchases):
#     inventory[purchases.pop()] += 1

s