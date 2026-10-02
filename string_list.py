#Strings are a list of chars
name = "Shane"
name = ["S","h","a","n","e"]

for character in name:
    print(character)

#Prompt the user for a character and their name and tell them if that character is in their name
name = input("Enter your name: ")
character = input("Enter a character: ")

if character in name:
    print(f"{character} is in {name}")
else:
    print(f"{character} is not in {name}")


